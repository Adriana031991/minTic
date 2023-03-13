<template>
  <div class="logIn_user">
    <div class="container_logIn_user">
      <h2>Iniciar sesión</h2>
      <div class="iconos">
        <a href="https://es-la.facebook.com/">
          <md-icon class="fa fa-facebook-square"></md-icon>
        </a>
        <a href="https://twitter.com/?lang=es">
          <md-icon class="fa fa-twitter-square"></md-icon>
        </a>
        <a href="https://www.google.com/">
          <md-icon class="fa fa-google"></md-icon>
        </a>
      </div>
      <form @submit.prevent="login()">
        <input type="text" v-model="user.username" placeholder="Username" />
        <br />
        <input type="password" v-model="user.password" placeholder="Password" />
        <br />
        <button type="submit">Iniciar Sesion</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import NProgress from "nprogress";
import { useAuthStore } from "../store/auth";

export default {
  name: "LogIn",
  data: function () {
    return {
      user: {
        username: "",
        password: "",
      },
      authStore: useAuthStore(),
    };
  },
  methods: {
    login() {
      NProgress.start();
      axios
        .post("http://127.0.0.1:8000/login/", this.user)
        .then((response) => {
          console.log(response);
          this.authStore.setUserLogin(response.data);
        })
        .catch((error) => {
          console.log(error);
        })
        .then(() => NProgress.done());
    },

  },
};
</script>

<style>
.logIn_user {
  margin: 0;
  padding: 0%;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.container_logIn_user {
  border: 1px solid #283747;
  border-radius: 10px;
  width: 40%;
  height: 80%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: rgb(167 165 165 / 53%);
}
.logIn_user h2 {
  color: #283747;
  text-shadow: 2px 2px 9px rgb(255, 255, 255), -2px -2px 9px rgb(255, 255, 255);
  padding: 10px;
  font-size: 2em;
}

.logIn_user form {
  width: 70%;
}

.logIn_user input {
  height: 40px;
  width: 100%;
  box-sizing: border-box;
  padding: 10px 20px;
  margin: 5px 0;
  border: 1px solid #283747;
}
.logIn_user button {
  width: 100%;
  height: 40px;
  color: #e5e7e9;
  background: #1a72dd;
  border: 1px solid black;
  border-radius: 5px;
  padding: 10px 25px;
  margin: 5px 0;
  font-size: 1.2em;
}
.logIn_user button:hover {
  color: #e5e7e9;
  background: crimson;
  border: 1px solid #283747;
}

.iconos {
  width: 100%;
  height: 50px;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  padding-bottom: 10px;
}

.iconos a {
  color: #1761b1;
  font-size: 2em;
  text-shadow: 2px 2px 9px rgb(255, 255, 255), -2px -2px 9px rgb(255, 255, 255);
}
</style>