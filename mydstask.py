ds=[23, 'Jane', (560), ['Lesson', 'Maths', {'currency' : 'KES'}], 987, (76,'John')]
#Print KES
print(ds[3][2]['currency'])
#2. Print 560
print(ds[2])
#3. Print Maths
print(ds[3][1])
#4. In the dictionary with the key currency, add another key “amount” with value 90
print(ds[3][2])
ds[3][2]['amount']=90
print(ds[3][2])
#5. Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually. Hint: Strings can be reversed using [::]
print(ds[4])
ds[4]=str(ds[4])
ds[4]=ds[4][::-1]
ds[4]=int(ds[4])
print(ds)

#6. Change the name “John” to “Jane” . 
ds[5]=list(ds[5])
ds[5][1]='Jane'
print(ds)
