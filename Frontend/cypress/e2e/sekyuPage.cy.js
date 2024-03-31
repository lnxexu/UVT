describe('User Routes Test', () => {
    it('GET users route', () => {
      cy.visit('')
      cy.request('GET','http://127.0.0.1:8000/api/account_types/').then((response)=>{
  expect(response.status).to.eq(200)
  expect(response.body).to.have.length.above(0)
      })
    
    })
  })