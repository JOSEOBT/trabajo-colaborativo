from abc import ABC, abstractmethod
from excepciones import *
import datetime


# LOGS
def registrar_log(tipo, mensaje):
    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{datetime.datetime.now()} [{tipo}] {mensaje}\n")


# ABSTRACTA
class Persona(ABC):
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    @abstractmethod
    def mostrar_info(self):
        pass


# CLIENTE
class Cliente(Persona):
    def __init__(self, nombre, documento, correo):
        if len(nombre.strip()) < 3:
            raise ClienteError("Nombre inválido")

        if not documento.isdigit():
            raise ClienteError("Documento debe ser numérico")

        if "@" not in correo:
            raise ClienteError("Correo inválido")

        super().__init__(nombre, documento)
        self.__correo = correo

    def get_correo(self):
        return self.__correo

    def mostrar_info(self):
        return f"{self.nombre} - CC:{self.documento}"


# SERVICIO ABSTRACTO
class Servicio(ABC):
    def __init__(self, nombre, tarifa):
        if tarifa <= 0:
            raise ServicioError("Tarifa inválida")

        self.nombre = nombre
        self.tarifa = tarifa

    @abstractmethod
    def calcular_costo(self, horas):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# HIJOS
class Sala(Servicio):
    def calcular_costo(self, horas):
        return self.tarifa * horas

    def descripcion(self):
        return "Reserva de sala"


class Equipo(Servicio):
    def calcular_costo(self, horas):
        return (self.tarifa * horas) + 20

    def descripcion(self):
        return "Alquiler de equipos"


class Asesoria(Servicio):
    def calcular_costo(self, horas):
        return (self.tarifa * horas) * 1.15

    def descripcion(self):
        return "Asesoría profesional"


# RESERVA
class Reserva:
    def __init__(self, cliente, servicio, horas):
        if horas <= 0:
            raise ReservaError("Horas inválidas")

        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    # SOBRECARGA SIMULADA
    def costo_total(self, descuento=0, impuesto=0):
        total = self.servicio.calcular_costo(self.horas)
        total -= total * descuento
        total += total * impuesto
        return total

    def procesar(self):
        try:
            total = self.costo_total()
        except Exception as e:
            raise ReservaError("Error al calcular reserva") from e
        else:
            self.confirmar()
            registrar_log("INFO", "Reserva confirmada")
            return total
        finally:
            registrar_log("INFO", "Proceso de reserva ejecutado")