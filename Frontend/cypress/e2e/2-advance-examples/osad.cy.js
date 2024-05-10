describe('User Routes Test', () => {
    it('GET users route', () => {
      cy.viewport(1920, 1080) // Set the viewport size to 1920 x 1080
      cy.visit('http://localhost:5173/OSAD')
      cy.get('button.hamburger').click() // Click on the hamburger button
    })
}),
// describe('OSAD Hamburger Features', () => {
  
//   it('GET pending reports', () => {
//     cy.viewport(1920, 1080)
//     cy.visit('http://localhost:5173/OSAD')
//     cy.get('button.hamburger').click()
//     cy.get('div#1st').click()
//     cy.get('.main-content > ul > :nth-child(1)').click()
//     cy.request('GET','http://127.0.0.1:8000/pending').then((response)=>{
//         expect(response.status).to.eq(200)
//         expect(response.body).to.have.length.above(0)
//       })
//   }),
  it('Post from pending reports to violation details', () => {
    cy.viewport(1920, 1080)
    cy.visit('http://localhost:5173/OSAD')
    cy.get('button.hamburger').click()
    cy.get('div#1st').click()
    cy.get('.main-content > ul > :nth-child(1)').click()
    cy.get('#editButton').click()
    cy.get(':nth-child(8) > .input').should('be.visible').contains('No ID')
    cy.get(':nth-child(9) > .input').type('One week suspension')
    cy.get('#approveButton').click()
    cy.get('.yes').click()
    cy.request('GET','http://127.0.0.1:8000/pending').then((response)=>{
        expect(response.status).to.eq(200)
        expect(response.body).to.have.length.above(0)
    })
  
})

  // it('GET back to homepage', () => {
  //   cy.viewport(1920, 1080)
  //   cy.visit('http://localhost:5173/OSAD')
  //   cy.get('button.hamburger').click()
  //   cy.get('div#2nd').click()
    
  // }),
  // it('GET OSAD staff accounts', () => {
  //   cy.viewport(1920, 1080)
  //   cy.visit('http://localhost:5173/OSAD')
  //   cy.get('button.hamburger').click()
  //   cy.get('div#3rd').click()
  //   cy.request('GET','http://127.0.0.1:8000/sekyuUsers').then((response)=>{
  //       expect(response.status).to.eq(200)
  //       expect(response.body).to.have.length.above(0)
  //     })
  // }),
  //   // it('Check Security accounts/ add students', () => {
  //   //   cy.viewport(1920, 1080)
  //   //   cy.visit('http://localhost:5173/OSAD')
  //   //   cy.get('button.hamburger').click()
  //   //   cy.get('div#3rd').click()
  //   //   cy.get('.main-content > ul > :nth-child(1)').click()
  //   //   cy.get('.main-content > ul > :nth-child(2').click()
  //   //   cy.request('GET','http://127.0.0.1:8000/sekyuUsers').then((response)=>{
  //   //       expect(response.status).to.eq(200)
  //   //       expect(response.body).to.have.length.above(0)
  //   //     })
  // // }),
  // it('GET all verified violations', () => {
  //   cy.viewport(1920, 1080)
  //   cy.visit('http://localhost:5173/OSAD')
  //   cy.get('button.hamburger').click()
  //   cy.get('div#4th').click()
  //   cy.request('GET','http://127.0.0.1:8000/violationDetails').then((response)=>{
  //       expect(response.status).to.eq(200)
  //       //expect(response.body).to.have.length.above(0)
  //     })

  // }),
    it('Check Myk Pa Violations', () => {
      cy.viewport(1920, 1080)
      cy.visit('http://localhost:5173/OSAD')
      cy.get('button.hamburger').click()
      cy.get('div#4th').click()
      cy.get('#search').type('220000000357')
      cy.get('#submit').click()
      cy.get('.main-content > ul > :nth-child(1)').click()
      cy.request('GET','http://127.0.0.1:8000/violationDetails').then((response)=>{
          expect(response.status).to.eq(200)
          //expect(response.body).to.have.length.above(0)
        })
  })
  // // it('Exit', () => {
  // //   cy.viewport(1920, 1080)
  // //   cy.visit('http://localhost:5173/OSADLogin')
  //   // cy.get('#email').type('demo')
  //   // cy.get('#password').type('password')
  //   // cy.get('#login-button').click()
  //   // cy.get('button.hamburger').click()
  //   // cy.get('div#5th').click()
  //   // cy.get('button.btn.btn-success').click()
  // })

