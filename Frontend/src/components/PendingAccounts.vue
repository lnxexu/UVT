<template>
    <div class="secAcc-list-container" v-if="closePendingAccounts">
      <div class="exit-button" @click="close()">
        <div class="bar2"></div>
        <div class="bar2"></div>
      </div>
      <!-- Main Content -->
      <div class="main-content">
        <h1>List of pending accounts</h1>
        <ul :class="{ 'scrollable-list': approveAccounts.length >= 5 }">
          <li v-for="accounts in approveAccounts" :key="accounts.id" @click="showAccountDetails(accounts)">
            {{ accounts.name }} </li>
        </ul>
  
        <!-- Detailed view for the selected guard -->
        <div v-if="selectedAccount">
          <h2>{{ selectedAccount.name }}</h2>
          <p><strong>Badge Number:</strong> {{ selectedAccount.guardID }}</p>
          <p><strong>Age:</strong> {{ selectedAccount.age }}</p>
          <p><strong>Contact Number:</strong> {{ selectedAccount.contactNumber }}</p>
          <button id="approveButton" @click="approve">Approve</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  export default {
    data() {
      return {
        approveAccounts: [],
        closePendingAccounts: true,
        selectedAccount: null,
      };
    },
    mounted() {
      this.fetchData();
    },
    methods: {
      close() {
        this.$emit('handlePendingAccountsClose', false);
        this.closePendingAccounts = false;
        this.$emit("close");
      },
      showAccountDetails(accounts) {
        this.selectedAccount = accounts;
      },
      fetchData() {
      // Fetch data from the API
      // Replace the URL with the actual API endpoint
      axios.get("http://127.0.0.1:8000/GetAllAccounts")
        .then((response) => {
          this.approveAccounts = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
      }
    },
    
  };
  </script>
  
  <style scoped>
  .secAcc-list-container {
    position: absolute;
    z-index: 5;
    left: 20%;
    width: 80%;
    height: 100%;
    background-color: #f1f1f1;
    overflow: hidden; /* Hide overflowing content */
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
  </style>
  