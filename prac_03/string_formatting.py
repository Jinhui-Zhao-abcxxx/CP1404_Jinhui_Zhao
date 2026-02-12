YEAR = 1922
MONEY = 16036
MONEY_STR = str(MONEY)
BASE_NUMBER = 2
print (MONEY)

print("{YEAR} Gibson L-5 CES for about ${MONEY1},{MONEY2}".format(YEAR=YEAR, MONEY1=MONEY_STR[:2],MONEY2=MONEY_STR[2:]))


for power in range (11):
    print("{BASE_NUMBER} ^{power:>2} is{result:>5}".format(BASE_NUMBER=BASE_NUMBER, power=power, result = BASE_NUMBER ** power))

