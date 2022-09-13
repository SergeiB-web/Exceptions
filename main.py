#a = input("чbсло")
#b = input("число")
#try:
#    print(int(a)+int(b))
    #except (ValueError,TypeError) :
#    print("Нельзя складывать строку с числом")
#    print("Нельзя складывать строку со строкой")

from datetime import datetime
human = datetime(1996, 9, 25)
print(human)
now = datetime.now()
print(now.date())
print(now.year - human.year)

