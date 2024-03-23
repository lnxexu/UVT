describe('Login Page', () => {
    beforeEach(() => {
        cy.viewport(1280, 720)
      // Visit the login page before each test
      cy.visit('http://localhost:5173/login');
    });
  
    it('should display error message for empty username', () => {
      // Click the login button without filling in any fields
      cy.get('[data-testid=login-button]').click();
      // Verify if error message is displayed
      cy.get('[data-testid=error-message]').should('be.visible').and('contain.text', 'Please enter both email and password');
      // Wait for 5 seconds to ensure error message disappears
      cy.wait(5000);
      // Verify if error message disappears
      cy.get('[data-testid=error-message]').should('not.exist');
    });
   
    it('should display error message for invalid username and valid password', () => {
      // Fill in invalid username and valid password
      cy.get('[data-testid=email]').type('invalid@example.com');-
      cy.get('[data-testid=password]').type('12345');
      // Click the login button
      cy.get('[data-testid=login-button]').click();
      // Verify if error message is displayed
      cy.get('[data-testid=error-message]').should('be.visible');
      // Wait for 5 seconds to ensure error message disappears
      cy.wait(5000);
      // Verify if error message disappears
      cy.get('[data-testid=error-message]').should('not.exist');
    });
  
    it('should login with valid username and password', () => {
      // Fill in valid username and password
      cy.get('[data-testid=email]').type('student@example.com');
      cy.get('[data-testid=password]').type('12345');
      // Click the login button
      cy.get('[data-testid=login-button]').click();
      // Verify if redirected to the next page
      cy.url().should('include', '/'); // Update the URL if the redirection is different
    });
  });