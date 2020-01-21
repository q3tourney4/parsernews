"""
    Основной модуль сбора всех файлов SuiteTest расположенных в подсистеме.
    В каждом компоненте присутствует собственный пакет с каталогом тестирования.
"""
import os
import unittest

os.sys.path.append(os.getcwd())

from parsernews.projectnews.api.test.test_suites import api_suites
from parsernews.projectnews.parcing.test.test_suites import parcing_suites


def inspect_text_suite():
    test_suite = unittest.TestSuite()

    test_suite.addTests(api_suites())
    test_suite.addTests(parcing_suites())

    return test_suite


if __name__ == "__main__":
    level = 1
    suite = inspect_text_suite()
    runner = unittest.TextTestRunner(verbosity=level)
    result = runner.run(suite)
    if result.failures or result.errors:
        raise Exception(
            f"Обнаружены ошибки во врермя выполнения unittests. FAILED: "
            f"failures={len(result.failures)}, errors={len(result.errors)}"
        )
