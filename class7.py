def colour_checker(colour):
    match colour:
        case 'blue': return 'You like blue'
        case 'red': return 'You like red'
        case 'green': return 'You like green'
        case _: return 'You like nothing'
colour  = input("What is your favourite colour: ")
print(colour_checker(colour))

#CHALLENGE

def factorial(user):
    total = 1
    while user > 0:
        total *= user
        user -= 1
    return total

n = int(input('Enter the number: '))
answer = factorial(n)
print(answer)

def is_palindrome(word):
    reverse = ''
    i = len(word) - 1
    while i > -1:
        a = word[i]
        reverse += a
        i -= 1
    if reverse == word:
        return True
    else:
        return False

word = input('Enter a word: ')
answer = is_palindrome(word)
print(answer)

def word_counter(sentence):
    counter = 1
    for i in sentence:
        if i == ' ':
            counter += 1
    return counter

sentence = input('Enter a sentence: ')
answer = word_counter(sentence)
print(answer)