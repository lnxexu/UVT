describe('User Routes Test', () => {
    it('GET users route', () => {
        cy.viewport(1920, 1080) // Set the viewport size to 1920 x 1080
        // Visit the login page
        cy.visit('http://localhost:5173/')
    })
  })