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
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container-fluid">
            <a class="navbar-brand" href="http://localhost:8080/">PlayerStats</a>
            <button
                class="navbar-toggler"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#navbarColor02"
                aria-controls="navbarColor02"
                aria-expanded="false"
                aria-label="Toggle navigation"
            >
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarColor02">
                <ul class="navbar-nav me-auto">
                <li class="nav-item">
                    <a class="nav-link" href="/nba">NBA</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link active" href="/nfl">NFL</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/mlb">MLB</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/nhl">NHL</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/pga">PGA</a>
                </li>
                </ul>
            </div>
            </div>
        </nav>
    </div>
</template>