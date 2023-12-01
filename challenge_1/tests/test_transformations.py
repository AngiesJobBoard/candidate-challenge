from challenge_1.src.transformations import (
    transform_raw_data_into_user,
    transform_raw_data_into_occupation,
    transform_raw_data_into_user_and_occupation,
    get_article,
    get_article_one_thousand
)

def test_create_user():
    data = {
        "name": "James Merilien",
        "age": 21,
        "is_cool": True
    }
    
    user = transform_raw_data_into_user(data)
    
    assert user.name == "James Merilien"
    assert user.age == 21
    assert user.is_cool is True

def test_create_occupation():
    data = {
        "title": "Software Developer",
        "salary": 80000
    }
    occupation = transform_raw_data_into_occupation(data)

    assert occupation.title == "Software Developer"
    assert occupation.salary == 80000

def test_create_user_occupation():
    user_data = {
        "name": "James Merilien",
        "age": 21,
        "is_cool": True
    }

    occupation_data = {
        "title": "Software Developer",
        "salary": 80000
    }

    user_occupation = transform_raw_data_into_user_and_occupation(user_data, occupation_data)

    assert user_occupation.name == "James Merilien"
    assert user_occupation.age == 21
    assert user_occupation.is_cool is True
    assert user_occupation.occupation.title == "Software Developer"
    assert user_occupation.occupation.salary == 80000




def test_get_article_one_thousand():
    article = get_article_one_thousand()

    assert article.author == "python_kiss"
    assert article.title == "How Important is the .com TLD?"
    assert article.type == "story"
    assert article.url == "http://www.netbusinessblog.com/2007/02/19/how-important-is-the-dot-com/"
    assert article.children == []
    assert str(article.created_at) == "2007-02-25 09:10:46+00:00" 
    assert article.id == 1000
    assert article.parent_id == None
    assert article.points == 4
