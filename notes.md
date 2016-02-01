# Course Summary

- Unit testing vocabulary & basic example using `unittest`
- Unit test - why and when
- An alternative to `unittest`: `pytest`
- Testable documentation using `doctest`
- Test doubles
- Assessing test suite coverage
- Maintainable unit tests


# Module Summary

- Unit testing vocabulary & "Phoneback" example
    - test suite
    - test case
    - test runner
- Test case design


# Review of Fundamentals

### System Under Test

- a unit test checks the behavior of an **element of code**
    - a method or function
    - a module or class

- an automated test
    - designed by a human
    - runs without intervention
    - report results unambiguously as "pass" or "fail"

- it's not a unit test if it uses
    - the file system
    - a database
    - the network


# Exercise - Phone Numbers

- Given a list of names and phone numbers, make a Phonebook that allows you to look up numbers by name

- Determine if a given Phonebook is consistent
    - In a consistent phone list, no number is a prefix of another
        - `Bob          91125436`
        - `Alice        97 625 922`
        - `Emergency    911
    - Bob and Emergency are inconsistent!
    
    
    
    