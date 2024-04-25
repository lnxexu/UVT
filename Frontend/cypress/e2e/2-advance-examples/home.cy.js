describe('User Routes Test', () => {
    it('GET users route', () => {
        cy.viewport(1920, 1080) // Set the viewport size to 1920 x 1080
        // Visit the login page
        cy.visit('http://localhost:5173/')

        cy.get('.w3-hide-small > [href="#about"]').click()
        cy.get('.w3-hide-small > [href="#team"]').click()
        cy.get('.w3-hide-small > [href="#work"]').click()
        cy.get('.w3-hide-small > [href="#signup"]').click()
        cy.get('.w3-hide-small > [href="#contact"]').click()
    })
  })