# palindrome
sentence = """He met his mom at noon and she was watching an epsoide of the begninging of her Solos. Her tenet helped her to level up her stats. After that he went to kayak driving Civic Honda."""

def reverse_word (word):
    return word[::-1]

def is_palindrome(word):
    reversed_word = reverse_word(word.lower())
    if word.lower() == reversed_word:
        return True
    return False

def find_list_palindrome(string):
    import re
    words = re.sub(r'[^a-zA-Z ]', '', string.lower()).split()
    palindromes = []
    for word in words:
        if is_palindrome(word):
            palindromes.append(word)
    return palindromes

print(find_list_palindrome(sentence))

def find_number_of_palindromes(string):
    palindromes =find_list_palindrome(string)
    return len(palindromes)

print(find_number_of_palindromes(sentence))