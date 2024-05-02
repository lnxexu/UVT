<template>
  <div class="w3-top">
  <div class="w3-bar w3-white w3-card" id="myNavbar">
    <a href="#" class="w3-bar-item w3-button w3-wide">UVT</a>
    <!-- Right-sided navbar links -->
    <div class="w3-right w3-hide-small">
      <a href="#about" class="w3-bar-item w3-button"><i class="fa fa-comment"></i> ABOUT</a>
      <a href="#team" class="w3-bar-item w3-button"><i class="fa fa-user"></i> TEAM</a>
      <a href="#work" class="w3-bar-item w3-button"><i class="fa fa-th"></i> PROTOTYPE</a>
      <a href="#signup" class="w3-bar-item w3-button"><i class="fa fa-sign-in"></i> SIGNUP</a>
      <a href="#contact" class="w3-bar-item w3-button"><i class="fa fa-envelope"></i> CONTACT</a>
    </div>
    <!-- Hide right-floated links on small screens and replace them with a menu icon -->

    <a href="javascript:void(0)" class="w3-bar-item w3-button w3-right w3-hide-large w3-hide-medium" onclick="w3_open()">
      <i class="fa fa-bars"></i>
    </a>
  </div>
</div>

<!-- Sidebar on small screens when clicking the menu icon -->
<nav class="w3-sidebar w3-bar-block w3-black w3-card w3-animate-left w3-hide-medium w3-hide-large" style="display:none" id="mySidebar">
  <a href="javascript:void(0)" onclick="w3_close()" class="w3-bar-item w3-button w3-large w3-padding-16">Close ×</a>
  <a href="#about" onclick="w3_close()" class="w3-bar-item w3-button">ABOUT</a>
  <a href="#team" onclick="w3_close()" class="w3-bar-item w3-button">TEAM</a>
  <a href="#work" onclick="w3_close()" class="w3-bar-item w3-button">PROTOTYPE</a>
  <a href="#signup" onclick="w3_close()" class="w3-bar-item w3-button">SIGNUP</a>
  <a href="#contact" onclick="w3_close()" class="w3-bar-item w3-button">CONTACT</a>
</nav>

<!-- Header with full-height image -->
<header>
  <img src="../assets/UIC.jpg" id = "UIC" style="filter: brightness(0.5);">
  <div class="w3-display-left w3-text-white" style="padding:48px">
    <span class="w3-jumbo w3-hide-small" style="text-transform: uppercase;display: flex;">
      University Violation Tracker
    </span><br>
  </div> 
</header>

<!-- About Section -->
<div class="w3-container" style="padding:128px 16px" id="about">
  <h3 class="w3-center">ABOUT THE COMPANY</h3>
  <p class="w3-center w3-large">Key features of our prototype</p>
  <div class="w3-row-padding w3-center" style="margin-top:64px">
    <div class="w3-quarter">
      <i class="fa fa-desktop w3-margin-bottom w3-jumbo w3-center"></i>
      <p class="w3-large">Responsive</p>
      <p>The "University Violation Tracker" system aims to provide a consistent, efficient, and user-friendly experience across a diverse range of devices, ensuring that users can easily access and interact with the system anytime, anywhere.</p>
    </div>
    <div class="w3-quarter">
      <i class="fa fa-heart w3-margin-bottom w3-jumbo"></i>
      <p class="w3-large">Passion</p>
      <p>The passion-driven engagement feature of the University Violation Tracker system is designed to inspire and sustain active participation, collaboration, and a shared commitment to fostering a positive university environment.</p>
    </div>
    <div class="w3-quarter">
      <i class="fa fa-diamond w3-margin-bottom w3-jumbo"></i>
      <p class="w3-large">Design</p>
      <p>The modern and intuitive design feature of the University Violation Tracker system prioritizes user experience, accessibility, and a visually appealing interface, ultimately contributing to increased user engagement and the overall success of the system.</p>
    </div>
    <div class="w3-quarter">
      <i class="fa fa-cog w3-margin-bottom w3-jumbo"></i>
      <p class="w3-large">Support</p>
      <p>The comprehensive support services feature of the University Violation Tracker system is designed to provide users with the resources and assistance they need, fostering a positive and collaborative user experience.</p>
    </div>
  </div>
</div>

<!-- Promo Section - "We know design" -->


<!-- Team Section -->
<div class="w3-container w3-light-grey" style="padding:128px 16px;" id="team">
  <h3 class="w3-center">THE TEAM</h3>
  <p class="w3-center w3-large">The ones who made this possible</p>
  <div class="w3-row-padding " style="margin-top:64px;display: flex;justify-content: space-evenly; filter:grayscale(0.4)">
    <div class="w3-col l3 m6 w3-margin-bottom">
      <div class="w3-card team-member" style="width:350px; height:100%">
        <img src="../assets/kobe.jpg" alt="John" style="width:100%; height:350px">
        <div class="w3-container">
          <h3>Kobe Corpuz</h3>
          <p class="w3-opacity">Programmer</p>
          <p>"You have to hurt in order to know. Fall in order to grow. Lose in order to gain. Because most of life’s lessons are learned in pain."</p>
          <p><button class="w3-button w3-light-grey w3-block" @click="composeEmail('kcorpuz_220000002183@uic.edu.ph', 'Subject 1', 'Body of message 1')"><i class="fa fa-envelope"></i> Contact</button></p>
        </div>
      </div>
    </div>
    <div class="w3-col l3 m6 w3-margin-bottom" >
      <div class="w3-card team-member" style="width:350px;height:100%">
        <img src="../assets/myk1.jpg" alt="Jane" style="width:100%; height:350px;">
        <div class="w3-container">
          <h3>Myk Lorence Palado</h3>
          <p class="w3-opacity">Analyst</p>
          <p>"Keep going. Everything you need will come to you at the perfect time."</p>
          <p><button class="w3-button w3-light-grey w3-block" style="margin-top: 11.9%;" @click="composeEmail('mpalado_220000002436@uic.edu.ph', 'Subject 1', 'Body of message 1')" ><i class="fa fa-envelope"></i> Contact</button></p>
        </div>
      </div>
    </div>
    <div class="w3-col l3 m6 w3-margin-bottom">
      <div class="w3-card team-member" style="width:350px; height:100%">
        <img src="../assets/jam.jpg" alt="Mike" style="width:100%; height:350px">
        <div class="w3-container">
          <h3>Jazmine Rose Quitoras</h3>
          <p class="w3-opacity">Web Designer</p>
          <p>"Psalm 46:5" "Long story short, I survived"</p>
          <p><button class="w3-button w3-light-grey w3-block"  style="margin-top: 19%;" @click="composeEmail('jquitoras_220000000357@uic.edu.ph', 'Subject 1', 'Body of message 1')"><i class="fa fa-envelope"></i> Contact</button></p>
        </div>
      </div>
    </div>
    <div class="w3-col l3 m6 w3-margin-bottom">
      <div class="w3-card team-member" style="width:350px; height:100%  ">
        <img src="../assets/gi.jpg" alt="Dan" style="width:100%; height:350px">
        <div class="w3-container">
          <h3>Gi Linghon</h3>
          <p class="w3-opacity">Documentator/Tester</p>
          <p>"Keep moving forward"</p>
          <p><button class="w3-button w3-light-grey w3-block" style="margin-top: 19%;"  @click="composeEmail('glinghon_220000002162@uic.edu.ph', 'Subject 1', 'Body of message 1')"><i class="fa fa-envelope"></i> Contact</button></p>
        </div>
      </div>
    </div>
    <div class="w3-col l3 m6 w3-margin-bottom">
      <div class="w3-card team-member" style="width:350px; height:100%;">
        <img src="../assets/chan.jpg" alt="Dan" style="width:100%; height:350px">
        <div class="w3-container">
          <h3>Christian Kyle Padilla</h3>
          <p class="w3-opacity">Documentator/Tester</p>
          <p>"If you don't take risks, you can't create a future."</p>
          <p><button class="w3-button w3-light-grey w3-block" style="margin-top: 11.9%;" @click="composeEmail('cpadilla_210000000910@uic.edu.ph', 'Subject 1', 'Body of message 1')"><i class="fa fa-envelope"></i> Contact</button></p>
        </div>
      </div>
    </div>
  </div>
</div>


<!-- Work Section -->
<div class="w3-container" style="padding:128px 16px" id="work">
  <h3 class="w3-center">UVT PROTOTYPE</h3>
  <p class="w3-center w3-large">Choose if whether you are Security Guard or a OSAD staff</p>
  <p class="w3-center w3-large">Note: Username: "demo@gmail.com", Password: "password"</p>

  <div class="w3-row-padding" style="margin-top:64px">
    <div style="display: flex; justify-content: space-evenly; height: 300px">
      <div class = "option one"><router-link to="/SekyuLogin"><button class="button-57 Sekyu" role="button" ><span class="text">Security Page</span><span>Security Page</span></button></router-link></div>
      <div class = "option two"><router-link to = "/OSADLogin"><button class="button-57 OSAD" role="button"><span class="text">OSAD</span><span>OSAD</span></button></router-link></div>
    </div>
  </div>
</div>

<!-- Signup Section -->
<div class="w3-container w3-light-grey" style="padding:128px 16px" id="signup">
  <h3 class="w3-center">SIGNUP</h3>
  <p class="w3-center w3-large">Sign up to obtain an account</p>
  <div class="w3-row-padding " style="margin-top:64px">
    <h4><strong>For Security Guards</strong></h4>
    <div class="w3-third">
      <p>First Name:</p>
      <input class="w3-input w3-border" type="text" placeholder="First Name" v-model="firstNameSekyu" required>
    </div>
    <div class="w3-third">
      <p>Last Name:</p>
      <input class="w3-input w3-border" type="text" placeholder="Last Name" v-model="lastNameSekyu" required>
    </div>
    <div class="w3-third">
      <p>Suffix:</p>
      <select class="w3-select w3-border" name="option" v-model="suffixSekyu" required>
        <option value="" disabled selected>Choose your option</option>
        <option value="NULL">None</option>
        <option value="Jr.">Jr.</option>
        <option value="Sr.">Sr.</option>
        <option value="III">III</option>
        <option value="IV">IV</option>
        <option value="V">V</option>
      </select>
    </div>
    
    <div class="w3-col">&nbsp;</div>

    <div class="w3-third">
      <p>Gender:</p>
      <select class="w3-select w3-border" name="option" v-model="genderSekyu" required>
        <option value="" disabled selected>Choose your option</option>
        <option value="Male">Male</option>
        <option value="Female">Female</option>
      </select>
    </div>
    <div class="w3-third">
      <p>Age:</p>
      <input class="w3-input w3-border" type="number" placeholder="Age" v-model="ageSekyu" required>
    </div>
    <div class="w3-third">
      <p>Birthdate:</p>
      <input class="w3-input w3-border" type="date" placeholder="Date of Birth" v-model="birthdateSekyu" required>
    </div>

    <div class="w3-col">&nbsp;</div>

    <div class="w3-third">
      <p>Complete Address:</p>
      <input class="w3-input w3-border" type="text" placeholder="Complete Address" v-model="addressSekyu" required>
    </div>
    <div class="w3-third">
      <p>Contact Number:</p>
      <input class="w3-input w3-border" type="tel" name="phone" pattern="^(09|\+639)\d{9}$" placeholder="Contact Number" v-model="contactSekyu" required>
    </div>
    <div class="w3-third">
      <p>Email:</p>
      <input class="w3-input w3-border" type="email" placeholder="Email" v-model="emailSekyu">
    </div>

    <div class="w3-col">&nbsp;</div>

    <div class="w3-half">
      <p>Password:</p>
      <input class="w3-input w3-border" type="password" placeholder="Password" v-model="passwordSekyu">
    </div>
    <div class="w3-half">
      <p>Confirm Password:</p>
      <input class="w3-input w3-border" type="password" placeholder="Confirm Password" v-model="confirmPasswordSekyu">
    </div>

    <div class="w3-col">&nbsp;</div>

    <div class="w3-center">
      <button class="button-57" type="submit" @click="postSignupDataSekyu()"><i class="fa fa-paper-plane"></i> <span>CREATE ACCOUNT</span> <span><i class="fa fa-paper-plane-o"></i> CREATE ACCOUNT</span></button>
    </div>
  </div>

  <div class="w3-row">&nbsp;</div>

  <div class="w3-row">&nbsp;</div>

  <div class="vl"></div>

  <div class="w3-row">&nbsp;</div>

  <div class="w3-row">&nbsp;</div>

  <div class=" w3-row-padding" >
    <h4><strong>For OSAD Staffs</strong></h4>
    <div class="w3-third">
      <p>First Name:</p>
      <input class="w3-input w3-border" type="text" placeholder="First Name" v-model="firstNameOSAD" required>
    </div>
    <div class="w3-third">
      <p>Last Name:</p>
      <input class="w3-input w3-border" type="text" placeholder="Last Name" v-model="lastNameOSAD" required >
    </div>
    <div class="w3-third">
      <p>Suffix:</p>
      <select class="w3-select w3-border" name="option" v-model="suffixOSAD" required>
        <option value="" disabled selected>Choose your option</option>
        <option value="NULL">None</option>
        <option value="Jr.">Jr.</option>
        <option value="Sr.">Sr.</option>
        <option value="III">III</option>
        <option value="IV">IV</option>
        <option value="V">V</option>
      </select>
    </div>

    <div class="w3-col">&nbsp;</div>

    <div class="w3-third">
      <p>Gender:</p>
      <select class="w3-select w3-border" name="option" v-model="genderOSAD" required>
        <option value="" disabled selected>Choose your option</option>
        <option value="Male">Male</option>
        <option value="Female">Female</option>
      </select>
    </div>
    <div class="w3-third">
      <p>Age:</p>
      <input class="w3-input w3-border" type="number" placeholder="Age" v-model="ageOSAD" required>
    </div>
    <div class="w3-third">
      <p>Birthdate:</p>
      <input class="w3-input w3-border" type="date" placeholder="Date of Birth" v-model="birthdateOSAD" required >
    </div>

    <div class="w3-col">&nbsp;</div>

    
    <div class="w3-third">
      <p>Complete Address:</p>
      <input class="w3-input w3-border" type="text" placeholder="Complete Address" v-model="addressOSAD" required>
    </div>
    <div class="w3-third">
      <p>Contact Number:</p>
      <input class="w3-input w3-border" type="text" name="phone" pattern="^(09|\+639)\d{9}$" placeholder="Contact Number" v-model="contactOSAD" required>
    </div>
    <div class="w3-third">
      <p>Email:</p>
      <input class="w3-input w3-border" type="email" placeholder="Email" v-model="emailOSAD">
    </div>

    <div class="w3-col">&nbsp;</div>
    
    <div class="w3-half">
      <p>Password:</p>
      <input class="w3-input w3-border" type="password" placeholder="Password" v-model="passwordOSAD">
    </div>
    <div class="w3-half">
      <p>Confirm Password:</p>
      <input class="w3-input w3-border" type="password" placeholder="Confirm Password" v-model="confirmPasswordOSAD">
    </div>

    <div class="w3-col">&nbsp;</div>

    <div class="w3-center">
      <button class="button-57" type="submit" @click="postSignupDataOSAD()"><i class="fa fa-paper-plane"></i> <span class="text"> CREATE ACCOUNT </span><span><i class="fa fa-paper-plane-o"></i> CREATE ACCOUNT</span></button>
    </div>
  </div>
</div>



<!-- Contact Section -->
<div class="w3-container" style="padding:128px 16px" id="contact">
  <h3 class="w3-center">CONTACT</h3>
  <p class="w3-center w3-large">Lets get in touch. Send us a message:</p>
  <div style="margin-top:48px">
    <p><i class="fa fa-map-marker fa-fw w3-xxlarge w3-margin-right"></i> Davao City, Philippines</p>
    <p><i class="fa fa-phone fa-fw w3-xxlarge w3-margin-right"></i> Phone: 09187085773</p>
    <p><i class="fa fa-envelope fa-fw w3-xxlarge w3-margin-right"> </i> Email: ephixa12321@gmail.com</p>
    <br>
    <form action="/action_page.php" target="_blank">
      <p><input class="w3-input w3-border" type="text" placeholder="Name" required name="Name"></p>
      <p><input class="w3-input w3-border" type="text" placeholder="Email" required name="Email"></p>
      <p><input class="w3-input w3-border" type="text" placeholder="Subject" required name="Subject"></p>
      <p><input class="w3-input w3-border" type="text" placeholder="Message" required name="Message"></p>
      <p><button class="w3-button w3-black" type="submit" @click="postSignupData"><i class="fa fa-paper-plane"></i> SEND MESSAGE</button></p>
    </form>
  </div>
</div>

<!-- Footer -->
<footer class="w3-center w3-black w3-padding-64">
  <a href="#home" class="w3-button w3-light-grey"><i class="fa fa-arrow-up w3-margin-right"></i>To the top</a>
  <div class="w3-xlarge w3-section">
    <i class="fa fa-facebook-official w3-hover-opacity"></i>
    <i class="fa fa-instagram w3-hover-opacity"></i>
    <i class="fa fa-snapchat w3-hover-opacity"></i>
    <i class="fa fa-pinterest-p w3-hover-opacity"></i>
    <i class="fa fa-twitter w3-hover-opacity"></i>
    <i class="fa fa-linkedin w3-hover-opacity"></i>
  </div>
</footer>

</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      buttonText: "Click me",
      buttonClass: "minimal-button",
      firstNameSekyu: "",
      lastNameSekyu: "",
      suffixSekyu: "",
      genderSekyu: "",
      ageSekyu: "",
      contactSekyu: "",
      birthdateSekyu: "",
      addressSekyu: "",
      emailSekyu: "",
      passwordSekyu: "",
      confirmPasswordSekyu: "",
      firstNameOSAD: "",
      lastNameOSAD: "",
      suffixOSAD: "",
      genderOSAD: "",
      ageOSAD: "",
      contactOSAD: "",
      birthdateOSAD: "",
      addressOSAD: "",
      emailOSAD: "",
      passwordOSAD: "",
      confirmPasswordOSAD: "",
      showModal: false,
    };
  },
  methods: {
    validateFormOSAD(){
      if (this.passwordOSAD !== this.confirmPasswordOSAD) {
        alert("Passwords do not match");
        return "Passwords do not match";
      }
      if (!this.emailOSAD.includes("@") || !this.emailOSAD.includes(".")) {
        alert("Invalid email");
        return "Invalid email";
      }
      if (isNaN(this.contactOSAD) || this.contactOSAD.length !== 11 || !this.contactOSAD.startsWith("09")) {
        alert("Invalid contact number");
        return "Invalid contact number";
      }
      if (isNaN(this.ageOSAD)) {
        alert("Age must be a number");
        return "Age must be a number";
      }
      else{
        if(this.ageOSAD < 18){
          alert("Age must be 18 and above");
          return "Age must be 18 and above";
        }
      }
      const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
      if (!passwordRegex.test(this.passwordOSAD)) {
        alert("Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one number, and one special character");
        return "Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one number, and one special character";
  }

    },
    validateFormSekyu() {
      if (this.passwordSekyu !== this.confirmPasswordSekyu) {
        alert("Passwords do not match");
        return "Passwords do not match";
      }
      if (!this.emailSekyu.includes("@") || !this.emailSekyu.includes(".")) {
        alert("Invalid email");
        return "Invalid email";
      }
      if (isNaN(this.contactSekyu) || this.contactSekyu.length !== 11 || !this.contactSekyu.startsWith("09")) {
        alert("Invalid contact number");
        return "Invalid contact number";
      }
      if (isNaN(this.ageSekyu)) {
        alert("Age must be a number");
        return "Age must be a number";
      }
      else{
        if(this.ageSekyu < 18){
          alert("Age must be 18 and above");
          return "Age must be 18 and above";
        }
      }

      const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
      if (!passwordRegex.test(this.passwordSekyu)) {
        alert("Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one number, and one special character");
        return "Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one number, and one special character";
      }
    },
    clearDataSekyu() {
      this.firstNameSekyu = "";
      this.lastNameSekyu = "";
      this.suffixSekyu = "";
      this.genderSekyu = "";
      this.ageSekyu = "";
      this.contactSekyu = "";
      this.emailSekyu = "";
      this.passwordSekyu = "";
      this.confirmPasswordSekyu = "";
      this.addressSekyu = "";
      this.birthdateSekyu = "";
    },
    clearDataOSAD() {
      this.firstNameOSAD = "";
      this.lastNameOSAD = "";
      this.suffixOSAD = "";
      this.genderOSAD = "";
      this.ageOSAD = "";
      this.contactOSAD = "";
      this.emailOSAD = "";
      this.passwordOSAD = "";
      this.confirmPasswordOSAD = "";
      this.addressOSAD = "";
      this.birthdateOSAD = "";
    },
    getFullName(firstName, lastName) {
      return firstName + " " + lastName;
    },
    async postSignupDataSekyu() {
      const fullNameSekyu = this.getFullName(this.firstNameSekyu.trim(), this.lastNameSekyu.trim());
      const dataSekyu = {
        fullName: fullNameSekyu,
        suffix: this.suffixSekyu,
        age: this.ageSekyu,
        gender: this.genderSekyu.trim(),
        contactInformation: this.contactSekyu,
        email: this.emailSekyu.trim(),
        password: this.passwordSekyu.trim(),
        address: this.addressSekyu.trim(),
        birthDate: this.birthdateSekyu
      };
      if(this.validateFormSekyu() === undefined){
        if (window.confirm(`Are you sure you want to submit the form?
        Full Name: ${fullNameSekyu}
        Suffix: ${this.suffixSekyu}
        Age: ${this.ageSekyu}
        Gender: ${this.genderSekyu}
        Birthdate: ${this.birthdateSekyu}
        Contact Number: ${this.contactSekyu}
        Address: ${this.addressSekyu}
        Email: ${this.emailSekyu}`)) {
          for (let key in dataSekyu) {
            if (!dataSekyu[key]) {
              console.error(`Missing value for ${key}`);
              return;
            }
          }
          const params = new URLSearchParams(dataSekyu).toString();
          axios.post(`http://127.0.0.1:8000/AddAccountSekyu?${params}`)
          .then((response) => {
            console.log(response);
            alert("Your account will be reviewed by the admin. Please wait for the confirmation.");
            this.clearDataSekyu();
          })
          .catch((error) => {
            console.log(error);
            alert("Account creation failed");
          });
        }
        else {
          console.log('Form not submitted');
        }
      }
    },
    async postSignupDataOSAD() {
      const fullNameOSAD = this.getFullName(this.firstNameOSAD.trim(), this.lastNameOSAD.trim());
      const dataOSAD = {
        fullName: fullNameOSAD,
        suffix: this.suffixOSAD,
        age: this.ageOSAD,
        gender: this.genderOSAD,
        contactInformation: this.contactOSAD.trim(),
        email: this.emailOSAD.trim(),
        password: this.passwordOSAD.trim(),
        address: this.addressOSAD,
        birthDate: this.birthdateOSAD
      };
      if(this.validateFormOSAD() === undefined){
        if (window.confirm(`Are you sure you want to submit the form?
        Full Name: ${fullNameOSAD}
        Suffix: ${this.suffixOSAD}
        Age: ${this.ageOSAD}
        Gender: ${this.genderOSAD}
        Contact: ${this.contactOSAD}
        Birthdate: ${this.birthdateOSAD}
        Address: ${this.addressOSAD}
        Email: ${this.emailOSAD}`)) {
          for (let key in dataOSAD) {
            if (!dataOSAD[key]) {
              console.error(`Missing value for ${key}`);
              return;
            }
          }
          const params = new URLSearchParams(dataOSAD).toString();
          axios.post(`http://127.0.0.1:8000/AddAccountOSAD?${params}`)
          .then((response) => {
            console.log(response);
            alert("Your account will be reviewed by the admin. Please wait for the confirmation.");
            this.clearDataOSAD();
          })
          .catch((error) => {
            console.log(error);
            alert("Account creation failed");
          });
        }
        else {
            console.log('Form not submitted');
        }
      }
    },
    toggleSidebar() {
      const mySidebar = this.$refs.mySidebar;
      mySidebar.style.display = mySidebar.style.display === 'block' ? 'none' : 'block';
    },
    composeEmail(email, subject, body) {
      window.location.href = "mailto:" + email + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
    } 
  }
};
</script>


<style scoped>
@import url('https://www.w3schools.com/w3css/4/w3.css');
@import url('https://fonts.googleapis.com/css?family=Raleway');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css');

body,h1,h2,h3,h4,h5,h6,span {font-family:"Raleway", sans-serif}

body, html {
  height: 100%;
  line-height: 1.8;
}

.w3-bar .w3-button {
  padding: 16px;
}

#UIC{
  position: relative;
  display: flex;
  width: 100%;
  offset-position: 100%;
}

.button-57 {
  position: relative;
  overflow: hidden;
  border: 1px solid #18181a;
  color: #18181a;
  display: inline-block;
  font-size: 15px;
  line-height: 15px;
  padding: 18px 18px 17px;
  text-decoration: none;
  cursor: pointer;
  background: #fff;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  border-radius: 5%;
}

.button-57 span:first-child {
  position: relative;
  transition: color 600ms cubic-bezier(0.48, 0, 0.12, 1);
  z-index: 10;
}

.button-57 span:last-child {
  color: white;
  display: block;
  position: absolute;
  bottom: 0;
  transition: all 500ms cubic-bezier(0.48, 0, 0.12, 1);
  z-index: 100;
  opacity: 0;
  top: 50%;
  left: 50%;
  transform: translateY(225%) translateX(-50%);
  height: 14px;
  line-height: 13px;
  width: 100%;
}

.button-57:after {
  content: "";
  position: absolute;
  bottom: -50%;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: black;
  transform-origin: bottom center;
  transition: transform 600ms cubic-bezier(0.48, 0, 0.12, 1);
  transform: skewY(9.3deg) scaleY(0);
  z-index: 50;
  width: 100%;
}

.button-57:hover:after {
  transform-origin: bottom center;
  transform: skewY(9.3deg) scaleY(2);
  width: 100%;
}

.button-57:hover span:last-child {
  transform: translateX(-50%) translateY(-65%);
  opacity: 1;
  transition: all 900ms cubic-bezier(0.48, 0, 0.12, 1);
  width: 100%;
}
.team-member {
  width: 350px;
  height: 400px; 
  overflow: hidden;
  transition: transform 0.3s ease-in-out;
}
.team-member img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.team-member:hover {
  transform: scale(1.05); 
  transition: 0.3s ease;
}
.team-member .w3-container {
  padding: 20px;
  background: #fff;
  text-align: center;
}

.option{
  width: 40%;
  height: 100%;
  border: #18181a 1px solid;
  border-radius: 20px;
}
.option .Sekyu{
  position: relative;
  top: 44%;
   left: 40%;
}
.option .OSAD{
  position: relative;
  top: 44%;
  left: 46%;
}
.one{
  background-image: url('../assets/n1.PNG');
  background-size: cover;
}
.two{
  background-image: url('../assets/n2.PNG');
  background-size: cover;
}
.one,.two {
  position: relative;
  background-size: cover;
  transition: filter 0.5s ease, transform 0.5s ease; /* Adding transition for filter and transform */
}

.one:hover,
.two:hover {
  transform: scale(1.1); /* Scale effect on hover */
}

.one::before,
.two::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0); /* Start with a fully transparent background */
  transition: background 0.5s ease; /* Adding transition for background */
  pointer-events: none; /* Allows mouse events to pass through the overlay */
  border-radius: 20px;
}

.one:hover::before,
.two:hover::before {
  background: rgba(0, 0, 0, 0.5); /* Transition to semi-transparent black on hover */
}

.vl {
  border: 1px solid rgb(0, 0, 0);
  width: 100%;
  position: relative;
  left: 0%;
}


/* Sidebar on small screens */
@media screen and (max-width: 600px) {
  .w3-sidebar {
    height: 100%;
    width: 100%;
    background-color: #0D0D0D;
    position: fixed;
    z-index: 1;
    overflow-x: hidden;
    transition: 0.3s;
    padding-top: 60px;
  }
}

#myModal{
 
  position: fixed;
  z-index: 1;
  padding-top: 100px;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgb(0,0,0);
  background-color: rgba(0,0,0,0.4);
}

.modal {
  display: none;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0,0,0,0.4);
}

.modal-content {
  margin: 15% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
  max-width: 600px;
  box-sizing: border-box;
}

.close {
  color: #aaaaaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
}
</style>