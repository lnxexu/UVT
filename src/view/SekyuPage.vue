<script>
import { ref } from 'vue';
import bg from "../components/Background.vue";
import PopSekyu from '../components/PopupSekyu.vue'

export default {
  name: 'SekyuPage',
  components: { bg, PopSekyu },
  data() {
    return {
      name: ref('Jazmine Rose Quitoras'),
      section: ref('BSIT-2B'),
      studentID: ref(''),
      timeInput: ref(''),
      dateInput: ref(''),
      violationInput: ref(''),
      tableData: ref([]),
      isPopupOpen1: false,
      isPopupOpen2: false,
      isLoaded: false,
    };
  },
  methods: {
    addViolation() {
      if (this.validateInputs()) {
        this.tableData.push(this.getFormData());
        this.clearInputs();
      }
    },  
    addViolation2() {
      if (this.validateInputs()) {
        this.tableData.pop();
        this.tableData.push(this.getFormData());
      }
    },
    clearInputs() {
      this.name = '';
      this.section = '';
      this.studentID = '';
      this.timeInput = '';
      this.dateInput = '';
      this.violationInput = '';
    },
    togglePopup1() {
      if (this.validateInputs(true)) {
        this.isPopupOpen1 = true;
        this.addViolation2();
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
    validateInputs(skipAlerts = false) {
      const inputs = [
    { value: this.name, message: 'name' },
    { value: this.section, message: 'section' },
    { value: this.studentID, message: 'Student ID' },
    { value: this.timeInput, message: 'Time' },
    { value: this.dateInput, message: 'Date' },
    { value: this.violationInput, message: 'Violation' },
  ];
  for (const input of inputs) {
    if (!input.value.trim()) {
      if (!skipAlerts) alert(`Please enter ${input.message}.`);
      return false;
    }
  }
  return true;
},

    getFormData() {
      return {
        name: this.name.value,
        section: this.section.value,
        studentID: this.studentID.value,
        time: this.timeInput.value,
        date: this.dateInput.value,
        violation: this.violationInput.value,
      };
    },
  },
  mounted() {
    const visibilityDuration = 1000;
    setTimeout(() => {
      this.isLoaded = true;
      const loaderContainers = document.getElementsByClassName('loader-container');
      for (const container of loaderContainers) {
        container.classList.add('loaded');
      }
    }, visibilityDuration)  
  },
};

</script>

<template>
  <div class="loader-container" id="loader">
    <div class="loader"></div>
  </div>
<bg/>

<div class = "Sekyu-page-container">
  <div id="transparent"></div>
<div id="sekyu">
  <h1>SECURITY</h1>
</div>
<div id="container1">
  <div id = "id">
    <div id="image"></div>
    <div id="name">
      <h2 class="info">Jazmine Rose Quitoras</h2>
    </div>
    <div id="section">
      <h3 class="'info'">BSIT-2B</h3>
    </div>
  </div>
  <div id="container-content">
    <div id="header">
      <h2 id = "first">Student ID</h2>
      <input v-model="studentID" type="text" class="form-control" id = "stud" />
      <h2 id = "second">Violation</h2>
      <div class="btn-group">
        <div class="dropdown">
          <button type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown trigger
          </button>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Menu item 1</a></li>
            <li><a class="dropdown-item" href="#">Menu item 2</a></li>
            <li><a class="dropdown-item" href="#">Menu item 3</a></li>
          </ul>
        </div>
      </div>
      <h2 id = "third">If others please specify</h2>
      <div id="below-input">
        <input v-model="specify" type="text" class="form-control" />
      </div>
    </div>
  </div>
  <div id="buttons">
    <button type="button" @click="clearInputs()" id = "option1" class="btn btn-danger">Clear</button>
    <button type="button" @click="togglePopup1()"  id = "option2" class="btn btn-success">Send</button>
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
      <p>Time: {{ timeInput }}</p>
      <p>Date: {{ dateInput }}</p>
      <p>Violation: {{ violationInput }}</p>
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
  left: 4%;
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
  top: 70%;
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


</style>