"""
Sean Killian
Thursday @ 2pm
"""

def process_user_contacts(user_input):
    user_contacts = {}

    pairs = user_input.split()
    # Put word pairs into a dictionary
    for pair in pairs:
        name, phone_number = pair.split(',')
        user_contacts[name] = phone_number

    # Get contact name from input, output contact's phone number
    contact_name = input("Enter the contact name: ")
    
    print(user_contacts[contact_name])

if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input)
