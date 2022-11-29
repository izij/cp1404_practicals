"""
CP1404 Prac 10
Wikipedia, API & Python Library
"""

import wikipedia

user_input = input("Title or search page: ").title()
while user_input != "":
    try:
        wiki_page = wikipedia.page(user_input, auto_suggest=False)
        print(wiki_page.title)
        print(wikipedia.summary(user_input))
        print(wiki_page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    user_input = input("Title or search page: ").title()
