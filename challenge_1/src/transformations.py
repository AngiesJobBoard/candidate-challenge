import requests

from challenge_1.src.models import User, Occupation, UserWithOccupation, ExampleArticle


def transform_raw_data_into_user(data: dict) -> User:
    return User(
        name=data["name"],
        age=data["age"],
        is_cool=data["is_cool"] if "is_cool" in data else None
    )


def transform_raw_data_into_occupation(data: dict) -> Occupation:
    return Occupation(
        title=data["title"],
        salary=data["salary"]
    )


def transform_raw_data_into_user_and_occupation(
    dict_1: dict | User,
    dict_2: dict | Occupation
) -> UserWithOccupation:
    if isinstance(dict_1, User):
        user = dict_1
    else:
        user = transform_raw_data_into_user(dict_1)
    
    if isinstance(dict_2, Occupation):
        occupation = dict_2
    else:
        occupation = transform_raw_data_into_occupation(dict_2)
    
    return UserWithOccupation(
        name=user.name,
        age=user.age,
        is_cool=user.is_cool,
        occupation=occupation
    )


def get_article(id: str):
    return requests.get(f"https://hn.algolia.com/api/v1/items/{id}")


def get_article_one_thousand() -> ExampleArticle:
    response = get_article("1000")
    return ExampleArticle(**response.json())
