-- Transacción con bloqueo optimista
-- Plantee un escenario donde dos usuarios intentan comprar el último producto disponible:
-- Use una transacción que lea el stock y actualice solo si el stock no cambió en el proceso
--Si otro proceso modificó el stock mientras tanto, debe abortar la compra

--ejercicio extra 3 bloqueo optimista

DO $$
DECLARE
    v_user_id INT := 1; -- usuario que realiza la compra
    v_product_id INT := 1; -- producto a comprar
    v_quantity INT := 1; -- cantidad a comprar
    v_stock INT;
    v_bill_id INT;
    v_total NUMERIC(12,2);
    v_product RECORD;
BEGIN

    -- validar que el usuario existe
    IF NOT EXISTS (SELECT 1 FROM Users WHERE user_id = v_user_id) THEN
        RAISE EXCEPTION 'El usuario % no existe', v_user_id;
    END IF;

    -- leer stock actual del producto
    SELECT stock INTO v_stock FROM Products WHERE product_id = v_product_id;

    -- validar stock suficiente
    IF v_stock < v_quantity THEN
        RAISE EXCEPTION 'Stock insuficiente para el producto %', v_product_id;
    END IF;

    -- crear factura vacía
    INSERT INTO Bills (user_id, total, status, bill_date)
    VALUES (v_user_id, 0, 'Pendiente', CURRENT_TIMESTAMP)
    RETURNING bill_id INTO v_bill_id;

    --intentar actualizar stock con condicion obtimista
    UPDATE Products
    SET stock = stock - v_quantity
    WHERE product_id = v_product_id
        AND stock = v_stock; -- solo actualizar si el stock no cambió

    -- verificar si la actualizacion se aplico
    IF NOT FOUND THEN
        RAISE EXCEPTION 'Otro proceso modificó el stock del producto %, la compra no se pudo completar', v_product_id;
    END IF;

    -- insertar detalle de la factura
    INSERT INTO Bill_Details (bill_id, product_id, quantity, subtotal, entregado)
    VALUES (v_bill_id, v_product_id, v_quantity, 
    (SELECT price FROM Products WHERE product_id = v_product_id) * v_quantity, FALSE);

    -- actualizar total de la factura
    SELECT SUM(subtotal) INTO v_total FROM Bill_Details WHERE bill_id = v_bill_id;
    UPDATE Bills
    SET total = v_total 
    WHERE bill_id = v_bill_id;

    RAISE NOTICE 'Compra realizada exitosamente, factura ID: %', v_bill_id;
END;
$$;
