<template>
<div class="secAcc-list-container" v-if="closePendingAccounts">
  <div class="w3-row">&nbsp;</div>
  <div class="w3-row">&nbsp;</div>
  <div class="w3-row">&nbsp;</div>
  <div class="exit-button" @click="close()">
    <div class="bar2"></div>
    <div class="bar2"></div>
  </div>

  <div class="w3-col"></div>

  <div class="main-content w3-half modal-content">
    <h1>Security Pending Accounts</h1>
    <div class="w3-row">&nbsp;</div>
    <ul :class="{ 'scrollable-list': sekyuAccounts.length >= 5 }">
      <li v-for="sekyu in sekyuAccounts" :key="sekyu.fullName" @click="showAccountDetailsSekyu(sekyu)">{{ sekyu.fullName }}</li>
    </ul>
    
    <div class="selectionSekyu" v-if="selectedSekyu">
      <h2>{{ selectedSekyu.fullName }}</h2>
      <hr>
      <p><strong>Age:</strong> {{ selectedSekyu.age }}</p>
      <p><strong>Gender:</strong> {{ selectedSekyu.gender }}</p>
      <p><strong>Birthdate:</strong> {{ selectedSekyu.birthDate }}</p>
      <p><strong>Address:</strong> {{ selectedSekyu.address }}</p>
      <p><strong>Contact Number:</strong> {{ selectedSekyu.contactInformation }}</p>
      <p>
        <strong>Assigned School Branch: &nbsp;&nbsp;</strong>
        <select class="input" v-model="assignLocation" style="border-radius: 5px;" required>
          <option v-for="option in assignLoc" :key="option.value" :value="option">{{ option }}</option>
        </select>
      </p>
      <p><strong>Email:</strong> {{ selectedSekyu.email }}</p>
      <p><strong>Password:</strong> {{ selectedSekyu.password }}</p>
      <div class="w3-row">&nbsp;</div>
      <div class="buttons">
        <button class="green" @click="noVenue()">Approve</button>
        <button class="red" @click="showRejectPopupSekyu = true">Reject</button>
      </div>
    </div>
  </div>


  <div class="main-content w3-half modal-content">
    <h1>OSAD Pending Accounts</h1>
    <div class="w3-row">&nbsp;</div>
    <ul :class="{ 'scrollable-list': osadAccounts.length >= 5 }">
      <li v-for="OSAD in osadAccounts" :key="OSAD.fullName" @click="showAccountDetailsOSAD(OSAD)">{{ OSAD.fullName }}</li>
    </ul>
    <div class="selectionOSAD" v-if="selectedOSAD">
      <h2>{{ selectedOSAD.fullName }}</h2>
      <hr>
      <p><strong>Age:</strong> {{ selectedOSAD.age }}</p>
      <p><strong>Gender:</strong> {{ selectedOSAD.gender }}</p>
      <p><strong>Birthdate:</strong> {{ selectedOSAD.birthDate }}</p>
      <p><strong>Address:</strong> {{ selectedOSAD.address }}</p>
      <p><strong>Contact Number:</strong> {{ selectedOSAD.contactInformation }}</p>
      <p><strong>Email:</strong> {{ selectedOSAD.email }}</p>
      <p><strong>Password:</strong> {{ selectedOSAD.password }}</p>
      <div class="w3-row">&nbsp;</div>
      <div class="buttons">
        <button class="green" @click="showConfirmPopupOSAD = true">Approve</button>
        <button class="red" @click="showRejectPopupOSAD = true">Reject</button>
      </div>
    </div>
  </div>
</div>

<div v-if="showConfirmPopupSekyu"class="model">
  <div class="w3-modal-content w3-card-4 popup " >
    <div class="w3-container w3-padding-16 ">
      <h1>Confirm Account Approval</h1>
      <h6>Are you sure you want to approve this account?</h6>
      <hr>
      <h2>{{ selectedSekyu.fullName }}</h2>
      <p><strong>Age:</strong> {{ selectedSekyu.age }}</p>
      <p><strong>Gender:</strong> {{ selectedSekyu.gender }}</p>
      <p><strong>Birthdate:</strong> {{ selectedSekyu.birthDate }}</p>
      <p><strong>Address:</strong> {{ selectedSekyu.address }}</p>
      <p><strong>Contact Number:</strong> {{ selectedSekyu.contactInformation }}</p>
      <p><strong>Assigned School Branch:</strong> {{ assignLocation }}</p>
      <p><strong>Email:</strong> {{ selectedSekyu.email }}</p>
      <p><strong>Password:</strong> {{ selectedSekyu.password }}</p>
    </div>
    <div class="buttons">
      <button class="green" @click="approveSekyu()">Yes, approve</button>
      <button class="red" @click="showConfirmPopupSekyu = false">No, go back</button>
    </div>
  </div>
</div>

<div v-if="showConfirmPopupOSAD" class="model">
  <div  class="w3-modal-content w3-card-4 popup ">
    <div class="w3-container w3-padding-16 ">
      <h1>Confirm Account Approval</h1>
      <h6>Are you sure you want to approve this account?</h6>
      <hr>
      <h2>{{ selectedOSAD.fullName }}</h2>
      <p><strong>Age:</strong> {{ selectedOSAD.age }}</p>
      <p><strong>Gender:</strong> {{ selectedOSAD.gender }}</p>
      <p><strong>Birthdate:</strong> {{ selectedOSAD.birthDate }}</p>
      <p><strong>Address:</strong> {{ selectedOSAD.address }}</p>
      <p><strong>Contact Number:</strong> {{ selectedOSAD.contactInformation }}</p>
      <p><strong>Email:</strong> {{ selectedOSAD.email }}</p>
      <p><strong>Password:</strong> {{ selectedOSAD.password }}</p>
    </div>
    <div class="buttons">
      <button class = "green" @click="approveOSAD()">Yes, approve</button>
      <button class = "red" @click="showConfirmPopupOSAD = false" >No, go back</button>
    </div>
  </div>
</div>


<div v-if="showRejectPopupSekyu"class="model">
  <div class="w3-modal-content w3-card-4 popup " >
    <div class="w3-container w3-padding-16 ">
      <h1>Confirm Account Rejection</h1>
      <h6>Are you sure you want to reject this account?</h6>
      <hr>
      <h2>{{ selectedSekyu.fullName }}</h2>
      <p><strong>Age:</strong> {{ selectedSekyu.age }}</p>
      <p><strong>Gender:</strong> {{ selectedSekyu.gender }}</p>
      <p><strong>Birthdate:</strong> {{ selectedSekyu.birthDate }}</p>
      <p><strong>Address:</strong> {{ selectedSekyu.address }}</p>
      <p><strong>Contact Number:</strong> {{ selectedSekyu.contactInformation }}</p>
      <p><strong>Email:</strong> {{ selectedSekyu.email }}</p>
      <p><strong>Password:</strong> {{ selectedSekyu.password }}</p>
    </div>
    <div class="buttons">
      <button class="green" @click="rejectSekyu()">Yes, reject</button>
      <button class="red" @click="showRejectPopupSekyu = false">No, go back</button>
    </div>
  </div>
</div>

<div v-if="showRejectPopupOSAD" class="model">
  <div  class="w3-modal-content w3-card-4 popup ">
    <div class="w3-container w3-padding-16 ">
      <h1>Confirm Account Rejection</h1>
      <h6>Are you sure you want to reject this account?</h6>
      <hr>
      <h2>{{ selectedOSAD.fullName }}</h2>
      <p><strong>Age:</strong> {{ selectedOSAD.age }}</p>
      <p><strong>Gender:</strong> {{ selectedOSAD.gender }}</p>
      <p><strong>Birthdate:</strong> {{ selectedOSAD.birthDate }}</p>
      <p><strong>Address:</strong> {{ selectedOSAD.address }}</p>
      <p><strong>Contact Number:</strong> {{ selectedOSAD.contactInformation }}</p>
      <p><strong>Email:</strong> {{ selectedOSAD.email }}</p>
      <p><strong>Password:</strong> {{ selectedOSAD.password }}</p>
    </div>
    <div class="buttons">
      <button class="green" @click="rejectOSAD()">Yes, reject</button>
      <button class="red" @click="showRejectPopupOSAD = false" >No, go back</button>
    </div>
  </div>
</div>

<div v-if="popupApprove" class="model">
  <div class="w3-modal-content w3-card-4 pop" >
    <div class="w3-container w3-padding-16 w3-light-grey">
      <h2>Account Approved</h2>
      <p>Account has been approved.</p>
      <div class="w3-row">&nbsp;</div>
      <button class="green" @click="handleCloseApprove()">Close</button>
    </div>
  </div>
</div>


<div v-if="popupReject" class="model">
  <div class="w3-modal-content w3-card-4 pop" >
    <div class="w3-container w3-padding-16 w3-light-grey">
      <h2>Account Rejected</h2>
      <p>Account has been rejected</p>
      <div class="w3-row">&nbsp;</div>
      <button class="green" @click="handleCloseReject()">Close</button>
    </div>
  </div>
</div>
</template>
  
<script>
import axios from "axios";
export default {
  data() {
    return {
      sekyuAccounts: [],
      osadAccounts: [],
      closePendingAccounts: true,
      selectedSekyu: null,
      selectedOSAD: null,
      popupApprove: false,
      popupReject: false,
      showConfirmPopupSekyu: false,
      showConfirmPopupOSAD: false,
      showRejectPopupSekyu: false,
      showRejectPopupOSAD: false,
      assignLoc: [ "UIC Bonifacio", "UIC Bangkerohan", "UIC Bajada"],
      assignLocation: '' 
    };
  },
  mounted() {
    this.fetchData();
  },
  emits: ['handlePendingAccountsClose','goHome2', 'close'],
  methods: {
    noVenue(){
      if(this.assignLocation == ''){
        alert("Please select a venue");
        return;
      }
      this.showConfirmPopupSekyu = true
    },
    handleCloseApprove() {
      this.popupApprove = false;
      this.showConfirmPopupSekyu = false;
      this.showConfirmPopupOSAD = false;
      this.selectedSekyu = null;
      this.selectedOSAD = null;
      this.fetchData();
    },
    handleCloseReject() {
      this.popupReject = false;
      this.showRejectPopupSekyu = false;
      this.showRejectPopupOSAD = false;
      this.selectedSekyu = null;
      this.selectedOSAD = null;
      this.fetchData();
    },
    close() {
      this.$emit('goHome2');
      this.$emit('handlePendingAccountsClose', false);
      this.closePendingAccounts = false;
    },
    showAccountDetailsSekyu(sekyu) {
      this.selectedSekyu = sekyu;
    },
    showAccountDetailsOSAD(OSAD) {
      this.selectedOSAD = OSAD;
    },
    fetchData() {
      axios.get("http://127.0.0.1:8000/GetAllAccountsSekyu")
      .then((response) => {
        this.sekyuAccounts = response.data;
      })
      .catch((error) => {
        console.error(error);
      });

      axios.get("http://127.0.0.1:8000/GetAllAccountsOSAD")
      .then((response) => {
        this.osadAccounts = response.data;
      })
      .catch((error) => {
        console.error(error);
      });
    },
    approveSekyu() {
      const data = {
        fullName: this.selectedSekyu.fullName,
        age: this.selectedSekyu.age,
        gender: this.selectedSekyu.gender,
        suffix: this.selectedSekyu.suffix,
        birthDate: this.selectedSekyu.birthDate,
        address: this.selectedSekyu.address,
        contactInformation: this.selectedSekyu.contactInformation,
        email: this.selectedSekyu.email,
        password: this.selectedSekyu.password,
        assignedLoc: this.assignLocation
      };
      for (let key in data) {
        if (!data[key]) {
          alert(`Missing value for ${key}`);
          return;
        }
      }
      const params = new URLSearchParams(data).toString();
      axios.post(`http://127.0.0.1:8000/sekyuUsers/addUser?${params}`)
      .then((response) => {
        console.log(response);
        this.popupApprove = true;
        this.rejectSekyu();
      })
      .catch((error) => {
        console.error(error);
        alert("Error approving account");
      }); 
    },
    approveOSAD() {
      const data = {
        fullName: this.selectedOSAD.fullName,
        age: this.selectedOSAD.age,
        gender: this.selectedOSAD.gender,
        suffix: this.selectedOSAD.suffix,
        birthDate: this.selectedOSAD.birthDate,
        address: this.selectedOSAD.address,
        contactInformation: this.selectedOSAD.contactInformation,
        email: this.selectedOSAD.email,
        password: this.selectedOSAD.password,
      };
      for (let key in data) {
        if (!data[key]) {
          console.error(`Missing value for ${key}`);
          return;
        }
      }
      const params = new URLSearchParams(data).toString();
      axios.post(`http://127.0.0.1:8000/osadUsers/addUser?${params}`)
      .then((response) => {
        console.log(response);
        this.popupApprove = true;
        this.rejectOSAD();
      })
      .catch((error) => {
        console.error(error);
        alert("Error approving account");
      });
    },
    rejectSekyu() {
      axios.delete(`http://127.0.0.1:8000/RejectAccountSekyu/${this.selectedSekyu.email}`)
      .then((response) => {
        console.log(response);
        this.popupReject = true;
      })
      .catch((error) => {
        console.error(error);
        alert("Error rejecting account");
      });
    },
    rejectOSAD() {
      axios.delete(`http://127.0.0.1:8000/RejectAccountOSAD/${this.selectedOSAD.email}`)
      .then((response) => {
        console.log(response);
        this.popupReject = true;
      })
      .catch((error) => {
        console.error(error);
        alert("Error rejecting account");
      });
    },
  }
};
</script>
  
<style scoped>
.secAcc-list-container {
  position: fixed;
  display: block;
  z-index: 1;
  left: 0%;
  width: 100%;
  height: 100%;
  background-color: #f1f1f1;
  overflow: hidden; /* Hide overflowing content */
  z-index: 2;
}

.main-content {
  flex: 1;
  padding: 20px;
  height: 80%;
}

ul {
  list-style-type: none;
  padding: 0;
  cursor: pointer;
  max-height: 200px; 
  overflow-y: auto; 
}

.scrollable-list {
  max-height: 200px; 
}

li {
  margin-bottom: 10px;
  padding: 10px;
  background-color: #ddd;
  border-radius: 5px;
  cursor: pointer;
}

li:hover {
  background-color: #ccc;
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
.vl {
  border: 1px solid rgb(0, 0, 0);
  height: 100%;
  width: 0;
  position: absolute;
  left: 50%;
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
  display: flex;
  justify-content: space-evenly;
}

* {font-family:"Raleway", sans-serif}

/* Modal Content/Box */
.w3-modal-content {
  margin: 5% auto;
  background-color: #fff;
  position: relative;
  padding: 0;
  border: 1px solid #888;
  width: 80%;
  height: 50%;
}

/* The Close Button */
.w3-container {
  padding: 16px;
}

.model {
  position: fixed;
  z-index: 3;
  left: 0;
  top: 0;
  width: 105%;
  height: 102%;
  overflow: -moz-hidden-unscrollable;
  background-color: rgba(0,0,0,0.4);
}
.popup{
  background-color: #f1f1f1;
  margin: 5% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 30%;
  height: auto;
  position: fixed;
  border-radius: 5px;
  overflow: hidden;
  transition: 0.3s;
  z-index: 99;
  left: 35%;
  top: 12%;
  display: block;
}

.popup button {
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

.selectionSekyu{
  padding: 20px;
  border-radius: 5px;
  position: fixed;
  left: 0%;
  top: 44.3%;
  width: 46.5%;
  margin: 0 30px;
  height: auto;
}

.selectionOSAD .buttons{
  position: relative;
  top: 4%;
}


.selectionOSAD{
  padding: 20px;
  border-radius: 5px;
  position: fixed;
  left: 50%;
  top: 44.3%;
  width: 46.5%;
  margin: 0 30px;
  height: 100%;
}
.w3-container h1, h6{
  text-align: center;
}
.pop{
  z-index: 10;
  background-color: #f1f1f1;
  margin: 5% auto;
  padding: 10px;
  border: 1px solid #888;
  width: 30%;
  height: auto;
  position: fixed;
  border-radius: 5px;
  overflow: hidden;
  transition: 0.3s;
  left: 35%;
  top: 28%;
  display: block;
  text-align: center;
}
.modal-content {
  background-color: #fefefe;
  padding: 20px;
  border: 1px solid #888;
  border-radius: 5px;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1);
  width: 48%;
  margin: 0 1%;
  height: 83%;
}

.modal-content h1{
  text-align: center;
}

</style>
  