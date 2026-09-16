pienin = None
suurin = None

while True:
    luku = input("Anna luku: ")

    if luku == "":
        break

    luku = float(luku)

    if pienin == None:
        pienin = luku
        suurin = luku

    if luku < pienin:
        pienin = luku

    if luku > suurin:
        suurin = luku

print("Pienin:", pienin)
print("Suurin:", suurin)