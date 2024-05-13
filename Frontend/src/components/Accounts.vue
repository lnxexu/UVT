<template>
    <div class="secAcc-list-container" v-if="closeSekyu">
      <div class="w3-row">&nbsp;</div>
      <div class="w3-row">&nbsp;</div>
      <div class="w3-row">&nbsp;</div>
      <div class="exit-button" @click="close()">
        <div class="bar2"></div>
        <div class="bar2"></div>
      </div>
      <div class="w3-row">&nbsp;</div>
      <div class="main-content w3-half modal-content">
        <h1 class="w3-center">Security Guards List</h1>
        <div class="w3-row">&nbsp;</div>

        <div class="w3-row w3-half center">
          <div class="w3-col s9 ">
            <input type="text" class="w3-input w3-border" v-model="searchQuery" placeholder="Search for security guards" @input="filterGuards()" />
            <ul v-if="filteredGuards.length" class="search">
              <li v-for="guard in filteredGuards" @click="selectGuard(guard)">{{ guard.fullName }}</li>
            </ul>
          </div>
          <div class="w3-col s3">
            <button @click="searchGuard()" class="w3-button w3-blue">Search</button>
          </div>
        </div>
        <div class="w3-quarter">&nbsp;</div>
        <div class="choice">
          <button class="show" @click="listGuards = !listGuards">Show list</button>
          <button class="show" @click="selectedGuard=null">Clear Details</button>
        </div>
        <ul v-if="listGuards" :class="{ 'scrollable-list': securityGuards.length >= 3 }" >
          <li v-for="guard in securityGuards" @click="showGuardDetails(guard)">{{ guard.fullName }}</li>
        </ul>
        <div v-if="selectedGuard">
          <h2>{{ selectedGuard.fullName }}</h2>
          <hr>
          <p><strong>Suffix:</strong> {{ selectedGuard.suffix }}</p>
          <p><strong>Birth Date:</strong> {{ selectedGuard.birthDate }}</p>
          <p><strong>Age:</strong> {{ selectedGuard.age }}</p>
          <p><strong>ID:</strong> {{ selectedGuard.id }}</p>
          <p><strong>Gender:</strong> {{ selectedGuard.gender }}</p>
          <p><strong>Address:</strong> {{ selectedGuard.address }}</p>
          <p><strong>Contact Number:</strong> {{ selectedGuard.contactInformation }}</p>
          <p><strong>Assigned School Branch:</strong> {{ selectedGuard.assignedLoc }}</p>
          <p><strong>Email:</strong> {{ selectedGuard.email }}</p>
        </div>
      </div>
      <div class="main-content w3-half modal-content">
        <h1 class="w3-center">OSAD Staffs List</h1>
        <div class="w3-row">&nbsp;</div>
        <div class="w3-row w3-half center">
          <div class="w3-col s9 ">
            <input type="text" class="w3-input w3-border" v-model="searchQueryStaff" placeholder="Search for OSAD staffs" @input="filterStaffs()"  />
            <ul v-if="filteredStaffs.length" class="search">
              <li v-for="staff in filteredStaffs" @click="selectStaff(staff)">{{ staff.fullName }}</li>
            </ul>
          </div>
          <div class="w3-col s3">
            <button @click="searchStaff()" class="w3-button w3-blue">Search</button>
          </div>
        </div>

        <div class="w3-row">&nbsp;</div>
        <div class="choice">
          <button class="show" @click="listStaffs = !listStaffs">Show list</button>
          <button class="show" @click="selectedGuard=null">Clear Details</button>
        </div>
        <ul v-if="listStaffs" :class="{ 'scrollable-list': osadAccounts.length >= 3 }">
          <li v-for="staff in osadAccounts" @click="selectStaff(staff)">{{ staff.fullName }}</li>
        </ul>
        <div v-if="selectedStaff">
          <h2>{{ selectedStaff.fullName }}</h2>
          <hr>
          <p><strong>Suffix:</strong> {{ selectedStaff.suffix }}</p>
          <p><strong>Birth Date:</strong> {{ selectedStaff.birthDate }}</p>
          <p><strong>ID:</strong> {{ selectedStaff.id }}</p>
          <p><strong>Gender:</strong> {{ selectedStaff.gender }}</p>
          <p><strong>Age:</strong> {{ selectedStaff.age }}</p>
          <p><strong>Address:</strong> {{ selectedStaff.address }}</p>
          <p><strong>Contact Number:</strong> {{ selectedStaff.contactInformation }}</p>
          <p><strong>Email:</strong> {{ selectedStaff.email }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
import axios from 'axios';

  export default {
    data() {
      return {
        searchQuery: '',
        searchQueryStaff: '',
        securityGuards: [],
        filteredGuards: [],
        osadAccounts: [],
        filteredStaffs: [],
        closeSekyu: true,
        selectedGuard: null,
        selectedStaff: null,
        listGuards: false,
        listStaffs: false,
      };
    },
    mounted() {
      this.fetchData();
    },
    methods: {
      close() {
        this.$emit("goHome");
        this.$emit('handleSecurityAccountsClose', false);
        this.closeSekyu = false;
        this.$emit("close");
      },
      showGuardDetails(guard) {
        this.selectedGuard = guard;
      },
      showStaffDetails(staff) {
        this.selectedStaff = staff;
      },
      filterGuards() {
        if (!this.securityGuards || !this.searchQuery) {
          this.filteredGuards = [];
          return;
        }
        this.filteredGuards = this.securityGuards.filter(guard =>
          guard.fullName && guard.fullName.toLowerCase().includes(this.searchQuery.toLowerCase())
        );
      },
      selectGuard(guard) {
        this.searchQuery = '';
        this.selectedGuard = guard;
        this.filteredGuards = [];
        this.listGuards = false; 
      },
      filterStaffs() {
        if (!this.osadAccounts || !this.searchQueryStaff) {
          this.filteredStaffs = [];
          return;
        }
        this.filteredStaffs = this.osadAccounts.filter(staff =>
          staff.fullName && staff.fullName.toLowerCase().includes(this.searchQueryStaff.toLowerCase())
        );
      },
      selectStaff(staff) {
        this.searchQueryStaff = '';
        this.selectedStaff = staff;
        this.filteredStaffs = [];
        this.listStaffs = false; 
      },
      searchGuard() {
        if (!this.searchQuery) {
          alert("Please enter a search query");
          return;
        }
        const query = this.searchQuery;
        const params = new URLSearchParams({ query }).toString();
        axios.get(`http://127.0.0.1:8000/sekyuUsers/search?${params}`)
        .then((response) => {
          console.log(response.data);
          this.securityGuards   = response.data.map(guard => {
            let birthDate = new Date(guard.birthDate);
            let formattedDate = birthDate.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
            return { ...guard, birthDate: formattedDate };
          })
          this.listGuards = true;
        })
        .catch((error) => {
          console.error(error);
          alert("No results found");
        });
      },
      searchStaff() {
        if (!this.searchQueryStaff) {
          alert("Please enter a search query");
          return;
        }
        const query = this.searchQueryStaff;
        const params = new URLSearchParams({ query }).toString();
        axios.get(`http://127.0.0.1:8000/OSADusers/search?${params}`)
        .then((response) => {
          console.log(response.data);
          this.osadAccounts = response.data.map(user => {
            let birthDate = new Date(user.birthDate);
            let formattedDate = birthDate.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
            return { ...user, birthDate: formattedDate };
          });
          this.listStaffs = true;
        })
        .catch((error) => {
          console.error(error);
          alert("No results found");
        });
      },
      fetchData() {
        axios.get("http://127.0.0.1:8000/sekyuUsers")
        .then((response) => {
          this.securityGuards = response.data.map(guard => {
            let birthDate = new Date(guard.birthDate);
            let formattedDate = birthDate.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
            return { ...guard, birthDate: formattedDate };
          });
        })
        .catch((error) => {
          console.error(error);
        });
        axios.get("http://127.0.0.1:8000/OSADusers")
        .then((response) => {
          console.log(response.data);
          this.osadAccounts = response.data.map(users => {
            let birthDate = new Date(users.birthDate);
            let formattedDate = birthDate.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
            return { ...users, birthDate: formattedDate };
          });
        })
        .catch((error) => {
          console.error(error);
        });
      }
    },
    
  };
  </script>
  
<style scoped>
* {font-family:"Raleway", sans-serif}
.secAcc-list-container {
  position: fixed;
  display: block;
  left: 0%;
  width: 100%;
  height: 100%;
  background-color: #f1f1f1;
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
  max-height: 200px; 
  overflow-y: auto; 
  width: 100%;
}

.scrollable-list {
  max-height: 150px; 
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
.search{
  background-color: #000000;
  border-radius: 5px;
  position: absolute;
  width: 78%;
  color: #ffffff;
  padding: 10px;
}
.search li{
  background-color: #000000;
  border-radius: 5px;
  border: #ffffff 1px solid;
}
.search li:hover{
  background-color: #ffffff;
  color: #000000;
}
.show{
  background-color: #ffffff;
  border-radius: 5px;
  padding: 10px;
  cursor: pointer;
  width: 50%;
  margin: 15px 0px;
}
.show:hover{
  background-color: #ccc;
}

.modal-content {
  background-color: #fefefe;
  padding: 20px;
  border: 1px solid #888;
  border-radius: 5px;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1);
  width: 47%;
  margin: 0 1.5%;
  height: 80%;
}
.center{
  position: relative;
  left: 26%;
}
.choice{
  display: flex;
  justify-content: space-between;
}
  </style>
  