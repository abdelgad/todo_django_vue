describe('Test Login Page Access', () => {
  it('should be able to successfully load', () => {
    cy.visit('/login')
  })
})

describe('Test login process', () => {

  it('should be able to login and be redirected to the todos page', function () {

    const username = Cypress.env('username');
    const password = Cypress.env('password');

    cy.visit('/login')

    cy.get('input[name=username]').clear().type(username)

    cy.get('input[name=password]').clear().type(`${password}{enter}`)

    cy.url().should('equal', 'http://localhost:8080/')
  })

  it('should not be able to login with invalid password', function () {
    // destructuring assignment of the this.currentUser object
    const username = 'incorrect'
    const password = 'incorrect'

    cy.visit('/login')

    cy.get('input[name=username]').clear().type(username)

    cy.get('input[name=password]').clear().type(`${password}{enter}`)

    cy.url().should('include', '/login')

    cy.contains('.error-message', 'Incorrect username or password entered !')
  })


  it('should not be able to login with no credentials', function () {

    cy.visit('/login')

    cy.get('input[name=username]').type(`{enter}`)

    cy.url().should('equal', 'http://localhost:8080/login')

    cy.contains('.error-message', 'Incorrect username or password entered !')
  })
})
