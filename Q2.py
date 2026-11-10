# # # # # # # # # # # # # # # Write a program to check if the given number is positive or negative.
# # # # # # # # # # # # # # num=int(input('enter number'))
# # # # # # # # # # # # # # if num < 0:
# # # # # # # # # # # # # #     print('negative')
# # # # # # # # # # # # # # elif num > 1:
# # # # # # # # # # # # # #         print('Positive')
# # # # # # # # # # # # # # else:
# # # # # # # # # # # # # #       print('Zero')

# # # # # # # # # # # # # # Write a program to input any alphabet and check whether it is vowel or consonant.
# # # # # # # # # # # # # user=input('enter latter')
# # # # # # # # # # # # # vowels='AEIOUaeiou'
# # # # # # # # # # # # # for i in vowels:
# # # # # # # # # # # # #     if user == i:
# # # # # # # # # # # # #         print('vowels')
# # # # # # # # # # # # #         break
# # # # # # # # # # # # # else:
# # # # # # # # # # # # #     print("not vowels")

# # # # # # # # # # # # a = int(input('Enter first angle: '))
# # # # # # # # # # # # b = int(input('Enter second angle: '))
# # # # # # # # # # # # c = int(input('Enter third angle: '))

# # # # # # # # # # # # if a+b+c==180 and a>0 and b>0 and c>0:
# # # # # # # # # # # #     print('valid ')
# # # # # # # # # # # # else:
# # # # # # # # # # # #     print('not valid')

# # # # # # # # # # # cp = float(input('Enter cost price: ')) # 700
# # # # # # # # # # # sp = float(input('Enter selling price: ')) #500
# # # # # # # # # # # if sp>cp:
# # # # # # # # # # #     profit=sp-cp
# # # # # # # # # # #     print('profit',profit)
# # # # # # # # # # # elif cp > sp:
# # # # # # # # # # #     loss=cp-sp
# # # # # # # # # # #     print('loss',loss)
# # # # # # # # # # # else:
# # # # # # # # # # #  ```python
# # # # # # # # # # # Check User ID, Password and CAPTCHA

# # # # # # # # # # import random

# # # # # # # # # # user_id = 'Ganesh@123'
# # # # # # # # # # password = '77362'

# # # # # # # # # # user = input('Enter user name: ')
# # # # # # # # # # passw = input('Enter password: ')

# # # # # # # # # # if user == user_id and passw == password:
# # # # # # # # # #     print('Username and password are correct')

# # # # # # # # # #     num = random.randint(1000, 9999)
# # # # # # # # # #     print('Your CAPTCHA is:', num)

# # # # # # # # # #     io = int(input('Enter CAPTCHA: '))

# # # # # # # # # #     if io == num:
# # # # # # # # # #         print('Login Successful!')
# # # # # # # # # #     else:
# # # # # # # # # #         print('CAPTCHA is wrong')

# # # # # # # # # # else:
# # # # # # # # # #     print('User ID or Password is wrong')



# # # # # # # # # # Input 5 subject marks from user and display grade(eg.First class,Second class ..)
# # # # # # # # # sub1=int(input('enter subject marks'))
# # # # # # # # # sub2=int(input('enter subject marks'))
# # # # # # # # # sub3=int(input('enter subject marks'))
# # # # # # # # # sub4=int(input('enter subject marks'))
# # # # # # # # # sub5=int(input('enter subject marks'))
# # # # # # # # # total=sub1+sub2+sub3+sub4+sub5
# # # # # # # # # persentage=total/5
# # # # # # # # # print(total)
# # # # # # # # # print(persentage)

# # # # # # # # # # Display Grade
# # # # # # # # # if persentage > 75:
# # # # # # # # #     print('Ditintion')
# # # # # # # # # elif persentage>=60:
# # # # # # # # #     print('First Class')
# # # # # # # # # elif persentage >=50:
# # # # # # # # #     print('Second class')
# # # # # # # # # elif persentage>=35:
# # # # # # # # #     print('pass class')
# # # # # # # # # else:
# # # # # # # # #     print('Faill')

# # # # # # # # # Write a program to check if person is eligible to marry or not (male age >=21 and
# # # # # # # # # female age>=18)
# # # # # # # # gender=input("enter gender ")
# # # # # # # # age=int(input(' Enter Age '))
# # # # # # # # if gender=='m' and age >=21:
# # # # # # # #     print('eligible for marrage')
# # # # # # # # elif gender=='f' and age>=18:
# # # # # # # #     print("Eligible for marrage")
# # # # # # # # else:
# # # # # # # #     print('not eligible')



# # # # # # # # ## LOPPING ASSIGMENT ##
# # # # # # # # # 1. WAP to print all even numbers until n.
# # # # # # # # n=int(input('enter numbers'))
# # # # # # # # for i in range(2,n+1,2):
# # # # # # # #     print(i)




# # # # # # # # ## LOPPING ASSIGMENT ##
# # # # # # # # # 2. WAP to print all odd numbers until n.
# # # # # # # # n=int(input('enter numbers odd number'))
# # # # # # # # for i in range(1,n+1,2):
# # # # # # # #     print(i)


# # # # # # # # 3. WAP to print sum of series upto n.
# # # # # # # sum=0
# # # # # # # for i in range(1,10+1):
# # # # # # #     sum+=i
# # # # # # # print(sum)

# # # # # # # 4. WAP to print factorial of a number .
# # # # # # n=5
# # # # # # fact=1
# # # # # # for i in range(1,n+1):
# # # # # #     fact=fact*i
# # # # # # print(fact)

# # # # # # WAP to check if a given number is prime number or not.
# # # # # n=int(input('Enter number to cheak prime or not'))
# # # # # if n <=1:
# # # # #     print('not a prime ')
# # # # # else:
# # # # #     for i in range(2,n):
# # # # #         if n % i==0:
# # # # #             print('not prime')
# # # # #             break
# # # # #     else:
# # # # #         print('prime number')


# # # # # WAP to print all integers upto n that aren’t divisible by 2 and 3.
# # # # for i in range(1,20+1):
# # # #     if i %2!=0 and i % 3 !=0:
# # # #         print(i)


# # # # 8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

# # # for i in range(1,10+1):
# # #     if i % 7==0 and i % 5==0:
# # #         print(i)


# # # WAP to print all numbers in a range divisible by a given number.
# # num=int(input('Enter Number '))
# # for i in range(1,100):
# #     if i % num==0:
# #         print(i)

# # 6
# # 
# num=int(input('Enter Number '))
# sum=0
# for i in range(1,num):
#     if num % i==0:
#         sum+=i
# if num==sum:
#     print('perfect number')
# else:
#     print('Not perfact number')


# 11. WAP to check if given number Strong Number.
num=int(input('Enter number '))
n=len(str(num))
temp=num
sum=0
while temp > 0:
    digit=temp%10
    sum+=digit**n
    temp//=10
if num==sum:
    print('Armstrong number ')
else:
    print('Not Armstrong number')
