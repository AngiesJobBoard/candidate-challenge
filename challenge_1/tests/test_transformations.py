from challenge_1.src.transformations import (
    transform_raw_data_into_user,
    transform_raw_data_into_occupation,
    transform_raw_data_into_user_and_occupation,
    get_article_one_thousand
)
from challenge_1.src.models import User, Occupation, UserWithOccupation, ExampleArticle
from datetime import datetime

def test_transform_raw_data_into_user():
    # Test user creation base case
    data = {
        "name": "John Doe",
        "age": 25,
        "is_cool": True
    }
    
    user = transform_raw_data_into_user(data)
    
    assert isinstance(user, User)
    assert user.name == "John Doe"
    assert user.age == 25
    assert user.is_cool is True

    # Test user creation without optional field is_cool
    data = {
        "name": "Jane Doe",
        "age": 23,
    }
    
    user = transform_raw_data_into_user(data) # Attempt to transform user data without is_cool field
    
    assert isinstance(user, User)
    assert user.name == "Jane Doe"
    assert user.age == 23

    # Failure cases
    # Ensure that an error is thrown when omitting a required field (name)
    missing_name_data = {
        "age": 18,
        "is_cool": True
    }

    failure = False
    try:
        user = transform_raw_data_into_user(missing_name_data)
        
        # Transformation should not succeed, so set a flag if it does.
        failure = True
    except:
        pass # The transformation errored as expected.

    if failure: # Check failure flag
        raise AssertionError("Expected error for missing 'name' field in user data")

    # Ensure that an error is thrown when omitting a required field (age)
    missing_age_data = {
        "name": "Tony Stark",
        "is_cool": True
    }

    try:
        user = transform_raw_data_into_user(missing_age_data)

        # Transformation should not succeed, so set a flag if it does.
        failure = True
    except:
        pass # The transformation errored as expected.

    if failure:
        raise AssertionError("Expected error for missing 'age' field in user data")
    
    # WRITE MORE CASES FOR INVALID TYPE CHECKING!!!
    # ALSO NORMALIZE ERROR MESSAGE

def test_transform_raw_data_into_occupation():
    # Test occupation creation base case
    data = {
        "title": "Software Engineer",
        "salary": 80000
    }
    
    occupation = transform_raw_data_into_occupation(data)
    
    assert isinstance(occupation, Occupation)
    assert occupation.title == "Software Engineer"
    assert occupation.salary == 80000
    
    # Failure cases
    # Ensure that an error is thrown when omitting a required field (title)
    missing_title_data = {
        "salary": 2000
    }
    
    failure = False
    try:
        occupation = transform_raw_data_into_occupation(missing_title_data)

        failure = True # Transformation should not succeed, so set a flag if it does
    except:
        pass # The transformation errored as expected.

    if failure:
        raise AssertionError("Expected error for missing 'title' field in occupation data")
    
    # Ensure that an error is thrown when omitting a required field (salary)
    missing_salary_data = {
        "title": "Full Stack Developer",
    }

    try:
        occupation = transform_raw_data_into_occupation(missing_salary_data)

        failure = True # Transformation should not succeed, so set the failure flag if it does
    except:
        pass # The transformation errored as expected.

    if failure:
        raise AssertionError("Expected error for missing 'salary' field in occupation data")
    
    # Ensure that an error is thrown with an invalid value for salary
    invalid_salary_data = {
        "title": "Intern",
        "salary": -1,
    }

    try:
        occupation = transform_raw_data_into_occupation(invalid_salary_data)

        failure = True
    except:
        pass # The transformation errored as expected.

    if failure:
        raise AssertionError("Expected error for invalid 'salary' field in occupation data")

def test_transform_raw_data_into_user_and_occupation():
    # Test base case for transformation into user with occupation
    user_data = {
        "name": "Alice",
        "age": 30,
        "is_cool": False
    }
    
    occupation_data = {
        "title": "Data Scientist",
        "salary": 90000
    }
    
    result = transform_raw_data_into_user_and_occupation(user_data, occupation_data)
    
    assert isinstance(result, UserWithOccupation)
    assert result.name == "Alice"
    assert result.age == 30
    assert result.is_cool is False
    assert isinstance(result.occupation, Occupation)
    assert result.occupation.title == "Data Scientist"
    assert result.occupation.salary == 90000

    # Failure cases
    # Test with missing 'name' field in user data
    user_data_missing_name = {
        "age": 25, 
        "is_cool": True
    }
    occupation_data = {
        "title": "Software Engineer", 
        "salary": 100000
    }

    failure = False
    try:
        transform_raw_data_into_user_and_occupation(user_data_missing_name, occupation_data)
        failure = True
    except:
        pass

    if failure:
        raise AssertionError("Expected error for missing 'name' field in user data")

    # Test with missing 'title' field in occupation data
    user_data = {
        "name": "John Doe", 
        "age": 25, 
        "is_cool": True
    }
    occupation_data_missing_title = {
        "salary": 100000
    }
    try:
        transform_raw_data_into_user_and_occupation(user_data, occupation_data_missing_title)
        failure = True
    except:
        pass
    
    if failure:
        raise AssertionError("Expected error for missing 'title' field in occupation data")

    # Test with invalid type for 'age' field in user data
    user_data_invalid_age_type = {"name": "John Doe", "age": "25", "is_cool": True}
    try:
        transform_raw_data_into_user_and_occupation(user_data_invalid_age_type, occupation_data)
        failure = True
    except:
        pass

    if failure:
        raise AssertionError("Expected error for invalid type of 'age' field in user data")

    # Test with invalid type for 'salary' field in occupation data
    occupation_data_invalid_salary_type = {"title": "Software Engineer", "salary": "100000"}
    try:
        transform_raw_data_into_user_and_occupation(user_data, occupation_data_invalid_salary_type)
        failure = True
    except:
        pass

    if failure:
        raise AssertionError("Expected error for invalid type of 'salary' field in occupation data")

def test_get_article_one_thousand(monkeypatch):
    # Mimic the response of the requests.get function to avoid sending HTTP requests
    class MockResponse:
        @staticmethod
        def json():
            return {
                "author": "python_kiss",
                "title": "How Important is the .com TLD?",
                "type": "story",
                "url": "http://www.netbusinessblog.com/2007/02/19/how-important-is-the-dot-com/",
                "children": [],
                "created_at": datetime.utcnow().isoformat(),
                "id": 1000,
                "parent_id": None,
                "points": 4
            }
    
    def mock_get_article(id):
        return MockResponse()
    
    # Monkeypatching the requests.get function to use the mock response method
    monkeypatch.setattr("challenge_1.src.transformations.get_article", mock_get_article)
    
    article = get_article_one_thousand()
    
    assert isinstance(article, ExampleArticle)
    assert article.author == "python_kiss"
    assert article.title == "How Important is the .com TLD?"
    assert article.type == "story"
    assert article.url == "http://www.netbusinessblog.com/2007/02/19/how-important-is-the-dot-com/"
    assert isinstance(article.children, list)
    assert isinstance(article.created_at, datetime)
    assert article.id == 1000
    assert article.parent_id is None
    assert article.points == 4
