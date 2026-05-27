print ('no sabia que poner bue soy el mejor enserio')


print ('_______________Bienvenido a la calculadora_________________')
print ()
print ()
operacion =input('ingresa la operacion que quieres hacer:\n1. Suma\n2. Resta\n3. Multiplicacion\n4. Division ')

num1 = float(input('Primer numero: '))
num2 = float(input('Segundo numero: '))



if operacion == 'Suma':
    resultado = num1 + num2     
    print('El resultado de la suma es: ', resultado)    
elif operacion == 'Resta':
    resultado = num1 - num2
    print('El resultado de la resta es: ', resultado)
elif operacion == 'Multiplicacion':
    resultado = num1 * num2
    print('El resultado de la multiplicacion es: ', resultado)  
elif operacion == 'Division':
    if num2 != 0:
        resultado = num1 / num2
        print('El resultado de la division es: ', resultado)
    else:
        print('Error: No se puede dividir por cero.')
