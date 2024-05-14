<template>
  <div class="Sekyu-login-container">
    <button id ="back"  @click="goBack"><i id="fa fa-long-arrow-left"></i><strong> Back</strong></button>
    <div class="shadow-box" :style="{ height: resetPassword ? '47%' : '30%' }">
        <h1 v-if="!resetPassword">Forgot Password (Security Guard)</h1>
        <h1 v-else>Reset Password (Security Guard)</h1>
        <hr>
        <div id="forms1" v-if="!resetPassword" >
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="text" id="email" class="size" pattern="^[a-zA-Z0-9]+@gmail\.com$" v-model="email" required/>
            <button id="button1" class="raise" @click = "findAccount()">SUBMIT</button>
        </div>
        </div>
        <div id="forms2" v-else>
        <div class="form-group">
            <label for="newPassword">New Password:</label>
            <input type="password" id="newPassword" class="size" v-model="newPassword" required>
            <div class="w3-row">&nbsp;</div>
            <label for="confirmPassword">Confirm New Password:</label>
            <input type="password" id="confirmPassword" class="size" v-model="confirmPassword" required>
            <button id="button2" class="raise" @click = "changePassword">CHANGE PASSWORD</button>
        </div>
        </div>
    </div>
  </div>
</template>
      
<script>
import axios from 'axios';
export default {
  data() {
    return {
      email: '',
      newPassword: '',
      confirmPassword: '',
      resetPassword: false, 
      }
  },
  methods: {
    goBack() {
      this.$router.go(-1);
    },
    changePassword() {
    const params = new URLSearchParams({
      password: this.newPassword
      }).toString();
      axios.put(`http://127.0.0.1:8000/sekyuUsers/changePassword/${this.email}?${params}`)
      .then((response) => {
          console.log(response);
          this.resetPassword = false;
          alert('Password changed successfully');
          this.$router.push({ name: 'OSADLogin' });
      })
      .catch((error) => {
          console.error(error);
          alert('Error changing password');
      });
    },
    findAccount(){
      axios.get(`http://127.0.0.1:8000/sekyuUsers/searchUser/${this.email}`)
      .then((response) => {
          console.log(response);
          this.resetPassword = true;
      })
      .catch((error) => {
          console.log(error);
          alert('Email not found');
      });
    }
  },
};
</script>

<style scoped>
@import url('https://www.w3schools.com/w3css/4/w3.css');
@import url('https://fonts.googleapis.com/css?family=Raleway');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css');

.Sekyu-login-container {
  width: 100%; 
  height: 100vh; 
  background-color: #0D0D0D;
  color: white;
  position: fixed;
  top: 50%; 
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 2%;
  display: flex;
  flex-direction: column;
  align-items: center; 
  background-image: url("../assets/LogInPage.jpg");
  background-size: cover;
  background-repeat: no-repeat;
}
#signup, p, label,h1{
  position: relative;
  text-align: center;
  color: #0D0D0D;
}
p, label, a{
  text-transform: uppercase;
  font-weight: 700;
}
hr{
  width: 100%;
  color: #000000;
  position: absolute;
  top: 13%;
  border: 2px solid;
}

h1{
  margin: 2% 0;
  font-size: 2em;
  text-transform: uppercase;
  font-style: italic;
}
#forms1 {
  display: flex;
  flex-direction: column; 
  margin-bottom: 20px; 
  position: absolute;
  top: 29%;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: auto;
}
#forms2 {
  display: flex;
  flex-direction: column; 
  margin-bottom: 20px; 
  position: absolute;
  top: 25%;
  align-items: center;
  width: 100%;
}

.form-group {
  margin-bottom: 10px; 
  display: flex;
  flex-direction: column;
  color: #0D0D0D;
  left: 20%;
  width: 80%;
}

#login1 {
  border-radius: 0px;
  position: fixed;
  top: 77%;
  left: 35.5%;
}
.raise:hover,
.raise:focus {
  box-shadow: 0 0.5em 0.5em -0.4em var(--hover);
  transform: translateY(-0.25em);
}
.raise {
  --color: #292929;
  --hover: #000000;
}
button:not(#back) { 
  color: var(--color);
  transition: 0.25s;
  background: none;
  border: 2px solid;
  font: inherit;
  line-height: 1;
  padding: 1em 2em;
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
}

button:hover,
button:focus { 
  border-color: var(--hover);
  color: black;
}
.shadow-box {
  position: relative;
  top: 45%;
  left: 0%;
  width: 37%;
  background-color: #ffffff;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.7); 
  border-radius: 10px;
}

.size {
  width: 100%;
  height: 2.7em;
  border-radius: 7em;
}

@media (max-width: 768px) {
  .Sekyu-login-container {
  padding: 1rem;
  background-image: url("../assets/LogInPage.jpg");
  background-repeat: no-repeat;
  background-position-x: 47% ;

  }

  .shadow-box {
  width: 95%;
  height: 70%;
  }

  .size {
  width: 95%;
  height: 2.5em;
  }

  button {
  left: 50%;
  top: 90%;
  transform: translateX(-50%);
  }

  h1 {
  font-size: 1.2em;
  }

  .form-group {
  font-size: 0.8em;
  left: 10%;
  width:90%;
  }

  .size {
  width: 100%;
  height: 2.5em;
  }
}
* {font-family:"Raleway", sans-serif}

#button1{
  width: 20%;
  position: absolute;
  left: 40%;
  top: 130%;
}

#button2{
  width: 30%;
  position: absolute;
  left: 35%;
  top: 120%;
}

#back {
  width: 3%;
  height: 3%;
  position: absolute;
  left: 2%;
  top: 3%;
  border-radius: 5px;
  border: 1px solid #ffffff;
}

#back:hover {
  background-color: #000000;
  color: rgb(255, 255, 255);
  border: 1px solid #000000;
  border-radius: 5px;
  transition: 0.3s;
}
</style>