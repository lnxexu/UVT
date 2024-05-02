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
      <button id="approveButton" @click="approve">Approve</button>
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
          <p><strong>Venue: </strong> <input class="input" type="text" v-model="editedReport.venue"></p>
          <p><strong>Sanction: </strong> <input class="input" type="text" v-model="editedReport.sanction"></p>
          <p><strong>Status: </strong> <input class="input" type="text" v-model="editedReport.status"></p>
          <p><strong>Guard: </strong> <input class="input" type="text" v-model="editedReport.guard"></p>
          <button id="save" @click="save">Save</button>
        </div>
        <div id="confirm-popup" v-if="showConfirmPopup">
          <p>Are you sure you want to save these changes?</p>
          <p><strong>Report ID: </strong>{{ editedReport.pReportID }}</p>
          <p><strong>Student ID: </strong>{{ editedReport.studentID }}</p>
          <p><strong>Date and Time: </strong>{{ editedReport.dateTime }}</p> 
          <p><strong>Violation: </strong>{{ editedReport.violation }}</p>
          <p><strong>Venue: </strong>{{ editedReport.venue }}</p>
          <p><strong>Sanction: </strong>{{ editedReport.sanction }}</p>
          <p><strong>Status: </strong>{{ editedReport.status }}</p>
          <p><strong>Guard: </strong>{{ editedReport.guard }}</p>
          <div class="buttons">
            <button id = "yes" @click="yes">Yes</button>
            <button id = "no" @click="showConfirmPopup = false">No</button>
          </div>
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
      showConfirmPopup: false,
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
    },
  },
  mounted() {
    this.fetchData();
  },
  created() {
    this.fetchData();
  },
  methods: {
    toggleExpansion() {
      document.querySelector('.violation-list-container').classList.toggle('expanded')
    },
    edit() {
      this.editedReport = Object.assign({}, this.selectedReport);
    },
    save() {
      this.showConfirmPopup = true;
    },
    yes() {
      this.showConfirmPopup = false;
      const formData = {
        violation: this.editedReport.violation,
        venue: this.editedReport.venue,
        sanction: this.editedReport.sanction,
        status: this.editedReport.status,
        guard: this.editedReport.guard
      };
      const id = this.editedReport.pReportID;
      for (let key in formData) {
        if (!formData[key]) {
          console.error(`Missing value for ${key}`);
          return;
        }
      }
      const params = new URLSearchParams(formData).toString();
      const newData = id + "?" + params;
      axios.put(`http://127.0.0.1:8000/pendingUpdate/${newData}`)
      .then((response) => {
        console.log(response.data);
        this.editedReport = null;
        this.showConfirmPopup = false;
        alert('Changes saved successfully!');
      })
      .catch((error) => {
        console.error(error);
      });
    },
    messageClicked(report) {
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
      const formData = {
        pReportID: this.selectedReport.pReportID,
        studentID: this.selectedReport.studentID,
        dateTime: this.selectedReport.dateTime,
        violation: this.selectedReport.violation
      };
      for (let key in formData) {
        if (!formData[key]) {
          console.error(`Missing value for ${key}`);
          return;
        }
      }
      axios.delete(`http://127.0.0.1:8000/pendingDelete/${formData.pReportID}`)
      .then((response) => {
        console.log(response.data);
        this.reportDeleted = true;
      })
      .catch((error) => {
        console.error(error);
      });
    },
    approve() {
      const formData = {
        studentID: this.selectedReport.studentID,
        dateTime: this.selectedReport.dateTime,
        violation: this.selectedReport.violation,
        venue: this.selectedReport.venue,
        sanction: this.selectedReport.sanction,
        status: this.selectedReport.status,
        guard: this.selectedReport.guard
      };
      for (let key in formData) {
        if (!formData[key]) {
          console.error(`Missing value for ${key}`);
          return;
        }
      }
      console.log(formData);
      const params = new URLSearchParams(formData).toString();
      axios.post(`http://127.0.0.1:8000/violationDetailsPost?${params}`)
        .then((response) => {
          console.log(response.data);
          this.deleteReport();
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
* {font-family:"Raleway", sans-serif}
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
#save:hover {
  background-color: #45a049;
}

#confirm-popup {
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #f1f1f1;
  padding: 20px;
  border-radius: 5px;
  width: 20%;
  display: flex;
  flex-direction: column;
  transition: 0.3s;
  z-index: 9999;
  border: #333 1px solid;
}
#confirm-popup button {
  padding: 10px;
  margin: 5px;
  background-color: #cccccc;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  text-transform: uppercase;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  margin-left: auto;
  margin-right: auto;
  width: 30%;
}
#confirm-popup button#yes {
  background-color: #4CAF50;
  color: white;
}
#confirm-popup button#yes:hover {
  background-color: #45a049;
}
#confirm-popup button#no {
  background-color: #f44336;
  color: white;
}
#confirm-popup button#no:hover {
  background-color: #ff2819;
}

#confirm-popup p {
  margin: 0;
  padding: 5px;
}
#confirm-popup h2 {
  margin: 0;
  padding: 5px;
}
#confirm-popup strong {
  margin: 0;
  padding: 5px;
}
#confirm-popup button ::hover {
  background-color: #ccc;

}
#confirm-popup .buttons {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

</style>
