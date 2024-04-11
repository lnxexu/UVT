<!-- ReceiverComponent.vue -->
<template>
  <div class="reports-list-container" v-if = "closeReport">
    <div class="exit-button" @click="close()" >
      <div class="bar2"></div>
      <div class="bar2"></div>
    </div>
    <div class="main-content">
      <h1>Received Messages</h1>
    <ul v-if="this.receivedReports.length > 0">
      <li v-for="(report, index) in receivedReports" :key="index" @click="messageClicked(report)">
        {{ report.pReportID }} 
      </li>
    </ul>
    <p v-else>No reports received yet.</p>

    <!-- Display detailed information when a message is clicked -->
    <div v-if="selectedReport">
      <h2>{{ selectedReport.studentID }}</h2>
      <p><strong>Violated Rules:</strong> {{ selectedReport.violation }}</p>
      <p><strong>Date and Time Violated:</strong> {{ selectedReport.dateAndTime }}</p>
      <!-- Add more details as needed -->
    </div>
  </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      receivedReports: [],
      selectedReport: null,
      closeReport: true,
      closeViolation: true,
    };
  },
  methods: {
    toggleExpansion() {
      document.querySelector('.violation-list-container').classList.toggle('expanded')
    },
    messageClicked(report) {
      // Set the selected report for detailed view
      this.selectedReport = report;
    },
    close() {
      this.closeReport = false;
      this.$emit("close");
    },
    fetchData() {
      // Fetch data from the API
      // Replace the URL with the actual API endpoint
      axios.get("http://127.0.0.1:8000/pending")
        .then((response) => {
          this.receivedReports = response.data;
          console.log(this.receivedReports.length)
        })
        .catch((error) => {
          console.error(error);
        });
  }
},
mounted() {
    this.fetchData();
  },
};
</script>

<style scoped>
.reports-list-container {
  position: absolute;
  z-index: 5;
  left: 20%;
  width: 80%;
  height: 100%;
  background-color: #f1f1f1;
}
.reports-list-container.expanded {
  width: 100%;
  height: 100%;
  position: fixed;
  left: 0;
  top: 0;
}


ul {
  list-style-type: none;
  cursor: pointer;
  padding: 0;
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

/* Style for the detailed information */
h2, p {
  margin: 0;
  padding: 5px;
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
.main-content {
  flex: 1;
  padding: 20px;
}
</style>
