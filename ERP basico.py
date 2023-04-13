# Importar librerías
import datetime

# Definir clase Compra
class Compra:
  def __init__(self, id, proveedor, productos, fecha):
    self.id = id
    self.proveedor = proveedor
    self.productos = productos
    self.fecha = fecha

  def total(self):
    return sum([producto.precio_compra for producto in self.productos])

# Definir clase Producto
class Producto:
  def __init__(self, id, nombre, descripcion, precio_compra, precio_venta, stock):
    self.id = id
    self.nombre = nombre
    self.descripcion = descripcion
    self.precio_compra = precio_compra
    self.precio_venta = precio_venta
    self.stock = stock

# Definir clase Venta
class Venta:
  def __init__(self, id, cliente, productos, fecha):
    self.id = id
    self.cliente = cliente
    self.productos = productos
    self.fecha = fecha

  def total(self):
    return sum([producto.precio_venta for producto in self.productos])

# Definir clase Inventario
class Inventario:
  def __init__(self):
    self.compras = []
    self.productos = []
    self.ventas = []

  def agregar_compra(self, proveedor, productos):
    id = len(self.compras) + 1
    fecha = datetime.datetime.now()
    compra = Compra(id, proveedor, productos, fecha)
    self.compras.append(compra)
    for producto in productos:
      if producto in self.productos:
        index = self.productos.index(producto)
        self.productos[index].stock += producto.stock
      else:
        self.productos.append(producto)

  def agregar_venta(self, cliente, productos):
    id = len(self.ventas) + 1
    fecha = datetime.datetime.now()
    venta = Venta(id, cliente, productos, fecha)
    self.ventas.append(venta)
    for producto in productos:
      index = self.productos.index(producto)
      self.productos[index].stock -= producto.stock

  def listar_productos(self):
    for producto in self.productos:
      print(f"{producto.nombre}: {producto.stock} unidades")

# Crear instancia de Inventario
inventario = Inventario()

# Crear instancia de Proveedor
proveedor = "Proveedor 1"

# Crear instancia de Productos
producto1 = Producto(1, "Producto 1", "Descripción del producto 1", 10.0, 20.0, 50)
producto2 = Producto(2, "Producto 2", "Descripción del producto 2", 15.0, 25.0, 30)

# Agregar productos a compra
productos_compra = [producto1, producto2]

# Agregar compra a inventario
inventario.agregar_compra(proveedor, productos_compra)

# Crear instancia de Cliente
cliente = "Cliente 1"

# Crear instancia de Productos
producto3 = Producto(3, "Producto 3", "Descripción del producto 3", 20.0, 30.0, 10)
producto4 = Producto(4, "Producto 4", "Descripción del producto 4", 25.0, 35.0, 20)

# Agregar productos a venta
productos_venta = [producto3, producto4]

# Agregar