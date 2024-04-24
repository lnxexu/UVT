<script>
import bg from "../components/Background.vue"
import axios from 'axios';
export default {
  data() {
    return {
      email: '',
      password: '',
      error: null
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
          return;
        }
      }
      console.log(formData);
      const params = new URLSearchParams(formData).toString();
      axios.get(`http://127.0.0.1:8000/sekyuUsers/verify/?${params}`)
      .then(response => {
        console.log(response);
        if (response.data.email === this.email && response.data.password === this.password) {
          this.$router.push('SekyuPage');
        } else {
          this.error = "Invalid email or password";
        }
      })
      .catch(error => {
        console.log(error);
        this.error = "Invalid email or password";
      });
    }
  }
};
</script>

<template>
<div class = "bg">
  <div class="Sekyu-login-container">
    <div class="shadow-box">
      <h1>For Security Guards</h1>
      <div id="forms">
        <hr>
        <div class="form-group">
          <label for="email">Email:</label>
          <input type="text" id="email" class="size" pattern="^[a-zA-Z0-9]+@gmail\.com$" v-model="email" required/>
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input type="password" id="password" class="size" v-model="password" required/>
        </div>
        <div id="signup">
          <p>Don't have an account?<a href="/SignUpSecurity">Sign Up</a></p>
          <p>Forgot your password?<a href="/ForgotPasswordSecurity">Click Here</a></p>
        </div>
      </div>
      <button id="login-button" class="raise" @click = "login()">LOG IN</button>
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

.Sekyu-login-container {
  width: 100%; 
  height: 700px; 
  background-color: #0D0D0D;
  color: white;
  position: absolute;
  top: 50%; 
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 20px;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  align-items: center; 
  background-image: url("../assets/UVTBanner.png");
  background-size: cover;
  background-repeat: no-repeat;
  background-position-y: 45%;
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
  left: 76%;
  top: 62%;
}


button:hover,
button:focus { 
  border-color: var(--hover);
  color: black;
}
.shadow-box {
  position: relative;
  top: 25%;
  left: 30%;
  width: 25%;
  height: 50%;
  background-color: #ffffff;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.7); 

}

.size {
  width: 25em;
  height: 2.7em;
  border-radius: 7em;
}
</style>
