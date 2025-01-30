thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.get("model")
print(x)
y = thisdict.keys()

print(y) #before the change

thisdict["color"] = "white"

print(y) #after the change