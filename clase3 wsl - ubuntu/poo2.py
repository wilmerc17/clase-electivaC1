

def main():
    class Persona():
        def __init__(self):
            self.nombre = input("ingrese el nombre: ")
            self.apellido = input("ingrese el apellido: ")
            self.direccion = input("ingrese la direccion: ")
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

            
            if self.__pension < 2000000:
                self.salud = 80000
                self.transporte = 60000

            else:
                self.alimentacion = 0
                self.transporte = 0

            self.pension = self.__sueldo *0.04
            self.salud = self.__sueldo *0.0375

            self.dev
        
            def calcularDevengado():
            dev = self.alimentacion + self.transporte
            return dev

            def calcularDeducciones():
                ded = self.pension + self.salud
                return ded


        def mostrarEmpleado(self):
            super().mostrarPersona()
            print(f"sueldo: {self.__sueldo}")
            print(f"devengado: {self.dev}")
            print(f"deducciones: {self.ded}")
            print(f"total a pagar: {self.__sueldo + self.dev + self.ded}")

       

    Empleado1 = Empleado()
    #Empleado1.__sueldo = 4000000
    Empleado1.mostarEmpleado()
            



if __name__=="__main__":
    main()
