import heapq

cola = []


menu = """
1. Registrar un paciente que llega
2. Consultar el siguiente paciente
3. Sacar al siguiente paciente
4. Eliminar un paciente de la lista de llegados
5. Ver las citas pendientes
6. Salir

Dime que quieres hacer: 
"""
continuar = True
while continuar:

    respuesta = input(menu) #string

    match respuesta:
        case "1": # 1. Registrar un paciente que llega
           nombre = input("Vas a pedir cita, dime tu nombre: ")
           hora = float(input("Dime la hora: (11,12, 13)"))
           heapq.heappush(cola, (hora,nombre)) # [(10, Alejandro), (11, Pedro)]
           print("Añadido a cola. Espera tu turno...")

        case "2": # 2. Consultar el siguiente paciente
            nombre_paciente = cola.popleft() # sale de la lista
            print(f"El siguiente en salir es {cola[0][1]}, que tiene cita a las {cola[0][0]}")
        case "3": # 3. Sacar al siguiente paciente
            hora, paciente = heapq.heappop(cola) # sacamos el que tiene la siguiente hora
            print(f"Que pase el siguientes que es {paciente} hora de referenia {hora}")
        case "4":# 4. Eliminar un paciente de la lista de llegados
            nombre = input("Dime el nombre del paciente que quieres eliminar")
            hora = float(input("Dime la hora que tenia ese paciente"))
            
            cola.remove((hora, nombre))
            # Devolver la estructura de cola de prioridad (heapq) a la cola.
            heapq.heapify(cola)
            
            print(f"El paciente {nombre}, ha salido de la cola.")
        case "5": # 5. Ver las citas pendientes (ordenados)
            #sin ordenar seria print(cola)
            i = 1
            cola_aux = cola
            while  cola:
                hora, nombre = heapq.heappop(cola) 
                print(f"{i}. El paciente {nombre} a las {hora}")
                i+=1
            cola = cola_aux
        case "6": #6. Salir
            print(f"Saliendo...")
            continuar = False
        case _:
            print("Prueba otra vez")  # Equivalente a 'default'
    