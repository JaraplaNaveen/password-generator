import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w,','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9']
specialchar=['@','#','$','%','&','*']
print("create strong password")
nm_letter=int(input("enter number of letters\n"))
nm_numbers=int(input("enter numbers\n"))
nm_special=int(input("enter number of special charactors\n"))
password=''
for char in range(1,nm_letter+1):
    password+=random.choice(letters)

for number in range(1,nm_numbers+1):
        password+=random.choice(numbers)
for special in range(1,nm_special+1):
          password+=random.choice(specialchar)
print(password)
print("save your password")