leiviskat = int(input("Anna leiviskät "))

naulat = int(input("Anna naulat "))

luodit = int(input("Anna luodit "))


grammat = (leiviskat * 20 * 32 + naulat * 32 + luodit) * 13.3

kilogrammat = int(grammat / 1000)

grammat_jaljella = grammat - kilogrammat * 1000


print("Massa on", kilogrammat, "kilogrammaa ja", grammat_jaljella, "grammaa")