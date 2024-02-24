import csv

name = input("What patriots player do you like? ")
reason = input("Why? ")

with open("favoriteplayers.csv", "a") as file:
          writer = csv.DictWriter(file, fieldnames=["name", "reason"])
          writer.writerow({"name": name, "reason": reason})


""" other examples
 names = []

with open("names.csv") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"Patriots Player: {name}") """

""" from logging import INFO, basicConfig, info

basicConfig(level=INFO)

names = input("Who is your favorite NE Patriot? ")

with open('names.txt', 'a', encoding='utf-8') as file:
   file.write(names +'\n')

with open('names.txt', 'r', encoding='utf-8') as file:
   content = file.read()
   info("Your favorite NE Patriot has been added to the list:\n%s", (content))
 """