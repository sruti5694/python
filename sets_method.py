cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = {"Tokyo","Madrid"}
new_c = cities.isdisjoint(cities2)
print(new_c)
# if all the element of set 2 are present in set 1 then A is superset of B
new_s = cities.issuperset(cities3)
print(new_s)
new_s1 = cities2.issubset(cities)
print(new_s)