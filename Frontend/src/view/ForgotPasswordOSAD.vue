<template>
    <div>
        <h1>Forgot Password</h1>
        <form @submit.prevent="sendResetEmail">
            <label for="email">Email:</label>
            <input type="email" id="email" v-model="email" required>
            <button type="submit">Send Reset code to Email</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            email: '',
            resetCode: ''
        };
    },
    methods: {
        sendResetEmail() {
            this.generateCode((code) => { 
                axios.get('http://localhost:3000/forgot-password', {
                    params: {
                        email: this.email,
                        resetCode: code
                    }
                }).then((response) => {
                    console.log(response);
                }).catch((error) => {
                    console.log(error);
                });
            });
        },
        generateCode(callback) {
            let code = '';
            for (let i = 0; i < 6; i++) {
                code += Math.floor(Math.random() * 10);
            }
            // Give at least 5 minutes of expiration time for the code
            setTimeout(() => {
                this.resetCode = '';
            }, 300000);
            this.resetCode = code;
            callback(code);
        }
    }
};
</script>

<style scoped>
* {font-family:"Raleway", sans-serif}

</style>
