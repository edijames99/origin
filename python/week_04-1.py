# List
num = [1,2,3,4,[4,3,4,2],5.5]
print(num)
print(num[4][0])
num[0] = 2
print(num)
print(id(num[2]))
a = [4,10]
b = a
# Memory
print(id(a), id(b))
a[0] = 10
print(id(a), id(b))
# Copy

c = [1,2,3,4,5]
d = c[:]
c[0] = 50
print("First list is : {} And Second list is : {}".format(c, d))

s = ["test", "football", "shena"]
if s[1] == "football" :
    print("I like to play {}".format(s[1]))

name = ["john","Abraham","Sam","Kelly"]
print(name[0][0], name[1][0], name[2][0], name[3][0])
if "john" in name :
    print("I Love you Allah")
v = [2,1,5,3,6,4]
for num in range(5) :
    print(num)
    pass
for a in range(2, 10, 2) :
    print("Value: {}".format(a))

name = "mostafa zamani"
for b in name :
    print("Value : {}".format(b))
for f in v : 
    # print(f)
    pass