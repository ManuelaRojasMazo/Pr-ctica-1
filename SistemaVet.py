class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__medicamento=""

    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def ver_Medicamento(self):
        return self.__medicamento 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarMedicamento(self,n):
        self.__medicamento = n 


class sistemaV:
    def __init__(self):
        self.__lista_caninos = {}
        self.__lista_felinos = {}

    def verificarExisteCaninos(self,historia):
        if historia in self.__lista_caninos:
            return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False

    def verificarExisteFelinos(self,historia):
        if historia in self.__lista_felinos:
            return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False

    def verNumeroFelinos(self):
        return len(self.__lista_felinos) 
    
    def verNumeroCaninos(self):
        return len(self.__lista_caninos)

    def ingresarCaninos(self,mascota):
        self.__lista_caninos[mascota.verHistoria()]=mascota

    def ingresarFelinos(self,mascota):
        self.__lista_felinos[mascota.verHistoria()]=mascota

    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None

    def verMedicamento(self,historia):
        #busco la mascota    y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.ver_Medicamento() 
        return None

    def eliminarCaninos(self, historia):
        if masc in self.__lista_caninos:
            del self.__lista_caninos(masc)  #opcion con el pop
            return True  #eliminado con exito
        return False 
    
    def eliminarFelinos(self, historia):
        if masc in self.__lista_caninos:
            del self.__lista_felinos(masc)  #opcion con el pop
            return True  #eliminado con exito
        return False 


class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 