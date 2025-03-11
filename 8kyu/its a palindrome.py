"""
Write a function that checks if a given string (case insensitive)
is a palindrome.

A palindrome is a word, number, phrase, or other sequence of symbols that
reads the same backwards as forwards, such as madam or racecar.
"""

def is_palindrome(s):
    if len(s) == 0:
        return True
    
    s_low = s.lower()
    left_counter = 0
    right_counter = len(s) - 1

    if s_low[right_counter] != s_low[left_counter]:
        return False

    while left_counter < right_counter:
        if s_low[left_counter] != s_low[right_counter]:
            return False
        left_counter += 1
        right_counter -= 1
    return True
