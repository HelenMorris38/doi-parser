from src.utils import get_prefix

def test_returns_empty_string_if_passed_empty_string():
    assert get_prefix("") == ""