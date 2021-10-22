Feature: Battery calculations assignment

    The battery calculation module is called with parameters. The
    parameters decide which calculation is made, i.e. when called
    with Uk and Rl, I will be calculated.

    @electronix
    Scenario Outline: Calculate I from Uk and Rl
        Given the battery calculation module is online and available
        When I call the battery calculation module with Uk=<Uk> and Rl=<Rl>
        Then the module calculates the correct value of I=<I>

        Examples: Calculate current I as Uk / Rl
            |  Uk |  Rl |   I |
            | 0.0 | 2.5 | 0.0 |
            | 5.0 | 2.5 | 2.0 |

    @electronix
    Scenario Outline: Calculate Uk from Ub, Ri and Rl
        Given the battery calculation module is online and available
        When I call the battery calculation module with Ub=<Ub>, Ri=<Ri>, and Rl=<Rl>
        Then the module calculates the correct value of Uk=<Uk>

        Examples:
            | Uk  | Ub  | Ri  | Rl  |
            | 4.5 | 6.0 | 3.0 | 9.0 |

    @electronix
    Scenario Outline: Calculate Ri from Ub, Uk and Rl
        Given the battery calculation module is online and available
        When I call the battery calculation module with Ub=<Ub>, Uk=<Uk>, and Rl=<Rl>
        Then the module calculates the correct value of Ri=<Ri>

        Examples:
            | Ri  | Ub  | Uk  | Rl  |
            |-2.4 | 3.0 | 5.0 | 6.0 |

    @electronix
    Scenario Outline: Calculate Rl from Uk and I
        Given the battery calculation module is online and available
        When I call the battery calculation module with Uk=<Uk> and I=<I>
        Then the module calculates the correct value for Rl=<Rl>

        Examples:
            | Rl  | Uk  | I   |
            | 1.3 | 3.0 | 8.0 |
