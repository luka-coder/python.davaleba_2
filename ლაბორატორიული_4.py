print("დავალება---1")
numbers = [5,12,52,4,9]
sum = 0
for i in numbers:
    sum+=i
print("რიცხვების ჯამი: ",sum)
maximum = max(numbers)
minimum = min(numbers)
avg = sum/len(numbers)
print("მაქსიმალური მნიშვნელობა: ",maximum)
print("მინიმალური მნიშვნელობა: ",minimum)
print("საშუალო არითმეტიკული: ",avg)
numbers.append(102)
print("102 დამატებული ბოლოში: ",numbers)
numbers.insert(2,205)
print("205 მესამე პოზიციაზე: ",numbers)
numbers.pop(3)
print("ამოვშალოთ მე-4 ელემენტი: ",numbers)
numbers.sort()
print("დალაგება ზრდადობით: ",numbers)
print("დავალება---2")
l = []
for i in range(10):
    i = input("შეიყვანეთ 10 მონაცემი: ")
    l.append(i)
print("10 მონაცემი: ",l)
print("დავალება---3")
fruits = ["Watermelon", "Banana", "Apple","Jonjoli"]
fruits.sort()
fruits.reverse()
print(fruits)
print("დავალება---4")
def li(l):
  m = 1
  for i in l:
    m=m * i
  return m
lst = [5,6,7,3,9]
print(li(lst))
print("დავალება---6")
lst = [6,12,51,37,9]
for i in lst:
    i+=10
    print(i)
print("დავალება---7")
import random
lst = []
for l in range(10):
    l = str(random.randint(25,110))
    lst.append(l)
print("ლისტი: ",lst)
print("მინიმალური ელემენტი: ",min(lst))
print("დავალება---9")
def li(l):
    for i in l:
        if i%2!=0:
            l.remove(i)
    print(l)
lst = [61,32,6,9,10,41]
li(lst)
print("დავალება---10")
lst = [61,32,6,9,10,41]
random.shuffle(lst)
print(lst)
print("დავალება---11")
lst = [61,32,6,9,10,41]
lst = random.choice(lst)
print(lst)
print("დავალება---12")
number = int(input("შეიყვანეთ ნებისმიერი დიდი რიცხვი: "))
num = str(number)
n = list(num)
print("list: ",n)
sum = 0
for i in n:
   s = str(i)
   n = int(s)
   sum += n
print("int: ", sum)
print("დავალება---14")
f = input("შეიყვანეთ ნებისმიერი ფაილის დასახელება: ")
extensions = ['txt', 'jpg', 'gif', 'html']
if f in extensions:
   print("Yes")
else:
   print("No")
print("დავალება---15")
#s = "python php pascal javascript java c++"
#l = list(s.split(" "))
#print(l)
#for i in l:
#   b = len(str(i))
#   print(b)
#   b = list(a.split())
#   x = b.append()
#   print(x)






























