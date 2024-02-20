# features/test_api.feature

Feature: Example of api testing with DonBot

  Scenario: Make a GET request
    Given who made a GET request to "https://pokeapi.co/api/v2/"
    Then the response must have status code 200