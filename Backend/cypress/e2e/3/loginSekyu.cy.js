describe('Login Sekyu', () => {

it('can GET Latest Login Sekyu', () => {
    cy.visit('http://127.0.0.1:8000/docs#/LoginSekyu/get_latest_login_loginSekyu_get')
    cy.get('#operations-LoginOSAD-get_latest_login_loginOSAD_get > .opblock-summary > .opblock-summary-control').should('be.visible').contains('Get Latest Login').click()
    cy.get('#operations-LoginOSAD-get_latest_login_loginOSAD_get > .opblock-summary > .opblock-summary-control').click()
    cy.get('.btn').click()
    cy.get('.execute-wrapper > .btn').click()
    // You can add more assertions here to validate the response body
  })
 it('can POST Add login sekyu', () => {
    cy.visit('http://127.0.0.1:8000/docs#/LoginSekyu/add_login_loginSekyu_post')
    cy.get('#operations-LoginOSAD-add_login_loginOSAD_post > .opblock-summary > .opblock-summary-control').should('be.visible').contains('Add Login').click()
    cy.get('#operations-LoginOSAD-add_login_loginOSAD_post > .opblock-summary > .opblock-summary-control').click()
    cy.get('.btn').click()
    cy.get('[data-param-name="email"] > .parameters-col_description > input').type('demo@gmail.com')
    cy.get('[data-param-name="fullName"] > .parameters-col_description > input').type('Kendrick Lamar')
    cy.get('[data-param-name="timestampLogin"] > .parameters-col_description > input').type('2024-04-28 18:16:48')
    cy.get('.execute-wrapper > .btn').click()
    // You can add more assertions here to validate the response body
  })
})
