

'''
    molto simili alle liste ma sono immutabili
'''
punto = (1.2,3.6)
print(F"la coordinata x del punto è {punto[0]}");

'''
    another example
'''


triangolo = [(1.5, 1.6), (1.7, 20), (4.2 , 5.0)]

area = 1/2 * abs(triangolo[0][0]*triangolo[1][1]+triangolo[1][0]*triangolo[2][0]+triangolo[1][0]*triangolo[2][1]-triangolo[2][0]*triangolo[1][1]-triangolo[2][1]*triangolo[0][0]-triangolo[1][0]*triangolo[1][1])
print(area)