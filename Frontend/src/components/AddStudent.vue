<template>
<div class="addStudent-list-container" v-if = "closeAddStudent">
    <div class="w3-col">&nbsp;</div>
    <div class="w3-col">&nbsp;</div>
    <div class="w3-col">&nbsp;</div>

    <div class="exit-button" @click="close()" >
        <div class="bar2"></div>
        <div class="bar2"></div>
    </div>
    <div class="main-content">
        <h1>Add Account</h1>
    </div>
    <div class=" w3-row-padding">
        <div class="w3-third">
            <p>First Name:</p>
            <input class="w3-input w3-border" type="text" placeholder="First Name" v-model="firstname" required>
        </div>
        <div class="w3-third">
            <p>Last Name:</p>
            <input class="w3-input w3-border" type="text" placeholder="Last Name" v-model="lastname" required >
        </div>
        <div class="w3-third">
            <p>Suffix:</p>
            <select class="w3-select w3-border" name="option" v-model="suffix" required>
                <option value="" disabled selected>Choose your option</option>
                <option value="NULL">None</option>
                <option value="Jr.">Jr.</option>
                <option value="Sr.">Sr.</option>
                <option value="III">III</option>
                <option value="IV">IV</option>
                <option value="V">V</option>
            </select>
        </div>
        
        <div class="w3-col">&nbsp;</div>

        <div class="w3-third">
            <p>Gender:</p>
            <select class="w3-select w3-border" name="option" v-model="gender" required>
                <option value="" disabled selected>Choose your option</option>
                <option value="Male">Male</option>
                <option value="Female">Female</option>
            </select>
        </div>
        <div class="w3-third">
            <p>Age:</p>
            <input class="w3-input w3-border" type="number" placeholder="Age" v-model="age" required>
        </div>
        <div class="w3-third">
            <p>Birthdate:</p>
            <input class="w3-input w3-border" type="date" placeholder="Date of Birth" v-model="birthdate" required >
        </div>

        <div class="w3-col">&nbsp;</div>

        <div class="w3-third">
            <p>Student ID:</p>
            <input class="w3-input w3-border" type="text" placeholder="Student ID" v-model="studentID" required>
        </div>

        <div class="w3-third">
            <p>Department: </p>
            <select class="w3-select w3-border" name="option" v-model="department" required>
              <option value="" disabled selected>Choose your option</option>
              <option value="CSS">College of Computer Studies (CCS)</option>
              <option value="CAH">College of Arts and Humanities (CAH)</option>
              <option value="CoEA">College of Engineering and Architechture (COEA)</option>
              <option value="CABE">College of Accounting and Business Education (CABE)</option>
              <option value="CHEFS">College of Human Environmental sciences and Food Studies (CHEFS)</option>
              <option value="CMBS">College of Medical Biological Sciences (CMBS)</option>
              <option value="CoM">College of Music (CoM)</option>
              <option value="CoN">College of Nursing (CoN)</option>
              <option value="CPC">College of Pharmacy and Chemistry (CPC)</option>
              <option value="CTE">College of Teacher Education (CTE)</option>
            </select>
        </div>

        <div class="w3-third">
            <p>Section: </p>
            <input class="w3-input w3-border" type="text" placeholder="Section" v-model="section" required>
        </div>

        <div class="w3-col">&nbsp;</div>
        
        <div class="w3-third">
            <p>Contact Number:</p>
            <input class="w3-input w3-border" type="text" name="phone" pattern="^(09|\+639)\d{9}$" placeholder="Contact Number" v-model="contact" required>
        </div>

        <div class="w3-third">
            <p>Complete Address:</p>
            <input class="w3-input w3-border" type="text" placeholder="Complete Address" v-model="address" required>
        </div>

        <div class="w3-third">
            <p>School Email:</p>
            <input class="w3-input w3-border" type="text" name="email"  placeholder="Automatic" v-model="computedEmail" readonly>
        </div>

        <div class="w3-col">&nbsp;</div>
        <div class="w3-col">&nbsp;</div>

        <div class="w3-center">
            <button class="button-57" type="submit" @click="validate"><i class="fa fa-paper-plane"></i> <span class="text"> ADD STUDENT </span><span><i class="fa fa-paper-plane-o"></i> ADD STUDENT</span></button>
        </div>
        
        <div v-if="showModal" class="modal">
          <div class="modal-content">

            <div class="content">
              <p><strong>Are you sure do you want to add this student to the school's database?</strong></p>
              <p>Full Name: {{ firstname }} {{ lastname }} {{ suffix }}</p>
              <p>Gender: {{ gender }}</p>
              <p>Age: {{ age }}</p>
              <p>Birthdate: {{ birthdate }}</p>
              <p>Address: {{ address }}</p>
              <p>Contact: {{ contact }}</p>
              <p>Student ID: {{ studentID }}</p>
              <p>Department: {{ department }}</p>
              <p>Section: {{ section }}</p>
              <p>Email: {{ computedEmail }}</p>
            </div> 
            <div class="w3-center buttons">
              <button class="green" @click="addStudent()">Yes</button>
              <button class="red"  @click="showModal = false">Cancel</button>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  data() {
    return {
      firstname: '',
      lastname: '',
      suffix: '',
      gender: '',
      age: '',
      birthdate: '',
      address: '',
      contact: '',
      studentID: '',
      section: '',
      department: '',
      showModal: false,
      closeAddStudent: true,
      computedEmail: '',
    }
  },
  computed: {
    computedEmail() {
      return this.computedEmail = this.firstname.charAt(0).toLowerCase() + this.lastname.toLowerCase() + "_" + this.studentID + "@uic.edu.ph";
    },
  },
  methods: {
      close() {
          this.$emit("goHome1");
          this.$emit('handleAddStudentPageClose', false); 
          this.closeAddStudent = false;
          this.$emit("close"); 
      },
      validate() {
        if (this.firstname == '' ) {
          alert("Please enter your first name.");
          return
        } 
        if (this.lastname == '') {
          alert("Please enter your last name.");
          return
        } 
        if (this.suffix == '') {
          alert("Please enter your suffix.");
          return
        }
        if (this.gender == '') {
          alert("Please enter your gender.");
          return
        }
        if (this.age == '') {
          alert("Please enter your age.");
          return
        }
        if (this.birthdate == '') {
          alert("Please enter your birthdate.");
          return
        }
        if (this.address == '') {
          alert("Please enter your address.");
          return
        }
        if (this.contact == '') {
          alert("Please enter your contact number.");
          return
        }
        if (this.studentID == '') {
          alert("Please enter your student ID.");
          return
        }
        if (this.department == '') {
          alert("Please enter your department.");
          return
        }
        if (this.section == '') {
          alert("Please enter your section.");
          return
        }
        if (isNaN(this.age)) {
          alert("Please enter a valid age.");
          return
        }
        if (isNaN(this.contact)) {
          alert("Please enter a valid Contact Number.");
          return
        }
        this.showModal = true;
        
      },
      addStudent() {

        const formData = {
          name: this.firstname + " " + this.lastname + " " + this.suffix,
          email: this.computedEmail,
          gender: this.gender,
          age: this.age,
          birthDate: this.birthdate,
          address: this.address,
          contactInformation: this.contact,
          studentID: this.studentID,
          department: this.department,
          section: this.section,
        }
        console.log(formData);
        for (let key in formData) {
          if (!formData[key]) {
            alert(`Missing value for ${key}`);
            return;
          }
        }
        console.log(formData);
        const params = new URLSearchParams(formData).toString();
        axios.post(`http://127.0.0.1:8000/addStudent?${params}`)
        .then(response => {
          console.log(response);
          alert("Student added successfully!");
          this.close();
        })
        .catch(error => {
          console.error(error);
        });
      }
  }
}
</script>
<style scoped>
@import url('https://www.w3schools.com/w3css/4/w3.css');
@import url('https://fonts.googleapis.com/css?family=Raleway');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css');


* {font-family:"Raleway", sans-serif}

.addStudent-list-container {
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
.button-57 {
  position: relative;
  overflow: hidden;
  border: 1px solid #18181a;
  color: #18181a;
  display: inline-block;
  font-size: 15px;
  line-height: 15px;
  padding: 18px 18px 17px;
  text-decoration: none;
  cursor: pointer;
  background: #fff;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  border-radius: 5%;
}

.button-57 span:first-child {
  position: relative;
  transition: color 600ms cubic-bezier(0.48, 0, 0.12, 1);
  z-index: 10;
}

.button-57 span:last-child {
  color: white;
  display: block;
  position: absolute;
  bottom: 0;
  transition: all 500ms cubic-bezier(0.48, 0, 0.12, 1);
  z-index: 100;
  opacity: 0;
  top: 50%;
  left: 50%;
  transform: translateY(225%) translateX(-50%);
  height: 14px;
  line-height: 13px;
  width: 100%;
}

.button-57:after {
  content: "";
  position: absolute;
  bottom: -50%;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: black;
  transform-origin: bottom center;
  transition: transform 600ms cubic-bezier(0.48, 0, 0.12, 1);
  transform: skewY(9.3deg) scaleY(0);
  z-index: 50;
  width: 100%;
}

.button-57:hover:after {
  transform-origin: bottom center;
  transform: skewY(9.3deg) scaleY(2);
  width: 100%;
}

.button-57:hover span:last-child {
  transform: translateX(-50%) translateY(-65%);
  opacity: 1;
  transition: all 900ms cubic-bezier(0.48, 0, 0.12, 1);
  width: 100%;
}

.button-57:hover span:first-child {
  color: white;
  transition: color 600ms cubic-bezier(0.48, 0, 0.12, 1);
}
.modal {
  display: block; 
  position: fixed; 
  z-index: 2; 
  padding-top: 100px; 
  left: 0;
  top: 0;
  width: 100%; 
  height: 100%; 
  overflow: auto; 
  background-color: rgb(0,0,0); 
  background-color: rgba(0,0,0,0.4); 
}
.modal-content {
  background-color: #fefefe;
  margin: 5% auto; 
  padding: 20px;
  border: 1px solid #888;
  width: 45%; 
  padding: 40px;
  height: 65%;
}
.modal-content .exit-button {
  position: absolute;
  cursor: pointer;
  display: inline-block;
  margin: 10px;
  padding: 10px;
  background-color: #ddd;
  border-radius: 5px;
  position: relative;
  left: 92%;
  width: 5%
}
.content{
  position: fixed;
  top: 27%;
}

.green {
  background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 5px;
}
.red {
  background-color: #f44336; /* Red */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 5px;
}
.green:hover {
  background-color: #129c18;
  transition: 0.3s ease-in-out;
}
.red:hover {
  background-color: #e0251b;
  transition: 0.3s ease-in-out;
}
.buttons {
  position: fixed;
  top: 70%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: auto;
  height: 10%;
}
.buttons button {
  margin: 30px;
 
  
}

</style>