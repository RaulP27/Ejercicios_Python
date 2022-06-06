#3.	Elabore un programa POO, en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular con estos dos valores la suma, resta, multiplicación y división. Utilizar un método para cada una de las operaciones e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

class Calculadora:
  def __init__(valores):
    valores.primero=int(input("Ingrese el primer digito: "))
    valores.segundo=int(input("Ingrese el segundo digito: "))
  
  def suma(valores):
    valores.suma=(valores.primero + valores.segundo)

  def resta(valores):
    valores.resta=(valores.primero - valores.segundo)

  def multiplicacion(valores):
    valores.multi=(valores.primero * valores.segundo)
      
  def division(valores):
    valores.divi=(valores.primero / valores.segundo)

  def resultado(valores):
    print("La suma es: ", valores.suma)
    print("La resta es: ", valores.resta)
    print("La multiplicacion es: ", valores.multi)
    print("La division es: ", valores.divi)
    
math=Calculadora()
math.suma()
math.resta()
math.multiplicacion()
math.division()
math.resultado()
