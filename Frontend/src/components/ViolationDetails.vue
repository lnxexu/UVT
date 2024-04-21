<template>
  <div class="blackBG">
    <h2>{{ selectedViolation.reportID }}</h2>
    <p>{{ selectedViolation.studentID }}</p>
    <table class="table">
      <thead>
        <tr>
          <th>Report ID</th>
          <th>Student ID</th>
          <th>Date</th>
          <th>Venue</th>
          <th>Status</th>
          <th>Sanctions</th>
          <th>Violation ID</th>
          <th>Guard ID</th>
        </tr>
      </thead>
      <tbody>
        <tr in selectedViolation >
          <td>{{ selectedViolation.reportID }}</td>
          <td>{{ selectedViolation.studentID }}</td>
          <td>{{ selectedViolation.dateTime }}</td>
          <td>{{ selectedViolation.venue }}</td>
          <td>{{ selectedViolation.status }}</td>
          <td>{{ selectedViolation.sanctions }}</td>
          <td>{{ selectedViolation.violationID }}</td>
          <td>{{ selectedViolation.guardID }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "ViolationDetails",
  props: ['selectedViolation'],
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
