from src.utils import get_prefix

def test_get_prefix_returns_empty_string_if_passed_empty_string():
    assert get_prefix("") == ""
def test_get_prefix_returns_prefix():
    assert get_prefix("10.1080/09500693.2022.2164474") == "10.1080"
    assert get_prefix("10.1037/a0040251") == "10.1037"
