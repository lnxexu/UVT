<template>
<div class="loader-container" id="loader">
    <div class="loader"></div>
  </div>
  <div class = "OSAD-container">
    <div id="OSADcontainer">
    <div id="logoStack">
      <img src="../assets/logoUVT1.png" alt="logo" />
      <img src="../assets/logoUVT1.png" alt="logo" />
      <img src="../assets/logoUVT1.png" alt="logo" />

    </div>
<div class = "dashboard">
  <div class="dashboard-container">
    <hr>
    <div class="dashboard-item clock-item hover-effect">
      <div class="clock integral-font"><h1 style="font-size:70px;">{{ currentTime }}</h1></div>
      <div class="weather-info">
        <div class="temperature">{{ weather.temperature }}°C</div>
        <div class="condition">{{ weather.condition }}</div>
      </div>
    </div>

    <div class="dashboard-item reports-item hover-effect">
      <h2 class="integral-font ">Violation Reports Today</h2>
      <div class="reports-count">{{ violationReportsToday }}</div>
    </div>

    <h1 class = "name-dashboard integral-font"> dashboard</h1>

    <div class="dashboard-item guard-item hover-effect">
      <h2 class="integral-font ">Security Guard On Duty</h2>
      <div class="guard-name">{{ securityGuardName }}</div>
    </div>

    <div class="dashboard-item pending-reports-item hover-effect">
      <h2 class="integral-font">Pending Reports</h2>
      <div class="pending-reports-count"><h1>{{ pendingReportsCount }}</h1></div>
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
    <span>USERNAME</span>
  </div>
  <nav>
    <ul>
      <li><img src="../assets/bell.png" class = "icon4">
        <a @click = "showReports()">Reports</a>
      </li>
      <li><img src="../assets/homepage.png" class = "icon1">
        <a @click = "showHome()">Home Page</a></li>
      <li><img src="../assets/securityAccount.png" class = "icon2">
        <a @click = "showSecurityAccounts()">Security Accounts</a>
      </li>
      <li><img src="../assets/clock.png" class = "icon3">
        <a @click="showViolations()">Violation Tracker</a>
      </li>
      <li><img src="../assets/logout.png" class = "icon5">
        <a @click="showPopup()">Log Out</a>
      </li>
    </ul>
  </nav>
</div>
</div>
<div v-if="violations" @close="closeContentPage">
  <Violations />
</div>
<div v-if="SecurityAccounts" @close="closeContentPage">
  <SecurityAccounts />
</div>
<div v-if="Reports" @close="closeContentPage">
  <Reports />
</div>
<div v-if="Popup" @close="closeContentPage">
  <popup />
</div>


<bg/>
</template>

<script>
import bg from "../components/Background.vue";
import Popup from '../components/Popup.vue';
import Violations from '../components/Violations.vue';
import SecurityAccounts from "../components/SecurityAccounts.vue";
import Reports from "../components/Reports.vue";
import { ref } from 'vue';



export default {
  name: 'OSAD',
  components: { bg, Popup, Violations, SecurityAccounts, Reports },
  data() {
    return{
      violations: false,
      SecurityAccounts: false,
      Reports: false,
      Popup: false,
      violationReportsToday: 0,
      currentTime: this.getCurrentTime(),
      securityGuardName: 'Travis Scott', // Replace with actual data
      weather: {
        temperature: 25, // Replace with actual data
        condition: 'Sunny', // Replace with actual data
      },
      pendingReportsCount: 0,
      isLoaded: false,
    }
  },
  methods: {
    show() {
      document.querySelector('.hamburger').classList.toggle('open')
      document.querySelector('.navigation').classList.toggle('active')
    },
    showHome(){
      document.querySelector('.hamburger').classList.remove('open')
      document.querySelector('.navigation').classList.remove('active')
    },
    showViolations(){
      this.violations = !this.violations;
    },
    showSecurityAccounts(){
      this.SecurityAccounts = !this.SecurityAccounts;
    },
    showReports(){
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

    // Example method to fetch violation reports (replace with your actual implementation)
    fetchViolationReports() {
      // Assuming you have a backend API to fetch violation reports
      // Replace this with your actual API endpoint and logic
      // For simplicity, setting a hardcoded value here
      this.violationReportsToday = 10; // Replace with your actual data
    },
    fetchWeather() {
      // Assuming you have an API key and endpoint for weather data
      // Replace this with your actual API endpoint and logic
      // For simplicity, setting hardcoded values here
      this.weather = {
        temperature: 25,
        condition: 'Sunny',
      };
    },
    fetchPendingReportsCount() {
      // Assume you have an API call or some logic to fetch the count of pending reports
      // For example, you might fetch it from a backend API
      // Replace this with your actual logic
      setTimeout(() => {
        // Simulating an asynchronous operation
        this.pendingReportsCount = 5; // Replace with the actual count
      }, 1000);
    },
    updateClock() {
      // Update the clock every second
      setInterval(() => {
        this.currentTime = this.getCurrentTime();
      }, 1000);
    },
  },
  mounted() {
    this.fetchViolationReports();
    this.fetchWeather(); // Call the method to fetch weather information
    this.updateClock()
    this.fetchPendingReportsCount();
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
  height: 73%; 
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
  left: 0%;
  top: 0;
  opacity: 50%;
  border: #F2D8E4 5px solid;
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
  border-bottom: 1pt solid #252525;
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
  color: #333;
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
  background-color: #FFF;
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


</style>

