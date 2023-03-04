import unittest
from Account import Account
import json



class TestProduct(unittest.TestCase):
    """Testing each function of the Account class"""

    def test_verify_account_creation(self):
        """Test case design to test the account creation function"""
        # Test case for a valid account creation
        account = Account()
        account.set_username("BILLY")
        account.set_password("PASSWORD123@")
        account.set_recovery_password("PENGUIN")
        self.assertIsNone(account.verify_account_creation())

        # Test case for an invalid username
        account.set_username("BILLY")
        account.set_password("PASSWORD123@")
        account.set_recovery_password("TEST")
        self.assertRaises(ValueError, account.verify_account_creation)

        # Test case for an invalid password
        account.set_username("JOHNDOE")
        account.set_password("password")
        account.set_recovery_password("Test")
        self.assertRaises(ValueError, account.verify_account_creation)

    def test_verify_account_login(self):
        """Test case design to test the verify account login function"""
        # Test case for a valid login verification
        my_account = Account()
        username = "BILLY"
        password = "Password123@"
        self.assertIsNone(my_account.verify_account_login(username, password))

        # Test case for an invalid login verification
        my_account.set_username("Penguin344")
        my_account.set_password("Password123@444")
        self.assertRaises(ValueError, my_account.verify_account_login())

    def test_update_password(self):
        """Test case design to test the update password function"""
        # Define the dictionary to be modified
        test_dict = {"username": "test_user", "password": "password123", "recoveryPass": "recovery123"}

        # Modify the required dictionary
        modify_key = "password"
        new_value = "new_password123"

        # Modify the dictionary with the new password
        test_dict[modify_key] = new_value

        # Write the modified dictionary back to the file
        with open("test_file.txt", "w") as file:
            file.write(json.dumps(test_dict))

        # Read the modified dictionary from the file
        with open("test_file.txt", "r") as file:
            modified_dict = json.loads(file.readline())

        # Check that the password was successfully updated
        assert modified_dict["password"] == new_value

    if __name__ == '__main__':
        unittest.main()