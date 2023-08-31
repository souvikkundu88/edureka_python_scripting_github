'''
case study 2 module 2 sequences and file operations

Domain – Telecom
focus – Optimization
Business challenge/requirement
LifeTel Telecom is the latest entrant in the highly competitive Telecom market of
Singapore. It issues SIM to the verified users. Till now verification was manual
through the photocopy of approved id card document. However government has
recently introduced Social ID called Reference ID which is mapped to fingerprint of
user. LifeTel should now verify user against the fingerprint and Reference ID
Key issues
Build a system where when user enters Reference ID it is encrypted, so that hackers
cannot view the mapping of Reference ID and finger print
Considerations
System should be secure
Data volume
- NA
Additional information
- NA
Business benefits
Company will be able to quickly issue SIM to user and expected gain in volume is
approximately 10 times as the manual process of verification is replaced with secure
automated system
Approach to Solve
You have to use fundamentals of Python taught in module 2
1. Read the input from command line – Reference ID
2. Check for validity – it should be 12 digits and allows on number and alphabet
'''

import re

def encrypt_reference_id(reference_id):
    # Implement the encryption logic here
    # For demonstration purposes, let's assume simple hashing
    encrypted_id = hash(reference_id)
    return encrypted_id

def verify_reference_id(reference_id):
    # Check for validity using regular expression
    if re.match(r'^[0-9a-zA-Z]{12}$', reference_id):
        return True
    return False

if __name__ == "__main__":
    reference_id = input("Enter the Reference ID: ")

    if verify_reference_id(reference_id):
        encrypted_id = encrypt_reference_id(reference_id)
        print("Reference ID encrypted:", encrypted_id)
    else:
        print("Invalid Reference ID. It should be 12 digits and allow numbers and alphabets only.")
