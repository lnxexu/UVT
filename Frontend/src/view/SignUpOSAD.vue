<template>
    <bg/>
    <div class="bodies">
        <form @submit.prevent = "handleSubmit()" id = "formsi">
            <h1 id = "title">OSAD SignUp</h1>
            <hr>
            <label class = "label">Full Name:</label>
            <input type= "fullName" required class = "input" v-model="fullname">

            <label class = "label">Suffix:</label>
            <select v-model="suffix">
                <option value="JR.">Jr.</option>
                <option value="SR.">Sr.</option>
                <option value="II">II</option>
                <option value="III">III</option>
            </select>

            <label class = "label">Gender:</label>
            <select required v-model="gender">
                <option value="Male">Male</option>
                <option value="Female">Female</option>
            </select>

            <label class = "label">Age:</label>
            <input type ="age" required class = "input" v-model="age">

            <label class = "label">Email:</label>
            <input type= "email" required class = "input" v-model="email">

            <label class = "label">Password:</label>
            <input type ="password" required class = "input" v-model="password">
            <div v-if="passwordError" class = "error">{{ passwordError }}</div>

            <label class = "label">Confirm Password:</label>
            <input type ="password" required class = "input"  v-model="confirmPass">

            <div class="submit">
                <button class="button">Create an Account</button>
            </div>
        </form>
    </div>
</template>
<script>
import { ref } from "vue";
import bg from "../components/Background.vue"
export default{
    data(){
        return {
            fullname: '',
            age: '',
            email: '',
            suffix: '',
            gender: '',
            passwordError: '',
            password: '',
            confirmPass: '',
        }
    },
    components:{bg},
    methods: {
        handleSubmit(){
            this.passwordError = this.password.length > 7 ?
            '' : 'Password must be at least 8 characters long'

            if(!this.passwordError){
                const data = {
                    fullname: this.fullname,
                    age: this.age,
                    email: this.email,
                    suffix: this.suffix,
                    gender: this.gender,
                    password: this.password,
                };
                console.log(res)
            }
        },
    }
};
</script>
<style scoped>

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
    background: #F2D8E4;
    border: 0;
    padding: 10px 20px;
    margin-top: 20px;
    color: black;
    border-radius: 20px;
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