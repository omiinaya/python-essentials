#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import platform
from decimal import *

version = platform.python_version()
text = 'This is python version {}'.format(version)
words = ['one', 'two', 'three', 'four', 'five']


def main():
    message()


def message():
    print('Hello, World.')
    print(f'{text}')
    if False:  # this is a comment.
        print('line 3')
    else:
        print('not true')
        test()


def test():
    x = 42
    y = 73

    if x < y:
        print(f'x < y: x is {x} and y is {y}')
        test2()
        test3()
        test5()
        test6()
        test7()
        test8()
        test9()
        test10()
        test11()
        test12()
        test13()
        test14()
        #test15()
        test16()
        test18()
        test20()
        test22()
        test24()
        test25()
        test26()
        test27()
        test28()
        test29()


def test2(num=0):  #passing default value of 0 to n
    while (num <= 3):
        print(words[num], end=' ', flush=True)
        num += 1


def test3():
    for i in words:
        print(i)


def test4(n):
    print(n)
    return n * 2


def test5():
    x = test4(42)
    print(x)


class Duck:
    sound = 'Quaaack!'
    walking = 'Walks like a duck.'

    def quack(self):
        print(self.sound)

    def walk(self):
        print(self.walking)


def test6():
    donald = Duck()
    donald.quack()
    donald.walk()
    print(type(donald.quack))


def test7():
    x = 'seven "{1:<9}" "{0:>9}"'.format(8, 9)
    y = 'seven "{1:<9}" "{0}"'.format(8, 9)
    print('x is {}'.format(x))
    print('y is {}'.format(y))
    print(type(x))


def test8():
    a = Decimal('0.10')
    b = Decimal('0.30')
    x = a + a + a - b
    print('x is {}'.format(x))
    print(type(x))


def test9():
    x = None  #None evaluates to false, so does 0 and ''
    if x:
        print(True)
    else:
        print(False)


def test10():
    x = [1, 2, 3, 4, 5]  #list instead of array?
    #x = (1, 2, 3, 4, 5)    #same thing but tuple are immutable
    #x = range(5, 10, 3)    #starts at 5, runs 10 times, increments by 3
    #x = list(range(5))     #transforms a tuple into a list (mutable array).
    x[2] = 42
    for i in x:
        print(f'i is {i}')


def test11():
    x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
    print(x["three"])
    print(f'test: {x["three"]}')
    for k, v in x.items():
        print(f'k: {k}, v: {v}')


def test12():
    x = (1, 'two', 3.0, [4, 'four'], 5)
    y = [1, 'two', 3.0, [4, 'four'], 5]
    print(f'{x}')
    print(type(x))
    print(type(x[1]))
    print(id(x))
    print(id(y))
    print(id(x[0]))
    print(id(y[0]))

    if x[0] is y[0]:
        print('yep')
        if isinstance(x, tuple):
            print('yes 2')
        elif isinstance(x, list):
            print('no 2')
    else:
        print('nope')


def test13():
    x = 5
    y = 3
    z = x + y
    print(f'{z}')
    print(f'{-z}')
    print(f'{+-z}')  #still negative?


def test14():
    x = True
    y = False
    z = True
    And = x and y
    Or = x or y
    Is = x is z
    if And:
        print(And)
    if Or:
        print(Or)
    if Is:
        print(Is)


def test15():
    secret = 'x'
    pw = ''
    auth = False
    count = 0
    max_attempt = 5

    while pw != secret:
        count += 1
        if count > max_attempt: break
        if count == 3: continue  #skips 3rd attempt1

        pw = input(f"{count}: What is the secret word?")
    else:
        auth = True

    print("Authorized" if auth else "Calling the FBI...")


def test16():
    animals = ('bear', 'bunny', 'dog', 'cat', 'velociraptor')

    for pet in animals:
        if pet == 'dog':
            continue
        print(pet)


def test17(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print('Meowxd.')


def test18():
    x = ('a', 'b', 'c', 'd')
    print(x)
    test17(*x)


def test19(**kwargs):
    if len(kwargs):
        for s in kwargs:
            print(f'{s} says {kwargs[s]}')
    else:
        print('Meowxd.')


def test20():
    x = dict(Buffy='meow', Zilla='grr', Angel='rawr')
    test19(**x)


def test21(o):
    for i in o:
        print(i, end=' ', flush=True)
    print()


def test22():
    game = ['r', 'p', 's', 'l']
    print(', '.join(game))
    print('r' in game)  #is element in array
    i = game.index('p')  #equivalent of indexOf()
    game.append('computer')  #equivalent of array.push
    #game.remove('computer')  #removes element that matches string
    #game.pop  #removes item from end of list. same as js.
    #game.pop(3) #removes item by index.
    #del game[1]
    #del game [1, 3]
    #del game [1, 5, 2] #start, end and step
    #game.insert(0, 'computer')  #push at specific index
    test21(game)


#items gives you pairs, keys give you keys and values give you values.

#set is a list that does not allow duplicate elements.

#sort is the same as javascript

#round() rounds

#from math import pi = pi


def test23(o):
    print('{', end='')
    for x in o:
        print(x, end='')
    print('}')


def test24():
    a = set('klk manin hoy hay coro')
    b = set('plomo hoy es viernes')
    test23(sorted(a - b))  #filter b from a
    #test23(sorted(a | b)) #all items that exist in one or the other.
    #test23(sorted(a ^ b)) #all items in one or the other, but not both.
    #test23(sorted(a & b)) #all items that exist in both of the sets.


class Duck2:
    sound = 'Quack quak.'
    movement = 'Walks like a duck.'

    def quack(self):
        print(self.sound)

    def move(self):
        print(self.movement)


def test25():
    donald = Duck2()
    donald.quack()
    donald.move()


class Animal:

    #def __init__(self, type, name, sound):
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'Kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'Fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'Rawr'

    def type(self, t=None):
        if t: self._type = t
        return self._type

    def name(self, n=None):
        if n: self._name = n
        return self._name

    def sound(self, s=None):
        if s: self._sound = s
        return self._sound

    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}"'


def test26():
    a0 = Animal()
    a1 = Animal(type='Duck', name='Donald', sound='Quack')
    x = dict(type='Velociraptor', name='Veronica', sound='Hello')
    y = {'type': 'Velociraptor', 'name': 'Veronica', 'sound': 'Hello'}
    z = {'type': 'Velociraptor', 'sound': 'Hello', 'name': 'Veronica'}
    a1.sound('Bark')
    print(a0)
    print(a1)
    print(Animal(**x))
    print(Animal(**y))
    print(Animal(**z))
    print(Animal(type='Velociraptor', name='Veronica', sound='Hello'))


class Animal2:

    #def __init__(self, type, name, sound):
    def __init__(self, **kwargs):
        if 'type' in kwargs: self._type = kwargs['type']
        if 'name' in kwargs: self._name = kwargs['name']
        if 'sound' in kwargs: self._sound = kwargs['sound']

    def type(self, t=None):
        if t: self._type = t
        try:
            return self._type
        except AttributeError:
            return None

    def name(self, n=None):
        if n: self._name = n
        try:
            return self._name
        except AttributeError:
            return None

    def sound(self, s=None):
        if s: self._sound = s
        try:
            return self._sound
        except AttributeError:
            return None

    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}"'


class Cow(Animal):

    def __init__(self, **kwargs):
        self._type = 'kcow'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs)


class Kitten(Animal):

    def __init__(self, **kwargs):
        self._type = 'kitten'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs)

    def kill(self, s):
        print(f'{self.name()} will now kill all {s}')


def test27():
    a0 = Kitten(name='fluffy', sound='rawr')
    a1 = Cow(name='donald', sound='quack')
    print(a0)
    print(a1)
    a0.kill('humans')


class RevStr(str):

    def __str__(self):
        return self[::-1]  #wtf reverses a string


def test28():
    x = 'Hello, world.'
    print(RevStr(x))


import sys


def test29():
    try:
        #x = int('foo')
        #x = int(5)
        x = int(5 / 0)
    except ValueError:
        print('I caught a ValueError')
    except ZeroDivisionError:
        print("don't divide by zero")
    except:
        print(f'Unknown error. {sys.exec_info()[1]}')
    else:  #executes if no error
        print('good job!')


if __name__ == '__main__':
    main()
