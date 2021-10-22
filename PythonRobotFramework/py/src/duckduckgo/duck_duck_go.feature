Feature: search for something with duckduckgo engine in firefox

    As a user
    I want to use the duckduckgo engine in firefox
    So that I can search on the internet

    @duckduckgo
    Scenario: Visit the engine url
        Given the browser has been started up
        Then visit the page for the engine

    @duckduckgo
    Scenario Outline: Enter <something> in the entry
        Given the home page of the engine has been openend
        When I enter <something> in the entry
        Then <something> must appear in the entry

        Examples: Items to search
            | something             |
            | who let the dogs out  |
    
    @duckduckgo
    Scenario Outline: Search the entered text on the internet
        Given <something> is entered in the entry box
        And a search button is shown
        When I press the search button
        Then the results must appear in the browser

        Examples:
            | something |
            | Namaste   |
    
    @duckduckgo
    Scenario: Close the browser
        Given the browser has been started up
        Then close the browser

