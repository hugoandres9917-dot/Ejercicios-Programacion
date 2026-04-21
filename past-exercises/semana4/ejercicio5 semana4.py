#ejercicio5 semana4
number_of_notes= int(input(" ingrese la cantidad de notas"))
notes = []
for i in range(number_of_notes):
    note = float(input(f"Ingrese la nota #{i+1}: "))
    notes.append(note)
approved = [note for note in notes if note > 70]
disapproved = [note for note in notes if note < 70]

approved_notes =len(approved)
disapproved_notes = len(disapproved)
total_averages = sum(notes)/ len(notes)
approved_average = sum(approved) / len(approved) if approved else 0
disapproved_average = sum(disapproved) / len(disapproved) if disapproved else 0

print("Cantidad de notas aprobadas:", approved_notes)
print("Cantidad de notas desaprobadas:", disapproved_notes)
print("Promedio de aprobadas:", round(approved_average, 2))
print("Promedio de desaprobadas:", round(disapproved_average, 2))
print("Promedio total:", round(total_averages, 2))