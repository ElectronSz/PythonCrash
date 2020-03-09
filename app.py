#variables

fname =  "Lunga" #string
age = 24 #int
salary = 1250.97 #float
retired = False #bool
children = ['Anele', 'Faye', 'Abraham'] #list
address = {'street': "Mbhilibhi Str", 'code': 180, 'city': "Mbabane"} #dict
tuples = ('Musa','Futhi')

#multiple variable assignment
a = b = c = 2 #same value
d, e, f = True, 125, "Marry"

#manipulating string

# print(fname[-1])
# print(fname[0])
# print(fname[0:3])

#<<lists>>
cars = ['BMW', 'MERC', 'Toyota', 'VW']
dubais = ['Honda Fit', 'Toyoya Vitz']

#manipulating list
# print(cars)
# print(cars[0])
# print(cars[1:4])
# print(cars +  dubais)
#print(cars*2)
#cars[0] = "Toyota"
#print(cars)

#<<Tuples>>

rivers = ('Umkhondvo', 'Mlumati')

#print(rivers[0])


#<Dict>>
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


# print(dict['one'] )      # Prints value for 'one' key
# print(dict[2])         # Prints value for 2 key
# print(tinydict)          # Prints complete dictionary
# print (tinydict.keys() )  # Prints all the keys
# print (tinydict.values()) # Prints all the values

#<<Conversion>>
this = "100"
# print(type(this))
that = int(this) 
# print(type(that))

#<Operators>>
ops, apps = 10, 6
# print(ops%apps) modulus
#print(ops**apps) expo

#Assignment>>
asi = 0
asi +=5
asi = asi + 5
# print(asi)


#Decisions
num1 = 1
num2 = 1
gone = False

# if num1 == num2:
#     print("They are the same")
    
# else:
#     print("They are not the same")


#While loop
zim = 0
# while zim < 10:
#     zim +=1 #control
#     print(zim)

#For loop
# for child in children:
#    print(child)


#Functions
# def addNumbers(a, b):
#     total = a + b
#     return total

# print(addNumbers(45,70))

# def substractNumbers(a, b):
#     total = a - b
#     return total


# print(substractNumbers(0,9))

def divideNumbers(a, b, c):
    
    if b < a:
       return "Hey, You cant divide by zero"
    else: 
        total = a/b
        return total + c
    

#alt 1
# def divideNumbers(a, b):
    
#         if b < a:
#             return "Hey, You cant divide by zero"
#         else: 
#             total = a/b
#             return total

# tot =  divideNumbers(10,10, 6) # invoke
# print(tot)

def displayList(people_list, *filters):
    
    for person in people_list:
        print(person)
    print(filters)


people = ['Musa', 'Linda', 'Luunga', 'Janet']
#displayList(people)
# displayList(cars, len(cars))

sum = lambda x, y, z: x+y+z
print(arr(cars))





