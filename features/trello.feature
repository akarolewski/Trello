Feature: Trello board

  Scenario: Trello Api Tests
  Given I create a new Trello Board
    When I create a new list
    And I create a first card
    And I create a second card
    And I create a third card
    And I post a comment on first card
    Then I update second card
    And I delete third card

  Scenario: Trello board tests
    Given I open Trello login page
    When I type in username
    And I press login button
    And I type in password
    And I press submit login button
    Then I make sure that Im logged in
    And I open recently added board
    And I make sure that two recently added cards are visible
    And I make sure that one card contains a comment
    And I open that card's details page
    And I check whether previous comment contains correct message
    And I add a comment to that card
    Then I make sure that the comment has been added
    And I set the card as done
