--Compra masiva con control por usuario
--Cree una transacción para registrar varias compras en una sola factura, que funcione así:
--Valide el stock para todos los productos solicitados
--Si algún producto no tiene stock suficiente, no debe registrarse ningún producto y se debe hacer rollback
--Inserte los detalles de la factura (varios productos) y reduzca el stock respectivo

--ejercicio extra 2 compra masiva con control por usuario

DO $$
DECLARE 
    v_user_id INT := 1;
    v_bill_id INT;
    v_total NUMERIC(12,2) := 0;
    v_product RECORD;
BEGIN
    -- validar que el usuario existe
    IF NOT EXISTS (SELECT 1 FROM Users WHERE user_id = v_user_id) THEN
        RAISE EXCEPTION 'El usuario % no encontrado', v_user_id;
    END IF;

    --crear factura vacía
    INSERT INTO Bills (user_id, total, status, bill_date)
    VALUES (v_user_id, 0, 'Pendiente', CURRENT_TIMESTAMP)
    RETURNING bill_id INTO v_bill_id;

    --simunlar compra de varios productos
    FOR v_product IN
        SELECT buy.product_id, buy.quantity, p.price, p.stock
        FROM (
            VALUES
                (1, 2),
                (2, 1),
                (3, 3)
        ) AS buy(product_id, quantity)
        JOIN Products p ON p.product_id = buy.product_id    
    LOOP

        -- validar stock suficiente
        IF v_product.stock < v_product.quantity THEN
            RAISE EXCEPTION 'Stock insuficiente para el producto %', v_product.product_id;
        END IF;

        -- insertar detalle de la factura
        INSERT INTO Bill_Details (bill_id, product_id, quantity, price, entregado)
        VALUES (v_bill_id, v_product.product_id, v_product.quantity, v_product.price, FALSE);

        -- reducir stock del producto
        UPDATE Products
        SET stock = stock - v_product.quantity
        WHERE product_id = v_product.product_id;

        -- acumular total 
        v_total := v_total + (v_product.quantity * v_product.price);
    END LOOP;

    -- actualizar total de la factura
    UPDATE Bills
    SET total = v_total
    WHERE bill_id = v_bill_id;

    RAISE NOTICE 'Compra registrada exitosamente con factura ID: %', v_bill_id;
END;
$$;

