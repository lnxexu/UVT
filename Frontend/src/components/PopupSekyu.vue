<template>
    <div class="popup-container" v-if="closePopup">
        <div class="popup-content" :style="{ maxWidth: '700px', overflow: 'auto' }">
        <div class="popup-inner">
            <slot />
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
            this.closePopup = false;
            this.$emit("close");
        },
        logout() {
            this.authenticationService.logout(); 
            this.$router.push({ name: 'OSADLogin' });
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
    opacity: 100;
    transition: opacity 0.9s ease-in-out;
   
    .popup-inner{
        background:rgb(255, 255, 255);
        padding: 32px;
        border-radius: 2%;
        height: 15%;
        
  

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
.popup-content {
    padding: 20px;
  }

</style>