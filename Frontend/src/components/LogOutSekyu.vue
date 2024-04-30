<template>
    <div class="popup-container" v-if="closePopup">
        <div class="popup-inner">
            <p>Are you sure you want to log out?</p>
            <div id="buttons">
                <button class="btn btn-danger" @click="close()">Back</button>
                <button class="btn btn-success" @click="logout()" v-if="authenticationService.isAuthenticated">Logout</button>
            </div>
        </div>
    </div>
</template>

<script>
import AuthenticationService from "../store.js"
export default{
    data(){
        return{
            closePopup: true,
            authenticationService: AuthenticationService,
        }
    },
    methods:{
        close() {
            this.$emit('handlePopupClose', false);
            this.closePopup = false;
            this.$emit("close");
        },
        logout() {
            this.authenticationService.logout(); 
            this.$router.push({ name: 'SekyuLogin' });
        },
    }
}
</script>

<style scoped>
.popup-container{
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 99;
    background-color: rgba(0,0,0,0.7);
    display: flex;
    align-items: center;
    justify-content: center;

   
    .popup-inner{
        background:rgb(255, 255, 255);
        padding: 32px;
        border-radius: 2%;
        height: 15%;
        width: 20%;
  

    }
    .popup-inner p{
        color: black;
        display: flex;
        justify-content: center;
    }
    
}


#buttons{
    display: flex;
    gap: 77%;
    align-items: flex-start;
    position: absolute;
    top: 51.5%;
    align-items: center;
}
* {font-family:"Raleway", sans-serif}
</style>