<template>
    <div class="addViolation-list-container">
      <div class="w3-row">&nbsp;</div>
      <div class="w3-row">&nbsp;</div>
      
      <div class="exit-button" @click="$emit('close')">
        <div class="bar2"></div>
        <div class="bar2"></div>
      </div>
      
      <div class="main-content modal-content">
        <h1>Add Violation</h1>
        <hr>
        <div class="div">
          <div class="w3-half">
            <label for="violation">Violation:</label>
            <input type="text" id="violation" v-model="violationForm.violationName" required>
          </div>

          <div class="w3-rest">
            <label for="createdBy">Created By :</label>
            <input type="text" id="createdBy" v-model="violationForm.createdBy" required readonly/>
          </div>

          <div class="w3-rest">
            <label for="description">Description:</label>
            <textarea id="description" v-model="violationForm.description" required></textarea>
          </div>
          <div class="w3-half">
            <label for="category">Category:</label>
            <div class="radioButton">
                <label for="category">Minor</label>
                <input type="radio" id="category" v-model="violationForm.category" value="Minor" required>
                <label for="category">Major</label>
                <input type="radio" id="category" v-model="violationForm.category" value="Major" required>
            </div>
          </div>

          <div class="w3-row">
            <button class="add" @click="confirmModal()">Add Violation</button>
          </div>
        </div>
      </div>
      <div id="myModal" class="modal" v-if="confirm">
          <div class="modal-content1">
            <h2>Are you sure do you want to post this law?</h2>
            <hr>
              <p><strong>Violation: </strong> {{ violationForm.violationName }}</p>
              <p><strong>Description: </strong> {{ violationForm.description }}</p>
              <p><strong>Category: </strong> {{ violationForm.category }}</p>
              <p><strong>Date Created: </strong> {{ violationForm.dateCreated }}</p>
              <p><strong>Created By: </strong> {{ violationForm.createdBy }}</p>
              <div class="buttons">
                  <button id = "submit" @click="addViolation(),pass=true">Submit</button>
                  <button id = "back" @click="confirm=false">Back</button>
              </div>
          </div>
      </div>
                
      <div id="myModal" class="modal" v-if="pass">
        <div class="modal-content1">
          <p>Violation has been added successfully!</p>
          <button @click="pass=false, confirm=false">Close</button>
        </div>
      </div>
      </div>  
</template>

<script>
import axios from 'axios';
export default {
    data() {
      return {
        confirm: false,
        pass: false,
        violationForm: {
            violationName: '',
            description: '',
            category: '',
            dateCreated: new Date().toISOString(),
            createdBy: ''
        },
      };
    },
    mounted() {
      this.getUsername();
      this.formatDate();  
    },
    methods: {
        confirmModal() {
          if (this.violationForm.violationName === '' || this.violationForm.description === '' || this.violationForm.category === '') {
            alert('Please fill out all fields');
            return;
          }
          this.confirm = true;
        },
        addViolation() {
          let dateCreated = new Date();
          let isoString = dateCreated.toISOString();
          this.violationForm.dateCreated = isoString;

          const formData = this.violationForm;
          const params = new URLSearchParams(formData).toString();
          axios.post(`http://127.0.0.1:8000/violation?${params}`)
          .then(response => {
              console.log(response.data);
              this.violationForm = {
                  violation: '',
                  description: '',
                  category: '',
                  dateCreated: new Date().toISOString(),
                  createdBy: ''
              };
          })
          .catch(error => {
              console.error(error);
          });
        },
        getUsername() {
          axios.get(`http://127.0.0.1:8000/loginOSAD`)
          .then(response => {
              console.log(response.data);
              this.violationForm.createdBy = response.data.fullname;
              this.formatDate();
          })
          .catch(error => {
              console.error(error);
          });
        },
        formatDate(){
          let dateCreated = new Date();
          let isoString = dateCreated.toISOString();
          let dateParts = isoString.slice(0, 10).split('-');
          let timeParts = isoString.slice(11, 19).split(':');
          let months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
          let formattedDate = `${months[parseInt(dateParts[1]) - 1]} ${parseInt(dateParts[2])}, ${dateParts[0]} at ${timeParts[0]}:${timeParts[1]}:${timeParts[2]}`;
          this.violationForm.dateCreated = formattedDate;
        },

    },
};
</script>

<style scoped>
.addViolation-list-container {
  position: fixed;
  display: block;
  left: 0%;
  width: 100%;
  height: 100%;
  background-color: #f1f1f1;
  z-index: 2;
}

.exit-button {
  cursor: pointer;
  display: inline-block;
  margin: 10px;
  padding: 10px;
  background-color: #ddd;
  border-radius: 5px;
  position: relative;
  left: 95%;
}

.exit-button:hover {
  background-color: #ccc;
}

.bar2 {
  width: 20px;
  height: 2px;
  background-color: #333;
  margin: 5px 0;
}

.exit-button:hover {
  background-color: #ccc;
}
.main-content {
  flex: 1;
  padding: 20px;
}

h1 {
  color: #333;
  font-size: 2em;
}

label {
  margin: 10px 0;
  font-size: 1.2em;
  color: #555;
  font-weight: bold;
}

input[type="text"], textarea {
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1);
}

button {
  padding: 10px;
  margin: 10px 0;
  border: none;
  border-radius: 5px;
  background-color: #007BFF;
  color: #fff;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #0056b3;
}

.radioButton {
  display: flex;
  margin: 10px 0;
  position: absolute;
  justify-content: space-between;
  left: 15%;
  width: 70%;
  top: 71.5%;
}

.modal {
  position: absolute;
  z-index: 10;
  display: block;
  background-color: rgba(0, 0, 0, 0.4);
}

.modal-content {
  background-color: #fefefe;
  margin: 5% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 50%;
}


.modal-content1{
  background-color: #fefefe;
  margin: 5% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 40%;
  border-radius: 5px;
  position: relative;
  height: auto;
  /* make it center */
  top: 20%;
}

.modal-content1 h2{
  text-align: center;
}

.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}

h1 {
  text-align: center ;
}
.div{
  width: 100%;
}
.add{
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 40%;
}
.w3-half, .w3-rest {
  margin: 5px;
}
.radioButton label{
  font-weight: 400;
}
.buttons{
  display: flex;
  justify-content: space-evenly ;
}
.buttons button{
  margin: 10px;
  width: 100px;
}
#submit{
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px;
}

#back{
  background-color: #f44336;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px;
}
</style>