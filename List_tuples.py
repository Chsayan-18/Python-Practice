#List is like the Array that we use in other programming languages
marks = [90, 92.36, 94.56, 84, 83.5]

#In list we can store any type of elements, it can be string, it can be integer, anything.

#Lists are Mutable, we can change the value in the list (Modify) through indexing

#List Methods

list = [2, 1, 3]

list.append(4) # This will add one element in the end of the list as the value [4]
list.sort() #This will sort the whole list in ascending order
list.sort(reverse=True) #This will sort the whole list in descending order
list.reverse() #This will simply reverse the list as it is.
list.insert(index number, value) #This will insert a new element at the exact index position where we want the value.
list.remove(1) #THis will remove the value "1" from the list, but the only the first occurance one, if one is continued in the list, it will not remove the other "1", only the first one.
list.pop(index number) #This will remove the value from the proper index number.

#In append we can add only one value at a time.

#Tuple
#Tuple are immutable just as Strings, and the difference with list is that, we have tu use () instead of [] to add any value in the tuple data type. We can not modify or remove anything from a tuple.

#Tuple Methods

tup = (1, 2, 4, 3, 1, 7)

tup.index(1) #This will return the index number of the first 1 that is "0".

tup.count(1) #This will count the total occurrences of 1, that is "2".
