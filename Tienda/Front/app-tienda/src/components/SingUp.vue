<template>
  <div class="signUp_user">
    <div class="container_signUp_user">
      <h2>Registrarse</h2>
      <form  @submit.prevent="createUser()">
        <input type="text" v-model="user.username" placeholder="Username" />
        <br />
        <input type="password" v-model="user.password" placeholder="Password" />
        <br />
        <input type="text" v-model="user.name" placeholder="Name" />
        <br />
        <input type="email" v-model="user.email" placeholder="Email" />
        <br />

        <br />
        <button type="submit">Registrarse</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import NProgress from "nprogress";
import { useAuthStore } from '../store/auth';

export default {
  name: "SignUp",
  data: function () {
    return {
      
      authStore: useAuthStore(),
      user: {
        username: "",
        password: "",
        name: "",
        email: "",
      },
      
    };
  },
  methods: {
    createUser() {
      const user = {
        ...this.user
      };


      NProgress.start();
      axios
        .post("http://127.0.0.1:8000/user/", user)
        .then((result) => {
          console.log(result)
          this.authStore.setUser(result.data);
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
.signUp_user {
  margin: 0;
  padding: 0%;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.container_signUp_user {
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
.signUp_user h2 {
  color: #283747;
  text-shadow: 2px 2px 9px rgb(255, 255, 255), -2px -2px 9px rgb(255, 255, 255);
  font-size: 2rem;
  margin: 0;
}
.signUp_user form {
  width: 70%;
}

.signUp_user input {
  height: 40px;
  width: 100%;
  box-sizing: border-box;
  padding: 10px 20px;
  margin: 5px 0;
  border: 1px solid #283747;
}
.signUp_user button {
  width: 100%;
  height: 40px;
  color: #e5e7e9;
  background: #1a72dd;
  border: 1px solid black;
  border-radius: 5px;
  padding: 10px 25px;
  margin: 5px 0 25px 0;
}

.signUp_user button:hover {
  color: #e5e7e9;
  background: crimson;
  border: 1px solid #283747;
}
</style>