# content of test_tmp_path.py, "tmp_path" is a special fixture
def test_needsfiles(tmp_path):
    print(tmp_path)
    assert 1
