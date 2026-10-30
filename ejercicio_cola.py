from collections import deque
cola = deque()

# 1. Añadir cita
# 2. Atender siguiente paciente
# 3. Ver citas pendientes
# 4. Ver siguiente paciente
# 5. Salir

menu = """
# 1. Añadir cita
# 2. Atender siguiente paciente
# 3. Ver citas pendientes
# 4. Ver siguiente paciente
# 5. Salir

Dime que quieres hacer: 
"""

continuar = True
# cola --> ["Pedro", "Juan" ,....] 
while True:

    respuesta = input(menu) #string

    match respuesta:
        case "1": # 1. Añadir cita
           nombre = input("Vas a pedir cita, dime tu nombre: ")
           cola.append(nombre)
           print("Añadido a cola. Espera tu turno...")
        case "2": # 2. Atender siguiente paciente
            nombre_paciente = cola.popleft() # sale de la lista
            print(f"Puede entrar a consulta {nombre_paciente}")

        case "3": # 3. Ver citas pendientes
            #print(cola)
            print("###Lista pacientes#####")
            for i in range(len(cola)):
                print(f"{i+1}: es {cola[i]}.")
            print("######################")
        case "4":
            print(f"Siguiente paciente es: {cola[0]},")
        case "5":
            break
        case _:
            print("Otro lenguaje")  # Equivalente a 'default'
    