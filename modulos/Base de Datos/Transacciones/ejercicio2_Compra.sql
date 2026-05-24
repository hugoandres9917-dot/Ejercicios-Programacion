-- Ejercicio 2: Transacción de Compra

--Construya una transacción para el proceso de compra de múltiples productos. El bloque debe realizar las siguientes validaciones y acciones:
--Comprobar si hay existencias suficientes de cada uno de los productos dentro de la factura.
--Confirmar que el usuario que realiza la compra existe en la DB.
--Insertar la factura con el usuario relacionado.
--Reducir el stock de los productos según la cantidad comprada.

-- 1. Insertar datos iniciales
--INSERT INTO Users (name, email) VALUES ('Hugo', 'hugo@mail.com');
--INSERT INTO Users (name, email) VALUES ('Ana', 'ana@mail.com');

INSERT INTO Products (name, price, stock) VALUES 
('Laptop', 1200, 10),
('Mouse', 25, 50),
('Teclado', 45, 30);

--ejercicio2_compra.sql
DO $$
DECLARE
    v_user_id INT := 1; --Usuario que realiza la compra
    v_bill_id INT;      -- id de la factura creada
    v_total NUMERIC(12,2) := 0;
    v_products RECORD;    -- ITERADOR para productos
BEGIN
    --validar que el usuario existe
    IF NOT EXISTS (SELECT 1 FROM Users  WHERE user_id = v_user_id) THEN
        RAISE EXCEPTION 'El usuario % no existe', v_user_id;
    END IF;

    --validar stock de todos los productos antes de iniciar la compra
    FOR v_products IN
        SELECT product_id, price, stock, 2 AS quantity
        FROM Products
        WHERE product_id IN (1, 2)
    LOOP
        IF v_products.stock < v_products.quantity THEN
            RAISE EXCEPTION 'Stock insuficiente para producto %', v_products.product_id;
        END IF;
    END LOOP;   

    --Crear factura vacia, todos los productos estan con stock suficiente
    INSERT INTO Bills (user_id, total, status, bill_date)
    VALUES (v_user_id, 0, 'Pendiente', CURRENT_DATE)
    RETURNING bill_id INTO v_bill_id;

    --simulacion de productos comprados
    FOR v_products IN 
        SELECT product_id, price, stock, 2 AS quantity
        FROM Products
        WHERE product_id IN  (1, 2)
    LOOP
        --INSERTAR detalle de factura
        INSERT INTO Bill_Details (bill_id, product_id, quantity, subtotal)
        VALUES (v_bill_id, v_products.product_id, v_products.quantity, v_products.price * v_products.quantity);

        --reducir stock
        UPDATE Products
        SET stock = stock - v_products.quantity
        WHERE product_id = v_products.product_id;

        --acumular total
        v_total := v_total + (v_products.price * v_products.quantity);
    END LOOP;

    --ACTUALIZAR TOTAL DE LA FACTURA
    UPDATE Bills
    SET total = v_total
    WHERE bill_id = v_bill_id;

    RAISE NOTICE 'Compra realizada con exito. Factura % total %', v_bill_id, v_total;
END;
$$;

-- 3. Consultar resultados
SELECT * FROM Bills;
SELECT * FROM Bill_Details;
SELECT * FROM Products;



