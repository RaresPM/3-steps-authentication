# Autentificare in trei pasi !

def getnume():
    nume = "JohnnyCage"
    input1 = input("Introduceti numele dorit: ")
    while nume != input1:
        print("Numele introdus este gresit!Incercati din nou!")
        input1 = input("Introuceti numele dorit: ")
    return nume


def getuser():
    userinput = "MortalKombat"
    string = input("Introduceti userul: ")
    while string != userinput:
        print("Userul este gresit! Incercati din nou!")
        string = input("Introduceti userul: ")
    return string


def getparola():
    parola = input("Introduceti parola: ")
    while len(parola) < 6:
        print("Parola este prea scurta!")
        parola = input("Introduceti parola: ")
    return parola


nume = getnume()
string = getuser()
parola = getparola()


def parolasecurizata(parola):
    parola_sec = hash(parola)
    return parola_sec


def getinfo(nume, string, parola):
    return nume, string, parola


parola_strong = parolasecurizata(parola)
print("Date de autentificare sunt : " + nume + "," + string + "," + parola)
print("Parola", parola, " a fost securizata si este", parola_strong)
