#ejercicio 3 semana12

class Printable:
    def print_info(self):
        print("Este objeto puede imprimir informacion")


class Savable:
    def save(self):
        print("Este objeto puede guardarse en el disco.")

class Report(Printable, Savable):
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def show(self):
        print("Reporte: {self.title}\nContenido: {self.content}")


if __name__ =="__main__":
    report = Report("ventas Q4, Ingresos aumentaron un 15%")
    report.show()

    report.print_info()

    report.save()

    