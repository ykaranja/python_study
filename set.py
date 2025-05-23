x={10,50,100,200,70,1,50,100}
print(x)

x.add(1000)
print(x)
x.remove(100)
print(x)

my_list=['you', 'me', 'you', 'us', 'we']
my_list=set(my_list)
my_list=list(my_list)
print(my_list)
x={1,2,3,4,5,6,7}
y={5,6,7,8,9,10}
#z=x.difference(y)
#z=x.union(y)
#z=x.symmetric_difference(y)
z=x.intersection(y)
print(z)