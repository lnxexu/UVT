<template>
<div class="loader-container" id="loader">
  <div class="loader"></div>
</div>
<div class = "OSAD-container">
  <div id="OSADcontainer">
    <div id="logoStack">
      <img id="firstpic" src="../assets/UVT.png" alt="logo" />
      <img id="secondpic" src="../assets/UVT.png" alt="logo" />
 
    </div>
    <div class = "dashboard">
      <div class="dashboard-container">
        <hr>
        <div class="dashboard-item clock-item hover-effect">
          <div class="clock integral-font"><h1 style="font-size:70px;">{{ currentTime }}</h1></div>
          <div class="date">
            <h1 style="font-size: 40px; position: relative; top: 20%; left: -15%;">{{ new Date().toLocaleDateString() }}</h1>
          </div>
        </div>
        <div class="dashboard-item reports-item hover-effect">
          <h2 class="integral-font ">Violation Reports Today</h2>
          <div class="reports-count"><h1>{{ violationReportsToday }}</h1></div>
        </div>
        <h1 class = "name-dashboard integral-font"> dashboard</h1>
        <div class="dashboard-item guard-item hover-effect">
          <h2 class="integral-font ">Total Violation</h2>
          <div class="guard-name"><h1>{{ violationReportsTotal }}</h1></div>
        </div>
        <div class="dashboard-item pending-reports-item hover-effect">
          <h2 class="integral-font">Pending Reports</h2>
          <div class="pending-reports-count"><h1>{{ pendingViolationReports }}</h1></div>
        </div> 
      </div>
    </div>
  </div>
  <div id="transparent"></div>
  <div id="OSAD">
    <h1>OSAD</h1>
  </div>
  <div class="navigation">
    <div class="overlay"></div>
    <button class = "hamburger" @click="show()">
      <div id="bar1" class="bar"></div>
      <div id="bar2" class="bar"></div>
      <div id="bar3" class="bar"></div>
    </button>
    <div id = "user">
      <img src="../assets/user.png" id = "userIcon">
      <span>{{  }}</span>
    </div>
    <nav>
      <ul>
        <div id="1st" @click = "showReports()">
          <li><img src="../assets/bell.png" class = "icon4"><a>Reports</a></li>
        </div>
        <div id="2nd" @click = "showHome()">
          <li><img src="../assets/homepage.png" class = "icon1"><a>Home Page</a></li>
        </div>
        <div id="3rd" @click = "showSecurityAccounts()">
          <li><img src="../assets/securityAccount.png" class = "icon2"><a>Security Accounts</a></li>
        </div>
        <div id="4th"@click="showViolations()">
          <li><img src="../assets/clock.png" class = "icon3"><a>Violation Tracker</a></li>
        </div>
        <div id="5th" @click="showPopup()">
          <li><img src="../assets/logout.png" class = "icon5"><a>Log Out</a></li>
        </div>
      </ul>
    </nav>
  </div>
</div>
<div v-if="violationsPage" @close="closeContentPage">
  <Violations @handleViolationsPageClose="handleViolationsPageClose" />
</div>
<div v-if="SecurityAccounts" @close="closeContentPage">
  <SecurityAccounts @handleSecurityAccountsClose="handleSecurityAccountsClose" />
</div>
<div v-if="Reports" @close="closeContentPage">
  <Reports @handleReportClose="handleReportClose" />
</div>
<div v-if="Popup" @close="closeContentPage">
  <Popup @handlePopupClose="handlePopupClose"/>
</div>
<bg/>
</template>

<script>
import bg from "../components/Background.vue";
import Popup from '../components/LogOutOSAD.vue';
import Violations from '../components/Violations.vue';
import SecurityAccounts from "../components/SecurityAccounts.vue";
import Reports from "../components/Reports.vue";
import { ref } from 'vue';

export default {
  name: 'OSAD',
  components: { bg, Popup, Violations, SecurityAccounts, Reports },
  data() {
    return{
      violationsPage: false,
      SecurityAccounts: false,
      Reports: false,
      Popup: false,
      pendingViolationReports: '',
      violationReportsToday: 0,
      currentTime: this.getCurrentTime(),
      violationReportsTotal:'',
      isLoaded: false,
    }
  },
  methods: {
    handleReportClose(value) {
      this.Reports = value;
    },
    handleViolationsPageClose(value) {
      this.violationsPage = value;
    },
    handleSecurityAccountsClose(value) {
      this.SecurityAccounts = value;
    },
    handlePopupClose(value) {
      this.Popup = value;
    },
    show() {
      document.querySelector('.hamburger').classList.toggle('open')
      document.querySelector('.navigation').classList.toggle('active')
    },
    showHome(){
      document.querySelector('.hamburger').classList.remove('open')
      document.querySelector('.navigation').classList.remove('active')
    },
    showViolations(){
      this.violationsPage = !this.violationsPage;
      this.SecurityAccounts = false;
      this.Reports = false;
    },
    showSecurityAccounts(){
      this.violationsPage = false;
      this.SecurityAccounts = !this.SecurityAccounts;
      this.Reports = false;
    },
    showReports(){
      this.violationsPage = false;
      this.SecurityAccounts = false;
      this.Reports = !this.Reports;
    },
    showPopup(){
      this.Popup = !this.Popup;
    },
    closeContentPage(){
      this.contentPageVisible = false;
    },
    showHome(){
      document.querySelector('.hamburger').classList.remove('open')
      document.querySelector('.navigation').classList.remove('active')
    },
    getCurrentTime() {
      const now = new Date();
      const hours = now.getHours().toString().padStart(2, '0');
      const minutes = now.getMinutes().toString().padStart(2, '0');
      const seconds = now.getSeconds().toString().padStart(2, '0');
      return `${hours}:${minutes}:${seconds}`;
    },
    fetchPendingViolationReports() {
      axios.get("http://127.0.0.1:8000/pendingCount")
        .then((response) => {
          this.pendingViolationReports = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    fetchTotalViolation() {
      axios.get("http://127.0.0.1:8000/violationCount")
        .then((response) => {
          this.violationReportsTotal = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    updateClock() {
      setInterval(() => {
        this.currentTime = this.getCurrentTime();
      }, 1000);
    },
    
  },
  mounted() {
    this.fetchTotalViolation();
    this.fetchPendingViolationReports();
    this.updateClock()
    const visibilityDuration = 1000;
    setTimeout(() => {
      this.isLoaded = true;
      const loaderContainers = document.getElementsByClassName("loader-container");
      for (const container of loaderContainers) {
        container.classList.add("loaded");
      }
    }, visibilityDuration);
  },
  
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Integral+CF:wght@300;400;700&display=swap");
.OSAD-container{
  overflow: hidden;
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}
#OSAD{
  color: #FFF;
  font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  font-size: 100em; 
  font-weight: 300;
  position: absolute;
  top: 6.5%;
  left: 5%;
}
#transparent {
  width: 100%; 
  height: 10%; 
  background-color: #0D0D0D;
  position: absolute;
  top: 9.3%; 
  left: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  opacity: 40%;
}
#OSADcontainer {
  width: 100%; 
  height: 70%; 
  background-color:black;
  position: absolute;
  top: 55.5%; 
  left: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  flex-direction: column;
  align-items: center;  
}
#logoStack{
  display: flex;
  height: 95%;
  width: 100%; 
  margin: 2% 0;
  position: relative;
  right: 0;
  top: 0;
  opacity: 50%;
  border: #CE2774 5px solid;
} 
button {
  cursor: pointer;
  color: white;
  text-decoration: none;
}

nav {
  position: absolute;
  top: 30%;
  left: 35%;
  transform: translateX(-50%);
}

nav ul li {
  width: 130%;
  left: 2%;
  display: flex;
  align-items: center;
}

nav ul li img {
  margin-right: 27%;
}

a {
  color: #FFF;
  text-align: center;
  text-decoration: none;
  font-size: 18px;
  position: relative;
  display: flex;
}

nav ul li a::after {
  content: '';
  width: 0;
  height: 2px;
  background: #F2D8E4;
  position: absolute;
  left: 0;
  bottom: -6px;
  transition: 0.5s;
}

nav ul li a:hover::after {
  width: 100%;
}

.navigation {
  position: fixed;
  left: -500px;
  width: 20%;
  height: 100%;
  background-color: black;
  transition: 0.5s;
}

#user {
  position: relative;
  top: 17%;
}

#userIcon {
  position: relative;
  left: 12%;
}

span {
  position: relative;
  left: 17%;
  color: #FFF;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  font-size: 30px;
  font-style: normal;
}

.navigation ul li {
  color: white;
  text-transform: uppercase;
  list-style-type: none;
  padding: 1.5em 2em;
  border-bottom: 1pt solid #1b1a1a;
}

.hamburger,
.bar {
  position: fixed;
}

.hamburger {
  display: block;
  top: 5.5%;
  left: 2%;
  width: 40px;
  height: 4%;
  transform: translateY(50%);
  border: 0;
  background: 0 0;
}

.bar {
  top: 3px;
  background: #F2D8E4;
  width: 100%;
  height: 4px;
  transition: all 0.3s ease-in;
  border: black 1px solid;
}

#bar2 {
  top: 11px;
}

#bar3 {
  top: 19px;
}

.navigation.active {
  left: 0;
}

.hamburger.open #bar1 {
  background-color: white;
  transform: rotate(45deg) translate(6px, 5px);
}

.hamburger.open #bar2 {
  opacity: 0;
}

.hamburger.open #bar3 {
  background-color: white;
  transform: rotate(-45deg) translate(6px, -5px);
}
.dashboard-container {
  display: flex;
  justify-content: space-around;
  align-items: center;
  padding: 20px;
}

.integral-font {
  font-family: 'Integral CF', sans-serif;
  transition: transform 0.3s ease-in-out, background-color 0.3s ease-in-out, color 0.3s ease-in-out;
}

.hover-effect:hover {
  transform: scale(1.05);
  background-color: #000000;
  color: #fff;
}

.dashboard-item {
  text-align: center;
  padding: 20px;
  border-radius: 8px;
  border: 2px solid #CE2774;
  width: 200px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s ease-in-out, color 0.3s ease-in-out;
}

.reports-item {
  background-color: #c0c0c0;
  color: #333;
  position: absolute;
  top: 50%;
  width: 27%;
  height: 40%;
}

.reports-count {
  font-size: 2em;
  font-weight: bold;
}
hr{
  border: 2px solid;
}

.clock-item {
  background-color: #c0c0c0;
  color: #333;
  width: 90%;
  position: absolute;
  top: 23%;
  display: flex;
}
.clock-item h1{
  margin-left: 2.5em;

}

.guard-item {
  background-color: #c0c0c0;
  color: #333;
  position: absolute;
  top: 50%;
  right: 5%;
  width: 27%;
  height: 40%;
}

.pending-reports-item{
  background-color: #c0c0c0;
  color: #191717;
  position: absolute;
  top: 50%;
  left: 5%;
  width: 27%;
  height: 40%;
}

.weather-info {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-left: 5rem;
}

.temperature {
  font-size: 2em;
  font-weight: bold;
}

.condition {
  margin-left: 1em;
  font-size: 1em;
}

.name-dashboard{
  font-weight: bold;
  position: absolute;
  top: 5%;
  text-decoration: underline;
}


.dashboard{
  background-color: #F7DCE8;
  position: absolute;
  text-transform: uppercase;
  top: 10%;
  width: 50%;
  height: 80%;
  border-radius: 8px;
  
}

.loader-container {
  position: fixed;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.9); /* Semi-transparent white background */
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999; /* Make sure it's above your content */
}

.loader {
  border: 8px solid #f3f3f3;
  border-top: 8px solid #3498db;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.loaded{
  display: none;
  opacity: 0;
}     

#firstpic{
  position: fixed;
  left: 0.2%;
  height: 87.5%;
}
#secondpic{
  position: fixed;
  right: 0.2%;
  height: 87.5%;
}

</style>

