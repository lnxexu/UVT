describe('Students', () => {
  
    it('can GET Student', () => {
      cy.visit('http://127.0.0.1:8000/docs#/Student/get_all_student_student_get')
      cy.get('#operations-Student-get_all_student_student_get > .opblock-summary > .opblock-summary-control').should('be.visible').contains('Get All Student').click()
      cy.get('#operations-Student-get_all_student_student_get > .opblock-summary > .opblock-summary-control').click()
      cy.get('.btn').click()
      cy.get('.execute').click()
      // You can add more assertions here to validate the response body
    })
    it('can Add Student', () => {
      cy.visit('http://127.0.0.1:8000/docs#/Student/add_student_student_post')
      cy.get('#operations-Student-add_student_student_post > .opblock-summary > .opblock-summary-control').should('be.visible').contains('Add Student').click()
      cy.get('#operations-Student-add_student_student_post > .opblock-summary > .opblock-summary-control').click()
      cy.get('.btn').click()
      cy.get('[data-param-name="studentID"] > .parameters-col_description > input').type('220000002436')
      cy.get('[data-param-name="section"] > .parameters-col_description > input').type('BSIT-2B')
      cy.get('[data-param-name="name"] > .parameters-col_description > input').type('GI Linghon')
      cy.get('[data-param-name="gender"] > .parameters-col_description > input').type('Male')
      cy.get('[data-param-name="age"] > .parameters-col_description > input').type('23')
      cy.get('[data-param-name="contactInformation"] > .parameters-col_description > input').type('09123456789')
      cy.get('[data-param-name="address"] > .parameters-col_description > input').type('Malvar')
      cy.get('[data-param-name="birthDate"] > .parameters-col_description > input').type('2000-10-10')
      cy.get('.execute-wrapper > .btn').click()
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


