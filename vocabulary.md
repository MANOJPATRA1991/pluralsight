##### test case

- each one is for a specific behavior of system
- each should be run independently of others
- clearly report whether it has passed or failed
- should not have side effects other test cases will rely on
    - i.e. a test case shouldn't create data another test case will use


##### test runner

- executes test cases and reports the results
- in the `unittest` module, the command line test runner is built-in
- shouldn't be considered when writing test cases


##### test suite

- a number of test cases that are executed together by a test runner


##### test fixture

- a piece of code that can construct and configure the system of the test to get it ready to be tested, and then clean up afterwards
- allows separation of concerns so the test cases can concentrate on specifying and checking a particular behavior, and not be cluttered by general set-up details
- `setUp` and `tearDown`
- in pure unit testing when all objects are in memory, there is usually no explicit need for `tearDown` step because the memory manager would take care of the cleanup

```python
def setUp(self):
    self.phonebook = Phonebook("extraneous argument")

def test_lookup_entry_by_name(self):
    self.phonebook.add("Bob", "12345")
    self.assertEqual("123456", self.phonebook.lookup("Bob"))

def tearDown(self):
    pass
```