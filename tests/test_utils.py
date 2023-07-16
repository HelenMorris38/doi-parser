from src.utils import  create_publisher_dict

# def test_get_prefix_returns_empty_string_if_passed_empty_string():
#     assert get_prefix("") == ""
# def test_get_prefix_returns_prefix():
#     assert get_prefix("10.1080/09500693.2022.2164474") == "10.1080"
#     assert get_prefix("10.1037/a0040251") == "10.1037"

def test_create_publisher_dict_returns_correct_val_list_len_1():
    input = [{
        "prefixes": [
            "10.54341"
        ],
        "name": "Francisk Skorina Gomel State University",
        "memberId": 32768
    }]
    output = {"10.54341": "Francisk Skorina Gomel State University"}
    assert create_publisher_dict(input) == output
def test_create_publisher_dict_returns_correct_val():
    input = [
        {
        "prefixes": [
            "10.54341"
        ],
        "name": "Francisk Skorina Gomel State University",
        "memberId": 32768
        },
        {
        "prefixes": [
            "10.1370"
        ],
        "name": "Annals of Family Medicine",
        "memberId": 1
        }
    ]
    output = {
        "10.54341" : "Francisk Skorina Gomel State University",
        "10.1370" : "Annals of Family Medicine"
        }
    assert create_publisher_dict(input) == output
def test_create_publisher_dict_returns_correct_val_multiple_prefixes():
    input = [
        {
        "prefixes": [
            "10.54341"
        ],
        "name": "Francisk Skorina Gomel State University",
        "memberId": 32768
        },
        {
        "prefixes": [
            "10.1370"
        ],
        "name": "Annals of Family Medicine",
        "memberId": 1
        },
        {
        "prefixes": [
            "10.1164",
            "10.34197",
            "10.1165",
            "10.1513"
        ],
        "name": "American Thoracic Society",
        "memberId": 19
        }
    ]
    output = {
        "10.54341" : "Francisk Skorina Gomel State University",
        "10.1370" : "Annals of Family Medicine",
        "10.1164" : "American Thoracic Society",
        "10.34197" : "American Thoracic Society",
        "10.1165" : "American Thoracic Society",
        "10.1513" : "American Thoracic Society",
        }
    assert create_publisher_dict(input) == output