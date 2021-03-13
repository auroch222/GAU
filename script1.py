from numpy import binary_repr
# დაწერეთ პროგრამა, რომელიც შეყვანილ ათობით რიცხვს გადაიყვანს ორობითში.
# print(binary_repr(10))
# დაწერეთ პროგრამა, სადაც მომხმარებელი შეიყვანს 3 რიცხვს და პროგრამა დაბეჭდავს რიცხვების საშუალო. არითმეტიკულს
# number1 = int(input('Please Enter Number 1: '))
# number2 = int(input('Please Enter Number 2: '))
# number3 = int(input('Please Enter Number 3: '))
# print('Average Is ' + str((number1 + number2 + number3) / 3))
# დაწერეთ პროგრამა, რომლის მეშვეობითაც შეიტანთ ნებისმიერ რიცხვს. პროგრამამ შეამოწმოს, თუ შეყვანილი
# რიცხვი 10-ის ჯერადია, დაბეჭდოს “რიცხვი ბოლოვდება 0-ით”, თუ არადა დაბეჭდოს “რიცხვი არ ბოლოვდება 0-ით”.
# (გაითვალისწინეთ: 10-ის ჯერადი ნიშნავს რომ 10-ზე გაყოფისას ნაშთი არის 0).
# seven_input = int(input("Please Enter Number: "))
# if seven_input % 10 == 0:
#     print('რიცხვი ბოლოვდება 0-ით')
# else:
#     print('რიცხვი არ ბოლოვდება 0-ით')
# 11) დაბეჭდეთ 5-ის ჯერადი რიცხვები 20-დან 125-ის ჩათვლით.
# [print(a) if a % 5 == 0 else '' for a in range(20, 126)]
# 14) შეიყვანეთ 10 რიცხვი კლავიატურიდან ციკლის გამოყენებით. დაითვალეთ შეყვანილი რიცხვების საშუალო
# არითმეტიკული.
# number_list = []
# for a in range(1, 11):
#     number = int(input('Please Enter Number: '))
#     number_list.append(number)
# average = sum(number_list) / len(number_list)
# print("average is {}".format(average))
# 21) შეიყვანეთ 2 დადებითი მთელი რიცხვი. იპოვეთ ამ ორი რიცხვის უდიდესი საერთო გამყოფი.
# import math
# number_one = int(input("Please Enter Number 1: "))
# number_two = int(input("Please Enter Number 2: "))
# print('greatest common divisor is {}'.format(math.gcd(number_one, number_two)))
# 24) შეიყვანეთ რიცხვი კლავიატურიდან. პროგრამამ უნდა დაბეჭდოს შეყვანილი რიცხვის ყველა გამყოფი. (მაგ. 18-ის
# გამოყოფებია: 1, 2, 3, 6, 9, 18)
# number = int(input("Find all divisors"))
#
# divs = [1]
# for i in range(2,int(math.sqrt(number))+1):
#     if number%i == 0:
#         divs.extend([i,number/i])
# divs.extend([number])
# 26) დაბეჭდეთ 2-დან 1000-მდე ყველა მარტივი რიცხვი.
# import sympy
# [print(a) if sympy.isprime(a) is True else '' for a in range(2, 1000)]
# 28) შეიყვანეთ ნებისმიერი რიცხი. იპოვეთ ამ რიცხვის ციფრთა რაოდენობა და დაბეჭდეთ.
# n=int(input("Enter a number:"))
# tot=0
# while(n>0):
#     dig=n%10
#     tot=tot+dig
#     n=n//10
# print("The total sum of digits is:",tot)
# 31) შეიყვანეთ ნებისმიერი რიცხი. დაადგინეთ არის თუ არა შეტანილი რიცხვი პალინდრომი. (მითითება: პალინდრომია
# რიცხვი, რომელიც მარჯვნიდან და მარცხნიდან ერთნაირად იკითხება). მაგ. 12521
#
# n=int(input("Enter number:"))
# temp=n
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# if(temp==rev):
#     print("The number is a palindrome!")
# else:
#     print("The number isn't a palindrome!")