#delcare and initialize the list i.e square list

l1=["apple","kiwi","mangos","pineapple"]

#display the type of l1
print(type(l1)) 

#display  length of list
print("length of an list is ")
print(len(l1))

#based on index print
print("Based on index values are ")
print(l1[0])
print(l1[1])
print(l1[2])
print(l1[3])

#changeable at index[2] replace mangos with banans
l1[2]="banana"

#based on index print
print("After change based on index values are ")
print(l1[0])
print(l1[1])
print(l1[2])
print(l1[3])

print("displaying the elements from list using for loop")
for x in l1:
    print(x)

#with help of constructor
l2=list(("raju","ramu")) #delcaring list using construtor

print(l2)

#different datatypes and duplicates
l3=["ramu",10.0,50,True,50,"ramu"]

print("displaying the elements from list using for loop")
for x in l3:
    print(x)


l4=list(s)
print(l4)