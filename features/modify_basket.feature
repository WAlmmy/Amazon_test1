Feature: As a user, I want to be see all items in my basket, so that I can modify it if required

    Scenario: Change item quantity
        Given a user is viewing their basket
        When the user changes the quantity of one of the items
        Then the item quantity changes accordingly
        And the overall number of items in the basket changes accordingly

    Scenario: Delete item
        Given a user is viewing their basket
        When the user deletes an item
        Then the item is no longer present in the basket
        And the overall number of items in the basket changes accordingly

    Scenario: Delete all items
        Given a user is viewing their basket
        When the user deletes all items
        Then no items are present in the basket
        And a message saying the basket is empty is displayed
        