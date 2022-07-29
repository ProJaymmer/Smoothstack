import pytest

@pytest.mark.xfail
def test_function():
    return 1/0
