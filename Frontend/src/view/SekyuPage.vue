<script>
import { ref } from 'vue';
import bg from "../components/Background.vue";
import PopSekyu from '../components/PopupSekyu.vue';
import PopupComponent from '../components/Popup.vue'; 
import axios from "axios";

export default {
  name: 'SekyuPage',
  components: { bg, PopSekyu, PopupComponent }, 
  data() {
    return {
      name: 'Jazmine Rose Quitoras',
      section: 'BSIT-2B',
      studentID: '220000000351',
      violationInput: '',
      currentDateTime: '',
      specify: '',
      tableData: [{}],
      isPopupOpen1: false,
      isPopupOpen2: false,
      isLoaded: false,
      Popup: false,
      error1: false,
      error2: false,
      error3: false,
      error4: false,
      error5: false,
      invalid: false,
      responseData: null
    };
  },
  mounted() {
    this.updateDateTime();
    const visibilityDuration = 1000;
    setInterval(this.updateDateTime, 1000);
    setTimeout(() => {
      this.isLoaded = true;
      const loaderContainers = document.getElementsByClassName('loader-container');
      for (const container of loaderContainers) {
        container.classList.add('loaded');
      }
    }, visibilityDuration);

  },
  methods: {
    async submitForm() {
      try {
        const response = await axios.post('http://127.0.0.1:5173/pending', {
          name: this.name,
          section: this.section,
          studentID: this.studentID,
          violation: this.violation,
          dateAndTime: this.dateAndTime,
          description: this.description
        })
        this.responseData = response.data
      } catch (error) {
        console.error(error)
      }
    },
    updateDateTime() {
      var currentDateTime = new Date();
      var year = currentDateTime.getFullYear();
      var month = ('0' + (currentDateTime.getMonth() + 1)).slice(-2);
      var day = ('0' + currentDateTime.getDate()).slice(-2);
      var hours = currentDateTime.getHours();
      var minutes = currentDateTime.getMinutes();
      var seconds = currentDateTime.getSeconds();
      hours = (hours < 10 ? "0" : "") + hours;
      minutes = (minutes < 10 ? "0" : "") + minutes;
      seconds = (seconds < 10 ? "0" : "") + seconds;
      this.currentDateTime = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
    },
    show() {
      document.querySelector('.hamburger').classList.toggle('open');
      document.querySelector('.navigation').classList.toggle('active');
    },
    clearInputs() {
      this.name = '';
      this.section = '';
      this.studentID = '';
      this.violationInput = '';
      this.specify = '';
      this.error1 = false;
      this.error2 = false;
      this.error3 = false;
      this.error4 = false;
      this.error5 = false;
      this.invalid = false;
    },
    togglePopup1() {
      if (this.validateInputs()) {
        this.isPopupOpen1 = true;
      }
    },
    togglePopup2() {
      this.isPopupOpen2 = true;
      this.clearInputs();
    },
    closePopup() {
      this.isPopupOpen1 = false;
      this.isPopupOpen2 = false;
      this.$emit('close');
    },
    showPopup(){
      this.Popup = !this.Popup;
    },
    validateInputs() {
      this.error1 = false;
      this.error2 = false;
      this.error3 = false;
      this.error4 = false;
      this.error5 = false;
      this.invalid = false;
      const trimmedName = this.name.trim();
      const trimmedSection = this.section.trim();
      const trimmedStudentID = this.studentID.trim();
      if(trimmedName === ''){
        this.error4 = true;
      }
      if(trimmedSection === ''){
        this.error5 = true;
      }
      if (trimmedStudentID === '') {
        this.error1 = true;
      } else if (!/^22000000\d{4}$/.test(trimmedStudentID)) {
        this.invalid = true;
      }
      if (!this.violationInput) {
        this.error2 = true;
      }
      if (!this.specify) {
        this.error3 = true;
      }
      return !(this.error1 || this.error2 || this.error3 || this.invalid || this.error4 || this.error5);
    }
  }
};
</script>



<template>
<div class="loader-container" id="loader">
  <div class="loader"></div>
</div>
<bg/>
<div class="Sekyu-page-container">
  <div class="navigation">
    <div class="overlay"></div>
    <button class="hamburger" @click="show()">
      <div id="bar1" class="bar"></div>
      <div id="bar2" class="bar"></div>
      <div id="bar3" class="bar"></div>
    </button>
    <div id="user">
      <img src="../assets/user.png" id="userIcon">
      <span>USERNAME</span>
    </div>
    <nav>
      <ul>
        <div @click="showReports()">
          <li><img src="../assets/bell.png" class="icon4">
            <a>Reports</a>
          </li>
        </div>
        <div @click="showHome()">
          <li><img src="../assets/homepage.png" class="icon1">
            <a>Home Page</a>
          </li>
        </div>
        <div @click="showPopup()">
          <li><img src="../assets/logout.png" class="icon5">
            <a>Log Out</a>
          </li>
        </div>
      </ul>
    </nav>
  </div>
  <div id="transparent"></div>
  <div id="sekyu">
    <h1>SECURITY</h1>
  </div>
  <div id="container1">
    <div id="id">
      <div id="image"></div>
      <div id="name">
        <h2 class="info">
          <textarea  v-model = 'name' readonly="readonly">{{ name }}</textarea>
        </h2>
        <span v-if="error4" class="error" id="error4">No name</span>
      </div>
      <div id="section">
        <h3 class="info">
          <textarea  v-model = 'section' readonly="readonly">{{ section }}</textarea>
        </h3>
        <span v-if="error5" class="error" id="error5">No section</span>
      </div>
    </div>
    <div id="container-content">
      <form class="needs-validation" @submit.prevent="submitForm" ref="form" novalidate>
        <div id="header">
          <h2 id="first">Student ID</h2>
          <input v-model="studentID" type="text" class="form-control" id="stud" required pattern="22000000\d{4}" @input="validateInputs" readonly="readonly"/>
          <span v-if="error1" class="error" id="error1">This field is required.</span>
          <span v-if="invalid" class="error" id="invalid">Invalid input</span>

          <h2 id="second">Violation</h2>
          <div class="btn-group">
            <select v-model="violationInput" id="display" class="form-select" aria-label="Default select example" @change="validateInputs">
              <option value="0" disabled selected>Select violation</option>
              <option value="Incomplete uniform">Incomplete uniform</option>
              <!-- Add your options here -->
            </select>
            <span v-if="error2" class="error" id="error2">This field is required.</span>
          </div>

          <h2 id="third">If others please specify</h2>
          <div id="below-input">
            <input v-model="specify" type="text" class="form-control" @input="validateInputs">
            <span v-if="error3" class="error" id="error3">This field is required. Type None if there are no Description</span>
          </div>
        </div>
        <div id="buttons">
          <button type="button" @click="clearInputs()" id="option1" class="btn btn-danger">Clear</button>
          <button type="submit" @click="togglePopup1()" id="option2" class="btn btn-success">Send</button>
        </div>
      </form>
    </div>
  </div>
</div>



<PopSekyu v-if="isPopupOpen1">
    <div class="popup-content">
      <p>
        Are you sure do you want to submit this report to the OSAD? 
        Kindly check the details before submitting the report.
      </p>
      <p>Student's Name : {{ name }}</p>
      <p>Student's Section : {{ section }}</p>
      <p>Student's ID : {{ studentID }}</p>
      <p>Date and Time: {{ currentDateTime }}</p>
      <p>Violation: {{ violationInput }}</p>
      <p>Description: {{ specify }}</p>
      <div class="options">
        <button type="button" @click="closePopup()" class="btn btn-danger back">Back</button>
        <button type="button" @click="togglePopup2() ,post()"  class="btn btn-success confirm">Confirm</button>
      </div>
    </div>
</PopSekyu>


<PopSekyu v-if="isPopupOpen2">
  <div class="content">
    <p>The report has been sent to the OSAD.</p>
    <div class="content-button">
    <button type="button" @click="closePopup()" class="btn btn-danger backAll">Back</button>
    </div>
  </div>
</PopSekyu>

<div v-if="Popup" @close="closeContentPage">
  <popup />
</div>

</template>
<style scoped>
.Sekyu-page-container{
  overflow: hidden;
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  font-family: Arial, Helvetica, sans-serif;
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
#sekyu{
  color: #FFF;
  font-size: 100em;
  font-style: normal;
  font-weight: 300;
  position: absolute;
  top: 6.5%;
  left: 5.5%;
}
#container1 {
  width: 100%; 
  height: 73%; 
  background-color: #0D0D0D;
  color: white;
  position: absolute;
  top: 55.5%; 
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  box-sizing: border-box;
  min-width: 600px;
}
#container-content{
  width: 56.5%; 
  height: 46%;
  top: 17%;
  left: 37%;
  background-color: white;
  position: relative;
  border-radius: 20px;
  min-width: 600px;
  box-sizing: border-box;
}

#header h2{
  display: inline;
  color: white;
  background-color: #262626;
  padding: 0.156em 0.625em;
  margin: 1.563em;   
  border-radius: 5px;
  text-transform: uppercase;
}
#header #first{   
    position: fixed;
    top: 3.68em;
    left: 38%;
}
#header #second{   
    position: fixed;
    top: 3.67em;
    left: 68%;
} 
#header #third{   
    position: fixed;
    top: 8.5em;
    left: 38%;
}
.form-outline{
  position: fixed;
  border: rgb(189, 175, 175) 1px solid;  
  width: 70%;
  border-radius: 5px;
  margin: 0 1%;
}

 .cs-form{
    position: relative;
    margin: 0 1%;
    width: 70%;
    border-radius: 5px;
}
 .md-form {
    position: relative;  
    margin: 0 1%;
    width: 70%;
    border-radius: 5px;
}
#image{
    background: rgb(255, 255, 255);
    border-radius: 50%;
    width: 22%;
    height: 55%;
    position: fixed;
    top: 10%;
    left: 7%;
    min-width: 400px;
    box-sizing: border-box;
}
.form-control{
    position: fixed;
    height: 6.2%;
    width: 49%;
    top: 53%;
    left: 40.5%;
    border-radius: 5px;
}
#buttons{
  position: absolute;
  top: 120%;
}
#buttons #option1{
    position: fixed;
    left: 45%;
    width: 300px;
}
#option2{
    position: fixed;
    left: 70%;
    width: 300px;   
}
#label h3{
    color:white;
    padding: 10px;
    text-align: center;
}
#name{
    width: 640px;
    height: 40px;
    position: absolute;
    top:520px;
    display: flex;
    align-items: center;
    justify-content: center;
}
#id{
    width: 500px;
}
#section{
    width: 640px;
    height: 30px;   
    position: absolute;
    top:560px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.info {
    margin-bottom: 10px; 
}

.options{
    width: 100%;
    display: flex;
    justify-content: space-evenly;
}

.back, .confirm{
  width: 20%;
  height: 10%;
}
.content-button{
    width: 500px;
    display: flex;
  justify-content: center;

}
.backAll{
  width: 20%;
  height: 10%;

}
.popup-content {
  padding: 20px;
}
.popup-content p{
  font: 1.4em sans-serif;
  font-weight: 500;
}
  
button {
    padding: 10px;
    font-size: 16px;
    cursor: pointer;
  }
  .content p{
    display: flex;
    justify-content: center;
  }
  .loader-container {
    position: fixed;
    width: 100%;
    height: 100%;
    background: rgba(255, 255, 255, 0.9); 
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 9999;
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

.btn-group  {
  position: fixed;
  left: 70.4%;
  top: 14.68em;
  width: 19%;
  height: 6.2%;
}

#stud{
  position: fixed;
  left: 40.49%;
  top: 14.68em;
  width: 23%;
  height: 6.2%;
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

.navigation {
  position: fixed;
  left: -500px;
  width: 20%;
  height: 100%;
  background-color: black;
  transition: 0.5s;
  z-index: 5;
  top: 0;
}
.navigation ul li {
  color: white;
  text-transform: uppercase;
  list-style-type: none;
  padding: 1.5em 2em;
  border-bottom: 1pt solid #252525;
}
.navigation.active {
  left: 0;
}

#user {
  position: relative;
  top: 17%;
}

#userIcon {
  position: relative;
  left: 12%;
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

span {
  position: relative;
  left: 17%;
  color: #FFF;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  font-size: 30px;
  font-style: normal;
}
a {
  color: #FFF;
  text-align: center;
  text-decoration: none;
  font-size: 18px;
  position: relative;
  display: flex;
}
.error{
  position: fixed;
  color: #ff2121;
  font-size: small;
}
#error1{
  position: fixed;
  top: 37.5%;
  left: 40.5%;
}
#error3{
  position: fixed;
  top: 59.3%;
  left: 40.5%;
}
#error2{
  position: fixed;
  top: 37.5%;
  left: 70.52%;
}
#error4{
  display: flex;
  align-items: center;
  justify-content: center;
}
#error5{
  display: flex;
  align-items: center;
  justify-content: center;
}
#invalid{
  position: fixed;
  top: 37.5%;
  left: 40.5%;
}


</style>