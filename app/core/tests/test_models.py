from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """test creating new user with email"""
        email = "test@whatever.com"
        password = "password"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test the email for a new user is normalized"""
        email = "test@WHATEVER.com"
        user = get_user_model().objects.create_user(email, "123456")

        self.assertEquals(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creating new user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "123456")

    def test_create_new_superuser(self):
        """test creating a new super user"""
        user = get_user_model().objects.create_super_user("test@whatever.com", "123456")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
