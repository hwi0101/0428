#練習一
def bmi(w, h):
    h_m = h / 100.0
    result = w / (h_m * h_m)
    return result


for i in range(3):
    h = int(input("Please enter height in (cm): "))
    w = float(input("Please enter weight in (kg): "))

    x=bmi(w,h)
    print("BMI = ", x)

    if x <18.5:
        print("體重過輕")
    elif x>=18.5 and x<24:
        print("健康體位")
    elif x>=24 and x<27:
        print("過重")
    elif x>=27 and x<=30:
        print("輕度肥胖")

    
    elif x>=30 and x<=35:
        print("中度肥胖")
    elif x>=35:
        print("重度肥胖")
    else:
        print("F")

#練習二 1
for i in range(5,0,-1):
    print(i)
    

#練習二 2
s=8

for i in range(s,0,-2):
    print (s)
    s=s-2

#練習三 1

import time
s=(time.time())
print ("幾秒:", s )

m=s//60
print ("幾分:", m )

h=m//60
print ("幾小時:", h )

d=h//24
print ("幾天:", d )

#練習三 2

def check_fermat(a,b,c,n):
    if n >= 2:   
        print (a**n+b**n==c**n)
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")
    

a1=int(input("請輸入a:"))
b1=int(input("請輸入b:"))
c1=int(input("請輸入c:"))
n1=int(input("請輸入n:"))

check_fermat(a1,b1,c1,n1)

#練習三 3
def is_triangle(a,b,c):
    
        if a+b==c or b+c==a or a+c==b:
            print("degenerate triangle")
        
        elif a+b<c or b+c<a or a+c<b:
            print("No")

        else:
            print("Yes")

length1=int(input("請輸入邊長1:"))
length2=int(input("請輸入邊長2:"))
length3=int(input("請輸入邊長3:"))
        
    
is_triangle(length1,length2,length3)

