<template>
    <div class="secAcc-list-container" v-if="closeSekyu">
      <div class="w3-row">&nbsp;</div>
      <div class="w3-row">&nbsp;</div>
      <div class="w3-row">&nbsp;</div>
      <div class="exit-button" @click="close()">
        <div class="bar2"></div>
        <div class="bar2"></div>
      </div>
      <!-- Main Content -->
      <div class="main-content">
        <h1>Security Guards List</h1>
        <ul :class="{ 'scrollable-list': securityGuards.length >= 5 }">
          <li v-for="guard in securityGuards" :key="guard.guardID" @click="showGuardDetails(guard)">
            {{ guard.name }} - Badge Number: {{ guard.guardID }}
          </li>
        </ul>
  
        <!-- Detailed view for the selected guard -->
        <div v-if="selectedGuard">
          <h2>{{ selectedGuard.name }}</h2>
          <p><strong>Badge Number:</strong> {{ selectedGuard.guardID }}</p>
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
        securityGuards: [],
        closeSekyu: true,
        selectedGuard: null,
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
      fetchData() {
      axios.get("http://127.0.0.1:8000/securityGuard")
        .then((response) => {
          this.securityGuards = response.data;
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
  