# SISTEMA DE PAGOS CINE COLOMBIA

print("Bienvenido a Cine Colombia")
usuario = str(input("Por favor ingrese su usuario: "))
contraseña_ingresada = str(input("Ingresa la contraseña: "))
contraseña_correcta = "KarolG"
# La contraseña es: “KarolG”


# Contraseña erronea ciclo while (Repitiendo requerimiento)
while True:
  if contraseña_ingresada == contraseña_correcta:
      print("Contraseña correcta. Acceso concedido ", usuario)
      break
  else:
      contraseña_ingresada = str(input("Contraseña incorrecta, por favor ingrese de nuevodf la contraseña: "))
      continue

# Valor a pagar Boletas y comida
def valor_pagar():
  avatar3 = str("Avatar 3")
  avengers14 = str("Avengers 14")
  peli = str(input("Que película quiere ver (Avatar 3) o (Avengers 14): "))
  valor_pelicula = 0
  while True:
    if peli == "Avatar 3":
        valor_pelicula = 100
        print("Ha escojido Avatar 3")
        break
    elif peli == "Avengers 14":
        valor_pelicula = 200
        print("Avengers 14")
        break
    else:
        peli = str(input("Escoja una película valida: "))
        continue
  print("Valor por boleta (Sin descuento): ",valor_pelicula)
  #Espacio de espera para ejecución
  print("")
  print("Escuja uno de los siguientes lugares (Escribalo exactamente igual!)")
  print("   Cine Av Chile, 100% valor_pelicula")
  print("   Cine Gran Estación, 90% valor_pelicula")
  print("   Cine Hayuelos, 80% valor_pelicula")
  print("   Cine San Martin, 60% valor_pelicula")
  print("   Cine Bosa center, 40% valor_pelicula")
  lugar = str(input("Digite aqui su lugar: "))
  while True:
      if lugar == "Cine Av Chile, 100% valor_pelicula":
          valor_pelicula2 = valor_pelicula * 1
          break
      elif lugar == "Cine Gran Estación, 90% valor_pelicula":
          valor_pelicula2 = valor_pelicula * 0.9
          break
      elif lugar == "Cine Hayuelos, 80% valor_pelicula":
          valor_pelicula2 = valor_pelicula * 0.8
          break
      elif lugar == "Cine San Martin, 60% valor_pelicula":
          valor_pelicula2 = valor_pelicula * 0.6
          break
      elif lugar == "Cine Bosa center, 40% valor_pelicula":
          valor_pelicula2 = valor_pelicula * 0.4
          break
      else:
          lugar = str(input("Error, Digite de nuevo aqui su lugar: "))
          continue
  print("Valor por boleta (Con descuento): ",valor_pelicula2)
  #Adición de comida
  comida = str(input("Desea adicionar comida si/no: "))
  while True:
    if comida == "si":
        valor_pelicula3 = valor_pelicula2 + 20
        print("Se adiciono comida a la cuenta")
        break
    elif comida == "no":
        valor_pelicula3 = valor_pelicula2
        break
    else:
        comida = str(input("Valor invalido digite de nuevo si/no: "))
        continue
  print("Valor a pagar (Con descuento) y comida: ",valor_pelicula3)
valor_pagar()

# Definir medio de Pago
def tarjeta():
    numero_tarjeta = str(input("Digite el número de tarjeta: "))
    CVC = str(input("Pedir código de seguridad de tarjeta (123"))
    print("Transacción realizada")
tarjeta()
    




    