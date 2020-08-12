num = [1,2,3,9,5]
for i in range(0, 4, 2) :
    print(i)


print(len(num))
print(num[0 : 4 : 2], "\n")
print(num[::2], "\n")
print(num[ :2 ], "\n")

num.append(5)
print(num, "\n")

num.insert(0, "Mostafa")
print(num, "\n")

items = [5, "ball", True]
items.pop()
removed_item = items.pop(0)
print(items, "\n", removed_item, "\n")

sports = ["baseball", "soccer", "football", "hocky"]
try: 
    sports.remove("baseball")
except:
    print("That item does not exist in the list")
print(sports, "\n")

nums = [5, 3, 9]
print(min(nums), max(nums), sum(nums), sorted(nums))
nums.sort()
print(nums)

names = ["Jack", "Robert", "Mary"]
if "Mary" in names:
    print("Found")
if "Mostafa" not in names:
    print("not found")

numbers = [1]
if not numbers:
    print("empty")
else:
    print("full")

sports2 = ["Baseball", "Hockey", "Football", "Basketball"]
for sport in sports2 :
    print(sport)

names2 = ["Bob", "Jack", "Rob", "Bob", "Robert"]
while "Bob" in names2 :
    names2.remove("Bob");
print(names2)