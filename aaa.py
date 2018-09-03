def a_add(x,y):
    s = x+y
    print(s)
a_add(3,2)

def b_max(x,y,z):
    max_num = x
    if y>max_num:
        max_num=y
        if z>max_num:
            max_num = z
    print(max_num)
b_max(6,30,29)
