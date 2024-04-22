<!-- ReceiverComponent.vue -->
<template>
  <div class="reports-list-container" v-if = "closeReport">
    <div class="exit-button" @click="close()" >
      <div class="bar2"></div>
      <div class="bar2"></div>
    </div>
    <div class="main-content">
      <h1>Received Reports</h1>
    <ul v-if="this.receivedReports.length > 0">
      <li v-for="(report, index) in receivedReports" :key="index" @click="messageClicked(report)">
        {{ report.pReportID }} , {{ report.studentID }}
      </li>
    </ul>
    <p v-else>No reports received yet.</p>
    <hr>
    <div v-if="selectedReport">
      <h2><strong>Report ID: {{ selectedReport.pReportID }}</strong></h2>
      <hr>
      <p><strong>Student ID:</strong> {{ selectedReport.studentID }}</p>
      <p><strong>Date and Time:</strong> {{ selectedReport.dateTime }}</p>
      <p><strong>Violation:</strong> {{ selectedReport.violation }}</p>
      <p><strong>Venue: </strong> {{ selectedReport.venue }}</p>
      <p><strong>Sanction: </strong> {{ selectedReport.sanction }}</p>
      <p><strong>Status: </strong> {{ selectedReport.status }}</p>
      <p><strong>Guard: </strong> {{ selectedReport.guard }}</p>
      <button id="editButton" @click="edit">Edit</button>
      <button id="deleteReportButton" @click="deleteReport">Delete</button>
      <div id="edit-modal" v-if="editedReport">
        <div id="edit">
          <div class="exit-button"  @click="closePop()" >
            <div class="bar2"></div>
            <div class="bar2"></div>
          </div>
          <h2>Edit Report</h2>
          <p><strong>Report ID:</strong> {{ editedReport.pReportID }}</p>
          <p><strong>Date and Time:</strong> {{ editedReport.dateTime }}</p>
          <p><strong>Violation:</strong> {{ editedReport.violation }}</p>
          <input class="input" type="text" v-model="editedReport.violation">
          <p><strong>Venue: </strong> <input class="input" type="text" v-model="venue"></p>
          <p><strong>Sanction: </strong> <input class="input" type="text" v-model="sanction"></p>
          <p><strong>Status: </strong> <input class="input" type="text" v-model="status"></p>
          <p><strong>Guard: </strong> <input class="input" type="text" v-model="guard"></p>
          <button id="save" @click="save">Save</button>
        </div>
      </div>
      <p v-if="reportDeleted">Report has been deleted.</p>
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
      reportDeleted: false,
      editedReport: null,
      venue: "",
      sanction: "",
      status: "",
      guard: "",
    };
  },
  computed: {
  reports() {
    return this.$store.state.reports;
  }
},
  methods: {
    toggleExpansion() {
      document.querySelector('.violation-list-container').classList.toggle('expanded')
    },
    edit() {
      this.editedReport = Object.assign({}, this.selectedReport);
    },
    save() {
      if (window.confirm('Are you sure you want to save these changes?')) {
        this.selectedReport = this.editedReport;
      }
    },
    
    messageClicked(report) {
      // Set the selected report for detailed view
      this.selectedReport = report;
      this.editedReport = null;
    },
    close() {
      this.$emit('handleReportClose', false); // Emitting the event
      this.closeReport = false;
      this.$emit("close");
    },
    fetchData() {
      axios.get("http://127.0.0.1:8000/pending")
      .then((response) => {
        this.receivedReports = response.data;
      })
      .catch((error) => {
        console.error(error);
      });
    },
    deleteReport() {
      axios.delete(`http://127.0.0.1:8000/pendingDelete/${this.pReportID}`)
      .then((response) => {
        console.log(response.data);
        this.reportDeleted = true;
      })
      .catch((error) => {
        console.error(error);
      });  
    },
    closePop() {
      this.editedReport = null;
    },
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
#edit-modal {
  position: fixed;
  z-index: 9999;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: -moz-hidden-unscrollable;
  background-color: rgba(0,0,0,0.4);
  transition: 0.3s;
}
#edit-modal .exit-button{
  position: absolute;
  top: 1%;
  left: 94%;
}

#edit {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #f1f1f1;
  padding: 20px;
  border-radius: 5px;
  width: 70%;
}
#editButton:hover {
  background-color: #ccc;
}

#deleteReportButton:hover {
  background-color: #ccc;
}
button {
  padding: 10px;
  margin: 5px;
  background-color: #cccccc;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  text-transform: uppercase;
}
.input{
  padding: 10px;
  margin: 5px;
  border-radius: 5px;
  border: 1px solid #ccc;
  width: 100%;
}

#save {
  background-color: #4CAF50;
  color: white;
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 30%;

}
</style>
