#練習二 2
def decimal_2_binary(n):
    s = ""
    while n >= 2:
        remainder = n % 2

        s = str(remainder) + s

        n = n // 2

    s = str(n) + s
    
    print(s)
    
def decimal_8_binary(x):
    y = ""
    while x >= 8:
        remainder = x % 8

        y = str(remainder) + y

        x = x // 8

    y = str(x) + y   
    
    print (y)
    
    
def decimal_16_binary(j):
    k = ""
    while j >= 16:
        remainder = j % 16

        k = str(remainder) + k

        j = j // 16

    k = str(j) + k   
    
    print (k)
    
    
dec = int(input('please enter a decimal integer:'))


result1 = decimal_2_binary(dec)
    
result2 = decimal_8_binary(dec)

result3 = decimal_16_binary(dec)

#練習二 2

def decimal_2_binary(n):
    print(bin(n))
    
def decimal_8_binary(x):
    print(oct(x))
    
def decimal_16_binary(j):
    print(hex(j))
    
for i in range(3):
    dec = int(input('please enter a decimal integer:'))
    result1 = decimal_2_binary(dec)
        
    result2 = decimal_8_binary(dec)
    
    result3 = decimal_16_binary(dec)