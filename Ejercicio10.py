#Desarrollar un TDA que permita manejar el calendario del mes actual, sobre el que se puedan resolver las siguientes actividades:
#obtener el día actual (número y día de la semana);
#obtener los días feriados;
#obtener los días en que inicia luna llena, luna nueva, cuarto menguante y cuarto creciente;
#Obtener los días y nivel de pesca del mes (calendario de pesca).

import datetime

class CalendarioMes:
    def __init__(self):
        self.dias_del_mes = self._generar_calendario_mes()

    def _generar_calendario_mes(self):
        # Generar el calendario del mes actual
        fecha_actual = datetime.date.today()
        primer_dia_mes = datetime.date(fecha_actual.year, fecha_actual.month, 1)
        ultimo_dia_mes = datetime.date(fecha_actual.year, fecha_actual.month + 1, 1) - datetime.timedelta(days=1)
        calendario_mes = {}
        for dia in range(primer_dia_mes.day, ultimo_dia_mes.day + 1):
            fecha = datetime.date(fecha_actual.year, fecha_actual.month, dia)
            dia_semana = fecha.strftime("%A")
            calendario_mes[dia] = {"dia_semana": dia_semana, "feriado": False, "fase_luna": None, "nivel_pesca": None}
        return calendario_mes

    def obtener_dia_actual(self):
        fecha_actual = datetime.date.today()
        dia_actual = fecha_actual.day
        dia_semana = fecha_actual.strftime("%A")
        return dia_actual, dia_semana

    def establecer_feriado(self, dia):
        if dia in self.dias_del_mes:
            self.dias_del_mes[dia]["feriado"] = True

    def obtener_dias_feriados(self):
        feriados = [dia for dia, info in self.dias_del_mes.items() if info["feriado"]]
        return feriados

    # Método para calcular las fases de la luna (luna llena, luna nueva, cuarto menguante, cuarto creciente)
    # Implementar según la lógica necesaria

    # Método para obtener el calendario de pesca
    # Implementar según la lógica necesaria

# Ejemplo de uso
calendario = CalendarioMes()
dia_actual, dia_semana = calendario.obtener_dia_actual()
print("Día actual:", dia_actual, "(", dia_semana, ")")

calendario.establecer_feriado(25)  # Ejemplo de establecer un día como feriado
print("Días feriados:", calendario.obtener_dias_feriados())
