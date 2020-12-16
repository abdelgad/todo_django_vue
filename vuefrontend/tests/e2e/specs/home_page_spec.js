
describe('Input form', () => {
  beforeEach(() => {
    cy.visit('/')
    cy.location('pathname').should('equal', '/login')

    // enter valid username and password
    cy.get('input[name=username]').type(Cypress.env('username'))
    cy.get('input[name=password]').type(`${Cypress.env('username')}{enter}`)

    // confirm we have logged in successfully
    cy.location('pathname').should('equal', '/')
  })

  it('accepts input', () => {
    const typedText = 'Testing the typing'

    cy.get('input[name=value]')
      .type(typedText)
      .should('have.value', typedText)
  })

  context('Form submission', () => {

    it('Adds a new todo on submit', () => {
      const itemText = 'Rendre le travail !'

      cy.get('input[name=value]')
        .type(itemText)
        .type('{enter}')
        .should('have.value', '')

      cy.get('.todo-list li')
        .should('contain', itemText)
    })

    it('Shows an error message on a failed submission', () => {
      const itemText = 'Rendre le travail !'

      cy.get('input[name=value]')
      .type(itemText)
      .type('{enter}')
      .should('have.value', itemText)
    })
  })
})


describe('List items', () => {
  beforeEach(() => {
    cy.visit('/')
    cy.location('pathname').should('equal', '/login')

    // enter valid username and password
    cy.get('input[name=username]').type(Cypress.env('username'))
    cy.get('input[name=password]').type(`${Cypress.env('username')}{enter}`)

    // confirm we have logged in successfully
    cy.location('pathname').should('equal', '/')
  })

  const itemText = 'Rendre le travail !'

  it('Removes a todo', () => {

    cy.get('li[class="todo-item"]').contains(itemText).click()
    cy.get('button').contains('Delete').click()

    cy.get('.todo-list li')
    .should('not.contain', itemText)
  })

  it('Marks an unchecked todo as checked', () => {

    cy.get('input[name=value]')
      .type(itemText)
      .type('{enter}')
      .should('have.value', '')

    cy.get('.todo-list li')
      .should('contain', itemText)

    cy.get('li[class="todo-item"]').contains(itemText).click()

    cy.get('button').contains('Check').click()

    cy.get('li.active').should('have.class', 'checkedTodo')

    cy.get('button').contains('Delete').click()
  })
})
