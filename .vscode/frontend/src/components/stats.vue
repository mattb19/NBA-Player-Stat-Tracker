<style scoped>
.addmargin {
  margin-top: 10px;
  margin-bottom: 10px;
}

.nba-logo {
  background-color: #17408b;
}

.col-sm-12 {
  margin-right: 100px;
}

.home {
  background-color: #383c44;
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
        width="54px"
        height="118px"
      />
    </div>
    <div class="row">
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/lux/bootstrap.min.css"
        integrity="sha384-9+PGKSqjRdkeAU7Eu4nkJU8RFaH8ace8HGXnkiKMP9I9Te0GJ4/km3L1Z8tXigpG"
        crossorigin="anonymous"
      />
      <div class="col-sm-12 centeralign">
        <a href="http://localhost:8080/comparing" class="btn btn-outline-light"
          >Compare</a
        >
        <table class="table table-dark">
          <thead>
            <tr>
              <th scope="col">Team</th>
              <th scope="col">Player</th>
              <th scope="col">Age</th>
              <th scope="col">#</th>
              <th scope="col">GP</th>
              <th scope="col">Min</th>
              <th scope="col">FG%</th>
              <th scope="col">3P%</th>
              <th scope="col">FT%</th>
              <th scope="col">REB</th>
              <th scope="col">AST</th>
              <th scope="col">BLK</th>
              <th scope="col">STL</th>
              <th scope="col">PF</th>
              <th scope="col">TO</th>
              <th scope="col">PTS</th>
              <th scope="col"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(stats, index) in stats" :key="index">
              <td>
                <img
                  :src="require('../assets/' + stats.team + '.png')"
                  width="80px"
                  height="80px"
                />
              </td>
              <td>{{ stats.name }}</td>
              <td>{{ stats.age }}</td>
              <td>{{ stats.number }}</td>
              <td>{{ stats.gp }}</td>
              <td>{{ stats.min }}</td>
              <td>{{ stats.fgpercent }}</td>
              <td>{{ stats.threeptpercent }}</td>
              <td>{{ stats.ftpercent }}</td>
              <td>{{ stats.reb }}</td>
              <td>{{ stats.ast }}</td>
              <td>{{ stats.blk }}</td>
              <td>{{ stats.stl }}</td>
              <td>{{ stats.pf }}</td>
              <td>{{ stats.to }}</td>
              <td>{{ stats.pts }}</td>
              <td>
                <button type="button" class="btn btn-outline-light">
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
      stats: [],
    };
  },
  methods: {
    getStats() {
      const path = "http://127.0.0.1:5000/playerstats";
      axios
        .get(path)
        .then((res) => {
          this.stats = res.data.stats;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  created() {
    this.getStats();
  },
};
</script>
