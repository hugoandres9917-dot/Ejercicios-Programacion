--Cancelación de factura incompleta

--Cree una transacción que permita cancelar una factura que aún no tiene todos los productos entregados:
--Verifique que la factura esté en estado "Pendiente"
--Cambie su estado a "Cancelada"
--Regrese el stock solo de los productos que aún no han sido entregados (puede agregar una columna "entregado" en los detalles de la factura)
--Garantice que si alguna validación falla, se haga rollback

-- agregamos una columna "entregado" a la tabla Bill_Details para marcar si un producto ha sido entregado o no

ALTER TABLE Bill_Details
ADD COLUMN entregado BOOLEAN DEFAULT FALSE;
--ejercicio extra 1 canelación de factura

DO $$
DECLARE
    v_bill_id INT := 1; -- factura a cancelar
    v_products RECORD;
BEGIN
    -- validar si factura existe y estado  Pendiente
    IF NOT EXISTS (SELECT 1 FROM Bills WHERE bill_id = v_bill_id AND status = 'Pendiente') THEN 
        RAISE EXCEPTION 'La factura % no existe o no esta en estado Pendiente', v_bill_id;
    END IF;

    -- recorrer los productos de la factura
    FOR v_products IN 
        SELECT product_id, quantity, entregado
        FROM Bill_Details
        WHERE bill_id = v_bill_id
    LOOP
        -- solo devolver stock de productos No entregados
        IF v_products.entregado = FALSE THEN
            UPDATE Products
            SET stock = stock + v_products.quantity
            WHERE product_id = v_products.product_id;
        END IF;
    END LOOP;    

    --cambiar estado de la factura a Cancelada
    UPDATE Bills
    SET status = 'Cancelada',
        bill_date = CURRENT_TIMESTAMP,
        total = 0
    WHERE bill_id = v_bill_id;

    RAISE NOTICE 'Factura % cancelada exitosamente y stock devuelto de productos no entregados', v_bill_id;
END;
$$; 







