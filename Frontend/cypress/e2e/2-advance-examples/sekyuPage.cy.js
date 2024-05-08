describe('User Routes Test/ input student violation', () => {
    it('GET users route', () => {
      cy.viewport(1920, 1080) // Set the viewport size to 1920 x 1080
        cy.visit('http://localhost:5173/SekyuPage')
        cy.get('#stud').type('220000002436')
        cy.get('#search').click()
        cy.get('#display').select('Incomplete uniform')
        cy.get('#below-input > .form-control').type('None')
        cy.get('#option2').click()
        cy.get('.options > .btn-success').click()
        cy.get('.content-button > .btn').click()
        // cy.request('GET','http://127.0.0.1:8000/api/account_types/').then((response)=>{
        //     expect(response.status).to.eq(200)
        //     expect(response.body).to.have.length.above(0)
      })
    })
  