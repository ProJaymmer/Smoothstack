import time
import pytest

# To skip slow
# pytest -m "not slow" marker.py

# To not skip slow
# pytest -m "slow" marker.py

@pytest.mark.slow
def test_slow():
    time.sleep(10)

def test_junk():
    pass
