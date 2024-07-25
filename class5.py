def maximum(array):
    remember = array[0]
    for i in array:
        if i > remember:
            remember = i
    return remember

def minimum(array):
    remember = array[0]
    for i in array:
        if i < remember:
            remember = i
    return remember 

def main():
    array = []
    function = input('What function would you like to use:')
    while True:
        num = input('Enter a number:')
        if num == 'q':
            break
        else:
            array.append(int(num))
    
    if function == 'max':
        print(maximum(array))
    elif function == 'min':
        print(minimum(array))


main()
