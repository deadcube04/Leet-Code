

def auxiliarValidation(number: str)-> bool:
    cont = 1
    for i in range(len(number)-1):
        if number[i] == number[i+1]:
            cont+=1
        else:
            cont = 1
        if cont >= 4:
            return False
    return True


def validadeCard(number: str) -> bool:
    if(number.isdecimal()):
        if (number.startswith(("4", "5", "6")) and len(number) == 16):
           return auxiliarValidation(numero)
        return False  
    else:
        if '-' in number and number.count('-') == 3:
            lista = number.split("-")
            for j in lista:
                if len(j) != 4:
                    return False
            numero = "".join(lista)
            return auxiliarValidation(numero)
        
    return False


n = int(input())
for k in range (n):   
    s = input()
    print("Valid") if validadeCard(s) else print("Invalid")
    