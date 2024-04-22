export default {
  user: null,
  login(username, password) {
    // Replace this with your actual login logic
    if (username === 'demo' && password === 'password') {
      this.user = { username };
      return true;
    }
    return false;
  },
  logout() {
    this.user = null;
  },
  isAuthenticated() {
    return this.user !== null;
  }
};

