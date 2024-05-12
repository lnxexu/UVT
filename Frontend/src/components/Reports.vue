<template>
  <div class="reports-list-container" v-if = "closeReport" >
    <div class="w3-row">&nbsp;</div>
    <div class="w3-row">&nbsp;</div>
    <div class="w3-row">&nbsp;</div>
    <div class="exit-button" @click="close()" >
      <div class="bar2"></div>
      <div class="bar2"></div>
    </div>
    <div class="main-content">
      <h1><strong>Received Reports</strong></h1>
      <div class="w3-row">&nbsp;</div>
      <div class="w3-row">&nbsp;</div>
      <ul v-if="this.receivedReports.length > 0" class="scrollable-list">
        <li v-for="(report, index) in receivedReports" :key="index" @click="messageClicked(report)">
          {{ report.pReportID }} , {{ report.studentID }}
        </li>
      </ul>
      <p v-else>No reports received yet.</p>
      <div class = "details" v-if="selectedReport">
        <h2><strong>Report ID: {{ selectedReport.pReportID }}</strong></h2>
        <hr>
        <p><strong>Student ID:</strong> {{ selectedReport.studentID }}</p>
        <p><strong>Date and Time:</strong> {{ selectedReport.dateTime }}</p>
        <p><strong>Violation:</strong> {{ selectedReport.violation }}</p>
        <p><strong>Venue: </strong> {{ selectedReport.venue }}</p>
        <p><strong>Sanction: </strong> {{ selectedReport.sanction }}</p>
        <p><strong>Guard: </strong> {{ selectedReport.guard }}</p>
        <div class="editViolation" >
          <button id="editButton" @click="editedReport=!editedReport, editViolation()">Edit</button>
          <button id="deleteReportButton" @click="deleteReport">Delete</button>
        </div>
        <div class = "modalPopup" v-if="editedReport">
          <div id="edit">
            <div class="exit-button"  @click="closePop()" >
              <div class="bar2"></div>
              <div class="bar2"></div>
            </div>
            <h2><strong>Edit Report</strong></h2>
            <hr>
            <p><strong>Report ID:</strong> {{ editedReport.pReportID }}</p>
            <p><strong>Date and Time:</strong> {{ editedReport.dateTime }}</p>
            <p><strong>Guard: </strong> {{ editedReport.guard }}</p>
            <p><strong>Venue: </strong>{{ editedReport.venue }}</p>
            <p><strong>Violation:</strong> {{ editedReport.violation }}
              <select class="input" v-model="editedReport.violation">
                <option v-for="option in violationOptions" :key="option.value" :value="option">
                  {{ option }}
                </option>
              </select>
            </p>
            <p><strong>Sanction: </strong><input class="input" type="text" v-model="editedReport.sanction"></p>
            <div class="confirmButtons">
              <button id="approveButton" @click="approve(),fetchData()">Approve</button>
              <button id="exceptionButton" @click="exception()">Exception</button>
            </div>
          </div>
          <div class="confirm-popup" v-if="showConfirmPopup">
            <p>Are you sure you want to save these changes?</p>
            <p><strong>Report ID: </strong>{{ editedReport.pReportID }}</p>
            <p><strong>Student ID: </strong>{{ editedReport.studentID }}</p>
            <p><strong>Date and Time: </strong>{{ editedReport.dateTime }}</p> 
            <p><strong>Violation: </strong>{{ editedReport.violation }}</p>
            <p><strong>Venue: </strong>{{ editedReport.venue }}</p>
            <p><strong>Sanction: </strong>{{ editedReport.sanction }}</p>
            <p><strong>Guard: </strong>{{ editedReport.guard }}</p>
            <div class="buttons">
              <button class = "yes" @click="yes()">Yes</button>
              <button class = "no" @click="showConfirmPopup = false">No</button>
            </div>
          </div>
        </div>
        <div class="modalPopup" v-if="showConfirmPopupExe">
          <div class="confirm-popup">
            <p>Are you sure you want to make this report an exception?</p>
            <p><strong>Report ID: </strong>{{ selectedReport.pReportID }}</p>
            <p><strong>Student ID: </strong>{{ selectedReport.studentID }}</p>
            <p><strong>Date and Time: </strong>{{ selectedReport.dateTime }}</p> 
            <p><strong>Violation: </strong>{{ selectedReport.violation }}</p>
            <p><strong>Venue: </strong>{{ selectedReport.venue }}</p>
            <p><strong>Sanction: </strong>{{ selectedReport.sanction }}</p>
            <p><strong>Guard: </strong>{{ selectedReport.guard }}</p>
            <div class="buttons">
              <button class = "yes" @click="yesExe">Yes</button>
              <button class = "no" @click="showConfirmPopupExe = false">No</button>
            </div>
          </div>
        </div>
      </div>
      <div class = "details" v-else>
        <h2 style="position: fixed; top:30%; display: flex; justify-content: center;"><strong>Select a report.</strong></h2>
      </div>
      <p v-if="reportDeleted">Report has been deleted.</p>
    </div>
</div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      receivedReports: [],
      selectedReport: null,
      showConfirmPopup: false,
      showConfirmPopupExe: false,
      closeReport: true,
      closeViolation: true,
      reportDeleted: false,
      editedReport: null,
      venue: "",
      sanction: "",
      guard: "",
      violationOptions: [ "Incomplete uniform","No ID", "Improper undershirt","Improper hair color","Bullying", "Littering", "Loitering", "Smoking"],
      edit: false,
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
    exception() {
        this.showConfirmPopupExe = true;
    },
    editViolation() {
      this.editedReport = Object.assign({}, this.selectedReport);
      this.getAssignedLoc();
    },
    save() {
      this.showConfirmPopup = true;
    },
    yes() {
      this.showConfirmPopup = false;
      const dateTime = new Date(this.editedReport.dateTime.replace(' at ', ' '));
      const formattedDate = dateTime.toISOString().split('.')[0];
      this.editedReport.dateTime = formattedDate;
      const formData = {
        studentID: this.editedReport.studentID,
        dateTime: this.editedReport.dateTime,
        violation: this.editedReport.violation,
        venue: this.editedReport.venue,
        sanction: this.editedReport.sanction,
        guard: this.editedReport.guard
      };
      for (let key in formData) {
        if (!formData[key]) {
          alert(`Missing value for ${key}`);
          return;
        }
      }
      console.log(formData);
      const params = new URLSearchParams(formData).toString();
      axios.post(`http://127.0.0.1:8000/violationDetailsPost/?${params}`)
      .then((response) => {
        console.log(response.data);
        alert('Changes saved successfully!');
        this.editedReport = null;
        this.showConfirmPopup = false;
        this.deleteReport();
        this.reportDeleted = true;
      })
      .catch((error) => {
        console.error(error);
      });
    },
    getAssignedLoc(){
      const data = this.editedReport.guard
      axios.get(`http://127.0.0.1:8000/sekyuUsers/assignedLoc/${data}`)
      .then((response) => {
        this.editedReport.venue = response.data.assignedLoc;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    messageClicked(report) {
      this.selectedReport = report; 
    },
    close() {
      this.$emit("goHome");
      this.$emit('handleReportClose', false);
      this.closeReport = false;
      this.$emit("close"); 
    },
    fetchData() {
      axios.get("http://127.0.0.1:8000/pending")
      .then((response) => {
        response.data.forEach((report) => {
          const dateTime = new Date(report.dateTime);
          report.dateTime = dateTime.toLocaleString('en-US', { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric' });
        });
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
      this.showConfirmPopup = true;
    },
    closePop() {
      this.editedReport = null;
    },
    getGuards() {
      axios.get(`http://127.0.0.1:8000/sekyuUsers/guards`)
      .then((response) => {
        this.guardOptions = response.data;
        console.log(this.guardOptions);
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
.reports-list-container {
  position: fixed;
  display: block;
  left: 0%;
  width: 100%;
  height: 100%;
  background-color: #f1f1f1;
  z-index: 2;
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
.modalPopup {
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

.modalPopup .exit-button{
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
  height: 55%;
}

#editButton {
  background-color: #f0a500;
  width: 30%;
}
#deleteReportButton {
  background-color: #f44336;
  width: 30%;
}
#approveButton{
  background-color: #4CAF50;
  width: 100%;
}
#exceptionButton {
  background-color: #008CBA;
  width: 100%;
}

#editButton:hover {
  background-color: #e69500;
}
#deleteReportButton:hover {
  background-color: #ff2819;
}
#approveButton:hover {
  background-color: #45a049;
}
#exceptionButton:hover {
  background-color: #0073a6;
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
  margin: 0%;
  width: 30%;
  position: relative;
  left: 34.5%;
}
#save:hover {
  background-color: #45a049;
}

ul {
  list-style-type: none;
  padding: 0;
  cursor: pointer;
  width: 45%;
}

.main-content .details {
  display: inline-block;
  justify-content: center;
  align-items: center;
  margin: 10px;
  padding: 10px;
  border-radius: 5px;
  width: 50%;
  position: fixed;
  left: 47.8%;
  top: 23%;
}

.confirm-popup {
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
.modalPopup button.yes {
  background-color: #4CAF50;
  color: white;
}
.modalPopup button.yes:hover {
  background-color: #45a049;
}
.modalPopup button.no {
  background-color: #f44336;
  color: white;
}
.modalPopup  button.no:hover {
  background-color: #ff2819;
}

.modalPopup button {
  margin: 10%;
  background-color: #cccccc;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  text-transform: uppercase;
  display: inline;
  justify-content: center;
  align-items: center;
  width: 100%;
}

.modalPopup  p {
  margin: 0;
  padding: 5px;
}
.modalPopup h2 {
  margin: 0;
  padding: 5px;
}
.modalPopup strong {
  margin: 0;
  padding: 5px;
}
.modalPopup button ::hover {
  background-color: #ccc;

}
.modalPopup.buttons {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
.scrollable-list {
  height: 670px; 
  overflow-y: auto;
}
.confirmButtons {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  height: 2%;
  margin-top: 4%;
}
button {
  padding: 10px;
  margin: 5px;
  background-color: #cccccc;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  text-transform: uppercase;
  display: inline;
  justify-content: center;
  align-items: center;
  width: 100%;
  color: white;
}
.edit{
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  height: 2%;
  margin-top: 4%;
  width: 70%;
  position: relative;
  left: 15%;
}
.edit #editButton {
  margin-right: 20%;
}
.edit #deleteReportButton {
  width: 30%;
}
.buttons{
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  text-transform: uppercase;
  display: inline;
  justify-content: center;
  align-items: center;
  width: 100%;
  color: white;
}
.buttons .yes, .buttons .no {
  width: 30%;
}

</style>
