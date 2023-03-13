<template>
  <div id="app" class="app">
    <div class="header">
      <h1>Tienda de la Esquina</h1>

      <nav>
        <button v-if="is_auth">Inicio</button>
        <button v-if="is_auth" v-on:click="loadAccount">Cuenta</button>
        <button v-if="is_auth">Cerrar Sesión</button>
        <button v-if="!is_auth" v-on:click="loadLogIn">Iniciar Sesión</button>
        <button v-if="!is_auth" v-on:click="loadSignUp">Registrarse</button>
      </nav>
    </div>

    <div class="main-component">
      <router-view
        v-on:completedLogIn="completedLogIn"
        v-on:completedSignUp="completedSignUp"
        v-on:logOut="logOut"
      >
      </router-view>
    </div>

    <div class="footer">
      <h2>
        <p>Misión TIC 2022</p>
        <p>Grupo 4</p>
      </h2>
    </div>
  </div>
</template>


<script>
export default {
  name: "App",

  data: function () {
    return { is_auth: false };
  },

  components: {},

  methods: {
    verifyAuth: function () {
      this.is_auth = localStorage.getItem("isAuth") || false;
      if (this.is_auth == false) this.$router.push({ name: "logIn" });
      else this.$router.push({ name: "home" });
    },

    loadLogIn: function () {
      this.$router.push({ name: "logIn" });
    },
    loadSignUp: function () {
      this.$router.push({ name: "signUp" });
    },

    completedLogIn: function (data) {
      localStorage.setItem("isAuth", true);
      localStorage.setItem("username", data.username);
      localStorage.setItem("token_access", data.token_access);
      localStorage.setItem("token_refresh", data.token_refresh);
      alert("Autenticación Exitosa");
      this.verifyAuth();
    },

    completedSignUp: function (data) {
      alert("Registro Exitoso");
      this.completedLogIn(data);
    },

    loadHome: function () {
      this.$router.push({ name: "home" });
    },

    logOut: function () {
      localStorage.clear();
      alert("Sesión Cerrada");
      this.verifyAuth();
    },

    loadAccount: function () {
      this.$router.push({ name: "account" });
    },
  },  
  created: function () {
    this.verifyAuth();
  },
};
</script>

<style>
body {
  margin: 0 0 0 0;
  font-family: "Varela Round", sans-serif;
  font-size: 14px;
}
.header {
  margin: 0%;
  padding: 0;
  width: 100%;
  height: 10vh;
  min-height: 100px;
  background-color: #1a72dd;
  color: #e5e7e9;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}
.header h1 {
  width: 35%;
  text-align: center;
  font-size:2.5em;
  /* line-height: 0; */
  margin: 0px;
}
.header nav {
  height: 100%;
  width: 20%;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  font-size: 20px;
  margin-right: 50px;
  color: transparent;
  background-color: transparent;
  box-shadow: 0 0 0 0 transparent;
}
.header nav button {
  color: #e5e7e9;
  background: #3669a0;
  border: 1px solid #e5e7e9;
  border-radius: 5px;
  padding: 10px 20px;
  margin-right: 8px;
  font-size: 1rem;
}

.header nav button:hover {
  color: #283747;
  background: #1a9fdd;
  border: 1px solid #e5e7e9;
  cursor: pointer;
}

.main-component {
  height: 75vh;
  margin: 0%;
  padding: 0%;
  background-image: url("https://business-intelligence.grupobit.net/hubfs/Imagen_BlogBIT_1600x478px_300719.jpg");
  background-size: cover;
  background-repeat: no-repeat;
}

.footer {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 10vh;
  min-height: 100px;
  background-color: #1a72dd;
  color: #e5e7e9;
}

.footer h2 {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  line-height: 0px;
  font-size:2.5em
}

.footer p {
  margin: 5px;
}
</style>