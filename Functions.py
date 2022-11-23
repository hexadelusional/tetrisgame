from math import sqrt
import turtle
import random
####################Beginner####################
#Exercise 1
'''
    a) It will return 25
    b) Error
'''
def add_list(l, val):
    l1 = l
    l1.append(val)
    return l1
'''
    c) 3
       4
       5
       6
       7
       8
       9
       10
'''
#Exercise 2
def yeah(deb : int ,fin : int ,step : int):
    assert fin >= deb, "Fin should be superior to deb"
    for i in range(deb, fin, step):
        print(i)

#Exercise 3
def even(x):
    if x%2 == 0:
        return True
    else:
        return False

####################Intermediate####################
#Exercise 1
##1)
def maximum(a:int,b:int,c:int):
    a = max(a,b)
    return max(a,c)

#Exercise 2
##1)
def prime(n):
    rep = True
    i = 2
    while (i<= sqrt(n)) and rep:
        if n%i == 0:
            rep = False
        else:
            i += 1
    return rep

#Exercise 3
##1)
def sum(L):
    s = 0
    for i in L:
        s += i
    return s

#Exercise 4
##1)
def position(l: list,val : int):
    ix = -1
    i = 0
    while (i<len(l)) and (ix<0):
        if l[i] == val:
            ix = i
        else :
            i += 1
    return ix

#Exercise 5
##1)
def unique(l):
    L = []
    for value in l:
        if value not in L :
            L.append(value)
    return L

#Exercise 6
##1)
def reverse(s):
    res = ""
    for character in s:
        res = character + res
    return res

#Exercise 7
##1)
def vowels(s):
    res = 0
    vow = ['a','e','u','i','o','y']
    for character in s:
        if character in vow:
            res += 1
    return res

#Exercise 8
##1)
def write(f1 :str,f2 :str):
    with open(f1, "r") as a, open(f2,"a") as b:
        content = a.read()
        b.write(content)

#Exercise 9
##1)
def double(M):
    N = M
    for i in range(0,len(N),2):
        for j in range(len(N[i])):
            N[i][j] *= 2
    return N

#Exercise 10
##1)
def altern(l1,l2):
    l3 = []
    for i in range(max(len(l1),len(l2))):
        if i < len(l2):
            l3.append(l2[i])
        if i < len(l1):
            l3.append(l1[i])
    return l3

#Exercise 11
##1)
def draw_dots(n):
    step = 360//n
    haha = turtle.Turtle()
    haha.up()
    for i in range(360):
        haha.forward(1)
        haha.right(1)
        if i%step == 0:
            haha.dot(5)

####################Advanced####################

#Exercise 1
##1)
def fill_list(n:int):
    l = []
    for i in range(n):
        l.append(round(random.random(),2))
    return l
##2)
def average_list(l :list):
    sum = 0
    for val in l:
        sum+= val
    return sum/len(l)
##3)
def print_list(l :list):
    for val in l:
        print(val, end =" ")

#Exercise 2
##1)
def pangram(s):
    w = [chr(i) for i in range(ord('A'),ord('Z')+1)]
    res = True
    i = 0
    while (i<len(w)) and res:
        if (w[i] not in s) and (chr(ord(w[i])+32) not in s):
            res = False
        else:
            i+=1
    return res

#Exercise 3
##1)
def hyphen(s):
    l = s.split('-')
    new = [l[0]]
    for i in range(1,len(l)):
        j = 0
        while j<len(new) and (new[j] < l[i]):
            j += 1
        new.insert(j,l[i])
    for val in new:
        print(val,end='-')

#Exercise 4
##1)
def volboite(a,b=0,c=0):
    if b == c == 0:
        return a**3
    elif c == 0:
        return 2*a*b
    else:
        return a*b*c

#Exercise 5
##1)
#use reverse function
##2)
def compare(s1,s2):
    return (s1==s2)
##3)
def palindrome(s):
    return (compare(s, reverse(s)))

#Exercise 6
##1)
def pos_max(l, bound_up):
    pmax = 0
    for i in range(1,bound_up+1):
        if l[i] > l[pmax]:
            pmax = i
    return pmax
##2)
def swap_list(l, i, j):
    h = l
    h[i],h[j] = h[j],h[i]
    return h
##3)
def sort_list(l):
    h = l
    for i in range(len(h)-1,1,-1):
        index = pos_max(h,i)
        if h[index] != h[i] :
            h = swap_list(h,i,index)
    return l


