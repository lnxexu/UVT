// AuthenticationService.js
export default {
  isAuthenticated: false,

  login(username, password) {
    // Perform authentication logic here
    // For simplicity, check for a hardcoded username and password
    if (username === 'demo' && password === 'password') {
      this.isAuthenticated = true;
      return true;
    } else {
      return false;
    }
  },

  logout() {
    // Perform logout logic here
    // For simplicity, just set isAuthenticated to false
    this.isAuthenticated = false;
  },
};
