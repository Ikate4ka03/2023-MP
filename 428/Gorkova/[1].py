
import datetime
from queue import Queue 

my_data = ("Горькова Екатерина Алексеевна", 23, 11, 2003)

disc_marks = {
    "Русский_язык": 4, 
    "Литература": 4, 
    "Алгебра": 5, 
    "История": 5, 
    "ОБЖ": 5,
    "Геометрия": 5,
    "Обществознание": 5,
    "Физкультура": 5,
    "География": 5,
    "Музыка": 5,
    "Английский_язык": 4,
    "Информатика": 5,
    "Биология": 5,
    "Химия": 4,
    "Технология": 5
    }

family_names = ["Екатерина","София", "Елена", "Андрей", "Андрей", "Ольга", "Ирина", "Арина", "Кирилл", "Алексей","Галина","Василий"]

kiwa_name = "Муся"


#1) Средняя оцнка в аттестате

average_mark = sum(disc_marks.values()) / len(disc_marks.values())

print("1)Cредняя оценка в аттестате:")
print(average_mark)

print("____________________________________________________________________________________________")

#2) Уникальные имена среди родственников

unique_names = []
for name in family_names:
    if name in unique_names:
        continue
    unique_names.append(name)
    
print("\n"+"2)Уникальные имена:")
print(*unique_names)
    

print("____________________________________________________________________________________________")

#3) Общая длина всех названий предметов

lenght=0
for i in list(disc_marks):
    lenght+=(len(i))
    
print("\n"+"3)Общая длина всех названий предметов:"+"\n"+str(lenght))

print("____________________________________________________________________________________________")


#4) Уникальны буквы в назыании предмета

p_letter = []
for letter in list(disc_marks):
    p_letter.extend(list(set(letter)))
    
print("\n"+"4)Уникальные буквы" )

unique_letter=set(p_letter)
print(*unique_letter)

print("____________________________________________________________________________________________")

    
#5) Имя пушистой киви в бинарном виде

print("\n"+"5)Имя киви в бинарном виде:")

for ch in bytearray(kiwa_name, 'utf-8'):
    print(bin(ch))


print("____________________________________________________________________________________________")

#6) Отсортированный по алфавиту (в обратном порядке) список родственников;  

print("\n"+"6)Отсортированный по алфавиту (в обратном порядке) список родственников:")

sorted_names = sorted(family_names)
family_names.sort()
family_names.reverse()

print(*family_names)

print("____________________________________________________________________________________________")


#7) Количество дней от вашей даты рождения до текущей даты (должна быть всегда актуальной)

today = datetime.datetime.now()

birthday = datetime.datetime(2003,11,23)

time_diff =today - birthday 

print("\n"+"Количество дней от вашей даты рождения до текущей даты:",  time_diff.days)

print("____________________________________________________________________________________________")


#8) FIFO очередь, в которую можно добавлять предметы по вводимому с клавиатуры индексу (до команды остановки), после введения - вывести все;

q=Queue()

print("\n"+'Чтобы прекратить ввод нажмите Enter: ')

for i in list(disc_marks):
    q.put(i)

while True:
    disc=input('  ')
    if disc=='':
        break
    else:
        q.put(disc)
print("8)Вывод всех предметов,после ввода с клавиатуры:")

while True:
    print(q.get(),sep = "\n")
    if q.empty()==True:
        break

print("____________________________________________________________________________________________")


#9) По введеному индексу, поменять имя в отсортированном списке родственников на имя ацтекского правителя (https://en.wikipedia.org/wiki/List_of_rulers_of_Tenochtitlan) под номером, получаемым из вашей даты рождения: number = (day + month**2 + year) % 21 + 1;

number=(int(my_data[1])+int(my_data[2])**2+int(my_data[3]))%21+1

index=int(input("\n"+"Введите индекс от 0 до 11:"))

if index<0 or index>11:
    print("ERROR")
else:
    new_name="Tenocotzin"
    family_names[index]=new_name
    print("9) Обновлённый список имён:"+"\n", *family_names, sep = "\n")

print("____________________________________________________________________________________________")


#10) создать связный список, например, как словарь, где ключ - имя родственника, а значение (ссылка на следующий элемент) - индекс следующего имени по исходному списку, упорядоченному по их (родственников) годам рождения), исходный список при этом должен остаться неизменным;

new_family_names= {"Василий 1945":1, "Галина 1946":2, "Ольга 1953":3, "Елена 1979":4, "Ирина 1979":5, "Алексей 1980":6,
                    "Андрей 1981":7,"Андрей 1989":8, "Екатерина 2003":9, "София 2014":10, "Кирилл 2016":11, "Арина 2021":0}

print("10)Связный список, где ключ - имя родственника, а значение - индекс следующего имени по исходному списку, упорядоченному по годам рождения:\n", *new_family_names, sep = "\n")

print("____________________________________________________________________________________________")



#11) написать функцию-генератор, свой вариант определяется как number = len("ФИО") * len (family_names) % 4:

generator = len(my_data[0]) * len (family_names) % 4

#print(len(my_data[0]))
#print(len (family_names))

print("\n"+"11) Number=",generator, "-аликвотная последовательность")

#Генератор аликвотной последовательности

def aliquot_sequentially(generator):
    a = 0
    for i in range(10):
        yield a
        a = a + generator
        if a == 0:
            break
