# Billy Bryant 25/02/2023 - A basic software that allows a user to create an account,
# login and reset their password using an account recovery question system.

from Account import Account


def main():

    while True:
        my_account = Account()

        # Welcome statement.
        print("~ Welcome, please sign-in or create an account ~")
        option = input("Enter A to Sign-in | Enter B to Create Account | Enter C to Recover Account: ")
        # While the input is not equal to displayed options - loop.
        while option.upper() != "A" and option.upper() != "B" and option.upper() != "C":
            print("Incorrect input, please try again.")
            option = input("Enter A to Sign In | Enter B to Create Account | Enter C to Recover Account: ")
        # If input equals A, run the sign-in process
        if option.upper() == "A":
            print("Please enter your account details: ")
            username = input("Username: ").upper()
            password = input("Password: ").upper()
            my_account.verify_account_login(username, password)
            break
        # If input equals CUSTOMER, run the customer function.
        elif option.upper() == "B":
            username = input("Username: ").upper()
            password = input("Password: ").upper()
            accountRecoveryPassword = input("Account Recovery Password: ").upper()
            my_account.set_username(username)
            my_account.set_password(password)
            my_account.set_recovery_password(accountRecoveryPassword)
            my_account.verify_account_creation()
            continue
        elif option.upper() == "C":
            my_account.update_password()
            continue


main()
