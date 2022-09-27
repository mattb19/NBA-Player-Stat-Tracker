<style scoped>
.addmargin {
  margin-top: 10px;
  margin-bottom: 10px;
}

.nba-logo {
  background-color: #17408b;
}

.btn {
  background-color: #000000;
}

.col-md-6 {
  margin-top: 20px;
  margin-bottom: 20px;
}
</style>

<template>
  <div class="home">
    <div class="nba-logo">
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/lux/bootstrap.min.css"
        integrity="sha384-9+PGKSqjRdkeAU7Eu4nkJU8RFaH8ace8HGXnkiKMP9I9Te0GJ4/km3L1Z8tXigpG"
        crossorigin="anonymous"
      />
      <img
        src="../assets/nba-logo-transparent.png"
        width="80px"
        height="176px"
      />
    </div>
    <div class="col-md-6 centeralign">
      <p>{{ msg }}</p>
    </div>
    <div class="row">
      <div class="col-sm-12">
        <button type="button" class="btn btn-info btn-lg">Compare</button>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Player</th>
              <th scope="col">W/L</th>
              <th scope="col">PPG</th>
              <th scope="col">Select</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td></td>
              <td></td>
              <td></td>
              <td>
                <button type="button" class="btn btn-info btn-sm">
                  Select
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      msg: "",
    };
  },
  methods: {
    getResponse() {
      const path = "http://127.0.0.1:5000/players";
      axios
        .get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  created() {
    this.getResponse();
  },
};
</script>
