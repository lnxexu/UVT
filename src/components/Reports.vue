<!-- ReceiverComponent.vue -->
<template>
  <div class="reports-list-container" v-if = "closeReport">
    <div class="exit-button" @click="close()" >
      <div class="bar2"></div>
      <div class="bar2"></div>
    </div>
    <div class="main-content">
      <h1>Received Messages</h1>
    <ul v-if="receivedReports.length > 0">
      <li v-for="(report, index) in receivedReports" :key="index" @click="messageClicked(report)">
        {{ report.studentName }} - {{ report.violatedRules }} ({{ report.date }} {{ report.time }})
      </li>
    </ul>
    <p v-else>No reports received yet.</p>

    <!-- Display detailed information when a message is clicked -->
    <div v-if="selectedReport">
      <h2>{{ selectedReport.studentName }}</h2>
      <p><strong>Violated Rules:</strong> {{ selectedReport.violatedRules }}</p>
      <p><strong>Date and Time Violated:</strong> {{ selectedReport.date }} {{ selectedReport.time }}</p>
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
    };
  },
  methods: {
    receiveReport(report) {
      this.receivedReports.push(report);
    },
    messageClicked(report) {
      // Set the selected report for detailed view
      this.selectedReport = report;
    },
    close() {
      this.closeReport = false;
      this.$emit("close");
    },
  }
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
