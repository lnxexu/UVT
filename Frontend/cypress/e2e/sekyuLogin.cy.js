describe('User Routes Test', () => {
  it('GET users route', () => {
      // Visit the login page
      cy.visit('http://localhost:5173/SekyuLogin')

      cy.get('#email').type('demo')

      cy.get('#password').type('password')

      cy.get('#login-button').click()

    
  })
})