a=20
b=10
print("Addition(+):",a+b)#Addition(+): 30
print("Subtraction(-):",a-b)#Subtraction(-): 10
print("Multiplication(*):",a*b)#Multiplication(*): 200
print("Division(/):",a/b)#Division(/): 2.0
print("Float division(//):",a//b)#Float division(//): 2
print("Modulus(%):",a%b)#Modulus(%): 0
print("Modulus(%):",b%a)#Modulus(%): 10
print("Exponentiation(**):",a**b)#Exponentiation(**): 10240000000000

#2.COMPARISION OPERATORS
print("Equal to(==):",a==b)#Equal to(==): False
print("Not Equal to(!=);",a!=b)#Not Equal to(!=); True
print("Greater than(>):",a>b)#Greater than(>): True
print("Less than(<):",a<b)#Less than(<): False
print("Greater than or Equal to(>=):",a>=b)#Greater than or Equal to(>=): True
print("Lesser than or Equal to(<=):",a<=b)#Lesser than or Equal to(<=): False

#3.Assignment operators
a=20
b=10
print("Assign(=):",a) #Assign(=): 20
a+=b 
print("Add & Assign(+=):",a) #Add & Assign(+=): 30
a-=b
print("Subtract & Assign(-=):",a) #Subtract & Assign(-=): 20
a*=b
print("Multiply & Assign(=):",a) #Multiply & Assign(=): 200
a/=b
print("Division & Assign(/=):",a) #Division & Assign(/=): 20.0
a//=b
print("Floor Divison & Assign(//=):",a) #Floor Divison & Assign(//=): 2.0
a%=b
print("Modulus & Assign(%=):",a) #Modulus & Assign(%=): 2.0
a**=b
print("Exponentiate & Assign(=):",a) #Exponentiate & Assign(=): 1024.0

#5.Membership Operators
a = [1,2,3]
print("In operator:",1 in a) #In operator: True
print("Not In operator:",5 not in a) #Not In operator: True

#6.Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("Is operator:",a is b) #In operator: True
print("Is Not operator:",a is not c) #Not In operator: True