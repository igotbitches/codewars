"""
В небольшом городке население p0 = 1000в начале года.
Население регулярно увеличивается на 2 процента каждым годом, и,
кроме того, 50 ежегодно в городе приезжают новые жители.
Сколько лет нужно городу, чтобы население было больше или равно p = 1200населению?

p0 - популяция на данный момент
persent - на сколько процентов увеличивается популяция в год
aug - сколько людей дополнительно презжает в город каждый год
p - конечкая популяция, на которой программа должна остановиться и выыести, сколько
лет понадобилось, чтобы достичь такой популяции"""


def nb_year(p0, percent, aug, p):
    percent /= 100
    year = 0
    while p > p0:
        p0 = p0 + p0*percent + aug
        year += 1
    return year

print(nb_year(1500000, 0.25, 1000, 2000000))