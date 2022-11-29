"""
CP1404 Prac 10
Wikipedia, API & Python Library
"""

import wikipedia

user_input = input("Title or search page: ").title()
while user_input != "":
    try:
        print(wikipedia.summary(user_input))
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    user_input = input("Title or search page: ").title()
