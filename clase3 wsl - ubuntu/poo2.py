

def main():
    class Persona():
        def __init__(self):
            self.nombre = input("ingrese el nombre: ")
            self.apellido = input("ingrese el apellido: ")
            self.direccion = input("ingrese la direccin: ")
            self.telefono = input("ingrese el telefono: ")

        def mostrarPersona(self):
            print(f"nombre: {self.nombre} {self.apellido}")

    

    #Persona1 = Persona()
    #Persona1.mostrarPersona()   

    #persona2 = persona()
    #persona2.mostrarPersona()

    class Empleado(Persona):
        def __init__(self):
            super().__init__()
            self.__sueldo = float(input("ingrese el sueldo: "))
            self.alimentacion = 0
            self.transporte = 0
            self.pension = 0
        def mostrarEmpleado(self):
            super().mostrarPersona()
            print(f"sueldo: {self.__sueldo}")
            print(f"transporte: {self.transporte}")
            print(f"alimentacion: {self.alimentacion}")
            print(f"pension: {self.pension}")

    Empleado1 = Empleado()
    #Empleado1.__sueldo = 4000000
    Empleado1.mostarEmpleado()
            



if __name__=="__main__":
    main()
