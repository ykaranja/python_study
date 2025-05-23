numbers = (10, 20, 30, 40, 50)
#Add 60 to the end,Replace 30 with 35
numbers=list(numbers)
numbers.append(60)
numbers[2]=35
numbers=tuple(numbers)
print(numbers)
values = (15, 5, 30, 25, 10) 
#Arrange the elements in ascending order
values=list(values)
values.sort()
values=tuple(values)
print(values)
fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
#Count occurrences of "banana",Remove all occurrences of "banana"
fruits.count('banana')
print(fruits)
fruits=set(fruits)
fruits.remove('banana')
fruits=tuple(fruits)
print(fruits)
#Reverse the order of elements using sort method.
names = ("Alice", "Bob", "Charlie", "David")
names=list(names)
names.sort(reverse=True)
names=tuple(names)
print(names)
#add "yellow" at index 1,Extend with ["purple", "orange"]
colors = ("red", "blue", "green")
colors=list(colors)
colors.insert(1,'yellow')
colors.extend(["purple", "orange"])
print(colors)
