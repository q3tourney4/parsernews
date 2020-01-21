"""
    Test Suite для пакета parcing
"""
import unittest

from parsernews.projectnews.parcing.test.test_hacker_news_parser import (
    HackerNewsParserTest,
)


def parcing_suites():
    loader = unittest.TestLoader()
    # Добавляем все test cases в список, после чего они будут загружены через loader.

    test_cases = [
        HackerNewsParserTest,  # unit-тестирование
    ]
    suites = []

    for case in test_cases:
        suites.append(loader.loadTestsFromTestCase(case))

    res_suite = unittest.TestSuite(suites)
    return res_suite


if __name__ == "__main__":
    level = 1
    suite = parcing_suites()
    runner = unittest.TextTestRunner(verbosity=level)
    result = runner.run(suite)
