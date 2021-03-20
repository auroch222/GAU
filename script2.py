import random
import statistics


# 2.შეიტანეთ სამი რიცხვი, იპოვეთ მათ შორის მაქსიმუმი და დაბეჭდეთ შედეგი. გამოიყენეთ max ფუნქცია.
# numers_list = []
# for a in range(1, 4):
#     number = int(input('Please Enter Number: '))
#     numers_list.append(number)
# print('Max Value From this numbers is {}'.format(max(numers_list)))
##########################################################################
# 6. დააგენერირეთ 10 შემთხვევითი მთელი რიცხვი და დაბეჭდეთ ეკრანზე. მითითება: გამოიყენეთ ციკლის ოპერატორი.
# for a in range(0, 10):
#     print(random.randint(0, 1000))
##########################################################################
# 8. დაწერეთ ფუნქცია, რომელსაც არგუმენტად გადაეცემა ორი რიცხვი და დაითვლის
# მათ საშუალო არითმეტიკულს და დაბეჭდავს შედეგს (გაითვალისწინეთ რომ
# დაბეჭდვა უნდა მოხდეს ფუნქციის შიგნით - ფუნქცია არ აბრუნებს
# მნიშვნელობას). გამოიძახეთ ფუნქცია 3-ჯერ სხვადასხვა რიცხვებისთვის.

# def average(a: int, b: int):
#     result = (a + b) / 2
#     print(result)
#
# for a in range(0, 3):
#     numbers1 = int(input('Please Enter Number1: '))
#     numbers2 = int(input('Please Enter Number2: '))
#     average(numbers1, numbers2)
##########################################################################
# 11.დაწერეთ ფუნქცია, რომელიც შეამოწმებს პარამეტრად გადაცემული რიცხვი არის
# თუ არა კენტი. თუ კენტია, დააბრუნოს მნიშვნელობა True, თუ არადა - False.
# შეამოწმეთ რამდენიმე რიცხვისთვის და დაბეჭდეთ შედეგი.
# def checkNum(a: int):
#     if a % 2 == 0:
#         return True
#     else:
#         return False
# for a in range(0, 10):
#     number = random.randint(1, 1000)
#     print("Chosen Number is {}" . format(number))
#     print(checkNum(number))

# 15. შექმენით სია numbs ნებისმიერ 5 რიცხვითი მნიშვნელობით. იპოვეთ ამ რიცხვების
# ჯამი, მინიმალური, მაქსიმალური და საშუალო არითმეტიკული. ასევე შეასრულეთ
# შემდეგი ოპერაციები:
# • სიას დაამატეთ ბოლო ელემენტად რიცხვი 102
# • სიის მესამე ელემენტად ჩასვით რიცხვი 205
# • წაშალეთ სიის მე-4 ელემენტი
# • დაალაგეთ სია ზრდადობის მიხედვით და დაბეჭდეთ.
# def average(rec: list):
#     number = len(rec)
#     return sum(rec) / number
#
#
# list_example = [40, 20, 30, 10, 50]
# print("Min Is {}".format(min(list_example)))
# print("Sum Is {}".format(sum(list_example)))
# print("Max Is {}".format(max(list_example)))
# print("Average Is {}".format(average(list_example)))
# list_example.append(102)
# list_example[2] = 205
# print(list_example)
# list_example.pop(3)
# print(list_example)
# list_example.sort()
# print(list_example)
##########################################################################
# 19. დაწერეთ პროგრამა, რომელიც რიცხვითი მნიშვნელობების სიაში ამოშლის კენტ
# რიცხვებს. დაბეჭდეთ მიღებული სია.
# list_example = [10, 11, 12, 13, 14, 15]
# for i, number in enumerate(list_example):
#     if number % 2 != 0:
#         list_example.pop(i)
# print(list_example)
##########################################################################
# 21. შექმენით 10 ელემენტიანი სია, რომლის ელემენტებია ნებისმიერი შემთხვევითი
# მთელი რიცხვები 25-დან 110-მდე. დაბეჭდეთ სია და იპოვეთ მინიმალური
# ელემენტი.
# list_example = []
# for a in range(1, 11):
#     list_example.append(random.randint(25, 100))
#
# print(list_example)
##########################################################################
# 24. შექმენით სია რიცხვითი ელემენტებით. shuffle ფუნქციის გამოყენებით (random
# მოდულიდან) მოახდინეთ სიის ელემენტების შემთხვევითად არევა და დაბეჭდეთ
# მიღებული სია. (მითითება: ფუნქცია იწერება შემდეგნაირად: random.shuffle(x)
# სადაც x სიის დასახელებაა)
# list_example = [2, 3, 4, 5, 76, 21, 21]
# random.shuffle(list_example)
# print(list_example)
##########################################################################
# 27. იპოვეთ სიაში [1, 5, 23, 5, 12, 2, 5, 1, 18, 5] ყველაზე ხშირად განმეორებადი რიცხვი.
# დაბეჭდეთ შედეგი. ასევე მიუთითეთ რამდენჯერ შეგხვდათ სიაში ყველაზე
# ხშირად განმეორებადი რიცხვი.
# list_example = [1, 5, 23, 5, 12, 2, 5, 1, 18, 5]
# dict_example = {}
# for a in list_example:
#     dict_example[a] = list_example.count(a)
#
# a = max(dict_example, key=dict_example.get)
# print('Max Number Is {} and its value is {}'. format(a, dict_example[a]))
##########################################################################
# 29. სტრიქონი python php pascal javascript java c++; წარმოადგინეთ სიის სახით
# (სტრიქონის თითოეული სიტყვა სიის თითოეული ელემენტად). იპოვეთ სიის
# ყველაზე გრძელი ელემენტი (ანუ ყველაზე გრძელი სიტყვა).
# string_example = 'python php pascal javascript java c++'
# list_example = string_example.split(' ')
# dict_example = {}
# for a in list_example:
#     dict_example[a] = len(a)
#
# a = max(dict_example, key=dict_example.get)
# print('Max Number Is {} and its value is {}'. format(a, dict_example[a]))
##########################################################################
# 30. შეიტანეთ სიის 10 ელემენტი. იპოვეთ ამ რიცხვების საშუალო არითმეტიკული,
# მედიანა და მოდა. გაითვალისწინეთ, მედიანა წარმოადგენს შუა ელემენტს,
# როდესაც რიცხვები დალაგებულია ზრდადობით (ან კლებადობით); თუ შუაში ორი
# ელემენტია, მაშინ მედიანა არის ამ შუა ელემენტების საშუალო არითმეტიკული.
# მოდა, არის მიმდევრობაში რიცხვი, რომელიც ყველაზე ხშირად გვხვდება.
# შეიძლება მიმდევრობას არ ქონდეს მოდა (თუ ყველა ელემენტს ერთნაირი სიხშირე
# აქვს), ან ქონდეს ერთი ან რამდენიმე მოდა.
def average(a: list):
    result = sum(a) / len(a)
    return result


list_example = [1, 2, 4, 3, 6, 7, 5, 9, 10, 8, 8]
print('Average is {}'.format(average(list_example)))
print('Median is {}'.format(statistics.median(list_example)))
print('Mode is {}'.format(statistics.mode(list_example)))
