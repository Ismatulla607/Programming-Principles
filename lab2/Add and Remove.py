thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.append("orange")
thislist.insert(1, "tomato")
thislist.extend(tropical)
print(thislist)

thislist.remove("banana")
thislist.pop()
del thislist[0]
print(thislist)