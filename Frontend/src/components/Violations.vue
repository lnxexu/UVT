<template>
  <div class="violation-list-container" v-if="closeViolation">
    <div class="w3-row">&nbsp;</div>
    <div class="w3-row">&nbsp;</div>
    <div class="w3-row">&nbsp;</div>
    <div class="exit-button" @click="close()">
      <div class="bar2"></div>
      <div class="bar2"></div>
    </div>
    <div class="main-content">
      <h1>Violation List</h1>
      <div id="searchbar">
        <input id = "search" type="text" v-model="student_id" placeholder="Search Student"  />
        <!-- <ul v-if="searchResults.length" class="search">
          <li v-for="violation in searchResults" @click="selectV(violation)">
            {{ violation.fullName }}
          </li>
        </ul> -->
        <button id= "submit" @click="fetchData(), selectedViolation = null">Submit</button>
        <span id="studentExists"v-if="studentExists">Student does not have any violations or exist in the database.</span>
      </div>
      <ul class="scrollable-list">
        <li v-for="(violation, index) in violations" :key="index" @click="showViolationDetails(violation)">
          {{ violation.reportID }} ({{ violation.dateTime }}) 
        </li>
      </ul>
      <ViolationDetails id="details" v-if="selectedViolation" :selectedViolation="selectedViolation" @close="closeViolation = false"  @resetEvent="reset" @resetList="resetList"/>
      
    </div>
  </div>
</template>

<script>
import ViolationDetails from './ViolationDetails.vue';
import axios from 'axios';

export default {
  name: "Violations",
  data() {
    return {
      violations: [],
      selectedViolation: null,
      closeViolation: true,
      student_id: '',
      studentExists: false,
      searchResults: [],
    };
  },
  components: {
    ViolationDetails,
  },  
  mounted() {
    this.getAllApprovedViolations();
  },
  methods: {
    // selectV(violation) {
    //   this.student_id = '';
    //   this.selectedGuard = violation;
    //   this.searchResults = [];
    // },
    // filterViolations() {
    //     if (!this.fetchData || !this.student_id) {
    //       this.searchResults = [];
    //       return;
    //     }
    //     this.filteredGuards = this.fetchData.filter(violation =>
    //       violation.fullName && violation.fullName.toLowerCase().includes(this.student_id.toLowerCase())
    //     );
    //   },
    reset(){
      this.getAllApprovedViolations();
      this.selectedViolation = false;
    },
    resetList(){
      this.getAllApprovedViolations();
    },
    getAllApprovedViolations() {
      axios.get(`http://127.0.0.1:8000/violationDetailsAll`)
      .then(response => {
        this.violations = response.data.map(report => {
          let dateTime = new Date(report.dateTime);
          let formattedDateTime = dateTime.toLocaleString('en-US', { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric' });
          return { ...report, dateTime: formattedDateTime};
        });
      })
      .catch(error => {
        console.error(error);
      });
    },
    async fetchData() {
      try {
        // if (!this.student_id) {
        //   this.searchResults = [];
        //   return;
        // }
        const data = { query : this.student_id };
        const params = new URLSearchParams(data).toString();
        const response = await axios.get(`http://127.0.0.1:8000/violationDetails/student/search?${params}`);
        this.violations = response.data.map(report => {
          let dateTime = new Date(report.dateTime);
          let formattedDateTime = dateTime.toLocaleString('en-US', { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric' });
          return { ...report, dateTime: formattedDateTime};
        });
        // this.searchResults = response.data.map(report => {
        //   let dateTime = new Date(report.dateTime);
        //   let formattedDateTime = dateTime.toLocaleString('en-US', { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric' });
        //   return { ...report, dateTime: formattedDateTime};
        // });
        if (this.violations.length === 0) {
          this.studentExists = true;
        } else {
          this.studentExists = false;
        }
      } 
      catch (error) {
        console.error(error);
        alert("Student does not exist in the database.");
        this.studentExists = false;
        this.getAllApprovedViolations();
      }
    },
    showViolationDetails(violation) {
      this.selectedViolation = violation;
      console.log(this.selectedViolation);
    },
    close() { 
      this.$emit("goHome1");
      this.$emit('handleViolationsPageClose', false);
      this.$emit("close");
    },
  } 
};
</script>

<style scoped>
* {font-family:"Raleway", sans-serif}
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
.violation-list-container {
  position: fixed;
  display: block;
  left: 0%;
  width: 100%;
  height: 100%;
  background-color: #f1f1f1;
  z-index: 2;
}
  
.violation-list-container.expanded {
  width: 100%;
}
.main-content {
  flex: 1;
  padding: 20px;
}

ul {
  list-style-type: none;
  padding: 0;
  cursor: pointer;
  width: 45%;
}

.main-content #details {
  display: inline-block;
  justify-content: center;
  align-items: center;
  margin: 10px;
  padding: 10px;
  border-radius: 5px;
  width: 50%;
  position: fixed;
  left: 47.8%;
  top: 31%;
}
li {
  margin-bottom: 10px;
  padding: 10px;
  background-color: #ddd;
  border-radius: 5px;
}

li:hover {
  background-color: #ccc;
}

#search {
  margin: 10px;
  padding: 10px;
  width: 20%;
  border-radius: 5px;
}

#submit {
  margin: 10px;
  padding: 10px;
  background-color: #ddd;
  border-radius: 5px;
  cursor: pointer;
}

#searchbar {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 10px;
  padding: 10px;
  border-radius: 5px;
  width: 100%;
  flex-wrap: wrap;
}

#studentExists {
  position: fixed;
  color: red;
  font-size: 20px;
  margin-top: 5%;
}

.scrollable-list {
  height: 600px; 
  overflow-y: auto;
}

</style>
