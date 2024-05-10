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
    <!-- Main Content -->
    <div class="main-content w3-half">
      <h1>Security Pending Accounts</h1>
      <div class="w3-row">&nbsp;</div>
      <ul :class="{ 'scrollable-list': sekyuAccounts.length >= 5 }">
        <li v-for="sekyu in sekyuAccounts" :key="sekyu.fullName" @click="showAccountDetailsSekyu(sekyu)">
          {{ sekyu.fullName }} </li>
      </ul>

      <!-- Detailed view for the selected guard -->
      <div v-if="selectedSekyu">
        <h2>{{ selectedSekyu.fullName }}</h2>
        <p><strong>Age:</strong> {{ selectedSekyu.age }}</p>
        <p><strong>Gender:</strong> {{ selectedSekyu.gender }}</p>
        <p><strong>Birthdate:</strong> {{ selectedSekyu.birthDate }}</p>
        <p><strong>Address:</strong> {{ selectedSekyu.address }}</p>
        <p><strong>Contact Number:</strong> {{ selectedSekyu.contactInformation }}</p>
        <p><strong>Email:</strong> {{ selectedSekyu.email }}</p>
        <p><strong>Password:</strong> {{ selectedSekyu.password }}</p>
        <div class="w3-row">&nbsp;</div>
        <div class="buttons">
          <button id="approveButton"  @click="showConfirmPopupSekyu = true">Approve</button>
          <button id="rejectButton"  @click="rejectSekyu">Reject</button>
        </div>
        <transition name="scale">
          <div v-if="showConfirmPopupSekyu" class="w3-modal-content w3-card-4 w3-animate-zoom popup" style="max-width: 600px">
            <div class="w3-container w3-padding-16 w3-light-grey">
              <h2>Confirm Approval</h2>
              <p>Are you sure you want to approve this account?</p>
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
              <button @click="approveSekyu()">Yes, approve</button>
              <button @click="showConfirmPopupSekyu = false">No, go back</button>
            </div>
          </div>
        </transition>
      </div>
    </div>

    <div class="vl"></div>

    <div class="main-content w3-half">
      <h1>OSAD Pending Accounts</h1>
      <div class="w3-row">&nbsp;</div>
      <ul :class="{ 'scrollable-list': osadAccounts.length >= 5 }">
        <li v-for="OSAD in osadAccounts" :key="OSAD.fullName" @click="showAccountDetailsOSAD(OSAD)">
          {{ OSAD.fullName }} </li>
      </ul>
      <div v-if="selectedOSAD">
        <h2>{{ selectedOSAD.fullName }}</h2>
        <p><strong>Age:</strong> {{ selectedOSAD.age }}</p>
        <p><strong>Gender:</strong> {{ selectedOSAD.gender }}</p>
        <p><strong>Birthdate:</strong> {{ selectedOSAD.birthDate }}</p>
        <p><strong>Address:</strong> {{ selectedOSAD.address }}</p>
        <p><strong>Contact Number:</strong> {{ selectedOSAD.contactInformation }}</p>
        <p><strong>Email:</strong> {{ selectedOSAD.email }}</p>
        <p><strong>Password:</strong> {{ selectedOSAD.password }}</p>
        <div class="w3-row">&nbsp;</div>
        <div class="buttons">
          <button id="approveButton"  @click="showConfirmPopupOSAD = true">Approve</button>
          <button id="rejectButton"  @click="rejectOSAD()">Reject</button>
        </div>
        <transition name="scale">
          <div v-if="showConfirmPopupOSAD"  class="w3-modal-content w3-card-4 w3-animate-zoom popup" style="max-width: 600px">
            <div class="w3-container w3-padding-16 w3-light-grey">
              <h2>Confirm Approval</h2>
              <p>Are you sure you want to approve this account?</p>
              <hr>
              <h2>{{ selectedOSAD.fullName }}</h2>
              <p><strong>Age:</strong> {{ selectedOSAD.age }}</p>
              <p><strong>Gender:</strong> {{ selectedOSAD.gender }}</p>
              <p><strong>Birthdate:</strong> {{ selectedOSAD.birthDate }}</p>
              <p><strong>Address:</strong> {{ selectedOSAD.address }}</p>
              <p><strong>Contact Number:</strong> {{ selectedOSAD.contactInformation }}</p>
              <p><strong>Email:</strong> {{ selectedOSAD.email }}</p>
              <p><strong>Password:</strong> {{ selectedOSAD.password }}</p>
              <div class="buttons">
                <button @click="approveOSAD()">Yes, approve</button>
                <button @click="showConfirmPopupOSAD = false" >No, go back</button>
              </div>
            </div>
          </div>
        </transition>
      </div>
    </div>
  </div>
  <transition name="scale">
    <div v-if="popupApprove">
      <div class="w3-modal-content w3-card-4 w3-animate-zoom model " style="max-width: 600px;">
        <div class="w3-container w3-padding-16 w3-light-grey popup">
          <h2>Account Approved</h2>
          <p>Account has been approved</p>
          <div class="w3-row">&nbsp;</div>
          <button id="approveButton" @click="popupApprove = false,showConfirmPopupSekyu = false,showConfirmPopupOSAD = false">Close</button>
        </div>
      </div>
    </div>
  </transition>
  
  <div v-if="popupReject">
    <div class="w3-modal-content w3-card-4 w3-animate-zoom popup" style="max-width: 600px">
      <div class="w3-container w3-padding-16 w3-light-grey">
        <h2>Account Rejected</h2>
        <p>Account has been rejected</p>
        <div class="w3-row">&nbsp;</div>
        <button id="approveButton" @click="close()">Close</button>
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
    };
  },
  mounted() {
    this.fetchData();
  },
  emits: ['handlePendingAccountsClose'],
  methods: {
    close() {
      this.$emit('goHome2');
      this.$emit('handlePendingAccountsClose', false);
      this.closePendingAccounts = false;
      this.$emit("close");
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
      };
      for (let key in data) {
        if (!data[key]) {
          console.error(`Missing value for ${key}`);
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
        this.popupReject = true;
      }); 
      this.popupApprove = true;
      console.log("Approve Sekyu");
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
      })
      .catch((error) => {
        console.error(error);
        this.popupReject = true;
      });
      this.popupApprove = true;
      console.log("Approve OSAD");
    },
    rejectSekyu() {
      axios.delete(`http://127.0.0.1:8000/RejectAccountSekyu/${this.selectedSekyu.email}`)
      .then((response) => {
        console.log(response);
      })
      .catch((error) => {
        console.error(error);
      });
    },
    rejectOSAD() {
      axios.delete(`http://127.0.0.1:8000/RejectAccountOSAD/${this.selectedOSAD.email}`)
      .then((response) => {
        console.log(response);
      })
      .catch((error) => {
        console.error(error);
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
}

ul {
  list-style-type: none;
  padding: 0;
  cursor: pointer;
  max-height: 200px; /* Maximum height for the list */
  overflow-y: auto; /* Add a scrollbar when the list exceeds the maximum height */
}

.scrollable-list {
  max-height: 200px; /* Set the maximum height for scrollable lists */
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
#approveButton {
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
#rejectButton {
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
#approveButton:hover {
  background-color: #129c18;
  transition: 0.3s ease-in-out;
}
#rejectButton:hover {
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

.scale-enter-active, .scale-leave-active {
  transition: transform 1s ease-in-out;
}

.scale-enter, .scale-leave-to {
  transform: scale(1);
}

.scale-leave-active {
  transform: scale(0);
}

.model {
  position: fixed;
  z-index: 9999;
  left: -1%;
  top: -10%;
  width: 105%;
  height: 102%;
  overflow: -moz-hidden-unscrollable;
  background-color: rgba(0,0,0,0.4);
  transition: 0.3s;
}
.popup{
  background-color: #f1f1f1;
  margin: 5% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 50%;
  height: auto;
  position: absolute;
  top: 15%;
  border-radius: 5px;
  overflow: hidden;
  transition: 0.3s;
}

.popup button {
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



</style>
  