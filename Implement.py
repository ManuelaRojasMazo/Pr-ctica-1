from SistemaVet import *

def main():
    servicio_hospitalario = sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Salir 
                       \nUsted ingresó la opción: ''' ))

        if menu == 1:
            tipo=int(input("Ingrese el tipo de mascota (1.felino o 2.canino): "))
            if tipo == 1:
                if servicio_hospitalario.verNumeroFelinos() >= 7:
                    print("No hay espacio dispnible...")
                    continue
                historia = int(input(" ingrese la historia clinica de la mascota: "))
                if servicio_hospitalario.verificarExisteFelinos(historia) == False:
                    nombre=input("Ingrese el nombre de la mascota: ")
                    peso=int(input("Ingrese el peso de la mascota: "))
                    fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
                    medicamento=Medicamento()
                    medicamento.asignarNombre(input("Ingrese nombre del medicamento: "))
                    medicamento.asignarDosis(int(input("Ingrese dosis del medicamento: ")))
                    mas = Mascota()
                    mas.asignarNombre(nombre)
                    mas.asignarHistoria(historia)
                    mas.asignarPeso(peso)
                    mas.asignarTipo(tipo)
                    mas.asignarFecha(fecha)
                    mas.asignarMedicamento(medicamento)
                    servicio_hospitalario.ingresarFelinos(mas)

                else:
                    print("Ya existe una mascota con el numero de historia clínica ingresado.") 
            elif tipo == 2:
                if servicio_hospitalario.verNumeroCaninos() >= 7:
                    print("No hay espacio dispnible...")
                    continue
                historia = int(input(" ingrese la historia clinica de la mascota: "))
                if servicio_hospitalario.verificarExisteCaninos(historia) == False:
                    nombre=input("Ingrese el nombre de la mascota: ")
                    peso=int(input("Ingrese el peso de la mascota: "))
                    fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")

                    nm = int(input("Ingrese la cantidad de mrdicamento: "))
                    lista_med=[]

                    for i in range(0,nm):
                        medicamento=Medicamento()

                        
                        medicamento.asignarNombre(input("Ingrese nombre del medicamento: "))
                        medicamento.asignarDosis(int(input("Ingrese dosis del medicamento: ")))
                        servicio_hospitalario.li
                    mas = Mascota()
                    mas.asignarNombre(nombre)
                    mas.asignarHistoria(historia)
                    mas.asignarPeso(peso)
                    mas.asignarTipo(tipo)
                    mas.asignarFecha(fecha)
                    mas.asignarMedicamento(medicamento)
                    servicio_hospitalario.ingresarCaninos(mas)

    

                else:
                    print("Ya existe una mascota con el numero de historia clínica ingresado.") 

            
        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            if fecha != None:  
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia  clínica ingresada no corresponde con ninguna mascota en el sistema.")
          
        elif menu==3: # Ver número de mascotas en el servicio 
            numero1=servicio_hospitalario.verNumeroCaninos()
            numero2=servicio_hospitalario.verNumeroFelinos()
            print("El número de pacientes en el sistema es: " + str(numero1+numero2))

        elif menu==4:
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento=servicio_hospitalario.verMedicamento(q)
            if medicamento != None: 
                print(f"El medicamento suministrado es: {medicamento.verNombre()} con dosis {medicamento.verDosis()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        elif menu == 5: # Eliminar mascota
            tipo=int(input("Ingrese el tipo de mascota (1.felino o 2.canino): "))
            if tipo == 1:
                q = int(input("Ingrese la historia clínica de la mascota: "))
                resultado_operacion = servicio_hospitalario.eliminarFelinos(q) 
                if resultado_operacion == True:
                    print("Mascota eliminada del sistema con exito")
                else:
                    print("No se ha podido eliminar la mascota")
            elif tipo == 2:
                q = int(input("Ingrese la historia clínica de la mascota: "))
                resultado_operacion = servicio_hospitalario.eliminarCaninos(q) 
                if resultado_operacion == True:
                    print("Mascota eliminada del sistema con exito")
                else:
                    print("No se ha podido eliminar la mascota")

        elif menu==6:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")



if __name__ == "__main__":
    main()