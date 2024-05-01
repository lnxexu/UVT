<template>
    <form @submit.prevent="submitForm">
      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required>
      </div>
      <button type="submit">Submit</button>


    </form>
    <bg/>

  </template>
  
  <script>

  export default {

    data() {
      return {
        email: '',
      };
    },
    methods: {
      submitForm() {
        // Handle form submission here
        // You might want to send a request to your server to initiate the password reset process
        console.log(`Initiating password reset for ${this.email}`);
      },
    },
  };
  </script>