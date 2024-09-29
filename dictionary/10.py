
thisdict = {
  "brand": ["Ford", "Ford"],
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue", "red"],
  "owners": None
}

print("\n",thisdict)

thisdict.pop("colors")
del thisdict["year"]

print(thisdict)

