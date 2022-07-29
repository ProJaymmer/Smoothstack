# Notes

## regular
```pytest <prog>.py```

## Quiet mode
```pytest -q <prog>.py```

## pytest fixtures
```pytest --fixtures```

## run tests by keyword expressions

This will run tests which contain names that match the given string expression (case-insensitive), which can include Python operators that use filenames, class names and function names as variables. The example above will run TestMyClass.test_something but not TestMyClass.test_method_simp

```pytest -k "MyClass and not method"```

## run test by node ids

Each collected test is assigned a unique nodeid which consist of the module filename followed by specifiers like class names, function names and parameters from parametrization, separated by :: characters.

To run a specific test within a module:

```pytest test_mod.py::test_func```

Another example specifying a test method in the command line:

```pytest test_mod.py::TestClass::test_method```

## Run tests by marker expressions

```pytest -m slow```

Will run all tests which are decorated with the @pytest.mark.slow decorator.

## Show captured (std) output of passed tests
pytest -rP fixtures_cached.py

## Show captured (std) output of failed tests
pytest -rx fixtures_cached.py
