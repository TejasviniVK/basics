
'''
1. Write a Python script to sort (ascending and descending) a dictionary by value.
'''

from collections import OrderedDict


def descending(d):
    dict={}
    d1 = sorted(d,key=d.get, reverse = True)
    for r in d:
        dict.update({r:d[r]})
    return dict



def ascending(d):
    dict10={}
    d1 = sorted(d,key=d.get, reverse = True)
    for r in d:
        dict10.update({r:d[r]})
    return dict10


def test_descending_ascending():
    assert {'e':23,'o':21,'u':54,'w':1} == descending({'w':1,'e':23,'o':21,'u':54})
    assert {'w':1,'u':54,'o':21,'e':23} == ascending({'w':1 ,'e':23,'o':21,'u':54})

'''

2. Write a Python script to add key to a dictionary.


Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}'''

def get_add_key(Dictionary):
    Dictionary[2] = 30
    return Dictionary

def test_add_key():
    assert {0:10,1:20,2:30} == get_add_key({0:10,1:20})
'''



3. Write a Python script to concatenate following dictionaries to create a new one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}'''

def concatenate(dict1,dict2,dict3):
    dict1.update(dict2)
    dict1.update(dict3)
    return dict1

def test_concatenate():
    assert {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} == concatenate({1:10,2:20},{3:30,4:40},{5:50,6:60})
'''


4. Write a Python script to check if a given key already exists in a dictionary.
'''
dict = {3:2,5:2,7:8}

def Exists(dict,key1):
    if key1 in dict.keys():
        return True


    else:
        return False

def test_Exists():
    assert (True) == Exists({3:2,5:2,7:8},3)


'''

5. Write a Python program to iterate over dictionaries using for loops.
'''
def Iterate(dict):
    dict11={}
    for key in dict:
        dict11.update({key:dict[key]})
    return dict11

def test_Iterate():
    assert {'a':1,'b':2,'c':3,'d':4} == Iterate({'a':1,'b':2,'c':3,'d':4})


'''


6. Write a Python script to generate and print a dictionary that contains number (between 1 and n) in the form (x, x*x).

Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}'''
def Square(n):
    dict={}
    for x in range(1,n+1):
        dict.update({x:x**2})
    return dict

def test_Square():
    assert ({1: 1, 2: 4, 3: 9, 4: 16, 5: 25}) == Square(5)
'''


7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.


Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}'''

def Square1():
    d={}
    for x in range(1,16):
        d.update({x:x**2})
    return d


def test_square1():
    assert ({1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}) == Square1()

#8. Write a Python script to merge two Python dictionaries.


#9. Write a Python program to iterate over dictionaries using for loops.

'''



10. Write a Python program to sum all the items in a dictionary.
'''
def sum1(d):
    return sum(d.values())

def test_sum1():
    assert(17) == sum1({'e':3, 'r':6,'g' :8})

'''


11. Write a Python program to multiply all the items in a dictionary.
'''
def Mul1(d):
    result=1
    for key in d:
        result=result*d[key]
    return result

def test_Mul1():
    assert (240) == Mul1({'t':5,'f':6,'r':8})
'''


12. Write a Python program to remove a key from a dictionary.

'''
def Remove(dict,key1):
    del dict[key1]
    return dict

def test_Remove():
    assert({1:2,3:4,4:5,5:6}) == Remove({1:2,2:3,3:4,4:5,5:6},2)

'''


13. Write a Python program to map two lists into a dictionary.
'''
def Map(keys,values):
    dictionary={}
    dictionary={key:value for key,value in zip(keys,values)}
    return dictionary

def test_Map():
    assert({1:3,2:4,3:5,4:6}) == Map([1,2,3,4],[3,4,5,6])


'''


14. Write a Python program to sort a dictionary by key. 
'''
def Sort1(mydict):
    dict={}
    for key in sorted(mydict.iterkeys()):
        dict.update({key : mydict[key]})

    return dict

def test_Sort1():
    assert({'d':3,'f':32,'g':65,'s':23}) == Sort1({'g':65,'d':3,'s':23,'f':32})

'''



15. Write a Python program to get the maximum and minimum value in a dictionary.
'''
def MaxMin(mydict):
    key_min = min(mydict.keys(),key=(lambda k: mydict[k]))
    key_max = max(mydict.keys(),key=(lambda k: mydict[k]))
    return mydict[key_max],mydict[key_min]

def test_MaxMin():
    assert(10,1) == MaxMin({2:3,5:2,3:1,8:10})
'''


16.
 Write a Python program to get a dictionary from an object's fields.
'''
def obj16():
    class Obj_test(object):

        def __init__(self):
            self.a=1
            self.b=2


    return Obj_test().__dict__

def test_obj16():
    assert {'a':1,'b':2} == obj16()


'''


17. Write a Python program to remove duplicates from Dictionary.
'''
def Duplicate(dict):
    # result={}
    # for key,value in dict.items():
    #     if key not in result.key():
    #         result[key] = value
    return dict

def test_Duplicate():
    assert({'e':34,'g':34,'f':32}) == Duplicate({'e':34,'g':23,'g':34,'f':32})

'''


18. Write a Python program to check a dictionary is empty or not.
   '''
def Empty(dict):
    if dict:
        return False

    else:
        True


def test_Empty():
    assert False == Empty({2:4,'i':5})
