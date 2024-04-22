<template>
    <div class="container">
        <div class = "forgot">
            <h2>Change Password</h2>
            <form @submit="changePassword">
                <label for="currentPassword">Current Password:</label>
                <input type="password" id="currentPassword" v-model="currentPassword" required>
                <label for="newPassword">New Password:</label>
                <input type="password" id="newPassword" v-model="newPassword" required>
                <label for="confirmPassword">Confirm Password:</label>
                <input type="password" id="confirmPassword" v-model="confirmPassword" required>
                <button class = "button" >Change Password</button>
            </form>
        </div>
    </div>
    <bg/>
</template>

<script>
import bg from '../components/Background2.vue';
export default {
    data() {
        return {
            currentPassword: '',
            newPassword: '',
            confirmPassword: ''
        };
    },
    components: {
        bg
    },
    methods: {
        changePassword() {
            // Perform password change logic 
            if (this.newPassword === this.confirmPassword) {
                // Call API or perform necessary actions to change the password
                console.log('Password changed successfully!');
            } else {
                console.log('New password and confirm password do not match!');
            }
        }
    }
};
</script>

<style scoped>
.forgot{
    position: absolute;
    z-index: 1;
    background-color: #0D0D0D;
    height: 50%;
    width: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    top: 25%;
    left: 25%;
    border-radius: 10px;
    box-shadow: 0 0 5px 5px #000000;
}
/* professional and dynamic styles */
.forgot h2{
    font-size: 2.5em;
    color: #cccccc;
    margin-bottom: 20px;
}
.forgot form{
    display: flex;
    flex-direction: column;
    align-items: center;
}
.forgot label{
    font-size: 1.5em;
    color: #cccccc;
    margin-top: 10px;
}
.forgot input{
    width: 300px;
    height: 30px;
    margin-top: 5px;
    padding: 5px;
    border-radius: 5px;
    border: 1px solid #ffffff;
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
.button:hover{
    background-color: #ff65a3;
    transition:ease-in-out 0.45s;
}
h2 {
    color: #CE2774;
    text-align: center;
}
  

</style>