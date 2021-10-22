Feature: Testing the links on the home page

    As website manager
    I want to be able to click on the home page links
    So that I will be directed to the destinated page

    @texel_header_links
    Scenario Outline: Clicking the links in the header
        Given we are on https://www.texel.net/en/
        And the id of the header is __name
        When I click on <placeholder>
        Then I want to be directed to <reference>

        Examples:
            | placeholder | reference |
            | Value 1  | Value 2  |
        

    