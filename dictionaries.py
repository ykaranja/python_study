student={'name':'yvonne',
         'age':21,
         'email':'yvonne@gmail.com',
         'name':'Brian'
         }
print(type(student))
#To access values use keys
print(student['name'])
#modify the value
student['age']=25
student['name']='Leo'
#To add to data if there is no key
student['phone']= '7067493144'
student['location']={
    'city':'Kisumu',
    'country':'Kenya',
    'street':'mathai rd'
}
student['skills']=['cooking','colouring','coding']
print(student['location']['country'])
print(student['skills'][2])
student['location']['address']=('thika','nairobi')
print(student['location'])
student['location']['address']=list(student['location']['address'])
student['location']['address'][1]='Mombasa'
student['location']['address']=tuple(student['location']['address'])
print(student)
#methods
print(student.keys())
print(student.values())
print(student.items())

x=student.keys()

print('age' in x)