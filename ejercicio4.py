import os
class Persona():
    def __init__(self):
        self.__perso = {}
        self.__listaPersonas = []

    def agregarPersona(self, ceula, nombre, apellido, direccion, telefono):
        self.__perso = {
            'cedula': cedula,
            'nombre': nombre,
            'apellido': apellido,
            'direccion': direccion,
            'telefono': telefono
        }
        self.__listaPersonas.append(self__perso)

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.__devengado = {}
        self.__deducciones = {}
        self.__listaEmpleados = {}

    def agregarEmpleado(self):
        cedula = input("digite la cedula ...")
        nombre = input("digite la nombre ...")
        apellido = input("digite la apellido ...")
        direccion = input("digite la direccion ...")
        telefono = input("digite la telefono ...")
        salario  = float(input("digite el salario ..."))

        per = {
            'cedula': cedula,
            'nombre': nombre,
            'apellido': apellido,
            'direccion': direccion,
            'telefono': telefono
        }

        self.__devengado = {
            'salario': salario,
            'alimentacion': 0,
            'transporte': 0,
        }

        self.__deducciones = {
            'salud': 0,
            'pension': 0,
        }

        super().agregarPersona(cedula, nombre, apellido, 
        direccion, telefono)

        self.__listaEmpleado.append([{"persona": per},
        {"devengado": self.__devengado}, {"deducciones": self.
        __deducciones}])
        

    def calcularDevengado(self):
        if self.__devengado['salario'] < 2000000:
            self.__devengado['alimentacion'] = 80000
            self.__devengado['transporte'] = 60000

    def calcularDeducciones(self):
        self.__deducciones['salud'] = self.__devengado
        ['salario'] * 4 / 1000
        self.__deducciones['pension'] = self.__devengado
        ['salario'] * 3.375 



    def menu(self, opciones):
        while(True):
            os.system("cls")
            for item in range(len(opciones)):
                print(opciones[item])

            opcion = input("digite una opcion correcta: ")

            if opcion == "1":
                os.system("cls")
                self.agregarEmpleado()
                self.calcularDevengado()
                self.calcularDeducciones()


def menuPrincipal():
    opciones = (
        "MENU PRINCIPAL",
        "1. Adicionar Empleado",
        "2. Mostrar Empleado",
        "3. Eliminar Emppleado",
        "4. salir"

    )

def main():
    menuPrincipal()
