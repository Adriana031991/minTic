<template>
  <div class="cabecera">
    <div class="greetings">
      <h1>
        ¡Bienvenido!
        <span> {{ userData.name }} </span>
      </h1>
      <div class="seccion">
        <button v-on:click="redirectToProducts()">Productos</button>

        <button v-on:click="redirectToBill()">Facturación</button>

        <button v-on:click="redirectToSales()">Venta</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import NProgress from "nprogress";
import { useAuthStore } from "../store/auth";

export default {
  name: "Home",
  data: function () {
    return {
      authStore: useAuthStore(),
      userData: null,
    };
  },

  created() {
    NProgress.start();
    this.getUserData()
      .then((data) => (console.log(data), (this.userData = data)))
      .catch((error) => {
        if (error.response.status === 401) {
          this.refreshToken().then(() => {
            this.getUserData().then((data) => (this.userData = data));
          });
        } else {
          this.redirectToSignIn();
        }
      })
      .then(() => NProgress.done());
  },

  methods: {
    getUserData() {
      return axios
        .get("http://127.0.0.1:8000/user/detailview/", {
          headers: {
            Authorization: `Bearer ${this.authStore.currentUser.access}`,
          },
        })
        .then((response) => response.data);
    },
    refreshToken() {
      const refresh = this.authStore.currentUser.refresh;

      axios
        .post("http://127.0.0.1:8000/user/detailview/refresh/", { refresh })
        .then((response) => {
          // OBTIENE NUEVO TOKEN
          localStorage.setItem("access", response.data.access);
          this.authStore.$patch({
            currentUser: {
              access: response.data.access,
              refresh,
            },
          });
          console.log("New token:", response.data);
        })
        .catch(() => {
          this.redirectToSignIn();
        });
    },
    redirectToSignIn() {
      this.$router.push({ name: "logIn" });
    },
    redirectToProducts() {
      this.$router.push({ name: "Productos" });
    },
    redirectToSales() {
      this.$router.push({ name: "Sales" });
    },
    redirectToBill() {
      this.$router.push({ name: "Bill" });
    },
  },
};
</script>

<style>
.cabecera {
  margin: 0;
  padding: 0%;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.cabecera h1 {
  color: #283747;
  text-shadow: 7px 10px 11px #fafafa, -4px -6px 31px #fafafa;
  margin: 28px 0px;
  font-weight: 600;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.cabecera span {
  color: #191816;
  font-weight: 700;
}

.greetings {
  border: 1px solid #283747;
  border-radius: 10px;
  width: 85%;
  height: 85%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: rgb(167 165 165 / 53%);
}
.greetings button {
  font-size: 2.5rem;
  /* line-height: 110%; */
  margin: 11px 17px;
  /* text-shadow: 0px 6px 7px #fafafa, 0px -5px 7px #fafafa; */
  color: #283747;
  /* margin-bottom: -30px; */
  background-color: rgb(255 255 255 / 70%);
  border-radius: 6px;
  border: 1px solid black;
  padding: 10px;
}

.seccion {
  margin: 0;
  padding: 0;
  border-radius: 15px;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  align-content: center;
  cursor: pointer;
}
</style>