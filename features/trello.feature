Feature: Trello board

  Scenario: Trello API Board Setup
    Given I create a new Trello Board
    When I create a new list
    When I create a "first" card
    When I create a "second" card
    When I create a "third" card
    When I post a comment on "first" card
    Then I update "second" card
    Then I delete "third"


  Scenario: Trello board tests
    Given I open Trello login page
    When I type in username
    When I type in password
    When I press submit login button
    Then I make sure that Im logged in