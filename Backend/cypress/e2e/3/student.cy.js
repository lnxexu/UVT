describe('Students', () => {
  
    it('can GET Student', () => {
      cy.visit('http://127.0.0.1:8000/docs#/Student')
      cy.get('#operations-Student-get_student_student_get > .opblock-summary > .opblock-control-arrow').click()
      cy.get('.btn').click()
      cy.get('.execute').click()
      // You can add more assertions here to validate the response body
    })

it('can GET StudentID', () => {
    cy.visit('http://127.0.0.1:8000/docs#/Student/get_student_by_id_student__student_id__get')
    cy.get('#operations-Student-get_student_by_id_student__student_id__get > .opblock-summary > .opblock-summary-control').should('be.visible').contains('Get Student By Id').click()
    cy.get('#operations-Student-get_student_by_id_student__student_id__get > .opblock-summary > .opblock-summary-control').click()
    cy.get('.btn').click()
    cy.get('input').type('1')
    cy.get('.execute-wrapper > .btn').click()
    // You can add more assertions here to validate the response body
  })
})


