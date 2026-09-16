unnus = "Leevi"
salasana = "0000"
yritykset = 0

while yritykset <= 5:
    kayttaja =input("Käyttäjätunnus: ")
    salasana1 =input("Salasana: ")

    if kayttaja == tunnus and salasana1 == salasana:
        print("Tervetuloa")
        break

    yritykset =yritykset + 1

if yritykset ==5:
    print("Pääsy estetty")