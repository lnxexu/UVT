describe('User Routes Test', () => {
    it('GET users route', () => {
      cy.viewport(1920, 1080) // Set the viewport size to 1920 x 1080
      cy.visit('http://localhost:5173')
      cy.get('.w3-hide-small > [href="#signup"]').click()
    })
  }),
  describe('Signup OSAD', () => {
  
    it('Signup OSAD ACCOUNT', () => {
      cy.viewport(1920, 1080)
      cy.visit('http://localhost:5173')
      cy.get('.w3-hide-small > [href="#signup"]').click()
      cy.get('#signup > :nth-child(5) > :nth-child(2) > .w3-input').type('yuki')
      cy.get('#signup > :nth-child(5) > :nth-child(3) > .w3-input').type('nery')
      cy.get(':nth-child(5) > :nth-child(4) > .w3-select').click()

      cy.get(':nth-child(5) > :nth-child(5) > .w3-input').type('24')
      cy.get(':nth-child(5) > :nth-child(6) > .w3-select').click()
      
      cy.get(':nth-child(3) > :nth-child(7) > .w3-input').type('09466800117')
      cy.get(':nth-child(3) > :nth-child(8) > .w3-input').type('yuki@gmail.com')
      cy.get(':nth-child(3) > :nth-child(9) > .w3-input').type('yuki')
      cy.get(':nth-child(3) > :nth-child(10) > .w3-input').type('yuki')
      cy.get(':nth-child(3) > .w3-col > .w3-button').click()
      cy.request('GET','http://127.0.0.1:8000/pending').then((response)=>{
          expect(response.status).to.eq(200)
          expect(response.body).to.have.length.above(0)
        })
      })
    })