<template>
    <bg/>
    <div class="bodies">
        <form @submit.prevent="handleSubmit()" id="formsi">
            <h1 id="title">OSAD SignUp</h1>
            <hr>
            <label class="label" for="fullName">Full Name:</label>
            <input type="text" name="fullName" required class="input" v-model="fullname" placeholder="Enter your full name">
            <label class="label" for="suffix">Suffix:</label>
            <select name="suffix" v-model="suffix">
                <option value="JR.">Jr.</option>
                <option value="SR.">Sr.</option>
                <option value="II">II</option>
                <option value="III">III</option>
            </select>
            <label class="label" for="gender">Gender:</label>
            <select required name="gender" v-model="gender">
                <option value="Male">Male</option>
                <option value="Female">Female</option>
            </select>
            <label class="label" for="age">Age:</label>
            <input type="number" name="age" required class="input" v-model="age" placeholder="Enter your age">
            <label class="label" for="email">Email:</label>
            <input type="email" name="email" required class="input" v-model="email" placeholder="Enter your email" autocomplete="email">
            <label class="label" for="password">Password:</label>
            <input type="password" name="password" required class="input" v-model="password" placeholder="Enter your password" autocomplete="new-password">
            <div v-if="passwordError" class="error">{{ passwordError }}</div>
            <label class="label" for="confirmPass">Confirm Password:</label>
            <input type="password" name="confirmPass" required class="input" v-model="confirmPass" placeholder="Confirm your password">
            <div class="submit">
                <button class="button" @click="showPopup = true">Create an Account</button>
            </div>
        </form>
        <div v-if="showPopup" class="popup">
            <h2>Confirm Account Creation</h2>
            <p><strong>Full Name:</strong> {{ fullname }}</p>
            <p><strong>Suffix:</strong> {{ suffix }}</p>
            <p><strong>Gender:</strong> {{ gender }}</p>
            <p><strong>Age:</strong> {{ age }}</p>
            <p><strong>Email:</strong> {{ email }}</p>
            <p><strong>Password:</strong> {{ password }}</p>
            <button class="button" @click="createAccount">Confirm</button>

            <button class="button" @click="showPopup = false">Cancel</button>
        </div>
    </div>
    
</template>

<script>
// Remove the unused import statement for 'ref'
// import { ref } from "vue";
import bg from "../components/Background.vue";
import axios from "axios";
export default {
    data() {
        return {
            fullname: "",
            age: "",
            email: "",
            suffix: "",
            gender: "",
            passwordError: "",
            password: "",
            confirmPass: "",
            showPopup: false,
        };
    },
    components: { bg },
    methods: {
        // Create a new account and save it to the database
        async createAccount() {
            
            // Validate age
            if (this.age < 18) {
                alert("You must be at least 18 years old to create an account");
            } else {
                this.showPopup = true;
            }
            // Verify that the email does not exist in the database
            // Send a GET request to the server to check if the email exists
            axios.get(`/OSADusers/${this.email}`)
                .then((response) => {
                    if (response.data) {
                        alert("An account with this email already exists");
                    } else {
                        this.showPopup = true;
                    }
                });

            // Validate the password
            if (this.password !== this.confirmPass) {
                this.passwordError = "Passwords do not match";
                return;
            }
            if (this.password.length < 8) {
                this.passwordError = "Password must be at least 8 characters long";
                return;
            }
            // Send a POST request to the server to create a new account
            const response = await axios.post("http://127.0.0.1:8000/OSADusers/add", {
                fullname: this.fullName,
                age: this.age,
                email: this.email,
                suffix: this.suffix,
                password: this.password,
                gender: this.gender
            })
            if (response.ok) {
                alert("Account created successfully");
                this.$router.push({ name: "OSADLogin" });
            } 
            else {
                alert("Failed to create an account");
            }
            
        },
    },
};
</script>

<style scoped>
/* design for the popup */
.popup {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: black;
    padding: 20px;
    border-radius: 10px;
    z-index: 2;
    color: white;
    text-align: center;
}
/* create a black transparent background behind the popup */
.bodies {
    margin: 0;
    background-color: transparent;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    height: 100%;
    width: 100%;
    color: #2c3e50;
    position: absolute;
    top: 0;
    z-index: 1;
}
.bodies{ 
    margin: 0; 
    background-color:transparent; 
    -webkit-font-smoothing: antialiased;
     -moz-osx-font-smoothing: grayscale; 
     text-align: center; 
     height: 100%; 
     width: 100%; 
     color: #2c3e50; 
     position: absolute; 
     top: 0; 
     z-index: 1; 
} 
#formsi{ 
    max-width: 700px; 
    margin: 30px auto; 
    background: black; 
    text-align: left; 
    padding: 40px; 
    border-radius: 10px; 
    display: flex; 
    flex-direction: column; 
    position: relative; 
    top:0; 
} 
.label{ 
    color: #aaa; 
    display: inline-block; 
    margin: 25px 0 15px; 
    font-size: 0.6em; 
    text-transform: uppercase; 
    letter-spacing: 1px; 
    font-weight: bold; 
} 
#title{ 
    color: #ffffff;
    display: inline-block; 
    font-size: 30px; 
    text-transform: uppercase; 
    letter-spacing: 1px; 
    font-weight: bold; 
    text-align: center; 
} 
.button{ 
    background: #CE2774; 
    border: 0; 
    padding: 10px 20px; 
    margin-top: 20px; 
    margin-right: 10px;
    color: #ffffff; 
    border-radius: 10px; 
    text-transform: uppercase; 
    font-weight: bold;


} 
.input,select{ 
    display: block; 
    padding: 10px 6px; 
    width: 100%; 
    box-sizing: border-box; 
    border: none; 
    border-bottom: 1px solid #ddd; 
    color: #555; 
    border-radius: 10px; 
} 
.submit{ 
    text-align: center;
} 
.error{ 
    color: #ff0062; 
    margin-top: 10px; 
    font-size: 0.8em; 
    font-weight: bold; 
} 
</style>
