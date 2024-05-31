
  Scenario: Search for a product, add to basket, and update quantity
    Given I am on the Amazon homepage
    When I search for "keyboard"
    And I select the first product from the search results
    And I add the product to my basket
    And I update the quantity of the item in the basket to 5
    Then the quantity of the item in the basket should be updated to 5