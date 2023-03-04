# mastring = "The ya ya ya ya"
# my_list = mastring.split(' ')
# print(my_list)

# import pytz

# utc = pytz.utc
# dt = datetime.datetime.now(utc)
# print("TimeZome", dt.strftime("%2"))

# import random
# print(random.random())
# print(random.randint(1, 4))
# print(random.randrange(2, 10, 2))
# print(random.uniform(1.0,2.0))


# language = input()
# print("Welcome to", end=" ")
# if language == "Python":
#     print("Senior Python Developer")
# elif language == "Java":
#     print("Senior Java Developer")
# elif language == "C++":
#     print("Senior C++ Developer")
# elif language == "JavaScript":
#     print("Senior JavaScript Developer")

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squares = [numbers * number for number in numbers]

# fruits = ["Apple", "Pear", "Peach", "Banana"]
# prices = [0.35, 0.40, 0.40, 0.23]
# fruit_dictory = dict(zip(fruits, prices))
# print(fruit_dictory)

# simple = [1 for i in range(10)]
# print(simple)

# hard = [[x, y] for x in range(1, 4) for y in range(1, 4)]
# print(hard)

# list = [1, 4, 4, 4, 2, 5, 6, 6, 7, 8, 9, 10]
# frequet = max(set(list), key=list.count)
# print(frequet)


# list = [10,20,30,40,50,60,70]

# fir i,red in enumerate(list)
# print(i, ":", res)

# print(my_dict['c']) #error

# print(my_dict.get('c')) #none

# print(round(10.7)) #11
# print(round(1.4))  #1
# print(round(2.5))  #2
# print(round(24.4)) #24
# Функция round()
# Очень простая оттого не менее полезная функция. Округляет дробные числа до целых. По следующим правилам. Если дробная часть больше 0.5, то округляем в большую сторону. Если меньше - в меньшую.
# В качестве аргумента принимает дробное число.


# subjects = ('Python', 'Coding', 'Tips',)
# for i, subjects in enumerate(subjects):
#     print(i, subjects)
# Использование функции enumerate()
# Функция enumerate() добавляет счетчик в итерируемый объект, в котором используется метод iter , возвращающий итератор. Он может принимать последовательные значения индекса, начиная с нуля. И выдаёт ошибку IndexError, когда индексы больше недействительны.
# Типичный пример использования функции enumerate() — создание цикла по списку с отслеживанием индекса. Для этого можно использовать переменную в качестве счетчика. Но функция enumerate() позволяет сделать то же самое намного удобнее.


# print(bool(1))
# #True
# print(bool(-1))
# #True
# print(bool(0))
# #FALSE
# print(1 and 0)
# #0 true and  false = false

# print(-1 and 0)
# -1 true or false = true

# for part in ["prog", "lib", ".io", "/n"]:
#     print(part, end="")
#proglib.io/n

# programmer = ["alex", "Jake", "sonya"]
# for i, value in enumerate(programmer):
#  print(i, value)
 #Alex
 #jake
 #sonya