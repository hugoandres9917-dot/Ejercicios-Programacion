--Ejercicio 3: Transacción de Retorno de Productos

--Construya una transacción para procesar la devolución de uno o varios productos. La transacción debe seguir este flujo:
--Verificar que la factura existe en la base de datos.
--Aumentar el stock de los productos en la cantidad que se registró en la compra.
--Modificar la factura original para marcarla con el estado de "Retornada"

--agregar columna de status a la tabla de bills 
-- para asignar el estado de la factura (Activa, Retornada, etc)

ALTER TABLE Bills
ADD COLUMN status VARCHAR(20) DEFAULT 'Activa';


--ejercicio3_transaccion_de_retorno_de_producto

DO $$
DECLARE
    v_bill_id INT := 1; --factura que se requiere retornar
    v_products RECORD;
BEGIN
    --validar que la factura existe
    IF NOT EXISTS (SELECT 1 FROM Bills WHERE bill_id = v_bill_id) THEN
        RAISE EXCEPTION ' La factura % no existe', v_bill_id;
    END IF;

    --Recorrer los productos de la factura
    FOR v_products IN
        SELECT product_id, quantity
        FROM Bill_Details
        WHERE bill_id = v_bill_id
    LOOP
        --Aumentar el stock segun la cantidad devuelta
        UPDATE Products
        SET stock = stock + v_products.quantity
        WHERE product_id = v_products.product_id;
    END LOOP;

    --Marcar la factura como Retornada
    UPDATE Bills
    SET total = 0,
    bill_date = CURRENT_TIMESTAMP,
    status = 'Retornada'
    WHERE bill_id = v_bill_id;

    RAISE NOTICE 'Factura % marcada como Retornada y stock actualizado', v_bill_id;
END;
$$;

--pendiente de revision 
