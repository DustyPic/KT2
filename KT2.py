#Ülesanne 1

arv1 = int(input("Sisestage esimene arv: "))
arv2 = int(input("Sisestage teine arv: "))
number = 0

if arv1 < arv2:
    number = arv1
    while number <= arv2:
        if number % 2 == 0:
            print(number)
        number = number + 1
            
elif arv2 < arv1:
    number = arv2
    while number <= arv1:
        if number % 2 == 0:
            print(number)
        number = number + 1
        
#Ülesanne 2
tekst = []

loeFaili = open("kttekst.txt", "r")
tekst = loeFaili.read().split()

tSõnadeArv = len(tekst)
print("Sõnu on tekstis: ", tSõnadeArv)
print("Sõnad, mis on väiksemad kui 5 tähte")
for t in tekst:
    if len(t) < 5:
        print(t)
        

#Ülesanne 3
first_list = [11,15,6,13,13,25,32,11,20,5,31,16,32,29,11,13,3,29,28,24]
second_list = [5,19,16,4,12,7,2,28,34,29,29,36,6,8,24,18,31,7,1,7]
#1)
print("Mõlemas listis on järgnevad elemendid: ")
for first in first_list:
    for second in second_list:
        if first == second:
            print(first)
#2,3)
print("Väikseim number on: ")
x = 100.0
for i in first_list:
    if i < x:
        x = i
for i in second_list:
    if i < x:
        x = i
print (x)

print("Suurim number on: ")
max= 0
for i in first_list:
    if i > max:
        max=i
for i in second_list:
    if i > max:
        max=i
print(max)
#4)
avg1 = float(sum(first_list))/len(first_list)
print("Esimese listi keskmine on: ")
print (avg1)
avg2 = float(sum(second_list))/len(second_list)
print("Teise listi keskmine on: ")
print (avg2)
#5)
avg3 = float((sum(first_list)+sum(second_list))/(len(first_list+second_list)))
print("Kahe listi keskmine on: ")
print(avg3)
