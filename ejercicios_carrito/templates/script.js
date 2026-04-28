// Lista de productos
const productos = [
  { id: 1, nombre: "Laptop", precio: 500, imagen: "../img/laptop.jpg" },
  { id: 2, nombre: "Mouse", precio: 20, imagen: "../img/mouse.jpg" },
  { id: 3, nombre: "Teclado", precio: 30, imagen: "../img/teclado.jpg" },
  { id: 4, nombre: "Camara", precio: 150, imagen: "../img/camara.jpg" },
  { id: 5, nombre: "Parlantes", precio: 80, imagen: "../img/parlantes.jpg" },
  { id: 6, nombre: "Audifonos", precio: 60, imagen: "../img/audifonos.jpg" }
];

// Carrito
let carrito = [];

// Mostrar productos
function mostrarProductos() {
  const contenedor = document.getElementById("productos");

  productos.forEach(p => {
    contenedor.innerHTML += `
        <div class="producto">
        <img src="${p.imagen}">
        <p>${p.nombre}</p>

        <div class="fila">
        <span>$${p.precio}</span>
        <button onclick="agregar(${p.id})">Agregar</button>
        </div>

    </div>
    `;
  });
}

// Agregar al carrito
function agregar(id) {
  const producto = productos.find(p => p.id === id);
  const existe = carrito.find(p => p.id === id);

  if (existe) {
    existe.cantidad++;
  } else {
    carrito.push({ ...producto, cantidad: 1 });
  }

  actualizarCarrito();
}

// Actualizar carrito
function actualizarCarrito() {
  const contenedor = document.getElementById("carrito");
  contenedor.innerHTML = "";

  let total = 0;

  carrito.forEach(p => {
    total += p.precio * p.cantidad;

    contenedor.innerHTML += `
      <div>
        ${p.nombre} - $${p.precio} x ${p.cantidad}
      </div>
    `;
  });

  document.getElementById("total").textContent = total;

  // Guardar en el navegador
  localStorage.setItem("carrito", JSON.stringify(carrito));
  
}

// Cargar datos guardados
function cargarCarrito() {
  const data = localStorage.getItem("carrito");

  if (data) {
    carrito = JSON.parse(data);
    actualizarCarrito();
  }
}

// Inicializar
mostrarProductos();
cargarCarrito();