"""
Word Occurrences
Estimate: 30 min
Actual:   25 min
"""

words_to_count = {}
max_length = 0

string = input("Text: ").lower()
words = string.split(" ")

for word in words:
    if word in words_to_count:
        words_to_count[word] += 1
    else:
        words_to_count[word] = 1
    if len(word) > max_length:
        max_length = len(word)

for word in sorted(words_to_count.keys()):
    print(f"{word:{max_length}}: {words_to_count[word]}")
