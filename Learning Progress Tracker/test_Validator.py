from unittest import TestCase
from Validator import Validator

class TestValidator(TestCase):
    def test_name(self):
        self.assertRegex("Joe", Validator.name_pattern)
        self.assertRegex("Jean-Claude", Validator.name_pattern)
        self.assertRegex("O'Neill", Validator.name_pattern)

    def test_last_name(self):
        self.assertRegex("Voldemort", Validator.last_name_pattern)
        self.assertRegex("Jemison Van de Graaff", Validator.last_name_pattern)
        self.assertRegex("Ronald Reuel Tolkien", Validator.last_name_pattern)

    def test_email(self):
        self.assertRegex("Joe@gmai.com", Validator.email_pattern)
        self.assertRegex("Olek123@domain.haha", Validator.email_pattern)
        self.assertRegex("jane.doe@yahoo.com", Validator.email_pattern)
        self.assertRegex("125367at@zzz90.z9", Validator.email_pattern)

    def test_id_points(self):
        self.assertRegex("10000 10 10 5 8", Validator.id_and_points_pattern)
        self.assertRegex("10000 10 -10 5 8", Validator.id_and_points_pattern)
        self.assertRegex("10000 10 10 5", Validator.id_and_points_pattern)