import re # regular expression module

""" logging is a better way to display messages to the user. It allows us to control the verbosity of
 the messages and the destination of the messages. """
from logging import info, INFO, basicConfig
basicConfig(level=INFO)
info("validating the email address..")

#take input from user when running validate.py
email = input("Enter your email (Bristol Bayhawks only only): ").strip() # strip method removes any leading or trailing whitespace, lower method converts the email to lowercase

# in regex, . is for anything so we have to use bckslash character as an escape character to treated the period as a literal period
pattern = r"^[\w\.-]+@(\w+\.)?bristolcc\.edu$" # r is for raw string, ^ is for start of string, . $ is for end of string

if re.search(pattern, email, re.IGNORECASE): # search function returns a match object if the pattern is found
    info(f"{email} appears to be a valid Bristol Community College email address.") # leverage formatted string to display the email variable
else:
    info(f"{email} is not affiliated with the Bayhawks.")

""" 
  # attempt 4 Matches .edu emails: ^[^@]+@[^@]+\.edu$ (start, allowed name characters, @, domain not @, .edu, end)
pattern = r"^[a-zA-Z0-9_]+@[^@]+\.edu$" """

""" Attempt #3
 # Regular expression to validate email address
pattern = r'^[\w\.-]+@bristolcc\.edu$' # r is for raw string, ^ is for start of string, $ is for end of string

if re.match(pattern, email): # match function returns a match object if the string matches the pattern
    info(f"{email} appears to be a valid bristolcc.edu email address.") # leverage formatted string to display the email variable
else:
    info(f"{email} does not appear to be an bristolcc.edu email address.") """

""" manual validation 2 
username, domain = email.split("@")
if username and domain.endswith("bristolcc.edu"):
    info(f"{email} appears to be a valid bristolcc.edu email address.")
else:
     info(f"{email} does not appear to be an bristolcc.edu email address.") """

""" first try
 if "@" in email and "." in email:
    info(f"{email} appears to be a valid email address.")
else: 
    info(f"{email} does not appear to be a valid email address.")
     """