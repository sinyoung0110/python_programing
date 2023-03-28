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
str='Monty Python'
print(len(str))

print (str[0:5],str[6:],str[6:12])
print (str[-12:-7],str[-6:],str[-6:0])

print('python'[1:5:3])
print('python'[::-1])

print("ab"+"\b"+"c")
print('\n')
print("hello\vworld")

str_var="하하하하"
print(str_var.replace("하","호"))

str_var2="안녕하세요. 파이썬. 파이썬 수업입니다."
str_var3=str_var2.replace("파이썬", "자바")
str_var4=str_var3.replace("파이썬","자바", 3)
print(str_var2,'\n', str_var3, str_var4)
'''
num_str=input('실수를 입력 받음')
num_str.replace('.','')
sum=int(num_str[0])+int(num_str[1])+int(num_str[2])+int(num_str[3])+int(num_str[4])+int(num_str[6])

print("sum: ",sum)

