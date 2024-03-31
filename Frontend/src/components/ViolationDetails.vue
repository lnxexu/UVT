<template>
  <div class="blackBG">
    <h2>{{ selectedViolation.title }}</h2>
    <p>{{ selectedViolation.description }}</p>
    <table class="table">
      <thead>
        <tr>
          <th>Date</th>
          <th>Time</th>
          <th>Violation ID</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(entry, index) in tableData" :key="index">
          <td>{{ entry.date }}</td>
          <td>{{ entry.time }}</td>
          <td>{{ entry.violation }}</td>
          <td>{{ entry.status }}</td>
        </tr>
      </tbody>
    </table>
    <!-- Add more details as needed -->
  </div>
</template>

<script>
export default {
  name: "ViolationDetails",
  props: ['selectedViolation'],
  data() {
    return {
      // Assuming you have some data for the table
      tableData: [
        { date: '2023-01-01', time: '12:00 PM', violation: 'V123', status: 'Resolved' },
        { date: '2023-01-02', time: '02:30 PM', violation: 'V124', status: 'Pending' },
        // Add more entries as needed
      ],
    };
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
  }
};
</script>

<style scoped>
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
  border: 1px solid black; /* Set border color to black */
  padding: 10px;
  text-align: left;
  background-color: white; /* Set background color to white */
}

.table th {
  background-color: #333;
  color: white;
}

.table tbody tr:hover {
  background-color: #555;
}

/* Add more styles as needed */
</style>
