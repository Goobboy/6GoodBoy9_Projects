# sorry this will be a bit flawed...I will few numbers... goodluck decrypting without the key and code.
import random

sabai = "QWERTYUIIOPASDFGHJKLZXCVBNMqwertyuiopasadfghjjklzzxcvbnm.,?+-_=@1234567890!!"

capital = "QWERTYUIOPASDFGHJKLZXCVBNM"
small = "qwertyuiopasdfghjklzxcvbnm"


def yeuata(message):
    global letter
    emp = ""

    for i in range(len(message)):
        letter = message[i]

        if task == "I":
            if small.count(letter) == 1:
                try:
                    emp = emp + small[(small.index(letter) + 2)]
                except:
                    t = len(small) - small.index(letter)
                    t1 = type - t

                    emp = emp + small[t1]

            elif capital.count(letter) == 1:
                try:
                    emp = emp + capital[(capital.index(letter) + 5)]
                except:
                    t = len(small) - capital.index(letter)
                    t1 = type - t
                    emp = emp + capital[t1]

            else:
                emp = emp + letter

        elif task == "D":
            if small.count(letter) == 1:
                try:
                    emp = emp + small[(small.index(letter) - 1)]
                except:
                    t = type - small.index(letter)
                    t1 = len(small) - t

                    emp = emp + small[t1]

            elif capital.count(letter) == 1:
                try:
                    emp = emp + capital[(capital.index(letter) - type)]
                except:
                    t = type - capital.index(letter)
                    t1 = len(capital) - t

                    emp = emp + capital[t1]

            else:
                emp = emp + letter

    return emp

def jnik():
    d = sabai[int(random.randint(0, len(small) - 1))]
    return d


def ulto(work):
    raaa = ""
    for i in range(0, 1):
        raaa = raaa + work[i]

    num = 0
    for i in range(2, len(work)):
        if num == chabi:
            num = 0
            pass
        else:
            raaa = raaa + work[i]
            num = num + 1
    return raaa


def deco(work):
    raaa = ""
    shit = ""
    for i in range(0, 2):
        if i == 0:
            raaa = raaa + work[i]
        if i == 1:
            shit = shit + work[i]
    check = 0
    num = 0

    for i in range(2, len(work)):
        if num == chabi:
            shit = shit + work[i]
            num = 0
            pass
        else:
            raaa = raaa + work[i]
            num = num + 1
        if (shit != code) and (len(shit) == (len(small) - len(code))):
            rad = ""
            for i in range(len(message)):
                rad = rad + message[int(random.randint(0, 12 - 1))]
            return rad
    return raaa


def opo(x):
    return x[::-1]


code = input("Code word:")
type = int(input("Type:"))

task = input("Encryption(I) or Decryption (D)?")
message = input("CODE message:")

chabi = int(((len(small) - len(code)) + 3) / type)

n = 0
n1 = ""
axe = ""

if task == "I":

    message = yeuata(message)

    for index, i in enumerate(message):
        axe = axe + message[index]
        if index % chabi == 0:
            axe = axe + code[n]
            n = n + 1
            if n == ((len(small) - len(code))):
                n = 0

    axe = opo(axe)

    for index, i in enumerate(axe):
        axe = axe + axe[index]
        if index % chabi == 0:
            axe = axe + jnik()
            n = n + 1
            if n == ((len(small) - len(code))):
                n = 0

    print("->", axe)

elif task == "D":
    n1 = ulto(message)
    revie = opo(n1)
    rampa = deco(revie)
    print("->", yeuata(rampa))

print("\n\n")
print("__________Task Completed__________")

input("Press Enter to exit.")
exit()
