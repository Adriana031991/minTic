<template>
  <div class="cointainer-menu">
    <h3>Listado de productos</h3>
    <button @click="openForm()">Crear Producto</button>

    <div class="modal" id="modal-producto">
      <div class="modal-content">
        <form action="" @submit.prevent="crearProducto(id)">
          <div class="row">
            <div class="col m12 card-panel" >
              <span>Crear Producto</span>
              <div class="row">
                <div class="col m">
                  <label>ID</label>
                  <input type="number" disabled v-model="id" />
                </div>
                <div class="col m8">
                  <label>Nombre Producto</label>
                  <input type="text" v-model="nombre" />
                </div>
              </div>
              <div class="row">
                <div class="col m4">
                  <label>Categoria</label>
                  <input type="text" v-model="categoria" />
                </div>
                <div class="col m4">
                  <label>Marca</label>
                  <input type="text" v-model="marca" />
                </div>
              </div>
              <div class="row">
                <div class="col m4">
                  <label>Precio</label>
                  <input type="number" v-model="precio" />
                </div>
                <div class="col m4">
                  <label>Referencia</label>
                  <input type="text" v-model="ref" />
                </div>
              </div>
              <div class="row">
                <div class="col m4">
                  <label>Unidad de medida</label>
                  <input type="text" v-model="unidad_medida" />
                </div>
                <div class="col m4">
                  <label>Unidades disponibles </label>
                  <input type="number" v-model="unidades_disponibles" />
                </div>
              </div>
            </div>
            <div class="card-action bton">
              <button class="">
                <i class="material-icons">save</i>
                {{ id == 0 ? "Guardar" : "Actualizar" }}
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>

    <table class="centered container-table striped">
      <thead>
        <tr>
          <th>ID</th>
          <th>Nombre Producto</th>
          <th>Categoria</th>
          <th>Marca</th>
          <th>Precio</th>
          <th>Unidades Disponibles</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in paginate()" :key="item.nombre">
          <td>{{ item.id }}</td>
          <td>{{ item.nombre }}</td>
          <td>{{ item.categoria }}</td>
          <td>{{ item.marca }}</td>
          <td>{{ numberFormat(item.precio) }}</td>
          <td>{{ item.unidades_disponibles }}</td>
          <td>
            <button class="" @click="openForm2(item.id)">
              <i class="material-icons">create</i>
            </button>
            <button class="" @click="borrarProducto(item.id)">
              <i class="material-icons">delete</i>
            </button>
          </td>
        </tr>
      </tbody>
    </table>
    <ul class="pagination">
      <li v-bind:class="{ disabled: pageNumber == 1 }">
        <a href="#!" @click="previousPage()"
          ><i class="material-icons">chevron_left</i></a
        >
      </li>
      <li
        v-bind:class="{ active: page + 1 == pageNumber }"
        v-for="page in getPagination()"
        :key="page"
      >
        <a href="#!" @click="paginate(page + 1)">{{ page + 1 }}</a>
      </li>
      <li v-bind:class="{ disabled: pageNumber == totalPages }">
        <a href="#!" @click="nextPage()"
          ><i class="material-icons">chevron_right</i></a
        >
      </li>
    </ul>
  </div>
</template>


<script>
import axios from "axios";
import NProgress from "nprogress";
import M from "materialize-css";
import { useAuthStore } from "../store/auth";

export default {
  name: "Productos",
  data: function () {
    return {
      authStore: useAuthStore(),
      productos: [],
      productosFiltered: [],
      producto: {},
      id: 0,
      categoria: "",
      marca: "",
      nombre: "",
      precio: 0,
      ref: "",
      unidad_medida: "",
      unidades_disponibles: 0,

      modalCrear: false,
      modales: [],
      pageSize: 10,
      pageNumber: 1,
      totalPages: 0,
    };
  },
  computed: {},
  created: function () {
    this.listarProductos();
  },

  mounted() {
    var elems = document.querySelectorAll(".modal");
    this.modales = M.Modal.init(elems, null);
  },

  methods: {
    numberFormat(value) {
      const formatter = new Intl.NumberFormat("es-CO", {
        style: "currency",
        currency: "COP",
        minimumFractionDigits: 0,
      });

      return formatter.format(value);
    },

    paginate(newPage) {
      this.pageNumber = newPage ? newPage : this.pageNumber;
      return this.productos.slice(
        (this.pageNumber - 1) * this.pageSize,
        this.pageNumber * this.pageSize
      );
    },

    getPagination() {
      var pages = Math.round(this.productos.length / this.pageSize);

      this.totalPages = pages;
      return Array.from(Array(pages).keys());
    },
    nextPage() {
      if (this.pageNumber == this.totalPages) return;

      this.pageNumber++;
    },
    previousPage() {
      if (this.pageNumber == 1) return;

      this.pageNumber--;
    },

    openForm() {
      var modal_producto = M.Modal.getInstance(
        document.querySelector("#modal-producto")
      );
      modal_producto.open();
    },
    openForm2(id) {
      this.id = id || 0;
      var modal_producto = M.Modal.getInstance(
        document.querySelector("#modal-producto")
      );
      modal_producto.open();
    },

    listarProductos() {
      NProgress.start();
      axios
        .get("http://127.0.0.1:8000/producto/")
        .then((response) => {
          this.productos = [...response.data];
          console.log(this.productos);
        })
        .catch((error) => {
          console.log(error);
        })
        .then(() => NProgress.done());
    },
    crearProducto(id) {
      {
        var data = {
          categoria: this.categoria,
          marca: this.marca,
          nombre: this.nombre,
          precio: this.precio,
          ref: this.ref,
          unidad_medida: this.unidad_medida,
          unidades_disponibles: this.unidades_disponibles,
        };
      }
      let config = {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("access")}`,
        },
      };
      if(this.id == 0){

        axios
          .post("http://127.0.0.1:8000/producto/crear/", data, config)
          .then((response) => {
            console.log(response);
            this.id= response.data.id;
            this.categoria = response.data.categoria;
            this.marca = response.data.marca;
            this.nombre = response.data.nombre;
            this.precio = response.data.precio;
            this.ref = response.data.ref;
            this.unidad_medida = response.data.unidad_medida;
            this.unidades_disponibles = response.data.unidades_disponibles;
            this.listarProductos();
          })
          .catch((error) => {
            console.log(error);
          });
      
            } else {
              axios
        .put(`http://127.0.0.1:8000/producto/${id}/`,data, config)
        .then((response) => {
          console.log(response.data);
          this.categoria = response.data.categoria;
          this.marca = response.data.marca;
          this.nombre = response.data.nombre;
          this.precio = response.data.precio;
          this.ref = response.data.ref;
          this.unidad_medida = response.data.unidad_medida;
          this.unidades_disponibles = response.data.unidades_disponibles;
          this.listarProductos();
        })
        .catch((error) => {
          console.log(error);
        });
            }
    },
    borrarProducto(id) {
      axios
        .delete(`http://127.0.0.1:8000/producto/${id}/`, {
          headers: {
            Authorization: `Bearer ${this.authStore.currentUser.access}`,
          },
          })
        .then((response) => {
          console.log(response.data);
          this.listarProductos();
        })
        .catch((error) => {
          console.log(error);
        });
    }
  },
};
</script>

<style>
.cointainer-menu {
  position: absolute;
  top: 175px;
  right: 85px;
  background-color: rgb(167 165 165 / 53%);
  left: 125px;
  border-radius: 20px;
  box-shadow: 11px 16px 41px #e5e7e9;
}
.cointainer-menu h3 {
  color: white;
  font-size: 2rem;
  padding: 0 90px;
}

.cointainer-menu li {
  margin-left: 80px;
  font-size: 18px;
}

.container-table {
  margin: 0 0 12px 0px;
  background-color: rgb(255 255 255 / 70%);
}

.centrar-modal {
  z-index: 999999999;
}
</style>