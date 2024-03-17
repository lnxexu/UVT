<template>
    <div class="secAcc-list-container" v-if="closeSekyu">
      <div class="exit-button" @click="close()">
        <div class="bar2"></div>
        <div class="bar2"></div>
      </div>
      <!-- Main Content -->
      <div class="main-content">
        <h1>Security Guards List</h1>
        <ul :class="{ 'scrollable-list': securityGuards.length >= 5 }">
          <li v-for="guard in securityGuards" :key="guard.id" @click="showGuardDetails(guard)">
            {{ guard.name }} - Badge Number: {{ guard.badgeNumber }}
          </li>
        </ul>
  
        <!-- Detailed view for the selected guard -->
        <div v-if="selectedGuard">
          <h2>{{ selectedGuard.name }}</h2>
          <p><strong>Badge Number:</strong> {{ selectedGuard.badgeNumber }}</p>
          <p><strong>Age:</strong> {{ selectedGuard.age }}</p>
          <p><strong>Contact Number:</strong> {{ selectedGuard.contactNumber }}</p>
          <!-- Add more personal information as needed -->
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        securityGuards: [
            { id: 1, name: '21 Savage', badgeNumber: 'SG001', age: 30, contactNumber: '123-456-7890' },
            { id: 2, name: 'Metro Boomin', badgeNumber: 'SG002', age: 28, contactNumber: '987-654-3210' },
            { id: 3, name: 'Drake', badgeNumber: 'SG003', age: 30, contactNumber: '123-456-7890' },
            { id: 4, name: 'J. Cole', badgeNumber: 'SG004', age: 30, contactNumber: '123-456-7890' },
            { id: 5, name: 'Bas', badgeNumber: 'SG005', age: 30, contactNumber: '123-456-7890' },
            { id: 6, name: 'JID', badgeNumber: 'SG006', age: 30, contactNumber: '123-456-7890' },
        ],
        closeSekyu: true,
        selectedGuard: null,
      };
    },
    methods: {
      close() {
        this.closeSekyu = false;
        this.$emit("close");
      },
      showGuardDetails(guard) {
        this.selectedGuard = guard;
      },
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
  