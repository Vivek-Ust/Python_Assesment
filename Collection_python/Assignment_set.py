#set problesm
#Exercise 1: Perform Basic Set Operations
def basic_set(st1, st2):
    st1.add(9)
    print(f"Add elements to Set1:", st1)
    st2.remove(7)
    print(f"Add elements to Set2:", st2)
    print("Union: ", st1 | st2)
    print("Intersection: ", st1 & st2)
    print("Difference: ", st1 - st2) #Elements in st1 but not in st2
    print("Symmetric Difference: ", st1 ^ st2) # Elements in either set but not both
basic_set({1,2,3,5}, {1,3,4,5,6,7})
 
#Exercise 2: Union of Sets
def union(s1, s2):
    print("Union:", s1 | s2)
union({3,8,2,6,5}, {4,3,2,5, 1})
 
#Exercise 3: Intersection of Sets
def intersection(s1, s2):
    print("intersection:", s1 & s2)
intersection({3,8,2,6,5}, {4,3,2,5,1})
 
#Exercise 4: Difference of Sets
def Difference(s1, s2):
    print("Difference of Sets:", s1 - s2)
Difference({3,8,2,6,5}, {4,3,2,5, 1})
 
#Exercise 5: Symmetric Difference
def Symmetric(s1, s2):
    print("Symmetric Difference:", s1 ^ s2)
Symmetric({3,8,2,6,5}, {4,3,2,5, 1})
 
#Exercise 6: Add a list of Elements to a Set
def add_elements(st, lst):
    st.update(lst)
    print("Add a list of Elements to a Set: ",st)
add_elements({1,2,3},[4,5,6])
 
#Exercise 7: Set Difference Update
def set_update(s1, l1):
    s1.difference_update(l1)
    print("Set Difference Update: ",s1)
set_update({3,4,5,6}, [5,6,8])
 
#Exercise 8: Remove Items From Set Simultaneously
def remove_items(s1, remove):
    for i in remove:
        s1.discard(i)
    print("Remove Items From Set Simultaneously: ", s1)
remove_items({1,2,3,4,5,6}, [2,3,4])
 
#Exercise 9: Check Subset
def check_subset(st1, st2):
    print("Check Subset: ", st1.issubset(st2))
check_subset({1,2}, {1,2,3,4})
check_subset({1,2}, {3,4})
 
#Exercise 10: Check Superset
def check_superset(st1, st2):
    print("Check Superset: ", st1.issuperset(st2))
check_superset({1,2,3,4}, {1,2})
check_superset({1,2}, {3,4})
 
#Exercise 11: Set Intersection Check
def intersection_check(s1, s2):
    if s1.intersection(s2):
        print("Common elements exist")
    else:
        print("No common elements exist")
intersection_check({3,8,2,6,5}, {4,3,2,5,1})
 
#Exercise 12: Set Symmetric Difference Update
def symmetric_update(s1, s2):
    s1.symmetric_difference_update(s2)
    print("Set Symmetric Difference Update: ", s1)
symmetric_update({3,8,2,6,5}, {4,3,2,5,1})
 
#Exercise 13: Set Intersection Update
def intersection_update(s1, s2):
    s1.intersection_update(s2)
    print("Set Intersection Update: ", s1)
intersection_update({3,8,2,6,5}, {4,3,2,5,1})
 
#Exercise 14: Find Common Elements in Two Lists
def common_elements(el1, el2):
    print("Find Common Elements in Two Lists: ", el1 & el2)
common_elements({1,2,3},{2,3,4})
 
#Exercise 15: Frozen Set
def frozen_set(s1):
    temp = frozenset(s1)
    print("Frozen Set: ", temp)
frozen_set({1,2,3})
 
#Exercise 16: Count Unique Words
def unique_count(strs):
    split_s = strs.split(" ")
    unique = set(split_s)
    print("Count Unique Words: ", len(unique))
    print("Unique Words: ", unique)
unique_count("python is easy and python is powerful")