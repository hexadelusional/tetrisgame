import Functions as f

####################Beginner####################
#Exercise 1
'''
if __name__ == '__main__':
    L = [1,2,3]
    add_list(L, 4)
    print(L)
'''
#Exercise 2
#yeah(1,10,2)

#Exercise 3
'''
if __name__ == '__main__':
    val = int(input("Enter an integer: "))
    if even(val) :
        print("{} is an even number".format(val))
    else:
        print("{} is an odd number".format(val))
'''
####################Intermediate####################

#Exercise 1
##2)
'''
if __name__ == '__main__':
    a, b, c = int(input()), int(input()), int(input())
    print(maximum(a, b, c))
'''

#Exercise 2
##2)
'''
if __name__ == '__main__':
    a = int(input())
    print(prime(a))
'''

#Exercise 3
##2)
'''
if __name__ == '__main__':
    l = [i**2 for i in range(8)]
    print(sum(l))
'''

#Exercise 4
##2)
'''
if __name__ == '__main__':
    l = [i**2 for i in range(8)]
    print(f.position(l,4))
'''

#Exercise 5
##2)
'''
if __name__ == '__main__':
    l = [2,42,97,66,21,21,87,2,42]
    print(f.unique(l))
'''

#Exercise 6
##2)
'''
if __name__ == '__main__':
    s = 'traverser'
    print(f.reverse(s))
'''
#Exercise 7
##2)
'''
if __name__ == '__main__':
    s = 'traverser'
    print(f.vowels(s))
'''

#Exercise 8
##2)
'''
if __name__ == '__main__':
    f1, f2 = 'wow.txt', 'yep.txt'
    f.write(f1,f2)
'''

#Exercise 9
##2)
'''
if __name__ == '__main__':
    M = [[31,31,38,1209],
         [212,9302,310],
         [301,382,3766,31],
         [3,378,3939,1000,38]]
    print(f.double(M))
'''

#Exercise 10
##2)
'''
if __name__ == '__main__':
    L1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    L2 = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
          'November', 'December']
    print(f.altern(L1,L2))
'''
#Exercise 11
##2)
'''
if __name__ == '__main__':
    n = int(input("Enter an int))
    f.draw_dots(n)
'''

####################Advanced####################

#Exercise 1
##4)
'''
if __name__ == '__main__':
    L = f.fill_list(int(input("Enter an int")))
    f.print_list(L)
    print('average :', f.average_list(L))
'''

#Exercise 2
##2)
'''
if __name__ == '__main__':
    s = "The quick brown fox jumps over the lazy dog"
    print(s, f.pangram(s))
    t = "absdefghijklmnopq"
    print(t, f.pangram(t))
'''

#Exercise 3
##2)
'''
if __name__ == '__main__':
    s = 'green-red-yellow-black-white'
    f.hyphen(s)
'''

#Exercise 4
##2)
'''
if __name__ == '__main__':
    print(f.volboite(5.2))
    print(f.volboite(5.2,3))
    print(f.volboite(5.2,3,7.4))
'''
#Exercise 5
##4)
'''
if __name__ == '__main__':
    s = input('Enter a string :')
    print(f.palindrome(s))
'''

#Exercice 6
##4)
if __name__ == '__main__':
    l = [31,9,31,90,32,890,31,8372,23,3]
    print(f.sort_list(l))