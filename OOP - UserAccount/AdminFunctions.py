import hashlib


class Admin:
    """Grant admin privileges to users"""

    def create_bin_file(self, string, filename):
        """Create a bin file to store encrypted strings"""
        userInput = string
        f = filename
        # Write to the .bin file using a try block.
        try:
            with open(f, "wb") as file:
                file.write(hashlib.sha512(userInput.encode('utf-8')).digest())
                file.close()
        except FileNotFoundError:
            print("File does not exist, please contact support.")
