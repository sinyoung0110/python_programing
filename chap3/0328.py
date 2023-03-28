# 주석 표현
'''
a,b=100,200
a+=b
print("a+=b: a= ",a)

a=100
b=5
a-=b
print(a)
a/=b
print(a)
a%=b
print(a)

name=input("너의 이름은?")
print("저의 이름은 ",name,"입니다")

year2class=input("2학년 몇반?")
print("저는 ", name, year2class, "반 입니다.")

age=input("How old are you?")
print("저는 ", age,"살 입니다.")
print(type(age))
print("우리 아빠는 저보다 30살 많은 ", int(age)+30, "이에요")

a=10
str_a=str(a)
print("type(a): ",type(a))
print("type(str_a):",type(str_a))

planet=input('원하는 행성은?')
strRadius=input(planet+'반지름은?')
radius=int(strRadius)

length=2*3.14*radius
print(planet,'반지름: ', radius)
print(planet,'둘레길이: ', length)

var="python"
print(var[-5])
print(len(var))
print("python"[0])
print(var[0:len(var)])
print('python'[0:len('python')])

print('python'[-5:-1])

print('python'[:3]) 
print('python'[:])
'''
str='Monty Python'
print(len(str))

print (str[0:5],str[6:],str[6:12])
print (str[-12:-7],str[-6:],str[-6:0])