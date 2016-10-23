import pytest


@pytest.mark.parametrize("word,length", [("abc", 3), ("dd", 2)], ids=["For 3", "For 2"]) #Ids are test names
def test_len(word, length):
    assert len(word) == length
