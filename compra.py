#Compra >50€ = 15%
#Compra <=30€ = 'Mensaje: tienes que llegar hasta 50€
#Compra 0-20€ = No descuento

print('PRODUCTOS:')
print('Agua = 4.5€')
print('Cerveza = 5.5€')
print('Leche = 12€')


producto1 = str(input('Selecciona un producto: '))
precio1 = float(input('Introduce su precio: '))
cantidad1 = int(input('Introduce la cantidad del producto: '))
producto2 = str(input('Selecciona un producto: '))
precio2 = float(input('Introduce su precio: '))
cantidad2 = int(input('Introduce la cantidad del producto: '))
producto3 = str(input('Selecciona un producto: '))
precio3 = float(input('Introduce su precio: '))
cantidad3 = int(input('Introduce la cantidad del producto: '))

subtotal1 = precio1 * cantidad1
subtotal2 = precio2 * cantidad2
subtotal3 = precio3 * cantidad3
total = subtotal1 + subtotal2 + subtotal3
iva = total * 0.21

if total > 50:
    descuento = total * 0.15 
    precioFinal = total + iva - descuento
    print(f'El descuento de su compra es: {descuento:.2f}€ \n'
    f'El iva de su compra es: {iva:.2f}€ \n'
    f'El total de su compra es: {precioFinal:.2f}€')

elif total > 20 and total <= 30 :
    print(f'Su compra es de {total:.2f}€, si desea optar a un descuento introduce tu CP, por favor')
    opcion = str(input('Y/N').upper())
    if opcion == 'Y':
        cp = int(input('C.P: '))
        descuento = total * 0.5
        precioFinal = total + iva - descuento
        print(f'El descuento de su compra es: {descuento:.2f}€ \n'
        f'El iva de su compra es: {iva:.2f}€ \n'
        f'Muchas gracias, el total de su compra con el descuento aplicado es: {precioFinal:.2f}€')  

else:
    precioFinal = total + iva
    print(f'El iva de su compra es: {iva:.2f}€ \n'
    f'El total de su compra es: {precioFinal:.2f}€') 