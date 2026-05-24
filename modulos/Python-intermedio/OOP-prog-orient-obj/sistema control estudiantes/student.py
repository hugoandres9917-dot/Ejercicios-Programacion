
   #Duplique el proyecto Sistema de Control de Estudiantes y modifíquelo para usar objetos para guardar la información de los estudiantes (creando una clase de Student).
   #Hay que cambiar los estudiantes de diccionarios a objetos.
   #Hay que convertir la data del csv (que viene por defecto en formato de diccionario) a objetos al importarla.
   #Hay que convertir los objetos a diccionarios para poder exportarlos a csv.
   #Hay que modificar el acceso a los keys para accesar a atributos.
   #student[’Name’] → student.name

#student.py

class Student:
    def __init__(self, name, section, spanish, english, social_studies, sciences):
        self.name = name
        self.section = section
        self.spanish = float(spanish)
        self.english = float(english)
        self.social_studies = float(social_studies)
        self.sciences = float(sciences)
        self.average_grade = round((self.spanish + self.english + self.social_studies + self.sciences)/4, 2)

    def to_dictionary(self):
        return {
            "name": self.name,
            "section": self.section,
            "spanish": self.spanish,
            "english": self.english,
            "social_studies": self.social_studies,
            "sciences": self.sciences,
            "average_grade": self.average_grade
        }

    def __str__(self):
        return (
            f"\nNombre: {self.name}\n"
            f"Seccion: {self.section}\n"
            f"Notas - Espanol: {self.spanish}, Ingles: {self.english},"
            f"Sociales: {self.social_studies}, Ciencias: {self.sciences}\n"
            f"Promedio: {self.average_grade}"
        )