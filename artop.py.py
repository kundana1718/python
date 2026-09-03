#bank balance
balance=10000

deposit=5000
balance+=deposit

print("after deposit:",balance)

withdraw=2000
balance-=withdraw


print("after withdrawal:",balance)

#comparison operators
a=10
b=20

print(a==b)
print(a!=b)
print(a<b)
print(a<=b)
print(a>b)
print(a>=b)
#age eligibility checker
age=int(input("enter your age:"))

print("eligible:",age>=18)

#pass or fail checker
marks=int(input("enter marks:"))

print("passed:",marks>=35)
#login validation
correct_user_name="admin"
correct_password="1234"

username=input("enter user name:")
password=input("enter pasword:")

print(username==correct_username)
print(password==correct_password)






