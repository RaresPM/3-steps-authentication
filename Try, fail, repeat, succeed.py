# Autentificare in trei pasi !

def getnume():
    count = 3
    name = "JohnnyCage"
    input1 = input("Introduceti numele dorit: ")
    while name != input1:
        if count > 0:
            print("Numele este gresit!Mai aveti " + str(count - 1) + " incercari! Incercati din nou!")
            input1 = input("Introduceti numele: ")
            count -= 1
        if name == input1:
            print("Ati introdus numele corect! Treceti la urmatoarea etapa.")
        elif count == 0:
            print("Ati atins limita de incercari!Incercati peste 3 ore!")
            count -= 1
        elif count == 3:
            break
    return input1


def getuser():
    count = 3
    userinput = "MortalKombat"
    user = input("Introduceti userul: ")
    while user != userinput:
        if count > 0:
            print("Userul este gresit!Mai aveti " + str(count - 1) + " incercari! Incercati din nou!")
            user = input("Introduceti userul: ")
            count -= 1
        if user == userinput:
            print("Ati introdus userul corect! Treceti la urmatoarea etapa.")
        elif count == 0:
            print("Ati atins limita de incercari! Incercati peste 3 ore!")
            count -= 1
        elif count == 3:
            break
    return user

def getparola():
    parola = input("Introduceti parola: ")
    while len(parola) < 8:
        print("Parola este prea scurta!")
        parola = input("Introduceti parola: ")
    return parola


def parolasecurizata(parola):
    parola_sec = hash(parola)
    return parola_sec


numele = getnume()
string = getuser()
parola = getparola()
parola_strong = parolasecurizata(parola)
print("Datele de autentificare sunt : " + numele + "," + string + "," + parola)
print("Parola", parola, " a fost securizata si este", parola_strong)
