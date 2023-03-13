<template>
  <h1>facturas</h1>
</template>

<script>
export default {
name: "Bill",
  data: function () {
    return {
    };
  },
   methods: {
    producto() {
      NProgress.start();
      axios
        .get("http://127.0.0.1:8000/facturas/")
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