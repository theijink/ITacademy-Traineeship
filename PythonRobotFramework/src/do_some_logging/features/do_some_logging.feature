Feature: Test if logging works

    As a developer
    I want to use the logging package
    So that I can view log activies happening during execution

    Scenario: Logging of an error
        Given the logfile is specified and initialised
        When an error occurs
        Then this error gets logged to the logfile