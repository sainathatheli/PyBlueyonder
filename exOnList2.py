l1=list(("apple","organge","mango","pineapple")) #initilaize the list using constructor

l2=["ramu",10,True,10.3,"ramu"]

print(l2)
#appending the element at end
l2.append("kiwi")
print("after append ",l2)

l2.insert(1,30) #element insert at index position 1
print("after insert at particular index ")
print(l2) #ramu 30 10 True 10.3 ramu kiwi

l2.remove(True) #pop(index position)
print("After remove: ")
print(l2) # ramu 30 10 10.3 ramu kiwi

print("conditional operations")
if "mangoo" in l1:
    print("yes mango exist in list l1")
else:
    print("not exist")

    -7-6-5-4-3-2-1	
l3=[12,4,5,6,7,8,9]
    0  1 2 3 4 5 6
 
#slice syntax :-[startendindex:endindex:step]

print(l3[2:6]) # 5 6 7 8 -- endindex not included

print(l3[1:8:2] #4 6 8 

print(l3[-4:2]) #4

print(l3[4:1:-2]








#copy(),sort(),clear(),reverse();

l1.reverse();
print("after reverse")
print(l1)

l1.sort()
print("after sort")
print(l1)


l1.sort(reverse=True)
print("after desc sort")
print(l1)

l3=l1.copy();
print("after copy in l3")
print(l3)

l3.clear();
print("after clear")
print(l3)

