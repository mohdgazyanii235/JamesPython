question = [1, 2, 5, 9, 13, 18, 27, 28, 31]
num = int(input('Enter a number: '))

def numberExists(question, num):
    i = 0
    found = False
    while i < len(question):
        if num == question[i]:
            found = True
        i += 1 
    
    return found


answer = numberExists(question, num)
print(answer)
