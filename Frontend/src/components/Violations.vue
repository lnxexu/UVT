<template>
  <div class="violation-list-container" v-if="closeViolation">
    <div class="exit-button" @click="close()">
      <div class="bar2"></div>
      <div class="bar2"></div>
    </div>
    <div class="main-content">
      <h1>Violation List</h1>
      <div id="searchbar">
        <input id = "search" type="text" v-model="student_id" placeholder="Search Student" />
        <!-- make a span that will show after the button is clicked if the student is existing in the database  -->
        <button id= "submit"@click="fetchData()">Submit</button>
        <span id="studentExists"v-if="studentExists">Student does not have any violations or exist in the database.</span>
      </div>
      <ul>
        <li v-for="(violation, index) in violations" :key="index" @click="showViolationDetails(violation)">
          {{ violation.reportID }} ({{ violation.dateTime }}) 
        </li>
      </ul>
      <ViolationDetails v-if="selectedViolation" :selectedViolation="selectedViolation" @close="closeViolation = false" />
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
      student_id: null,
      studentExists: false,
    };
  },
  components: {
    ViolationDetails,
  },  
  computed: {
    filteredViolations() {
      return this.violations.filter(violation => {
        return violation.reportID.toLowerCase().includes(this.student_id.toLowerCase());
      });
    },
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/violationDetails/student/${this.student_id}`);
        this.violations = response.data;
        if (this.violations.length === 0) {
          this.studentExists = true;
        } else {
          this.studentExists = false;
        }
      } 
      catch (error) {
        console.error(error);
        this.studentExists = false;
      }
    },
    toggleExpansion() {
      document.querySelector('.violation-list-container').classList.toggle('expanded');
    },
    showViolationDetails(violation) {
      this.selectedViolation = violation;
      this.$emit("close");
    },
    close() { 
      this.$emit('handleViolationsPageClose', false);
      this.closeViolation = !this.closeViolation;
    },
  } 
};
</script>

<style scoped>
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
  position: absolute;
  z-index: 5;
  left: 20%;
  width: 80%;
  height: 100%;
  background-color: #f1f1f1;
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

</style>