<template>
<div class = "bg">
  <div class="Sekyu-login-container">
    <div class="shadow-box">
        <h1 v-if="!resetPassword">Forgot Password</h1>
        <h1 v-else>Reset Password</h1>
        <form @submit.prevent="submitForm">
            <hr>
            <div id="forms1" v-if="!resetPassword" >
                
                <div class="form-group">
                    <label for="email">Email:</label>
                    <input type="text" id="email" class="size" pattern="^[a-zA-Z0-9]+@gmail\.com$" v-model="email" required/>
                    <button id="button1" class="raise" @click = "login(), postLogin()">SUBMIT</button>
                </div>
            </div>
            <div id="forms2" v-else>
                <div class="form-group">
                    <label for="newPassword">New Password:</label>
                    <input type="password" id="newPassword"  class="size" v-model="newPassword" required>
                    <label for="confirmPassword">Confirm New Password:</label>
                    <input type="password" id="confirmPassword"  class="size" v-model="confirmPassword" required>
                    <button id="button2" class="raise" @click = "login(), postLogin()">CHANGE PASSWORD</button>
                </div>
            </div>
            
        </form>
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
        };
      },
      methods: {
        submitForm() {
          if (!this.resetPassword) {
            console.log(`Initiating password reset for ${this.email}`);
            this.resetPassword = true; 
  
          } else {
            
            axios.put(`http://127.0.0.1:8000//OSADusers/changePassword/${this.email}`)
              .then((response) => {
                console.log(response);
                console.log(`Resetting password for ${this.newPassword}`);
              })
              .catch((error) => {
                console.log(error);
              });
          }
        },
      },
  };
  </script>
  
<style scoped>

.bg{
  background-color: #0D0D0D;
  height: 100vh;
  width: 100%;
}
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
  border-radius: 1%;
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
  top: 25%;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 20%;
  
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
button {  
  color: var(--color);
  transition: 0.25s;
  background: none;
  border: 2px solid;
  font: inherit;
  line-height: 1;
  margin: 0.5em;
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
  height: 47%;
  background-color: #ffffff;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.7); 
  border-radius: 10px;

}

.size {
  width: 100%;
  height: 2.7em;
  border-radius: 7em;
}



/* For mobile phones */
@media (max-width: 768px) {
  .Sekyu-login-container {
    padding: 1rem;
    /* make the picture go center */
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
  
</style>