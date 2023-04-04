
'''
newstr=str.replace("파이썬","자바")
print("str: ",str)
print("newstr: ", newstr)

print("str.count('파이썬')",str.count("파이썬"))
print('->'.join(str)) #join은 str사이마다 ->를 넣어줘 라는 뜻임


print(str.find("파이썬"))
print(str.find("파"))
print(str.find("썬"))
print(str.find("자바")) #-1나옴
print(str.index("파이썬"))
print(str.index("파"))
print(str.index("썬"))
#print(str.index("자바")) #오류남


str="파이썬은 파이썬은 파이썬은 파이썬은 ㅍ파이썬은 "
newstr="파이썬은, 파이썬은, 히히히, 파이썬은, 호호호 , 파이썬은, ㅍ파이썬은 "
print(str.split())
print(newstr.split())


print(2,"+",3,"=",5)
print(('{}+{}={}'.format(2,3,5))) #꺽쇠하안에 숫자를 넣을 수 있음

a,b=5,10.00
print('{}+{}={}'.format(a,b,a+b))
print('{0}+{1}={2}'.format(a,b,a+b)) #몇 번째에 넣어야하는지 index를 붙일 수 있다.
print('{2}+{0}={1}'.format(a,b,a+b))
print('{0:d}+{1:f}={2:f}'.format(a,b,a+b)) 


print(bool(0),bool(1),bool(1.22222),bool(-12))
print(bool("dsdfsd"),bool("-1"),bool(""))

hour=15
if hour<12 :
    print("12시가 지났으니 오전입니다.")
elif hour<18 :
    print("12시가 지나고, 18시가 안 지났으니 오후입니다.")
else :
    print("18시가 지났으니 저녁입니다.")

#장학금
score_str=input("점수는?")
score=int(score_str)
if score<200 :
    print("50만원을 줌")
elif score<400 :
    print("100만원을 줌")
else :
    print("100000만원을 줌")

#점심
lunch=input("배가 고픈가?")
if lunch=='y' :
    launch=input("서브웨이 먹을래?")
    if launch=='y' :
        print("8호관 1층")
    else :
        haksik=input("학식먹을래?")
        if haksik=='y' :
            print("8호관 3층 가")
        else :
            print("먹지마")
else :
    print("그렇구나 그럼 다음에 먹어")

for i in 1,3,4,5,6,8 :
    print(i) 
for i in range(0,11) :
    print(i)
for i in range(0,11,3) :
    print(i)

#1부터 10까지 합을 구하시오.
sum=0
for i in range(1,11) :
    sum+=i
else:
    print("for문의 조건이 더 이상 만족하지 않습니다.")
    print("i가range(11)에서 벗어남")
    print("for 문이 break나 continue로 종료된게 아니라 정상종료했습니다.")
print(sum)

i=1
while i>5 :
    print(i,"는 5보다 크다")
print(i,"는 5보다 작다")

#n=1부터 5까지 찍어보는 프로그래밍
#1 2 3 4 5
i=1
while i<=5 :
    print(i, end=' ')
    i+=1

#놀이기구 탑승 4명 가능 5명 X  키는 150이상 
people=0
while people<4 :
    height_str= input("키가 몇인가?")
    height=int(height_str)
    if height>=150 :
        people+=1
        print("환영합니다.")
        print("현재 인원: ",people)
    else :
        print("더 커서 와라 애기야")
else:
    print("탑승 불가능합니다.")
    '''
#input 입력 후 무한반복한다.  exit 이라는 값을 받으면 , 입력종료 //apple을 받으면 출력 안함
while True :
    str=input("단어를 넣으세요.")
    if str=="exit" :
        print("종료")
        break
    else:
        if str=="apple":
            print("apple을 입력받음")
            print("continue실행함")
            continue
        print(str,"를 입력했다")
print("while이 종료됨")
