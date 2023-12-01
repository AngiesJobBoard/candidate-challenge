from challenge_1.src.transformations import (
    transform_raw_data_into_user,
    transform_raw_data_into_occupation,
    transform_raw_data_into_user_and_occupation,
    get_article_one_thousand
)
import unittest
from unittest.mock import patch, MagicMock


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




class test_get_one_article_one_thousand(unittest.TestCase):

    @patch('challenge_1.src.transformations.requests.get')
    def test_get_article_one_thousand(self, mock_get):
        
        reponse = MagicMock()
        reponse.json.return_value = {
            "author": "python_kiss",
            "title": "How Important is the .com TLD?",
            "type": "story",
            "url": "http://www.netbusinessblog.com/2007/02/19/how-important-is-the-dot-com/",
            "children": [],
            "created_at": "2007-02-25T09:10:46Z",
            "id": 1000,
            "parent_id": None,
            "points": 4
        }
        mock_get.return_value = reponse

        article = get_article_one_thousand()

        self.assertEqual(article.author, "python_kiss")
        self.assertEqual(article.title, "How Important is the .com TLD?")
        self.assertEqual(article.type, "story")
        self.assertEqual(article.url, "http://www.netbusinessblog.com/2007/02/19/how-important-is-the-dot-com/")     
        self.assertEqual(article.children, [])
        #print("Actual created_at format:", article.created_at)
        self.assertEqual(str(article.created_at), "2007-02-25 09:10:46+00:00") 
        self.assertEqual(article.id, 1000)
        self.assertIsNone(article.parent_id)
        self.assertEqual(article.points, 4)

if __name__ == '__main__':
    unittest.main()