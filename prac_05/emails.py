"""
Emails
Estimate: 20 minutes

Actual:40 minutes
"""

from operator import itemgetter

email_to_name = {}

email = input("Enter email: ")
while email != "":
    name = email.split("@")[0]
    print(f"is {name}? (y/n)")
    choice = input().lower()
    if choice == "y" or choice == "":
        email_to_name[email] = name
    else:
        name = input("Enter new name: ")
        email_to_name[email] = name
    email = input("Enter new email: ")

for name, email in email_to_name.items():
    print(f"{name}({email})")