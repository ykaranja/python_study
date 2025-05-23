x=(10,20,30,40)
print(type(x))
print(x[-1])
#convert to a list
x=list(x)
x.append(100)
#convert back to tuple
x=tuple(x)
print(x)
days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")
#1. Find wednesday using an index
print(days[2])
#2. Using a function a find the length of the tuple.
print(len(days))
#3. Replace Thursday with Thur
days=list(days)
days[3]="Thur"
days=tuple(days)
print(days)