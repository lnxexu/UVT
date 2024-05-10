<template>
  <div class="blackBG">
    <h2> {{ fullName }}</h2>
    <p> Report Number:{{ selectedViolation.reportID }}</p>
    <table class="table">
      <thead>
        <tr>
          <th>Report ID</th>
          <th>Student ID</th>
          <th>Date</th>
          <th>Venue</th>
          <th>Sanctions</th>
          <th>Violation</th>
          <th>Guard</th>
        </tr>
      </thead>
      <tbody in selectedViolation>
        <tr>
          <td>{{ selectedViolation.reportID }}</td>
          <td>{{ selectedViolation.studentID }}</td>
          <td>{{ selectedViolation.dateTime }}</td>
          <td>{{ selectedViolation.venue }}</td>
          <td>{{ selectedViolation.sanction }}</td>
          <td>{{ selectedViolation.violation }}</td>
          <td>{{ selectedViolation.guard }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "ViolationDetails",
  props: ['selectedViolation'],
  data() {
    return {
      fullName: '',
    };
  },
  methods: {  
    getFullName() {
      axios.get(`http://127.0.0.1:8000/student/${this.selectedViolation.studentID}`)
      .then(response => {
        this.fullName = response.data.name;
      })
      .catch(error => {
        console.error(error);
      });
      
    },
    
    
  },
  watch: {
    selectedViolation: {
      handler: 'getFullName',
      immediate: true,
    },
  },
};
</script>

<style scoped>
* {font-family:"Raleway", sans-serif}
.blackBG {
  position: relative;
  background-color: black;
  color: white;
  padding: 20px;
}

.table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.table th,
.table td {
  border: 1px solid black; 
  padding: 10px;
  text-align: left;
  background-color: white; 
}

.table th {
  background-color: #333;
  color: white;
}

.table tbody tr:hover {
  background-color: #555;
}
</style>
