describe('User Routes Test', () => {
    it('GET users route', () => {
      cy.viewport(1920, 1080) // Set the viewport size to 1920 x 1080
      cy.visit('http://localhost:5173')
      cy.get('.w3-hide-small > [href="#signup"]').click()
    
    })
  }),
  describe('Signup Sekyu', () => {
  
  
    it('Signup SEKYU ACCOUNT', () => {
      cy.viewport(1920, 1080)
      cy.visit('http://localhost:5173')
      cy.get('.w3-hide-small > [href="#signup"]').click()
      cy.get('[style="margin-top: 64px;"] > :nth-child(2) > .w3-input').type('Edward')
      cy.get('[style="margin-top: 64px;"] > :nth-child(3) > .w3-input').type('Corpuz')
      cy.wait(1000);  // wait for 1 second
      cy.get('[style="margin-top: 64px;"] > :nth-child(4) > .w3-select').select('None') // replace 'option1' with the value of the option you want to select
      cy.get('[style="margin-top: 64px;"] > :nth-child(6) > .w3-select').select('Male') // replace 'option1' with the value of the option you want to select
      cy.get('[style="margin-top: 64px;"] > :nth-child(7) > .w3-input').type('24')
      cy.get('[style="margin-top: 64px;"] > :nth-child(8) > .w3-input').type('1998-01-12')
      cy.get('[style="margin-top: 64px;"] > :nth-child(10) > .w3-input').type('Matina Crossing, Davao City')
      cy.get('[style="margin-top: 64px;"] > :nth-child(11) > .w3-input').type('09466800117')
      cy.get('[style="margin-top: 64px;"] > :nth-child(12) > .w3-input').type('Earl@gmail.com')
      cy.get('[style="margin-top: 64px;"] > :nth-child(14) > .w3-input').type('Earllabjam1!')
      cy.get('[style="margin-top: 64px;"] > :nth-child(15) > .w3-input').type('Earllabjam1!')
      cy.get('[style="margin-top: 64px;"] > .w3-center > .button-57').click()
      // cy.request('POST','http://127.0.0.1:8000/AddAccountOSAD').then((response)=>{
      //     expect(response.status).to.eq(200)
      //     expect(response.body).to.have.length.above(0)
        })
      })