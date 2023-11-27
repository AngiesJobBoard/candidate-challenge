from challenge_1.src.transformations import (
    transform_raw_data_into_user,
    transform_raw_data_into_occupation,
    transform_raw_data_into_user_and_occupation
)


def test_create_user():
    data = {
        "name": "John Doe",
        "age": 42,
        "is_cool": True
    }
    
    user = transform_raw_data_into_user(data)
    
    assert user.name == "John Doe"
    assert user.age == 42
    assert user.is_cool is True
