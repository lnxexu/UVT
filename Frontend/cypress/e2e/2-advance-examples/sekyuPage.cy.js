describe('User Routes Test', () => {
    it('GET users route', () => {
      cy.viewport(1920, 1080) // Set the viewport size to 1920 x 1080
        cy.visit('http://localhost:5173/SekyuPage')
        cy.request('GET','http://127.0.0.1:8000/api/account_types/').then((response)=>{
            expect(response.status).to.eq(200)
            expect(response.body).to.have.length.above(0)
      })
    })
  })