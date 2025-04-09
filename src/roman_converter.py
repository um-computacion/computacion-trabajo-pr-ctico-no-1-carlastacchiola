def decimal_to_roman(numero):
    valores_romanos = {
          1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 50:
          'L', 100: 'C', 500: 'D', 1000: 'M' }
    resultado = ''
    for valor in sorted(valores_romanos.keys(), reverse=True):
        while numero >= valor:
            resultado += valores_romanos[valor]
            numero -= valor
    return resultado
numero = int(input('Insertar un numero decimal: '))
if 1 <= numero <= 3999:
        roman = decimal_to_roman(numero)
        print('numero romano: ', roman)
else:
        print("Error: el número debe estar entre 1 y 3999")
        

        