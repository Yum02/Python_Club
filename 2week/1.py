#조건문

print(2>1)  #True
print(2<1) #False
print(2==1) #False
print(2!=1) #True

print(1=="1") #False -> 1은 숫자, "1"은 문자

#논리연산자
#and : 둘 다 참일 때 참
print(True and True)   #True
print(True and False)  #False
print(False and False) #False

#or : 둘 중 하나만 참이면 참
print(True or True)    #True
print(True or False)   #True
print(False or False)  #False

#not : 참을 거짓으로, 거짓을 참으로
print(not True)        #False
print(not False)       #True

#순서는 not > and > or
print(not True and False or not False) #True