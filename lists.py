"""
1. Write a Python program to sum all the items in a list.

          a = [1,4,23,5,6,5]"""



def Sum1(a):
    b = sum(a)
    return b

def test_Sum1():
    assert (9) == Sum1([1,2,3,3])


"""
2. Write a Python program to multiplies all the items in a list.

                a = [4,3,2,1,3]"""

def Mul1(a):
    pro=1
    for i in a:
        pro = pro * i
    return pro

def test_Mul():
    assert(30) == Mul1([2,3,5])

"""3. Write a Python program to get the largestand smallest number from a list."""
'''
                        a= [2,1,4,5,6,3,53]
                        a.sort
                        small = a[0]
                        large = a[6]
'''
def smalar(a):
    a.sort()
    return a[0],a[6]

def test_smalar():
    assert(1,53)==smalar([2,1,4,5,6,3,53])


"""4. Write a Python program to find given string is a palindrome or not
   ex:madam returns True
      Hello returns False"""
def Palindrome(S):
    m = S[::-1]
    if m == S:
        return True
    else:
        return False

def test_Palindrome():
    assert(True) ==  Palindrome('madam')
    assert(False) == Palindrome('Karthik')
    assert(False) == Palindrome('Aditya')



 
"""5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2"""

def String(list1):
    ctr=0
    for word in list1:
        if len(word) > 1 and word[0] == word[-1]:
            ctr+=1
    return ctr

def test_String():
    assert(2) ==  String(['abc', 'xyz', 'aba', '1221'])
    assert(3) ==  String(['abc', 'xyz', 'aba', '1221','avgvga'])


"""6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]"""

def last(a):
    return a[-1]
def Sort_list(T):
     return sorted(T, key=last)


def test_Sort_list():
    assert ( [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]) == Sort_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])




"""7. Write a Python program to remove duplicates from a list. """
def Duplicate(L):
    L1=[]
    for i in L:
        if i not in L1:
            L1.append(i)
    return L1

def test_Duplicate():
    assert([1,2,3,4,5,6]) == Duplicate([1,2,3,3,4,5,6])



"""8. Write a Python program to check a list is empty or not. """
def Empty(L):
    if L:
        return False
    else:
        return True

def test_Empty():
    assert (False) == Empty([1,2,3,4])
    assert (True) == Empty([])
    assert (True) == Empty(None)



"""9. Write a Python program to clone or copy a list."""
def Copy(L):
    L1=[]
    for i in L:
        L1.append(i)
    return L1

def test_Copy():
    assert ([1,2,3,4,5]) == Copy([1,2,3,4,5])


"""10. Write a Python program to find the list of words that are longer than n from a given string.
    ex:str="The quick brown fox jumps over the lazy dog"
    n=3
    output=[quick,brown,jumps,over,dog]"""

def Wordss(str1,n):
    word_len = []
    txt = str1.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len

def test_Wordss():
    assert(['heylo','byyeee']) == Wordss("heylo hiee byee byyeee red bhy  ",4)




"""11. Write a Python function that takes two lists and returns True if they have at least one common member. """

def Common(a,b):
    for i in a:
        for j in b:
            if i==j:
                return True
    return False


def test_Common():
    assert(True) == Common([1,2,3],[7,8,2])
    assert(True) == Common([1,2,3],[7,2,5])
    assert (False) == Common([1,2,3],[4,5,6])


"""12. Write a Python program to print a specified list after removing the 0th, 2nd, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']"""

def Specific(T1):
    T1 = [x for (i,x) in enumerate(T1) if i not in (0,2,4,5)]
    return T1

def test_Specific():
    assert(['Green', 'Black']) == Specific(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'])



'''13.given string as input.remove all non-alphabets in a string
   ex:str="ab$23#44"
   output: "ab2344"  '''

def Non_alpha(str):
    str1 = ''.join(e for e in str if e.isalnum())
    return str1

def test_Non_alpha():
    assert ("ab2344") == Non_alpha("ab$23#44")



'''14. Write a Python program to print the numbers of a specified list after removing even numbers from it.'''

def Even(L):
    L1=[]
    for i in L:
        if i%2==1:
            L1.append(i)
    return L1

def test_Even():
    assert([1,3,5]) == Even([1,2,3,4,5,6])


'''15. Write a Python program to shuffle and print a specified list. '''

import random

def Shuffle(L):
    L1=random.shuffle(L)
    if L1!=L:
        return True
    return False


def test_Shuffle():
    assert True == Shuffle([1,2,3,4,5,8])




'''16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

def printValues():
	l = list()
	for i in range(1,31):
		l.append(i**2)
	return(l[:5])
	return(l[-5:])'''



def Square_first_Last():
    L1=list()
    for i in range(1,31):
        L1.append(i**2)
    L2=L1[:5]
    L3=L1[-5:]
    L2.extend(L3)
    return L2



def test_Square_first_last():
    assert([1,4,9,16,25,676,729,784,841,900]) == Square_first_Last()



'''17. Write a Python program to generate and print a list except the first 5 elements, where the values are square of numbers between 1 and 15 (both included).

def printValues():
	l = list()
	for i in range(1,21):
		l.append(i**2)
	print(l[5:])

printValues()'''

def Last5():
    l=list()
    for i in range(1,16):
        l.append(i**2)
    return l[5:]

def test_Last5():
    assert ([36,49,64,81,100,121,144,169,196,225]) == Last5()



'''18. Write a Python program to generate all permutations of a list in Python. '''

import itertools

def Permutations(L):
    L1=list(itertools.permutations(L))
    return L1

def test_Permutations():
    assert ([(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]) == Permutations([1,2,3])



'''19. Write a Python program to get the difference between the two lists. '''

def Diff(L1,L2):
    L3=[]
    L3=set(L1)-set(L2)
    L3=list(L3)
    return L3

def test_Diff():
    assert([1]) == Diff([1,2,3],[7,10,2,3])

'''20. Write a Python program access the index of a list.
 nums = [5, 15, 35, 8, 98]
for num_index, num_val in enumerate(nums):
    print(num_index, num_val)

'''

def Access(L):
    L1=[]
    for num_index, num_val in enumerate(L):
        return (num_index,num_val)

def test_Access():
    assert ((0,10)) == Access([10])


'''21. Write a Python program to convert a list of characters into a string. '''

def Char_to_String(L):
    str1=""
    str1=''.join(L)
    return str1

def test_Char_to_String():
    assert ('TDK') == Char_to_String(['T','D','K'])



'''22. Write a Python program to find the index of an item of a specified list.'''

def Index(L,n):
    a = L.index(n)
    return a

def test_Index():
    assert(3) == Index([0,1,2,3,4,5],3)


'''23.given an integer array and length as input .write a function to remove all adjacent duplicate values
   ex:[1,2,2,5,2,6,6,6,3,2,6,9]
   output:[1,2,5,2,6,3,2,6,9]'''

def Duplicate1(L,num):
    o=[]
    p=None
    if num>0:
        for n in L:
            if n==p:
                continue
            o.append(n)
            p=n
    return o

def test_Duplicate1():
    assert([1,2,3,4,5,1,2]) == Duplicate1([1,1,2,2,3,4,5,1,2],9)

'''24. Write a Python program to append a list to second list.'''

def Append(L1,L2):
    L3=[]
    L3=L1+L2
    return L3

def test_Append():
    assert ([1,2,3,4,5,6]) == Append([1,2,3],[4,5,6])


'''25. Write a Python program to select an item randomly from a list.'''

import random

def Random_Item(L):
    if random.choice(L):
        return True
    else:
        return False

def test_Random_Item():
    assert(True) == Random_Item(['red','blue','green','violet'])


'''26. Write a python program to check whether two lists are circularly identical.
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]
Compare list1 and list2 returns True
Compare list1 and list3 return False'''

def Lis1_lis2(L1,L2):
    if ' '.join(map(str, L2)) in ' '.join(map(str, L1 * 2)):
        return True
    else:
        return False
def Lis2_Lis3(L2,L3):
    if ' '.join(map(str, L3)) in ' '.join(map(str, L2 * 2)):
        return True
    else:
        return False


def test_JINGLEE():
    assert(True) == Lis1_lis2([10, 10, 0, 0, 10], [10, 10, 10, 0, 0])
    assert (False) == Lis2_Lis3([10, 10, 10, 0, 0] , [1, 10, 10, 0, 0])







