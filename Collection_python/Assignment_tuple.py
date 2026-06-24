#tuple problems
#Exercise 1: Perform Basic Tuple Operations
def basic(tup):
    print("Total Count of 20",tup.count(20))
    print("Index of 40:", tup.index(40))
    print("Slicing:", tup[1:4])
basic((10,20,10,40,20))
 
#Exercise 2: Tuple Repetition
def repeat(tp, n):
    print("Tuple Repetition", tp * n)
repeat((9, 8, 7), 3)
 
#Exercise 3: Slicing Tuples
def slicing(tpl):
    print("Slicing:", tpl[1:4])
slicing(('a', 'd', 67, 'c', 82, 7))
 
#Exercise 4: Reverse the tuple
def reverse(tup):
    print("Reverse using slicing:",tup[::-1])
    #OR
    print("Reverse using reverse function:", tuple(reversed(tup)))
reverse(('a', 'd', 67, 'c', 82, 7,'k'))
 
#Exercise 5: Access Nested Tuples
def access_nested(tup):
    print("Access Nested Tuples:")
    print(tup[1])
    print(tup[2][1])
    print(tup[3][1][0])
access_nested((1, (4, 5), (9, 3, 6), (2, (8, 7))))
 
#Exercise 6: Create a tuple with single item 50
def create_tup():
    t = (50,)
    print("Creating tuple with single item:", t)
    print("Type: ",type(t))
create_tup()
 
#Exercise 7: Unpack the tuple into 4 variables
def unpack(tup):
    a, b, c, d = tup
    print("Unpacking tuple into 4 variables:", a, b, c, d)
unpack((6,5,4,3))
 
#Exercise 8: Swap two tuples in Python
def swap(t1, t2):
    print("Before swap: ",t1, t2)
    t1, t2 = t2, t1
    print("After swap : ",t1, t2)
swap((1,2,3), (4,5,6))
 
#Exercise 9: Copy Specific Elements From Tuple
def copy(tup):
    cp = tup[3]
    print("Coping Specific Elements: ",cp)
copy(('a', 'd', 67, 'c', 82, 7), )
 
#Exercise 10: List to Tuple
def list_to_tuple(lst):
    print("List to Tuple: ", tuple(lst))
list_to_tuple([1,2,'a','b',3,4])
 
#Exercise 11: Function Returning Tuple
def return_tuple(tp1, tp2):
    return tp1+tp2, tp1*tp2
res = return_tuple(4, 6)
print(res)
print(type(res))
 
#Exercise 12: Comparing Tuples
def compare(t1, t2):
    if t1 == t2:
        print("Two tuples are equal")
    elif t1 > t2:
        print("t1 is greater than t2")
    else:
        print("t2 is greater t1")
compare((1,2,3), (9,8,7))
 
#Exercise 13: Removing Duplicates from Tuple
def duplicate(dup):
    print("Removing Duplicates from Tuple", tuple(set(dup)))
duplicate((1,2,1,3,4,3,5,3,6))
 
#Exercise 14: Filter Tuples
def filter_tup(tup):
    res = tuple(filter(lambda i:i%2==0, tup))
    print("Filtering Even number using filter: ", res)
filter_tup((1,2,3,4,5,6,7,8,9))
 
#Exercise 15: Map Tuples
def map_tup(n1):
    new=tuple(map(lambda i: i*2, n1))
    print("Square number using map function: ",new)
map_tup((1,2,3,4,5,6,7,8,9))
 
#Exercise 16: Modify Tuple
def modity_tup(tup):
    temp = list(tup)
    temp.append(99)
    print("Adding Element:", tuple(temp))
modity_tup((22,33,55,66))
 
#Exercise 17: Sort a tuple of tuples by 2nd item
def sort_2nditem(tp):
    sort_tp = tuple(sorted(tp, key = lambda x:x[1]))
    print("Sorting a tuple of tuples by 2nd item:", sort_tp)
sort_2nditem(((1,5),(3,2),(4,8),(2,1)))
 
#Exercise 18: Count Elements
def count_element(tp):
    print("Count Elements:",len(tp))
    #OR
    count = 0
    for i in tp:
        count += 1
    print("Count elements using loop:", count)
count_element((1,2,3,4,7,5,6))
 
#Exercise 19: Check if all items in the tuple are the same
def check_items(tup):
    for i in range(len(tup)):
        for j in range(i+1, len(tup)):
            if tup[i] == tup[j]:
                return True
            else:
                return False
    #OR
    if len(set(tup)) == 1:
        return "All elements in tuples are same"
    else:
        return "All elements in tuples are not same"
print(check_items((1,2,3,4,7,5,6)))
print(check_items((2,2,2,2,2)))