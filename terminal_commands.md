# Running Tests

### Python 2.x
```bash
python -m unittest discover -v
```

### Python 3.x

```
python3 -m unittest
python3 -m unittest -v
python3 -m unittest -q <test_file>.<test_suite>.<test_case>
```


# Doctest 
```
python3 -m doctest <test_file> -v
python3 -m pytest --doctest-modules -v
```


# Test Coverage

## `pytest`

```
python3 -m pytest --cov-report term-missing --cov <test_file>
python3 -m pytest --cov-report html --cov <test_file>
```

## `unittest`

```
python3 -m coverage run -m unittest
python3 -m coverage report
python3 -m coverage html
```