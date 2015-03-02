def dy_dx(x,y):
    return float(x*y/2)

for x in range(-3,4):
    for y in range(-3,4):
        print (x, y, dy_dx(x,1.0))    
