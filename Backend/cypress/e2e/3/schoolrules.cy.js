describe('Schoolrules', () => {
  
    it('can GET admin (Read Admins)', () => {
      cy.visit('http://127.0.0.1:8000/docs#/School%20Rules')
      cy.get('#operations-School_Rules-get_school_rules_schoolRules_get > .opblock-summary > .opblock-control-arrow').click()
      cy.get('.btn').click()
      cy.get('.execute-wrapper > .btn').click()
      // You can add more assertions here to validate the response body
    })
})
    