import mariadb

conn = mariadb.connect(
    user="root",
    password="larap319",
    host="localhost",
    database="project")
cur = conn.cursor()

# Procedimiento almacenado CRUD de ajuste
cur.execute("CREATE PROCEDURE insertarAjuste (IN id INT, IN id_detalle_ajuste VARCHAR(100), IN id_usuario INT, "
            "IN fecha DATETIME, IN comentario TEXT) BEGIN INSERT INTO ajuste VALUES (id_ajuste, id_detalle_ajuste, "
            "id_usuario, fecha, comentario); END")

cur.execute("CREATE PROCEDURE actualizarAjuste (IN id INT, IN id_detalle_ajuste VARCHAR(100), IN id_usuario INT, "
            "IN fecha DATETIME, IN comentario TEXT) BEGIN UPDATE ajuste SET id_detalle_ajuste = id_detalle_ajuste, "
            "id_usuario = id_usuario, fecha = fecha, comentario = comentario WHERE id_ajuste = id; END")

cur.execute("CREATE PROCEDURE eliminarAjuste (IN id INT) BEGIN DELETE FROM ajuste WHERE id_ajuste = id; END")

# Procedimiento almacenado CRUD de cliente

cur.execute(
    "CREATE PROCEDURE insertarCliente (IN id INT, IN nombre VARCHAR(100), IN apellido VARCHAR(100), IN id_usuario int) "
    "BEGIN INSERT INTO cliente VALUES (id_cliente, nombre, apellido, id_usuario); END")

cur.execute("CREATE PROCEDURE actualizarCliente (IN id INT, IN nombre VARCHAR(100), IN apellido VARCHAR(100), "
            "IN id_usuario int) BEGIN UPDATE cliente SET nombre = nombre, apellido = apellido, id_usuario = id_usuario "
            "WHERE id_cliente = id; END")

cur.execute("CREATE PROCEDURE eliminarCliente (IN id INT) BEGIN DELETE FROM cliente WHERE id_cliente = id; END")

# cur.execute("CREATE PROCEDURE eliminarCliente (IN nombre VARCHAR(100)) BEGIN DELETE FROM cliente WHERE "
#             "nombre = nombre; END")

# Procedimiento almacenado CRUD de compra

cur.execute("CREATE PROCEDURE insertarCompra (IN id INT, IN id_proveedor INT, IN id_usuario INT, IN fecha DATETIME, "
            "IN proveedor_compra VARCHAR(100), IN total double) BEGIN INSERT INTO compra VALUES (id_compra, "
            "id_proveedor, id_usuario, fecha, proveedor_compra, total); END")

cur.execute("CREATE PROCEDURE actualizarCompra (IN id INT, IN id_proveedor INT, IN id_usuario INT, IN fecha DATETIME, "
            "IN proveedor_compra VARCHAR(100), IN total double) BEGIN UPDATE compra SET id_proveedor = id_proveedor, "
            "id_usuario = id_usuario, fecha = fecha, proveedor_compra = proveedor_compra, total = total WHERE "
            "id_compra = id; END")

cur.execute("CREATE PROCEDURE eliminarCompra (IN id INT) BEGIN DELETE FROM compra WHERE id_compra = id; END")

# Procedimiento almacenado CRUD de Factura

cur.execute("CREATE PROCEDURE insertarFactura (IN id INT, IN id_cliente_ INT, IN id_usuario_ INT, IN fecha_ DATETIME, "
            "IN subtotal_ double) "
            "BEGIN declare impuesto_ double default 0.15 * subtotal_; declare descuento_ double default  0.10 * "
            "subtotal_; declare total_ double default subtotal_ + impuesto_ - descuento_; "
            "INSERT INTO factura(id_factura, id_cliente, id_usuario, fecha, subtotal, impuesto, descuento, total) "
            "VALUES (id, id_cliente_, id_usuario_, fecha_, subtotal_, impuesto_, descuento_, total_); "
            "END")

cur.execute("CREATE PROCEDURE actualizarFactura (IN id INT, IN id_cliente_ INT, IN id_usuario_ INT, IN fecha_ DATETIME,"
            "IN subtotal_ double) "
            "BEGIN declare impuesto_ double default 0.15 * subtotal_; declare descuento_ double default  0.10 * "
            "subtotal_; declare total_ double default subtotal_ + impuesto_ - descuento_; "
            "UPDATE factura SET id_cliente = id_cliente_, id_usuario = id_usuario_, fecha = fecha_, subtotal = "
            "subtotal_, impuesto = impuesto_, descuento = descuento_, total = total_ WHERE id_factura = id; "
            "END")

cur.execute("CREATE PROCEDURE eliminarFactura (IN id INT) BEGIN DELETE FROM factura WHERE id_factura = id; END")

# Procedimiento almacenado CRUD de Producto
cur.execute("CREATE PROCEDURE insertarProducto (IN id INT, IN id_usuario INT, IN nombre VARCHAR(100), IN costo double, "
            "IN categoria VARCHAR(100), IN marca VARCHAR(100), IN precio double, IN existenciaMin INT, "
            "IN existenciaMax int, IN estado TINYINT) BEGIN INSERT INTO producto VALUES (id_producto, id_usuario,"
            " nombre, costo, categoria, marca, precio, existenciaMin, existenciaMax, estado); END")

cur.execute("CREATE PROCEDURE actualizarProducto (IN id INT, IN id_usuario INT, IN nombre VARCHAR(100), "
            "IN costo double, IN categoria VARCHAR(100), IN marca VARCHAR(100), IN precio double, IN existenciaMin INT,"
            "IN existenciaMax int, IN estado TINYINT) BEGIN UPDATE producto SET id_usuario = id_usuario, nombre = "
            "nombre, costo = costo, categoria = categoria, marca = marca, precio = precio, existencia_min = "
            "existenciaMin, existencia_max = existenciaMax, estado = estado WHERE id_producto = id; END")

cur.execute("CREATE PROCEDURE eliminarProducto (IN id INT) BEGIN DELETE FROM producto WHERE id_producto = id; END")

# Procedimiento almacenado CRUD de Proveedor
cur.execute("CREATE PROCEDURE insertarProveedor (IN id INT, IN id_usuario INT, IN nombre VARCHAR(100), IN direccion "
            "VARCHAR(100), IN telefono VARCHAR(100), IN contacto VARCHAR(100), IN estado tinyint) "
            "BEGIN INSERT INTO proveedor VALUES (id_proveedor, id_usuario, nombre, direccion, telefono, contacto, "
            "estado); END")

cur.execute("CREATE PROCEDURE actualizarProveedor (IN id INT, IN id_usuario INT, IN nombre VARCHAR(100), IN direccion "
            "VARCHAR(100), IN telefono VARCHAR(100), IN contacto VARCHAR(100), IN estado tinyint) "
            "BEGIN UPDATE proveedor SET id_usuario = id_usuario, nombre = nombre, direccion = direccion, telefono = "
            "telefono, nombre_contacto_principal = contacto, estado = estado WHERE id_proveedor = id; END")

cur.execute("CREATE PROCEDURE eliminarProveedor (IN id INT) BEGIN DELETE FROM proveedor WHERE id_proveedor = id; END")

# Procedimiento almacenado CRUD de Rol
cur.execute("CREATE PROCEDURE insertarRol (IN id INT, IN nombre VARCHAR(100)) BEGIN INSERT INTO rol VALUES (id_rol, "
            "nombre); END")

cur.execute("CREATE PROCEDURE actualizarRol (IN id INT, IN nombre VARCHAR(100)) BEGIN UPDATE rol SET nombre = nombre "
            "WHERE id_rol = id; END")

cur.execute("CREATE PROCEDURE eliminarRol (IN id INT) BEGIN DELETE FROM rol WHERE id_rol = id; END")

# Procedimiento almacenado CRUD de Privilegio
cur.execute("CREATE PROCEDURE insertarPrivilegio (IN id INT, IN nombre VARCHAR(100)) BEGIN INSERT INTO privilegio "
            "VALUES (id_privilegio, nombre); END")

cur.execute("CREATE PROCEDURE actualizarPrivilegio (IN id INT, IN nombre VARCHAR(100)) BEGIN UPDATE privilegio SET "
            "nombre = nombre WHERE id_privilegio = id; END")

cur.execute("CREATE PROCEDURE eliminarPrivilegio (IN id INT) BEGIN DELETE FROM privilegio WHERE id_privilegio = id; "
            "END")

# Procedimiento almacenado CRUD de Usuario
cur.execute("CREATE PROCEDURE insertarUsuario (IN id INT, IN nombre VARCHAR(100), IN apellido VARCHAR(100)) BEGIN "
            "INSERT INTO usuario VALUES (id_usuario, nombre, apellido); END")

cur.execute("CREATE PROCEDURE actualizarUsuario (IN id INT, IN nombre VARCHAR(100), IN apellido VARCHAR(100)) BEGIN "
            "UPDATE usuario SET nombre = nombre, apellido = apellido WHERE id_usuario = id; END")

cur.execute("CREATE PROCEDURE eliminarUsuario (IN id INT) BEGIN DELETE FROM usuario WHERE id_usuario = id; END")

# commit the transaction
conn.commit()

# close the connection
conn.close()
