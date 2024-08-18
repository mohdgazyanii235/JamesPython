def pythagorous_theorem(a,b):
    c_squared = a**2 + b**2
    c = c_squared**0.5
    return c



def euclidean_distance(x1,x2,y1,y2):
    dx = x2 - x1
    dy = y2 - y1
    c = pythagorous_theorem(dx,dy)
    return c

x1 = int(input('Enter you first x value:'))
x2 = int(input('Enter you second x value:'))
y1 = int(input('Enter you first y value:'))
y2 = int(input('Enter you second y value:'))
answer = euclidean_distance(x1,x2,y1,y2)
print(answer)