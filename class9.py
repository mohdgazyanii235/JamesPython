question = [1, 2, 5, 9, 13, 18, 27, 28, 31]
num = int(input('Enter a umber: '))

def numberExists(question, num):
    i = 0
    x = len(question)
    while i < x:
        if num == question[i]:
            return True
        i += 1 
    return False
answer = numberExists(question, num)
print(answer)




    # check if num exists in question?
    # return true if it exists, return false if it doesn't exist.
