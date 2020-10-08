print("დავალება---1")
thisdict = {0: 10, 1: 20}
thisdict.update({2:12,3:23})
print(thisdict)
thisdict.pop(1)
print(thisdict)
print("დავალება---2")
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
thisdict = dic1.update(dic2)
thisdict = dic1.update(dic3)
print(dic1)
print("დავალება---3")
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
if 3 in d:
  print("3 არის ერთერთი გასაღები ლექსიკონში!")
else:
  print("3 არ არის ერთერთი გასაღები ლექსიკონში!")
print("დავალება---4")
d = {'x': 10, 'y': 20, 'z': 30}
for i in d:
  print(f"{i}->{d[i]}")
print("დავალება---5")
d = dict()
for x in range(1,11):
  d[x] = x**2
print(d)
print("დავალება---6")
r = open("ტექსტ ფაილი.txt", "r")
print(r.read())
print("დავალება---7")
set = {0,1,2,3,4}
x = {9,8,5}
set.update(x)
print(set)
set.remove(1)
set.remove(2)
print(set)
for i in set:
  print(i)
print("სიმრავლის ელემენტების რაოდენობა: ",len(set))
print("დავალება---8")
set1 = {"green", "blue"}
set2 = {"blue", "yellow"}
set = set1.union(set2)
s = set1.intersection(set2)
d1 = set1.difference(set2)
d2 = set2.difference(set1)
d = d1.union(d2)
sim = set1.symmetric_difference(set2)
print(set)
print(s)
print(d)
print(sim)
print("დავალება---9")
set = {0,1,2,3,4,5,9,8}
maximum = max(set)
print("მაქსიმალური ელემენტი: ",maximum)
minimum = min(set)
print("მინიმალური ელემენტი: ",minimum)
print("დავალება---10")
i = ()
m = int(i)
while m<100:
  m = int(input("5-ის ჯერადი რიცხვები: "))
  m+=5
  print(m)






































