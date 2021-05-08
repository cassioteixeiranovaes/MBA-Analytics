#%%
def calculadora(numero1,numero2,operador):
    if operador == '+':
        resultado=numero1 + numero2
    if operador == '-':
        resultado=numero1 + numero2
    if operador == '*' or operador == 'x':
        resultado=numero1 * numero2
    if operador == '/' :
        if numero2 == 0:
            print('Não é possivel fazer divisão por zero')
            resultado=0
        else :
            resultado=numero1 / numero2
    if operador == '^' or operador == '**':
            resultado=numero1 ** numero2
    return resultado

resultado=calculadora(10,2,'*')
print(resultado)

