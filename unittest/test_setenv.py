from py_setenv import click_command
import unittest
from click.testing import CliRunner


class TestSetEnv(unittest.TestCase):
    runner = None

    @classmethod
    def setUpClass(cls):
        cls.runner = CliRunner()

    @classmethod
    def tearDownClass(cls):
        cls.runner.invoke(click_command, ["unittest", "-d", "--user"])
        cls.runner.invoke(click_command, ["unittest", "-d"])

    def test_01_user_environment(self):
        self.run_checks(user=True)

    def test_02_system_environment(self):
        self.run_checks(user=False)

    def run_checks(self, user):
        # check that variable does not exist before start
        user_list = ["--user"] if user else []
        result = self.runner.invoke(click_command, ["unittest"] + user_list)
        self.assertEqual("Environment Variable 'unittest' does not exist", result.output.strip())

        # check that set returns True
        result = self.runner.invoke(click_command, ["unittest", "-v", "test_str"] + user_list)
        self.assertTrue(bool(result.output.strip()))

        # check that 'unittest' is in dictionary
        result = self.runner.invoke(click_command, ["--list-all"] + user_list)
        self.assertIn("unittest=test_str", result.output.strip())

        # test that new value was added
        result = self.runner.invoke(click_command, ["unittest"] + user_list)
        self.assertEqual("test_str", result.output.strip())

        # test that new text was appended
        result = self.runner.invoke(click_command, ["unittest", "-v", "appended_str", "-a"] + user_list)
        self.assertTrue(bool(result.output.strip()))

        result = self.runner.invoke(click_command, ["unittest"] + user_list)
        self.assertEqual("test_str;appended_str", result.output.strip())

        # check that delete returns True
        result = self.runner.invoke(click_command, ["unittest", "-d"] + user_list)
        self.assertTrue(bool(result.output.strip()))

        # check that deleted
        result = self.runner.invoke(click_command, ["unittest"] + user_list)
        self.assertEqual("Environment Variable 'unittest' does not exist", result.output.strip())
