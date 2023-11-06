roman=input("enter the value")
value={"I":1,
"V":5,
"X":10,
"L":50,
"C":100,
"D":500,
"M":1000,}

result=0
a=0
for x in roman[::-1]:
    roman=value[x]
    ##print(roman)
    if roman<a:
        result-=roman
        ##print(roman)
    else:
        result+=roman
        a=roman
        ##print(a)
            
print(result)
