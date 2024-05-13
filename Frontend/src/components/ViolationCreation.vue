<template>
    <div class="addViolation-list-container">
        <div class="w3-row">&nbsp;</div>
        <div class="w3-row">&nbsp;</div>
        
        <div class="main-content modal-content">
            <div class="exit-button" @click="$emit('close')">
                <div class="bar2"></div>
                <div class="bar2"></div>
            </div>  
            <div class="w3-row">&nbsp;</div>
            <h1>Add Violation</h1>
            <div >
              <label for="violation">Violation:</label>
            <input type="text" id="violation" v-model="violationForm.violationName" required>

            <label for="description">Description:</label>
            <textarea id="description" v-model="violationForm.description" required></textarea>

            <label for="category">Category:</label>
            <div class="radioButton">
                <label for="category">Minor</label>
                <input type="radio" id="category" v-model="violationForm.category" value="Minor" required>
                <label for="category">Major</label>
                <input type="radio" id="category" v-model="violationForm.category" value="Major" required>
                <label for="category">Critical</label>
                <input type="radio" id="category" v-model="violationForm.category" value="Critical" required>
            </div>

            <label for="createdBy">Created By:</label>
            <input type="text" id="createdBy" v-model="violationForm.createdBy" required>

            <button @click="confirmModal()">Add Violation</button>
            </div>
        </div>
        <div id="myModal" class="modal" v-if="confirm">
            <div class="modal-content">
                <p><strong>Violation: </strong> {{ violationForm.violationName }}</p>
                <p><strong>Description: </strong> {{ violationForm.description }}</p>
                <p><strong>Category: </strong> {{ violationForm.category }}</p>
                <p><strong>Created By: </strong> {{ violationForm.createdBy }}</p>
                <div class="buttons">
                    <button  @click="addViolation(),pass=true">Submit</button>
                    <button @click="confirm=false">Back</button>
                </div>
            </div>
        </div>
                
        <div id="myModal" class="modal" v-if="pass">
            <div class="modal-content">
                <span class="close">&times;</span>
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
    methods: {
        confirmModal() {
            console.log('confirm'); 
            this.confirm = true;
        },
        addViolation() {
            const formData = this.violationForm;
            console.log(formData);
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
        }
    }
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

.bar2 {
  width: 20px;
  height: 2px;
  background-color: #333;
  margin: 5px 0;
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
  justify-content: space-evenly;
  margin: 10px 0;
}

.modal {
  position: absolute;
  z-index: 10;
  display: block;
}

.modal-content {
  background-color: #fefefe;
  margin: 5% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
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
</style>