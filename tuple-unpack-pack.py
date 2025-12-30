info = ("Alice", 30, "New York",35000)
(name, age, city, salary) = info
print("name:", name)
print("age:", age)
print("city:", city)
print("salary:", salary)

fauna = ("parrot","crow","sparrow", "Elephant", "Tiger", "Giraffe", "Zebra", "Dolphin", "Whale", "Seal")
birds = fauna[0:3]
land_mammals = fauna[3:7]
Aquatic_mammals = fauna[7:10]
print("birds:",birds)
print("land-mammals:",land_mammals)
print("Aquatic-mammals:",Aquatic_mammals)

fauna = ('cat',"dog", "horse", "pig", "parrot", "salmon")
(*animals, birds, fish) = fauna
print("animals:", animals)
print("birds:", birds)
print("fish:", fish)