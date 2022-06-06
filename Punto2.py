#2.	Realizar un programa POO que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Ingresar por teclado. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la calificación y si ha aprobado o no. Nota >=3 aprobó

class Alumno:
  def __init__(notas):
      notas.nombre=input("Ingrese su nombre: ")
      notas.nota=int(input("Ingrese la nota: "))

  def mostrar(notas):
      print("Nombre: ",notas.nombre)
      print("Nota: ",notas.nota)

  def aprobados(notas):
    if(notas.nota>=3):
      print("El estudiante:",notas.nombre," aprobo con: ", notas.nota)
    else:
      print("El estudiante:",notas.nombre," no aprobo con: ", notas.nota)

estudiante=Alumno()
estudiante.mostrar()
estudiante.aprobados()
