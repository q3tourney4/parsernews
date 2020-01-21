"""
    Test Suite для пакета api
"""
import unittest

from parsernews.projectnews.api.test.test_helpers import HelpersTest, ResourcesTest


def api_suites():
    loader = unittest.TestLoader()
    # Добавляем все test cases в список, после чего они будут загружены через loader.

    test_cases = [
        HelpersTest,  # unit-тестирование
        ResourcesTest,  # интеграционное тестирование
    ]
    suites = []

    for case in test_cases:
        suites.append(loader.loadTestsFromTestCase(case))

    res_suite = unittest.TestSuite(suites)
    return res_suite


if __name__ == "__main__":
    level = 1
    suite = api_suites()
    runner = unittest.TextTestRunner(verbosity=level)
    result = runner.run(suite)
