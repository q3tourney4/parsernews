import unittest

from parsernews.projectnews.api.helpers import validate_paramters
from parsernews.projectnews.api.resources import get_posts


class HelpersTest(unittest.TestCase):

    # Тестирование функции validate_paramters

    # Позитивные тесты
    def test_validate_paramters_positive(self):
        result = validate_paramters("title", 10, 10)
        self.assertTrue(result)

        result = validate_paramters("titles", 10, 10)
        self.assertFalse(result)

        result = validate_paramters("title", 10, -10)
        self.assertFalse(result)

        result = validate_paramters("title", -10, 10)
        self.assertFalse(result)

    # Негативные тесты
    def test_validate_paramters_negative(self):
        result = validate_paramters(10, 10, 10)
        self.assertFalse(result)

        result = validate_paramters(10, True, 10)
        self.assertFalse(result)

        result = validate_paramters(10, True, False)
        self.assertFalse(result)


class ResourcesTest(unittest.TestCase):

    # Тестирование функции get_posts

    # Интеграционный тест
    def test_get_posts(self):
        result = get_posts(wizard="hackernews", order="title", offset=10, limit=3)
        self.assertTrue(list, result)

        result = get_posts(
            wizard="hackernews", order="title", offset=10, limit=3, ofset=100
        )
        self.assertTrue(str, result)


if __name__ == "__main__":
    unittest.main()
