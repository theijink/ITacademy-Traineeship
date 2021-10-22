Feature: Exercise with examples and a Data Table

    This feature contains two scenarios, both passing data through steps.
    We make use of a Scenario Outline and a Data Table

    Within the step implementation we make a file in which data from the Examples and Data Table is written

Scenario: Create a file
    Given there is an empty text file available to us
    When I open this file
    And I write the following table in it
        | course            | participants  |
        | Behave            | 213           |
        | Cucumber          | 0             |
        | Robot Framework   | 42            |
    Then this file has three lines in it

Scenario Outline: some records
    Given the text file has been opened
    Then I write the values <first>, <second> and <third>
    And I close the file

    Examples:
        | first | second    | third     |
        | one   | monkey    | monday    |
        | two   | cow       | tuesday   |
        | three | moose     | wednesday |
        | four  | dodo      | thursday  |