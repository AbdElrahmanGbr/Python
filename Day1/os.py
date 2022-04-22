#!/usr/bin/env python3

# Numbers

# x = 2
# y = 3
# print(x)
# print(y)
# # z = x 
# # x = y
# # y = z
# x, y = y, x 
# print('---------')
# print(x)
# print(y)
# z = x ** y # ** power / expo
# z = pow(x, y)
# x +=1
# print(x)
# z = abs(2) #absolute
# z = round(x) #return round

# print(z)

# Strings
# s = 'hello'

# print(len(s))
# print(s[-5])
# print(s.lower())
# print(s.upper())
# print(s.capitalize())
# print(s.isalpha())
# print(s.isdigit())
# print(s.isalnum())
# x = '5'
# y = int(x)
# y = 5

# i = input("enter your age")
# i = eval(i)
# print(i)

# x = 'hi'
# y = 'there'
# print (x + y)

# List

# l = [1, 2, 'c', "hi", [3, '5']]

# print(l)

# l = [1l = [1, 1, 5, 9, 2, 4]
# l.remove(1)
# print(l)t(min(l))
# # print (l)
# # l.reverse() # reverse list items order
# # print (l)
# # print(l)
# l2.sort()
# print(l2)

# l = [1, 1, 5, 9, 2, 4]
# l.remove(1)
# print(l)
# l2 = ['one', 'two']
# l.extend(l2)
# print (l)
# l.append(7)
# l.insert(1, 8)
# print(l)
# p = l.pop()
# print(p)
# print(l)


# r = range(1, 11, 1)
# l = list(r)
# t = tuple(r)
# print(l)
# print(t)

# import random

# r = random.randrange(1, 6, 1)
# print(r)

# Tuple immut

# t = (1, 2, 'o')

# dictionary - name value pair (key = immut)

# d = {'one': 1 , 'two': 2 }

# d2 = {'three': 3}

# d.update(d2)

# print(d)
# d.clear()
# print(d)
# print(d.keys() )
# print(d.values() )
# print(d.items() )

# users = { ('mo', 123): 'Welcome Mr Mohamed' , ('ah', 456) :'Welcome Mr Ahmed'  }

# print(users[('mo', 123)])

# d['one'] = 'one value'
# print(d['one'])

# flow control

# === , ++ are not python supported
# x = '9' 
# if x === 9:
#     print("x == 9")
# elif x == 3:
#     print("x == 3")
# else:
#     print("else")


# loop

# l = [1, 2, 3]

# for item in l:
#     print(item)

# x = 5
# while x > 0:  
#     if(x == 3):
#         pass # pass: do nothing keyword, continue, break
#     print(x)
#     x -=1


#  functions

# def myFunc(x , y = 1, z = 6 ):
#     print('x: ' , x)
#     print ('y: ' , y)
#     print ('z: ' , z)


# myFunc(1,2)


# File IO

# f = open('alex.txt', 'w')
# f.write("this is some string ")
# f.close()

# f = open('alex.txt', 'r')
# c = f.read()
# print(c)
# f.close()

# f = open('alex.txt', 'a')
# f.write(" this is another  string ")
# f.close()

# l = [1,2,0, False, '']
# v = all(l)
# any(l)
# print(v)

# l = 'hello'
# v = 'z' in l
# print (v)
# print(l[0:3])

d = {'one': 1, 'two': 2}

for k,v in d.items():
    print(k, v)
