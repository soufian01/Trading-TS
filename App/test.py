# Funzione che preso un numero mi rritoan M se in milioni, t se in trilioni, b se in bilioni, k se in migliaia e niente se in unità con solo due cifre decimali prende in ingresso la colonnaa di un df
def abbrevia_numero(numero):
    if numero >= 1000000000:
        return str(round(numero / 1000000000, 2)) + 'B'
    elif numero >= 1000000:
        return str(round(numero / 1000000, 2)) + 'M'
    elif numero >= 1000:
        return str(round(numero / 1000, 2)) + 'k'
    else:
        return str(round(numero, 2))
    

print(abbrevia_numero(123123123123))
print(abbrevia_numero(453453453))
print(abbrevia_numero(453453))
print(abbrevia_numero(453))
