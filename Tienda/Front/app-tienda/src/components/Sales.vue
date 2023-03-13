<template>
  <h1>ventas</h1>
</template>

<script>
export default {
name: "Sales",
  data: function () {
    return {
    };
  },
   methods: {
    producto() {
      NProgress.start();
      axios
        .get("http://127.0.0.1:8000/producto/")
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        })
        .then(() => NProgress.done());
    },
  },
}
</script>

<style>

</style>