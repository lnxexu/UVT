<template>
  <nav id = "navi">
    <router-link to="/"><h1>Home</h1></router-link>
    <router-link to="/SekyuLogin"><h1>SekyuLogin</h1></router-link>
    <router-link to="/SekyuPage"><h1>SekyuPage</h1></router-link>
    <router-link to="/OSAD"><h1>OSAD</h1></router-link>
    <router-link to="/OSADLogin"><h1>OSADLogin</h1></router-link>
    <router-link to="/SignUpSecurity"><h1>SignUpSecurity</h1></router-link>
    <router-link to="/SignUpOSAD"><h1>SignUpOSAD</h1></router-link>
  </nav>     
</template>
<style scoped>
  nav h1{
    display: inline;
    color: white;
    font-family: 'Courier New', Courier, monospace;
    margin: 20px;
  }
  #navi{
    width: 100%;
    position: absolute;
    top: 0;
    left: 0;
    text-align: center;
    background-color: black;
    z-index: 10;
  }
</style>
<script>
export default{
  name: "NavigationBar",
};
</script>
