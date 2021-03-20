Feature: As a user, I want to add an item I like, so that I can purchase it later on

    Scenario: Add initial item
        Given the user's basket has 0 items in it
        When the user adds the item to the basket
        Then the user's basket has 1 items in it

    Scenario: Add more items
        Given the user's basket has at least 1 item
        When the user adds the item to the basket
        Then the user's basket has one more item in it

