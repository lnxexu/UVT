<script>
import bg from "../components/Background.vue"
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: '',
      error: null,
      username: '',
      fullName: '',
      timestampLogin: ''
    };
  },
  components: { bg },
  methods: {
    login() {
      const formData = {
        email: this.email,
        password: this.password
      };
      for (let key in formData) {
        if (!formData[key]) {
          console.error(`Missing value for ${key}`);
          alert(`Missing value for ${key}`);
          return;
        }
      }
      const params = new URLSearchParams(formData).toString();
      axios.get(`http://127.0.0.1:8000/OSADusers/verify/?${params}`)
      .then(response => {
        console.log(response);
        if (response.data.email === this.email && response.data.password === this.password) {
          this.$router.push('OSAD');
        } else {
          this.error = "Invalid email or password";
          alert("Invalid email or password");
        }
      })
      .catch(error => {
        console.log(error);
        this.error = "Invalid email or password";
        alert("Invalid email or password");
      });
    },
    postLogin() {
      axios.get(`http://127.0.0.1:8000/OSADusers/searchUser/${this.email}`)
      .then(response => {
        this.username = response.data.fullName;
        const formData1 = {
          email: this.email,
          fullName: this.username,
          timestampLogin: this.timestampLogin
        };
        for (let key in formData1) {
          if (!formData1[key]) {
            console.error(`Missing value for ${key}`);
            return;
          }
        }
        const params1 = new URLSearchParams(formData1).toString();
        axios.post(`http://127.0.0.1:8000/loginOSAD?${params1}`) 
        .then(response => {
          console.log(response);
        })
        .catch(error => {
          console.error(error);
        });
      })
      .catch(error => {
        console.error(error);
      });
    },
    timestamp() {
      var dateTime = new Date();
      var year = dateTime.getFullYear();
      var month = ('0' + (dateTime.getMonth() + 1)).slice(-2);
      var day = ('0' + dateTime.getDate()).slice(-2);
      var hours = dateTime.getHours();
      var minutes = dateTime.getMinutes();
      var seconds = dateTime.getSeconds();
      hours = (hours < 10 ? "0" : "") + hours;
      minutes = (minutes < 10 ? "0" : "") + minutes;
      seconds = (seconds < 10 ? "0" : "") + seconds;
      this.timestampLogin = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
    },
  },
  mounted() {
    this.timestamp();
  }
};
</script>

<template>
<div class = "bg">
  <div class="OSAD-login-container">
  <div class="shadow-box" >
    <h1>For OSAD staffs</h1>
    <div id="forms" >
      <hr>
    <div class="form-group">

      <label for="email">Email: </label>
      <input type="text" id="email" class="size" pattern="^[a-zA-Z0-9]+@gmail\.com$" v-model="email" autocomplete="off" required/>
    </div>
    <div class="form-group">
      <label for="password">Password: </label>
      <input type="password" id="password" class="size" v-model="password" required />
    </div>
    <div id="signup">
      <p>Don't have an account? <a href="/#signup">Sign Up</a></p>
      <p>Forgot your password?<a href="/ForgotPasswordSecurity">Click Here</a></p>
    </div>
  </div>
  <button id="login-button" class="raise" type = "submit" @click="login(), postLogin()">LOG IN</button>
  </div>
</div>
</div>
</template>

<style scoped>
.bg{
  background-color: #0D0D0D;
  height: 100vh;
  width: 100%;
}
.OSAD-login-container {
  width: 100%; 
  height: 100vh; 
  background-color: #0D0D0D;
  color: white;
  position: absolute;
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
  top: -17%;
  border: 2px solid;
}

h1{
  margin: 2% 0;
  font-size: 2em;
  text-transform: uppercase;
  font-style: italic;
}
#forms {
  display: flex;
  flex-direction: column; 
  margin-bottom: 20px; 
  position: relative;
  top: 5%;
  align-items: center;
}

.form-group {
  margin-bottom: 10px; 
  display: flex;
  flex-direction: column;
  color: #0D0D0D;
  left: 20%;
  width: 80%;
}

#login {
  border-radius: 7px;
  position: absolute;
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
  position: fixed;
  left: 47%;
  top: 80%;
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
  .OSAD-login-container {
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
