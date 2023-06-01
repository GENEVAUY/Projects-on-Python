def get_unique_elements_f(lst):
    return list(set(lst))

lst = [100, 100, 100, 200, 200, 300, 400, 500, 500]
print(get_unique_elements_f(lst))

type (get_unique_elements_f(lst))

def count_case_f(string):
    uppercase_count = 0
    lowercase_count = 0

    for letter in string:
        if letter.isupper():
            uppercase_count += 1
        elif letter.islower():
            lowercase_count += 1

    return uppercase_count, lowercase_count

sentence = "I am starting to get very confused."
result = count_case_f(sentence)
print("Uppercase count:", result[0])
print("Lowercase count:", result[1])

import string

def remove_punctuation_f(sentence):
    change = str.maketrans("", "", string.punctuation)
    no_punctuation = sentence.translate(change)
    return no_punctuation

def word_count_f(sentence):
    words = sentence.split()
    word_count_f = len(words)
    return word_count_f

sentence = "I feel like I am losing my mind!!! Help!"
result = remove_punctuation_f(sentence)
count = word_count_f(result)
print (result)
print(count)