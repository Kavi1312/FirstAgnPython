#Python script to check the password strength. 

def main():
    while True:
        # Take password input from the user
        password = input("Please enter your password: ")
        
        # Check the strength of the password
        if check_password_strength (password):
            print("Success!Password is strong.")
            
            # Verification process
            attempts = 0  # Initialize attempt counter
            while attempts < 3:
                pwd_validation = input("Please re-enter your password for verification: ")
                
                if password == pwd_validation :
                    print("Congrats! Both passwords match and it is Set.")
                    return  # Exit the function after success
                else:
                    attempts += 1
                    print(f"The passwords do not match. You have {3 - attempts} attempts left.\n")
            
            # If the user fails to verify within 3 attempts, reset the process
            print("Sorry!You have exceeded the max number of attempts. Please enter a New Password.\n")
        else:
            print("Sorry!Given Passwordis weak, Please try again.\n")

import re
# re is a regular expression , upon patterns  re helps to provide support to validating input string format, text pattern search or parsing the data

def check_password_strength (password: str) -> bool:
    approved_special_characters = "!@#$%^&*(),.?\":{}|<>"

    # Length of the password is to be checked.
    if len(password) < 8:
        print("Password is too short.")
        return False

        # Password should contain atleast one Alphabetical Character , check whether upper and lower case in given.
    if not re.search(r'[A-Z]', password):
        print("uppercase letter is missing in the given password.")  #checking for upper case
        return False
    
    if not re.search(r'[a-z]', password):
        print("Lowercase letter is mission in the given password.")  #checking for lower case
        return False
    
    # Check whether user is given atleast one numerical digit.
    if not re.search(r'[0-9]', password):
        print("Numerical digit is missing in the given Password.")
        return False
    
    # Check whether user is given atleast one special Character.
    if not re.search(r'[!@#$%^&*(),.?"_:{}|<>]', password):
        print("Special character not found in the given password.")
        return False

    if not re.search(r'[!@#$%^&*(),.?"_:{}|<>]', password):  
        print("Special character not found in the given password.")
        return False

    # Check if all special characters are approved
    for char in re.findall(r'[^\w\s]', password):
       if char not in approved_special_characters:
            print(f"Provided special character '{char}' is not valid.")
            print(f"Please use only the following special characters: {approved_special_characters}")
            return False
    
    # Return the value true if it pass through all above check.
    return True

if __name__ == "__main__":
    main()