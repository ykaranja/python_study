fruits=['mangoes', 'orange','kiwi',[39,10,['a','e','i'],25],'pawpaw','pineapple']
print(type(fruits))
print(fruits[3][2][1])
fruits[0]='Lemon'
print(fruits)
week=['monday','tuesday','wednesday','thursday','friday','sato','sunday','monday']
print(week[2])
#List methods:functions inside a class
week.append(1000) #add objects at the end of the list
#week.clear() #deletes everything from the list
x=week.copy() #creates a copy of the original list
week.remove('monday') #remove first occurence of value
week.count('monday') #return number of occurence of a value
week.pop(1) #remove and return item at index
week.reverse() #reverses the list
y=2,4,5
week.extend(y) #extend list by appending items
print(week)
numbers=[5,3,4,2,8]
numbers.sort(reverse=True)
print(len(numbers))

trainees= ["John", [2, ["James","Mary"]]]
# 1. Display 2 from the list.
print(trainees[1][0])
# 2. Output James  from the list.
print(trainees[1][1][0])
# 3. Using a method add 56 at the end of the list.
trainees.append(56)
print(trainees)
# 4. Using a method add the name Mike between James and Mary
trainees[1][1].insert(1,'Mike')
print(trainees)
# 5. Change the value of 2 to 8
trainees[1][0]=8
print(trainees)
# 6. Remove John and Mary from the list.
trainees.remove('John')
trainees[0][1].remove('Mary')
print(trainees)
# 7. Using a function, determine the length of the list
print(len(trainees))