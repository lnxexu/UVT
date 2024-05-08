describe('Violation Details', () => {
  
    it('can GET Report ID', () => {
      cy.visit('http://127.0.0.1:8000/docs#/Violation%20Details/get_specifyViolation_violationDetails__reportID__get')
      
      cy.get('#operations-Violation_Details-get_specifyViolation_violationDetails__reportID__get > .opblock-summary > .opblock-summary-control').should('be.visible').contains('Get Specifyviolation').click()
      cy.get('#operations-Violation_Details-get_specifyViolation_violationDetails__reportID__get > .opblock-summary > .opblock-summary-control').click()
      cy.get('.btn').click()
      cy.get('input').type('1')
      cy.get('.execute-wrapper > .btn').click()

      // You can add more assertions here to validate the response body
    })
it('can GET Student ID', () => {
  cy.visit('http://127.0.0.1:8000/docs#/Violation%20Details/get_violation_details_violationDetails_student__studentID__get')
  cy.get('#operations-Violation_Details-get_violation_details_violationDetails_student__studentID__get > .opblock-summary > .opblock-summary-control').should('be.visible').contains('Get Violation Details').click()
  cy.get('#operations-Violation_Details-get_violation_details_violationDetails_student__studentID__get > .opblock-summary > .opblock-summary-control').click()
  cy.get('.btn').click()
  cy.get('input').type('1')
  cy.get('.execute-wrapper > .btn').click()

  // You can add more assertions here to validate the response body
})
it('can POST details', () => {
  cy.visit('http://127.0.0.1:8000/docs#/Violation%20Details/create_violation_details_violationDetailsPost__post')
  cy.get('#operations-Violation_Details-create_violation_details_violationDetailsPost__post > .opblock-summary > .opblock-summary-control').should('be.visible').contains('Create Violation Details').click()
  cy.get('#operations-Violation_Details-create_violation_details_violationDetailsPost__post > .opblock-summary > .opblock-summary-control').click()
  cy.get('.btn').click()
  cy.get('[data-param-name="studentID"] > .parameters-col_description > input').type('220000002436')
  cy.get('[data-param-name="violation"] > .parameters-col_description > input').type('NO ID')
  cy.get('[data-param-name="dateTime"] > .parameters-col_description > input').type('2021-10-10T00:00:00Z')
  cy.get('[data-param-name="venue"] > .parameters-col_description > input').type('UIC Bangke')
  cy.get('[data-param-name="sanction"] > .parameters-col_description > input').type('1 week suspension')
  cy.get('[data-param-name="status"] > .parameters-col_description > input').type('Approved')
  cy.get('[data-param-name="guard"] > .parameters-col_description > input').type('None')
  cy.get('.execute-wrapper > .btn').click()

  // You can add more assertions here to validate the response body
})
it('can GET Student ID', () => {
  cy.visit('http://127.0.0.1:8000/docs#/Violation%20Details/get_violation_count_violationDetails_get')
  cy.get('#operations-Violation_Details-get_violation_count_violationDetails_get > .opblock-summary > .opblock-summary-control').should('be.visible').contains('Get Violation Count').click()
  cy.get('#operations-Violation_Details-get_violation_count_violationDetails_get > .opblock-summary > .opblock-summary-control').click()
  cy.get('.btn').click()
  cy.get('.execute-wrapper > .btn').click()

  // You can add more assertions here to validate the response body
})

})
