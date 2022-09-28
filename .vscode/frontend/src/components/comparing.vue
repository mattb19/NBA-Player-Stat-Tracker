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
        <div class="row">
          <div class="col-sm-12">
            <button type="button" class="btn btn-info btn-lg">Home</button>
          </div>
        </div>
      </div>
      <div class="row gtr-150">
							<div class="col-6 col-6-medium col-12-xsmall">
									<section id="content">
										
										<section>
											<h3>Player #1 Selected</h3>
											<ul>Stat</ul>
											<ul></ul>
											<ul></ul>
											<ul></ul>
											<ul></ul>
										</section>
										<section>
											<h3>Player #2 Selected</h3>
											<ul>Stat</ul>
											<ul></ul>
											<ul></ul>
											<ul></ul>
										</section>
								   </section>
								
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