s1=set({101,"ram",True,30.0,"ram",10,101}) #initialize the constructor

print("elements from s1")
print(s1)

s2={"orange","apple","grapes","Kiwi"}

print("elements from s2")
print(s2)

s2.add("ram")
print("After add the element from s2")
print(s2)

#remove an element
s2.remove("apple") #element exist it will delete andif not exist it will throw an error
print("After remove the element from s2")
print(s2)

s2.discard("aseesss") #element exist it will delete and if not exist it will not throw any error

print("After remove the element from s2")
print(s2)




#copy(),pop()==>random element deleted,clear()==>empty the set


print("print using loop")
for x in s1:
    print(x)





