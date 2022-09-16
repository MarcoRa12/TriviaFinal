# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
#Importar libreria random
import random 
#Agregare el puntaje
puntaje = random.randint(0 , 10)
#Agregando time
import time 
# numero de intentos
r_trivia = True
n_intentos =0
#colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

print(GREEN + "Bienvenido a mi trivia sobre The flash")
print(RED+"\nPondremos a prueba tus conocimientos")
time.sleep (2)
print("Comenzaras con un puntaje aleatorio que como máximo tendrá 10 "+RESET)
print(YELLOW+"\nTienes",puntaje,"puntos.")
print("Cada respuesta correcta equivale a un puntaje que será aleatorio que como máximo sera 10")
print("Cada respuesta incorrecta equivale a  menos un puntaje que sera aleatorio como máximo -10 "+RESET)
# Agregamos los datos del jugador
while r_trivia == True :
     n_intentos += 1
     time.sleep(2)
     print("Cantidad de intentos : ", n_intentos)
     nombre = input("Ingresa tu nombre: ")
     time.sleep(1)
     apellido = input("Ingrese su primer apellido : ")


# Es importante dar instrucciones sobre cómo jugar:
     time.sleep(1)
     print("\nHola", nombre,apellido,
     "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")

#Variable de conteo
     conteo = 0
     for conteo in range (5 ,0 ,-1) :
        print(conteo,".... " )
        time.sleep(1)
# Pregunta 
     print("")
     print(GREEN+"1)¿Quien creo flash point?"+RESET)
     time.sleep (1)
     print(WHITE+"a)Savitar")
     print("b)Flash")
     print("c)Godspeed")
     print("d)Caitlin"+RESET)

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
     respuesta_1 = input("\nTu respuesta: ")

#Validacion
     while respuesta_1 not in ("a","A","b","B","c","C","d","D","x","X"):
         print("Debes responder  a,b,c o d . ")
         print("")
         print(GREEN+"1)¿Quien creo flash point?"+RESET)
         time.sleep (1)
         print(WHITE+"a)Savitar")
         print("b)Flash")
         print("c)Godspeed")
         print("d)Caitlin"+RESET)
         respuesta_1 = input("Ingrese nuevamente la respuesta: ")
    
#condicional 
     if respuesta_1 == "b" or respuesta_1 =="B":
         puntaje += random.randint(0 , 10)
         print(nombre,apellido,"la respuesta que has escogido es la  correcta")
         print("Tu puntaje actual es : ",puntaje)
     elif respuesta_1 == "x" or respuesta_1== "X":
         puntaje +=random.randint(0 , 10)
         print('Este es un mensaje secreto : la respuesta es "b" , has ganado el puntaje de esta pregunta ')
         print("Tu puntaje actual es : ",puntaje)
     else:
         puntaje -=random.randint(0 , 10)
         print(nombre,apellido,"la respuesta es incorrecta")
         print("Tu puntaje actual es : ",puntaje)
#Pregunta 2 
     time.sleep (2)
     print(GREEN+"\n2)¿Quien asesinó a Harrison wells?"+RESET)
     print(WHITE+"a)Eobard thawne")
     print("b)Barry allen")
     print("c)Cisco")
     print("d)Wally"+RESET)
#Almacena la respuesta
     respuesta_2 = input("\nIngrese su respuesta: ")

#Validacion
     while respuesta_2 not in ("a","A","b","B","c","C","d","D","x","X"):
        print("Debes responder a,b,c o d .")
        print(GREEN+"\n2)¿Quien asesinó a Harrison wells?"+RESET)
        print(WHITE+"a)Eobard thawne")
        print("b)Barry allen")
        print("c)Cisco")
        print("d)Wally"+RESET)
        respuesta_2 = input("Ingrese nuevamente la respuesta: ")

#Condicional
     if respuesta_2 == "a" or respuesta_2 =="A" :
             puntaje += random.randint(0 , 10)
             print(nombre,apellido," la respuesta que has escogido es la correcta")
             print("Tu puntaje actual es : ",puntaje)
     elif respuesta_2 == "x" or respuesta_2== "X":
             puntaje += random.randint(0 , 10)
             print('Este es un mensaje secreto : la respuesta es "a", has ganado el puntaje de esta respuesta')
             print("Tu puntaje actual es : ",puntaje)
     else:
            puntaje -=random.randint(0 , 10)
            print(nombre,apellido," la respuesta que has escogido es incorrecta")
            print("Tu puntaje actual es : ",puntaje)
             
#Pregunta 3
     time.sleep (2)
     print(GREEN+"\n3)¿Quien viajo al pasado para asesinar a la madre de flash ?"+RESET)
     print(WHITE+"a)Hunter zoolemon")
     print("b)Cicada")
     print("c)Flash reverso")
     print("d)Barry"+RESET)
#Almaceno la respuesta
     respuesta_3 = input("\nIngrese su respuesta: ")

#Validacion
     while respuesta_3 not in ("a","A","b","B","c","C","d","D"):
                print("Debes responder a,b,c o d .")
                print(GREEN+"\n3)¿Quien viajo al pasado para asesinar a la madre de flash ?"+RESET)
                print(WHITE+"a)Hunter zoolemon")
                print("b)Cicada")
                print("c)Flash reverso")
                print("d)Barry"+RESET)
                respuesta_3 = input("Ingrese nuevamente la respuesta: ")

#Condicional
     if respuesta_3 == "c" or respuesta_3 == "C" :
           puntaje += random.randint(0 , 10)
           print(nombre,apellido," la respuesta que has escogido es la correcta")
           print("Tu puntaje actual es : ",puntaje)
     else:
         puntaje -=random.randint(0 , 10)
         print(nombre,apellido," la respuesta que has escogido es incorrecta")
         print("Tu puntaje actual es : ",puntaje)

#Pregunta 4  
     time.sleep (2)
     print(GREEN+"\n4)¿Gracias a quien wally se convirtio en velocista ?"+RESET)
     print(WHITE+"a)Savitar")
     print("b)Zoom")
     print("c)killer Frost")
     print("d)Jay Garrick"+RESET)

#Almaceno la respuesta
     respuesta_4 = input("\nIngrese su respuesta: ")

#Validacion
     while respuesta_4 not in ("a","A","b","B","c","C","d","D"):
               print("Debes responder a,b,c o d .")
               print(GREEN+"\n4)¿Gracias a quien wally se convirtio en velocista ?"+RESET)
               print(WHITE+"a)Savitar")
               print("b)Zoom")
               print("c)killer Frost")
               print("d)Jay Garrick"+RESET)
               respuesta_4 = input("Ingrese nuevamente la respuesta: ")

#Condicional
     if respuesta_4 == "a" or respuesta_4 == "A" :
             puntaje += random.randint(0 , 10)
             print(nombre,apellido," la respuesta que has escogido es la correcta")
             print("Tu puntaje actual es : ",puntaje)
     else:
             puntaje -=random.randint(0 , 10)
             print(nombre,apellido," la respuesta que has escogido es incorrecta")
             print("Tu puntaje actual es : ",puntaje)

#Pregunta 5
     time.sleep (2)
     print(GREEN+"\n5)¿Quién creo a savitar ?"+RESET)
     print(WHITE+"a)Zoom")
     print("b)Flash")
     print("c)Cicada")
     print("d)Se creo el mismo"+RESET)    

     print("\nSi eliges la alternativa mas indicada , tu puntaje se multiplicará por 2 , pero si su puntaje es negativo solo se le quitara este y se le añadira 2 puntos")
     print("Si eliges aquella menos  indicad , tu puntaje se sumara más 5 ")
     print("Si eliges una incorrecta  , tu puntaje se le restará 5 ")
     print("Si eliges aquella menos  indicad , tu puntaje se sumara más 5 ")
     print("Finalmente si eliges la más disparatada , tu puntaje se dividirá entre 2")

#Almaceno respuesta
     respuesta_5 = input("\nIngrese su respuesta : ")
#Validación
     while respuesta_5 not in ("a","A","b","B","c","C","d","D"):
           print("Debes responder a,b,c o d .")
           print(GREEN+"\n5)¿Quién creo a savitar ?"+RESET)
           print(WHITE+"a)Zoom")
           print("b)Flash")
           print("c)Cicada")
           print("d)Es como un bucle se creo el mismo"+RESET) 
           respuesta_5 = input("Ingrese nuevamente la respuesta: ")




#condicionales
     if respuesta_5 == "a" or respuesta_5 == "A" :
           puntaje = puntaje/2
           print("Totalmente  incorrecto!")
           print("Tu puntaje actual es : ",puntaje)

     elif respuesta_5 == "b" or respuesta_5 == "B" :
           puntaje = puntaje+5
           print("......")
           print("Tu puntaje actual es : ",puntaje)

     elif respuesta_5 == "c" or respuesta_5 == "C" :
           puntaje = puntaje-5
           print("Incorrecto!")
           print("Tu puntaje actual es : ",puntaje)
    
     elif  respuesta_5  ==  "d" or respuesta_5 == "D":
            
           if puntaje <0 :   
                 print("Su puntaje negativo se ha ido y se le incremento 2 puntos")
           else :
                 puntaje = puntaje * 2
                 print("Correcto!")
                 print("Tu puntaje actual es : ",puntaje)
  
      
#Variable de conteo
     conteo_2 = 0
     for conteo_2 in range (5 ,0 ,-1) :
        print(conteo_2,".... " )
        time.sleep(1)
        print("")

        time.sleep(1)




#Una operacion matemática

     print("Antes de terminar hagamos una operación matemática  ,")
     x = int(input("Ingrese un numero : "))
     y= int(input("Ingrese  otro numero : "))
     z = input("Ingrese el operador (+ ,- , * ,/): ")
#while
     while z not in ("+" , "-","*","/"):
        z= input("Ingresa correctamente el operador : ")


        time.sleep(2)
#condicional
     if z == "+" :
       resultado = x + y
       print("La respuesta es : ",resultado)

     if  z == "-" :
       resultado = x - y
       print("La respuesta es : ",resultado)

     if z == "*" :
       resultado = x * y
       print("La respuesta es : ",resultado)

     if z == "/" :
       resultado = x / y
       print("La respuesta es : ",resultado)

#Una ruleta rusa
     hasta = random.randint(0,3)
     print("Ruleta rusa en ejecucion : ")
     time.sleep(3)
     for puntaje in range (puntaje,hasta,-5):
           print("Tu puntaje es : ", puntaje)
     print("\nTu puntaje final es  : " , puntaje) 
#continuar o no
     continuar = input ("¿Deseas jugar otra vez ? (si o no ) : " )
     if continuar != "si" : 
         print("Gracias por jugar ",nombre ,apellido," tu puntaje final es : ",puntaje)
         r_trivia = False
     time.sleep(2)
