thislist = ["apple", "banana", "cherry", "orange," "kiwi," "mango"]
thislist[1:3] = ["blackcurrent", "watermelon"]
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
thislist.append(tropical)
print(thislist, "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
