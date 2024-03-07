"""
Sean Killian
Thursday @ 2pm
"""

def check_palindrome(user_input):
 #type your code here
    word_without_spaces = user_input.replace(" ", "")

    if word_without_spaces == word_without_spaces[::-1]:
        print(f"palindrome: {user_input}")
    else:
        print(f"not a palindrome: {user_input}")


if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)
