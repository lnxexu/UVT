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
    <div id="user" >
      <span id = "userSpan">Welcome {{ username }}!</span>
    </div>
    <nav>
      <ul>
        <div @click="showPopup()">
          <li><img src="../assets/logout.png" class="icon5">
            <a>Log Out</a>
          </li>
        </div>
      </ul>
    </nav>
  </div>
  <div id="transparent">
    <h1>SECURITY</h1>
  </div>
  <div id="container1">
    <div id="id">
      <div class="image">
        <input type="file" @change="onFileChange" accept="image/*" id="file" style="display: block;  position: fixed; top: 66%; left: 12.5%;">
        <img class="image" v-if="imageUrl" :src="imageUrl">
      </div>
      <div id="name">
        <h2 class="info">
          <input class = "stuInfo" v-model = 'name' readonly="readonly" />
        </h2>
        <span v-if="error4" class="error" id="error4">No name</span>
      </div>
      <div id="section">
        <h3 class="info">
          <input class = "stuInfo" v-model = 'section' readonly="readonly" />
        </h3>
        <span v-if="error5" class="error" id="error5">No section</span>
      </div>
    </div>
    <div id="container-content">
      <form class="needs-validation" @submit.prevent="submitForm()" ref="form" >
        <div id="header">
        
          <h2 id="first">Student ID</h2>
          <input v-model="studentID" type="text" class="form-control" id="stud" @input="validateInputs" />
          <button id="search" @click="getStudentInfo()"><i class="fa fa-search"></i></button>
          <span v-if="notFound" class="error" id = "notFound">Student not found.</span>
          <span v-if="error1" class="error" id="error1">This field is required.</span>
          <span v-if="invalid" class="error" id="invalid">Invalid input</span>

          <h2 id="second">Violation</h2>
          <div class="btn-group">
            <select v-model="violation" id="display" class="form-select" aria-label="Default select example" @change="validateInputs">
              <option value="" selected disabled hidden>Choose here</option>
              <option v-for="data in tableData2" :key="data.violationName" :value="data.violationName">{{ data.violationName }}</option>
            </select>
            <span v-if="error2" class="error" id="error2">This field is required.</span>
          </div>

          <h2 id="third">If others please specify</h2>
          <div id="below-input">
            <input v-model="description" type="text" class="form-control" @input="validateInputs">
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
      <p>Date and Time: {{ dateTime }}</p>
      <p>Violation: {{ violation }}</p>
      <p>Description: {{ description }}</p>
      <div class="options">
        <button type="button" @click="closePopup()" class="btn btn-danger back">Back</button>
        <button type="button" @click="togglePopup2()"  class="btn btn-success confirm">Confirm</button>
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
  <Popup @handlePopupClose="handlePopupClose"/>
</div>

</template>

<script>
import bg from "../components/Background2.vue";
import PopSekyu from '../components/PopupSekyu.vue';
import Popup from '../components/LogOutSekyu.vue';
import axios from "axios";

export default {
  name: 'SekyuPage',
  components: { bg, Popup, PopSekyu, axios }, 
  data() {
    return {
      name: '',
      section: '',
      studentID: '',
      violation: '',
      dateTime: '',
      description: '',
      tableData: [],
      tableData2: [],
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
      responseData: null,
      username: '',
      imageUrl: null,
      notFound: false,
      guard: "",
    };
  },
  mounted() {
    this.getViolation();
    this.getUsername();
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
    onFileChange(e) {
      const file = e.target.files[0];
      this.imageUrl = URL.createObjectURL(file);
    },
    getUsername() {
      axios.get(`http://127.0.0.1:8000/loginSekyu`)
        .then((response) => {
          this.username = response.data.fullName;
          console.log(response.data);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getStudentInfo() {
      const stud = this.studentID;
      if (!stud) {
        this.error1 = true;
        return;
      }
      if (!/^22000000\d{4}$/.test(stud)) {
        this.invalid = true;
        return;
      }
      const params = parseInt(stud);
      axios.get(`http://127.0.0.1:8000/student/${params}`)
        .then((response) => {
          console.log(response.data);
          this.name = response.data.name;
          this.section = response.data.section;
          this.error4 = false;
          this.error5 = false;
          this.notFound = false;
        })
        .catch((error) => {
          console.error(error);
          this.notFound = true;
        });
    },
    getViolation() {
      axios.get(`http://127.0.0.1:8000/violation`)
        .then((response) => {
          this.tableData2 = response.data;
          console.log(this.tableData2);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    handlePopupClose(value) {
      this.Popup = value;
    },
    showPopup(){
      this.Popup = !this.Popup;
    },
    submitForm() {
      const formData = {
        name: this.name,
        section: this.section,
        studentID: this.studentID,
        violation: this.violation,
        description: this.description,
        dateTime: this.dateTime,
        guard: this.username,
      };
      for (let key in formData) {
        if (!formData[key]) {
          console.error(`Missing value for ${key}`);
          return;
        }
      }
      const params = new URLSearchParams(formData).toString();
      axios.post(`http://127.0.0.1:8000/pendingAdd?${params}`)
        .then((response) => {
          this.tableData = response.data;
          console.log(response.data);
        })
        .catch((error) => {
          console.error(error);
        });
      },
    updateDateTime() {
      var dateTime = new Date();
      var year = dateTime.getFullYear();
      var month = ('0' + (dateTime.getMonth() + 1)).slice(-2);
      var day = ('0' + dateTime.getDate()).slice(-2);
      var hours = dateTime.getHours();
      var minutes = dateTime.getMinutes();
      var seconds = dateTime.getSeconds();
      hours = (hours < 10 ? "0" : "") + hours;
      minutes = (minutes < 10 ? "0" : "") + minutes;
      seconds = (seconds < 10 ? "0" : "") + seconds;
      this.dateTime = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
    },
    show() {
      document.querySelector('.hamburger').classList.toggle('open');
      document.querySelector('.navigation').classList.toggle('active');
    },
    clearInputs() {
      this.name = '';
      this.section = '';
      this.studentID = '';
      this.violation = '';
      this.description = '';
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
    closeContentPage(){
      this.Popup = false;
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
      if (!this.violation) {
        this.error2 = true;
      }
      if (!this.description) {
        this.error3 = true;
      }
      return !(this.error1 || this.error2 || this.error3 || this.invalid || this.error4 || this.error5);
    },

  }  
};
</script>
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
  /* transparent */
  background-color: rgba(0, 0, 0, 0.5);
  position: absolute;
  top: 9.3%; 
  left: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  flex-direction: column;
  align-items: center;  
  z-index: 1;
}
#transparent h1{
  color: white;
  font-size: 50px;
  font-weight: bold;
  position: fixed;
  top: 16%;
  left: 6%;
}

#container1 {
  width: 100%; 
  height: 73%; 
  background-color: #0D0D0D;
  color: white;
  position: absolute;
  top: 55.5%; 
  left: 49.999991%;
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
.image{
  background: rgb(255, 255, 255);
  border-radius: 50%;
  width: 22%;
  height: 55%;
  position: fixed;
  top: 10%;
  left: 7%;
  min-width: 400px;
  box-sizing: border-box;

  object-fit: cover;

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
  height: 15px;
  position: absolute;
  top: 520px;
  display: flex;
  align-items: center;
  justify-content: center;
}
#id{
  width: 500px;
}
#section{
  width: 640px;
  height: 15px;   
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
.hamburger,.bar {
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
  top: 13%;
  left: 0%;
  display: block;
  height: 15%;
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
#container-content #notFound{
  position: fixed;
  top: 37.5%;
  left: 40.5%;
}

#container-content #error1{
  position: fixed;
  top: 37.5%;
  left: 40.5%;
}
#container-content #error3{
  position: fixed;
  top: 59.3%;
  left: 40.5%;
}
#container-content #error2{
  position: fixed;
  top: 37.5%;
  left: 70.52%;
}
#container-content #error4{
  display: flex;
  align-items: center;
  justify-content: center;
}
#container-content #error5{
  display: flex;
  align-items: center;
  justify-content: center;
}
#container-content #invalid{
  position: fixed;
  top: 37.5%;
  left: 40.5%;
}
#container-content #search{
  position: fixed;
  top: 31.3%;
  left: 64%;
  height: 6%;
  width: 2%;
  border-radius: 5px;
}
.stuInfo{
  border: none;
  outline: none;
  background-color: transparent;
  color: #f3f3f3;
  text-align: center;
  height: 1.7em;
  width: 150%;
  left: -57%;
  position: fixed;
} 
* {font-family:"Raleway", sans-serif}
#userSpan {
  position: relative;
  top: 7%;
  left: 13%;
  display: flex;
  font-size: 20px;
  font-weight: bold;
  color: white;
}

</style>