import re, hashlib, binascii, os

fileName = "StoredPW.txt"

def hash_password(x):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', x.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')    

def verify_password(stored_password, x):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  x.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password
    
        
def pLength(x): ##Check the length
    if 6 > len(x):
        return False
    if 16 < len(x):
        return False
    else:
        return True
    
def noSpec(x): ##Check for at least one special character
    if re.search(r"[$#@]", x) is None:
        return False
    else:
        return True
    
def noNum(x): ##Check for at least one number
    if re.search(r"\d", x) is None:
        return False
    else:
        return True
    
def noLower(x): ##Check for at least one lowercase letter
    if re.search(r"[a-z]", x) is None:
        return False
    else:
        return True
    
def noUpper(x): ##Check for at least one uppercase letter
    if re.search(r"[A-Z]", x) is None:
        return False
    else:
        return True

def NotValid(x): ##Establishing validity for loop purposes
    if pLength(x) is False:
        return True
    elif noNum(x) is False:
        return True
    elif noSpec(x) is False:
        return True
    elif noLower(x) is False:
        return True
    elif noUpper(x) is False:
        return True
    else:
        return False
    
def pass_Validate(x): ##Defining the validate function    
    if pLength(x) is False:
        print("Password must be between 6 and 16 characters long. ")
        return False
    elif noNum(x) is False or noSpec(x) is False or noLower(x) is False or noUpper(x) is False:
        print("Password did not meet requirements.")
        return False
    else:
        print("Password validated successfully. ")
        return True

def check_pw(x):
    file = open(fileName, 'r')
    stored_pass = file.read()
    verify_password(stored_pass, x)
    if verify_password(stored_pass, x) == True:       
        return True
    else:        
        return False

def save_pw(x):
    pw_Hash = hash_password(x)    
    file = open(fileName, 'w')
    file.write(pw_Hash)
    file.close()
    print("Password saved successfully")
        
def main(): ##Defining the main function    
    newPW = input("Are you entering a new password? ")
    if newPW == 'y' or newPW == 'Y':
        print("Passwords must contain 1 ea of the following: a-z, A-Z, 0-9, $#@")
        pWord = input("Enter your password: ")
        NotValid(pWord)
        if NotValid(pWord) == True:
            print("Something is wrong. ")
            pass_Validate(pWord)
        else:
            pass_Validate(pWord)
            save_pw(pWord)
        while NotValid(pWord) == True:
            pWord = input("Please re-enter your password: ")
            pass_Validate(pWord)
    else:
        print("Passwords must contain 1 ea of the following: a-z, A-Z, 0-9, $#@")
        pWord = input("Enter your password: ")
        NotValid(pWord)
        if NotValid(pWord) == True:
            print("Something is wrong. ")
        else:
            pass_Validate(pWord)
            check_pw(pWord)
            if check_pw(pWord) == True:
                print("Passwords match! ")
            if check_pw(pWord) == False:
                print("Passwords do not match! ")
            while check_pw(pWord) == False:
                pWord = input("Please re-enter your password: ")
                pass_Validate(pWord)
                check_pw(pWord)
                if check_pw(pWord) == True:
                    print("Passwords match! ")
                if check_pw(pWord) == False:
                    print("Passwords do not match! ")
        while NotValid(pWord) == True:
            pWord = input("Please re-enter your password: ")
            pass_Validate(pWord)        
    
main() ##Calling the main function to run the program
