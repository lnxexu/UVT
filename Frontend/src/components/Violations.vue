<template>
  <div class="violation-list-container" v-if="closeViolation">
    <div class="exit-button"  @click="close()">
        <div class="bar2"></div>
        <div class="bar2"></div>
      </div>
    <!-- Main Content -->
    <div class="main-content">
      <h1>Violation List</h1>
      <ul>
        <li v-for="(violation, index) in violations" :key="index" @click="showViolationDetails(violation)">
          {{ violation.title }}
        </li>
      </ul>
      <!-- Show ViolationDetails component when a violation is selected -->
      <ViolationDetails v-if="selectedViolation" :selectedViolation="selectedViolation" />
    </div>
  </div>


</template>

<script>
import ViolationDetails from './ViolationDetails.vue';
import OSAD from '../view/OSAD.vue';


export default {
  data() {
    return {
      violations: [
        { title: 'Violation 1', description: 'Description 1' },
        { title: 'Violation 2', description: 'Description 2' },
        // Add more violations as needed
      ],
      selectedViolation: null,
      closeViolation: true,

    };
  },
  components: {
    ViolationDetails,
  },
  methods: {
    async fetchViolations() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/violation');
        this.violations = response.data;
        console.log(this.violations)
      } 
      catch(error) {
        console.error(error);
      }
    },
    toggleExpansion() {
      document.querySelector('.violation-list-container').classList.toggle('expanded');
    },
    showViolationDetails(violation) {
      this.selectedViolation = violation;
    },
    close() { 
      this.closeViolation = !this.closeViolation;
      this.$emit("close");
      
    },
  },
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
  height: 100%;
  position: fixed;
  left: 0;
  top: 0;
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
</style>