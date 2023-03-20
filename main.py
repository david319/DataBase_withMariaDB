import mariadb
import pandas as pd
import openpyxl

conn = mariadb.connect(
    user="root",
    password="larap319",
    host="localhost",
    database="project")
cur = conn.cursor()

# Procedimiento almacenado CRUD de ajuste
#cur.execute("CREATE PROCEDURE sp_insertarAjuste (IN id_usuario INT, "
#            "IN fecha DATETIME, IN comentario TEXT, in usuario_creo INT, in fecha_creo DATETIME) "
#            "BEGIN DECLARE  fecha_creo DATETIME DEFAULT CURRENT_TIMESTAMP; declare usuario_creo INT default "
#            "id_usuario; INSERT INTO ajuste VALUES (id_ajuste, id_usuario, fecha, comentario, usuario_creo, "
#            "usuario_modifico, fecha_creo, fecha_modifico); END")
#
#cur.execute("CREATE PROCEDURE sp_actualizarAjuste (IN id INT, IN id_usuario INT, IN fecha DATETIME, "
#            "IN comentario TEXT, in usuario_creo INT, in fecha_creo DATETIME, in usuario_modifico INT, "
#            "in fecha_modifico DATETIME) BEGIN DECLARE fecha_modifico DATETIME DEFAULT CURRENT_TIMESTAMP; "
#            "declare usuario_modifico INT default id_usuario; UPDATE ajuste SET id_usuario = id_usuario, "
#            "fecha = fecha, comentario = comentario, usuario_modifico = usuario_modifico, fecha_modifico = "
#            "fecha_modifico WHERE id_ajuste = id; END")
#
#cur.execute("CREATE PROCEDURE sp_readAjuste (IN id INT) BEGIN SELECT * FROM ajuste WHERE id_ajuste = id; END")
#
#cur.execute("CREATE PROCEDURE sp_eliminarAjuste (IN id INT) BEGIN DELETE FROM ajuste WHERE id_ajuste = id; END")
#
## # Procedimiento almacenado CRUD de cliente
##
#cur.execute(
#    "CREATE PROCEDURE sp_insertarCliente (IN id_usuario INT, IN nombre VARCHAR(100), IN apellido VARCHAR(100), "
#    "IN usuario INT) BEGIN declare fecha_creo DATETIME default CURRENT_TIMESTAMP; "
#    "declare usuario_creo INT default id_usuario; INSERT INTO cliente VALUES (id_cliente, id_usuario, nombre, "
#    "apellido, usuario_creo, usuario_modifico, fecha_creo, fecha_modifico); END")
#
#cur.execute("CREATE PROCEDURE sp_actualizarCliente (IN id INT, IN nombre VARCHAR(100), IN apellido VARCHAR(100), "
#            "IN id_usuario int, IN usuario_modifico INT, IN fecha_modifico DATETIME) BEGIN declare fecha_modifico "
#            "DATETIME default CURRENT_TIMESTAMP; declare usuario_modifico INT default id_usuario; UPDATE cliente "
#            "SET nombre = nombre, apellido = apellido, usuario_modifico = usuario_modifico, fecha_modifico = "
#            "fecha_modifico WHERE id_cliente = id; END")
#
#cur.execute("CREATE PROCEDURE sp_readCliente (IN id INT) BEGIN SELECT * FROM cliente WHERE id_cliente = id; END")
#
#cur.execute("CREATE PROCEDURE sp_eliminarCliente (IN id INT) BEGIN DELETE FROM cliente WHERE id_cliente = id; END")
#
## Procedimiento almacenado CRUD de compra
#
#cur.execute("CREATE PROCEDURE sp_insertarCompra (IN id_proveedor INT, IN id_usuario INT, IN fecha DATETIME, "
#            "IN proveedor_compra VARCHAR(100), IN total double, IN usuario_creo INT, IN fecha_creo DATETIME) "
#            "BEGIN declare fecha_creo DATETIME default CURRENT_TIMESTAMP; declare usuario_creo INT default "
#            "id_usuario; INSERT INTO compra VALUES (id_compra, id_proveedor, id_usuario, fecha, proveedor_compra, "
#            "total, usuario_creo, usuario_modifico, fecha_creo, fecha_modifico); END")
#
#cur.execute("CREATE PROCEDURE sp_actualizarCompra (IN id INT, IN id_proveedor INT, IN id_usuario INT, "
#            "IN fecha DATETIME, IN proveedor_compra VARCHAR(100), IN total double, IN usuario_modifico INT, "
#            "IN fecha_modifico DATETIME) BEGIN declare fecha_modifico DATETIME default CURRENT_TIMESTAMP; "
#            "declare usuario_modifico INT default id_usuario; UPDATE compra SET id_proveedor = id_proveedor, "
#            "id_usuario = id_usuario, fecha = fecha, proveedor_compra = proveedor_compra, total = total, "
#            "usuario_modifico = usuario_modifico, fecha_modifico = fecha_modifico WHERE id_compra = id; END")
#
#cur.execute("CREATE PROCEDURE sp_readCompra (IN id INT) BEGIN SELECT * FROM compra WHERE id_compra = id; END")
#
#cur.execute("CREATE PROCEDURE sp_eliminarCompra (IN id INT) BEGIN DELETE FROM compra WHERE id_compra = id; END")
#
## Procedimiento almacenado CRUD de Factura
#
#cur.execute("CREATE PROCEDURE sp_insertarFactura (IN id_cliente_ INT, IN id_usuario_ INT, "
#            "IN fecha_ DATETIME, IN subtotal_ double, IN usuario_creo INT, IN fecha_creo DATETIME) "
#            "BEGIN declare impuesto_ double default 0.15 * subtotal_; declare descuento_ double default  0.10 * "
#            "subtotal_; declare total_ double default subtotal_ + impuesto_ - descuento_; "
#            "declare fecha_creo DATETIME default CURRENT_TIMESTAMP; declare usuario_creo INT default id_usuario_; "
#            "INSERT INTO factura VALUES (id_factura, id_cliente_, id_usuario_, fecha_, subtotal_, impuesto_, "
#            "descuento_, total_, usuario_creo, usuario_modifico, fecha_creo, fecha_modifico); END")
#
#cur.execute("CREATE PROCEDURE sp_actualizarFactura (IN id INT, IN id_cliente_ INT, IN id_usuario_ INT, "
#            "IN fecha_ DATETIME, IN subtotal_ double, IN usuario_modifico INT, IN fecha_modifico DATETIME) "
#            "BEGIN declare impuesto_ double default 0.15 * subtotal_; declare descuento_ double default  0.10 * "
#            "subtotal_; declare total_ double default subtotal_ + impuesto_ - descuento_; "
#            "declare fecha_modifico DATETIME default CURRENT_TIMESTAMP; declare usuario_modifico INT default "
#            "id_usuario_; UPDATE factura SET id_cliente = id_cliente_, id_usuario = id_usuario_, fecha = fecha_, "
#            "subtotal = subtotal_, impuesto = impuesto_, descuento = descuento_, total = total_, "
#            "usuario_modifico = usuario_modifico, fecha_modifico = fecha_modifico WHERE id_factura = id; END")
#
#cur.execute("CREATE PROCEDURE sp_readFactura (IN id INT) BEGIN SELECT * FROM factura WHERE id_factura = id; END")
#
#cur.execute("CREATE PROCEDURE sp_eliminarFactura (IN id INT) BEGIN DELETE FROM factura WHERE id_factura = id; END")
#
## Procedimiento almacenado CRUD de Producto
#cur.execute("CREATE PROCEDURE sp_insertarProducto (IN id_usuario INT, IN nombre VARCHAR(100), "
#            "IN costo double, IN categoria VARCHAR(100), IN marca VARCHAR(100), IN precio double, IN existenciaMin INT,"
#            "IN existenciaMax int, IN estado TINYINT, IN usuario_creo INT, IN fecha_creo DATETIME) "
#            "BEGIN declare fecha_creo DATETIME default CURRENT_TIMESTAMP; declare usuario_creo INT default id_usuario; "
#            "INSERT INTO producto VALUES (id_producto, id_usuario, nombre, costo, categoria, marca, precio, "
#            "existenciaMin, existenciaMax, estado, usuario_creo, usuario_modifico, fecha_creo, fecha_modifico); END")
#
#cur.execute("CREATE PROCEDURE sp_actualizarProducto (IN id INT, IN id_usuario INT, IN nombre VARCHAR(100), "
#            "IN costo double, IN categoria VARCHAR(100), IN marca VARCHAR(100), IN precio double, IN existenciaMin INT,"
#            "IN existenciaMax int, IN estado TINYINT, IN usuario_modifico INT, IN fecha_modifico DATETIME) "
#            "BEGIN declare fecha_modifico DATETIME default CURRENT_TIMESTAMP; declare usuario_modifico INT default "
#            "id_usuario; UPDATE producto SET id_usuario = id_usuario, nombre = nombre, costo = costo, categoria = "
#            "categoria, marca = marca, precio = precio, existencia_min = existenciaMin, existencia_max = existenciaMax,"
#            "estado = estado, usuario_modifico = usuario_modifico, fecha_modifico = fecha_modifico WHERE id_producto = "
#            "id; END")
#
#cur.execute("CREATE PROCEDURE sp_readProducto (IN id INT) BEGIN SELECT * FROM producto WHERE id_producto = id; END")
#
#cur.execute("CREATE PROCEDURE sp_eliminarProducto (IN id INT) BEGIN DELETE FROM producto WHERE id_producto = id; END")
##
## # Procedimiento almacenado CRUD de Proveedor
#cur.execute("CREATE PROCEDURE sp_insertarProveedor (IN id INT, IN id_usuario INT, IN nombre VARCHAR(100), IN direccion "
#            "VARCHAR(100), IN telefono VARCHAR(100), IN contacto VARCHAR(100), IN estado tinyint, IN usuario_creo INT, "
#            "IN fecha_creo DATETIME) BEGIN declare fecha_creo DATETIME default CURRENT_TIMESTAMP; declare usuario_creo "
#            "INT default id_usuario; INSERT INTO proveedor VALUES (id, id_usuario, nombre, direccion, telefono, "
#            "contacto, estado, usuario_creo, usuario_modifico, fecha_creo, fecha_modifico); END")
#
#cur.execute("CREATE PROCEDURE sp_actualizarProveedor (IN id INT, IN id_usuario INT, IN nombre VARCHAR(100), "
#            "IN direccion VARCHAR(100), IN telefono VARCHAR(100), IN contacto VARCHAR(100), IN estado tinyint, "
#            "IN usuario_modifico INT, IN fecha_modifico DATETIME) BEGIN declare fecha_modifico DATETIME default "
#            "CURRENT_TIMESTAMP; declare usuario_modifico INT default id_usuario; UPDATE proveedor SET id_usuario = "
#            "id_usuario, nombre = nombre, direccion = direccion, telefono = telefono, "
#            "nombre_contacto_principal = contacto, estado = estado, usuario_modifico = usuario_modifico, "
#            "fecha_modifico = fecha_modifico WHERE id_proveedor = id; END")
#
#cur.execute("CREATE PROCEDURE sp_readProveedor (IN id INT) BEGIN SELECT * FROM proveedor WHERE id_proveedor = id; END")
#
#cur.execute(
#    "CREATE PROCEDURE sp_eliminarProveedor (IN id INT) BEGIN DELETE FROM proveedor WHERE id_proveedor = id; END")
#
## # Procedimiento almacenado CRUD de Rol
#cur.execute("CREATE PROCEDURE sp_insertarRol (IN nombre VARCHAR(100), IN usuario_creo INT "
#            ") BEGIN declare fecha_creo DATETIME default CURRENT_TIMESTAMP; insert into rol "
#            "values (id_rol, nombre, usuario_creo, usuario_modifico, fecha_creo, fecha_modifico); END")
#
#cur.execute("CREATE PROCEDURE sp_actualizarRol (IN id INT, IN nombre VARCHAR(100), in id_usuario INT "
#            " ) BEGIN declare fecha_modifico DATETIME default CURRENT_TIMESTAMP; declare usuario_modifico INT default "
#            "id_usuario; update rol set nombre = nombre, usuario_modifico = usuario_modifico, fecha_modifico = "
#            "fecha_modifico where id_rol = id; END")
#
#cur.execute("CREATE PROCEDURE sp_readRol (IN id INT) BEGIN SELECT * FROM rol WHERE id_rol = id; END")
#
#cur.execute("CREATE PROCEDURE sp_eliminarRol (IN id INT) BEGIN DELETE FROM rol WHERE id_rol = id; END")
#
## # Procedimiento almacenado CRUD de Privilegio
#cur.execute("CREATE PROCEDURE sp_insertarPrivilegio (IN nombre VARCHAR(100), IN usuario_creo INT) "
#            "BEGIN declare fecha_creo DATETIME default CURRENT_TIMESTAMP; insert into privilegio "
#            "values (id_privilegio, nombre, usuario_creo, usuario_modifico, fecha_creo, fecha_modifico); END")
#
#cur.execute("CREATE PROCEDURE sp_actualizarPrivilegio (IN id INT, IN nombre VARCHAR(100), IN usuario_modifico INT) "
#            "BEGIN declare fecha_modifico DATETIME default CURRENT_TIMESTAMP; update privilegio set nombre = nombre, "
#            "usuario_modifico = usuario_modifico, fecha_modifico = fecha_modifico where id_privilegio = id; END")
#
#cur.execute("CREATE PROCEDURE sp_readPrivilegio (IN id INT) BEGIN SELECT * FROM privilegio WHERE id_privilegio = id; "
#            "END")
#
#cur.execute("CREATE PROCEDURE sp_eliminarPrivilegio (IN id INT) BEGIN DELETE FROM privilegio WHERE id_privilegio = id; "
#            "END")
#
## # Procedimiento almacenado CRUD de Usuario
#cur.execute("CREATE PROCEDURE sp_insertarUsuario (IN nombre VARCHAR(100), IN apellido VARCHAR(100), "
#            "IN usuario_creo INT) BEGIN declare fecha_creo DATETIME default CURRENT_TIMESTAMP; insert into usuario "
#            "values (id_usuario, nombre, apellido, usuario_creo, usuario_modifico, fecha_creo, fecha_modifico); END")
#
#cur.execute("CREATE PROCEDURE sp_actualizarUsuario (IN id INT, IN nombre VARCHAR(100), IN apellido VARCHAR(100), "
#            "IN usuario_modifico INT) BEGIN declare fecha_modifico DATETIME default CURRENT_TIMESTAMP; update usuario "
#            "set nombre = nombre, apellido = apellido, usuario_modifico = usuario_modifico, fecha_modifico = "
#            "fecha_modifico where id_usuario = id; END")
#
#cur.execute("CREATE PROCEDURE sp_readUsuario (IN id INT) BEGIN SELECT * FROM usuario WHERE id_usuario = id; END")
#
#cur.execute("CREATE PROCEDURE sp_eliminarUsuario (IN id INT) BEGIN DELETE FROM usuario WHERE id_usuario = id; END")

# Triggers para kardex
cur.execute("CREATE TRIGGER tr_insertarKardex AFTER INSERT ON kardex FOR EACH ROW BEGIN declare fecha_creo DATETIME "
            "default CURRENT_TIMESTAMP; declare usuario_creo INT default NEW.usuario_editor; SET @inventario_antes = "
            "(SELECT cantidad FROM producto WHERE id_producto = NEW.id_producto); SET @inventario_despues = "
            "@inventario_antes + NEW.cantidad; UPDATE producto SET cantidad = @inventario_despues WHERE "
            "id_producto = NEW.id_producto; insert into kardex values (id_kardex, NEW.id_producto, NEW.usuario_editor, "
            "NEW.nombre_operacion, NEW.cantidad, NEW.costo, NEW.precio, NEW.fecha, @inventario_antes, "
            "@inventario_despues, NEW.usuario_creo, NEW.usuario_modifico, fecha_creo, fecha_modifico); END")

cur.execute("CREATE TRIGGER tr_actualizarKardex AFTER UPDATE ON kardex FOR EACH ROW BEGIN declare fecha_modifico "
            "DATETIME default CURRENT_TIMESTAMP; declare usuario_modifico INT default NEW.usuario_editor; "
            "SET @inventario_antes = (SELECT cantidad FROM producto WHERE id_producto = NEW.id_producto); "
            "SET @inventario_despues = @inventario_antes + NEW.cantidad; UPDATE producto SET "
            "cantidad = @inventario_despues WHERE id_producto = NEW.id_producto; UPDATE kardex SET "
            "id_producto = NEW.id_producto, usuario_editor = NEW.usuario_editor, nombre_operacion = "
            "NEW.nombre_operacion, cantidad = NEW.cantidad, costo = NEW.costo, precio = NEW.precio, fecha = NEW.fecha, "
            "inventario_antes = @inventario_antes, inventario_despues = @inventario_despues, usuario_modifico = "
            "usuario_modifico, fecha_modifico = fecha_modifico WHERE id_kardex = NEW.id_kardex; END")

# Guardar la información de la tabla productos en una variable para pasarla a un excel
cur.execute("SELECT id_producto FROM producto")
idProducto = cur.fetchall()
cur.execute("SELECT id_usuario FROM producto")
idUsuario = cur.fetchall()
cur.execute("SELECT nombre FROM producto")
nombre = cur.fetchall()
cur.execute("SELECT costo FROM producto")
costo = cur.fetchall()
cur.execute("SELECT categoria FROM producto")
categoria = cur.fetchall()
cur.execute("SELECT marca FROM producto")
marca = cur.fetchall()
cur.execute("SELECT precio FROM producto")
precio = cur.fetchall()
cur.execute("SELECT existencia_min FROM producto")
existenciaMin = cur.fetchall()
cur.execute("SELECT existencia_max FROM producto")
existenciaMax = cur.fetchall()
cur.execute("SELECT estado FROM producto")
estado = cur.fetchall()
cur.execute("SELECT usuario_creo FROM producto")
usuarioCreo = cur.fetchall()
cur.execute("SELECT fecha_creo FROM producto")
fechaCreo = cur.fetchall()
cur.execute("SELECT usuario_modifico FROM producto")
usuarioModifico = cur.fetchall()
cur.execute("SELECT fecha_modifico FROM producto")
fechaModifico = cur.fetchall()

col1 = "ID Producto"
col2 = "ID Usuario"
col3 = "Nombre"
col4 = "Costo"
col5 = "Categoria"
col6 = "Marca"
col7 = "Precio"
col8 = "Existencia Minima"
col9 = "Existencia Maxima"
col10 = "Estado"
col11 = "Usuario Creo"
col12 = "Fecha Creo"
col13 = "Usuario Modifico"
col14 = "Fecha Modifico"

info = pd.DataFrame(
    {col1: idProducto, col2: idUsuario, col3: nombre, col4: costo, col5: categoria, col6: marca, col7: precio,
     col8: existenciaMin, col9: existenciaMax, col10: estado, col11: usuarioCreo, col12: fechaCreo,
     col13: usuarioModifico, col14: fechaModifico})

with pd.ExcelWriter("Reporte.xlsx", engine="openpyxl", mode="w") as writer:
    info.to_excel(writer, sheet_name="Reporte", index=False)

# commit the transaction
conn.commit()

# close the connection
conn.close()
