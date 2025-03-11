class Human:

    def __init__ (my,name,age,height,gender):
        my.name=name
        my.age=age
        my.height=height
        my.gender=gender

    def displayAge(my):
        print(f'my age is {my.age}')
c1= Human ('John',50,1.93,'M')
c2= Human ('Mark',50,1.93,'M')
c1.displayAge()
c2.displayAge()



def displayName(my):
        print(f'my name is {my.name} i am {my.age} years old')
c1= Human ('John',50,1.93,'M')
c2= Human ('Mark',50,1.93,'M')
c1.displayName()
c2.displayName()

    
    

#c1= My('John',50,1.93,'M')
#print(c1.name)
#print("my name is",c1.name, 'and i am', c1.age,'years old')
#print(f'my name is{c1.name}')

    
    
