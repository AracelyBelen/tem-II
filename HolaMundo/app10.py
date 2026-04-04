# funciones - bloques de codigo que realiza una tarea especifica y que son reutilizables
# funcion sin parametros ni devolucion de valor
def saludar():
    print('hola, bienvenidos a curso de python')
    
# funcion con parametros
def saludo(nombre):
    print('hola '+nombre+' bienvenido a clases')
    
# funcion que devuelve valores
def suma(a,b):
    return a + b
# establecer valores por defecto para los parametros de una funcion 
def bienvenida(nombre='estudiante'):
    print('bienvenido ',nombre) 

# funcion con argumentos variables
def sumador(*args):
    return sum(args)
   
# llamar a la funcion 
saludar()
saludo('bruno diaz')
resultado = suma(10,4)
print('la suma es: ', resultado)
bienvenida('susana')
print(sumador(1,2,3,4,5))
print(sumador(4,5,6))