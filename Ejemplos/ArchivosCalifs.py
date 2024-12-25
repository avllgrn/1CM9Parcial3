from os import system
from random import randrange

if __name__ == '__main__':
    system('cls')

    alumnos = int(input('Cuántos alumnos? '))
    parciales = int(input('Cuántos parciales? '))
    nombreArchivo = input('Dónde se guardará? ')

    # Se genera matriz con calificaciones aleatorias entre 0 y 10
    Matriz = []
    for alumno in range(alumnos):
        renglon = []
        for parcial in range(parciales):
            renglon.append(randrange(101)/10)
        Matriz.append(renglon)

    print(f'Matriz\n{Matriz}')
    print()

    # Se muestra matriz con calificaciones aleatorias entre 0 y 10
    print(f'Matriz')
    for alumno in range(alumnos):        
        for parcial in range(parciales):
            print(Matriz[alumno][parcial],end='\t')
        print()
    print()

    # Se almacena matriz con calificaciones aleatorias entre 0 y 10, en un archivo
    with open(nombreArchivo, 'w') as Archivo:
        for alumno in range(alumnos):
            for parcial in range(parciales):
                Archivo.write(str(Matriz[alumno][parcial])+', ')
            Archivo.write('\n')


    # Se carga matriz con calificaciones aleatorias entre 0 y 10, desde un archivo
    with open(nombreArchivo, 'r') as Archivo:
        Calificaciones = []
        for renglon in Archivo:
            alumno = []
            datos = renglon.split(',')
            for dato in datos:
                try:
                    alumno.append(float(dato))
                except:
                    pass
            Calificaciones.append(alumno)


    # Se muestra matriz cargada con calificaciones aleatorias entre 0 y 10
    m = len(Calificaciones)
    n = len(Calificaciones[0])
    print(f'Calificaciones de {m} alumnos y {n} parciales')
    for i in range(m):        
        for j in range(n):
            print(Calificaciones[i][j],end='\t')
        print()
    print()

    # Se agrega columna para promedios, a cada alumno en la matriz de calificaciones
    for i in range(m):
        Calificaciones[i].append(0.0)

    # Se muestra matriz cargada con calificaciones aleatorias entre 0 y 10
    print(f'Calificaciones de {m} alumnos y {n} parciales')
    for i in range(m):        
        for j in range(n + 1):  # Ahora hay una columna extra (para calificaciones finales)
            print(Calificaciones[i][j],end='\t')
        print()
    print()

    for i in range(m):                                      # Para cada alumno,
        for j in range(n):                                  # cada parcial,
            Calificaciones[i][n] += Calificaciones[i][j]    # se acumula en la nueva columna y, despues, 
        Calificaciones[i][n] /= n                           # se divide entre la cantidad de parciales

    # Se muestra matriz cargada con calificaciones aleatorias entre 0 y 10
    print(f'Calificaciones de {m} alumnos y {n} parciales')
    for i in range(m):        
        for j in range(n + 1):  # Ahora hay una columna extra (para calificaciones finales)
            print(Calificaciones[i][j],end='\t')
        print()
    print()

    # Se busca la menor calificacion en todos los parciales
    alumnoMenorParcial = 0
    examenMenorParcial = 0
    calificacionMenorParcial = Calificaciones[alumnoMenorParcial][examenMenorParcial]   # Se supone que el primer alumno en el primer parcial saco la menor calificiacion
    for i in range(m):                                                                  # Para cada alumno,
        for j in range(n):                                                              # cada parcial,
            if Calificaciones[i][j] < calificacionMenorParcial:                         # se comparan las calificaciones contra la supuesta menor
                    alumnoMenorParcial = i                                                              # Se guarda el numero de alumno
                    examenMenorParcial = j                                                              # Se guarda el numero de examen
                    calificacionMenorParcial = Calificaciones[alumnoMenorParcial][examenMenorParcial]   # Se guarda la nueva calificacion menor supuesta

    print(f'El alumno {alumnoMenorParcial}, en el paricial {examenMenorParcial} tiene la calificacion más baja de todos los parciales: {calificacionMenorParcial}')

    # Se busca la mayor calificacion en todos los parciales
    alumnoMayorParcial = 0
    examenMayorParcial = 0
    calificacionMayorParcial = Calificaciones[alumnoMayorParcial][examenMayorParcial]   # Se supone que el primer alumno en el primer parcial saco la menor calificiacion
    for i in range(m):                                                                  # Para cada alumno,
        for j in range(n):                                                              # cada parcial,
            if Calificaciones[i][j] > calificacionMayorParcial:                         # se comparan las calificaciones contra la supuesta menor
                    alumnoMayorParcial = i                                                              # Se guarda el numero de alumno
                    examenMayorParcial = j                                                              # Se guarda el numero de examen
                    calificacionMayorParcial = Calificaciones[alumnoMayorParcial][examenMayorParcial]   # Se guarda la nueva calificacion menor supuesta

    print(f'El alumno {alumnoMayorParcial}, en el paricial {examenMayorParcial} tiene la calificacion más alta de todos los parciales: {calificacionMayorParcial}')

    # Se cuentan los alumnos aprobados del semestre
    aprobadosSemestre = 0
    for i in range(m):
        if Calificaciones[i][n] >= 6:
            aprobadosSemestre += 1
    print(f'En el semestre, aprobaron {aprobadosSemestre} alumnos')
        
    # Se cuentan los alumnos reprobados del semestre
    reprobadosSemestre = 0
    for i in range(m):
        if Calificaciones[i][n] < 6:
            reprobadosSemestre += 1
    print(f'En el semestre, reprobaron {reprobadosSemestre} alumnos\n')

    # Se busca la menor calificacion del primer parcial
    alumnoMenorPrimerParcial = 0
    calificacionMenorPrimerParcial = Calificaciones[alumnoMenorPrimerParcial][0]
    for i in range(m):
        if Calificaciones[i][0] < calificacionMenorPrimerParcial:
            alumnoMenorPrimerParcial = i
            calificacionMenorPrimerParcial = Calificaciones[alumnoMenorPrimerParcial][0]
    print(f'En el primer paricial, el alumno {alumnoMenorPrimerParcial} tiene la calificacion más baja: {calificacionMenorPrimerParcial}')

    # Se busca la mayor calificacion del primer parcial
    alumnoMayorPrimerParcial = 0
    calificacionMayorPrimerParcial = Calificaciones[alumnoMayorPrimerParcial][0]
    for i in range(m):
        if Calificaciones[i][0] > calificacionMayorPrimerParcial:
            alumnoMayorPrimerParcial = i
            calificacionMayorPrimerParcial = Calificaciones[alumnoMayorPrimerParcial][0]
    print(f'En el primer paricial, el alumno {alumnoMayorPrimerParcial} tiene la calificacion más alta: {calificacionMayorPrimerParcial}')

    # Se cuentan los alumnos aprobados del primer parcial
    aprobadosPrimerParcial = 0
    for i in range(m):
        if Calificaciones[i][0] >= 6:
            aprobadosPrimerParcial += 1
    print(f'En el primer paricial, aprobaron {aprobadosPrimerParcial} alumnos')
        
    # Se cuentan los alumnos reprobados del primer parcial
    reprobadosPrimerParcial = 0
    for i in range(m):
        if Calificaciones[i][0] < 6:
            reprobadosPrimerParcial += 1
    print(f'En el primer paricial, reprobaron {reprobadosPrimerParcial} alumnos\n')

    # Se busca la menor calificacion del ultimo parcial
    alumnoMenorUltimoParcial = 0
    calificacionMenorUltimoParcial = Calificaciones[alumnoMenorUltimoParcial][n-1]
    for i in range(m):
        if Calificaciones[i][n-1] < calificacionMenorUltimoParcial:
            alumnoMenorUltimoParcial = i
            calificacionMenorUltimoParcial = Calificaciones[alumnoMenorUltimoParcial][n-1]
    print(f'En el ultimo paricial, el alumno {alumnoMenorUltimoParcial} tiene la calificacion más baja: {calificacionMenorUltimoParcial}')

    # Se busca la mayor calificacion del Ultimo parcial
    alumnoMayorUltimoParcial = 0
    calificacionMayorUltimoParcial = Calificaciones[alumnoMayorUltimoParcial][n-1]
    for i in range(m):
        if Calificaciones[i][n-1] > calificacionMayorUltimoParcial:
            alumnoMayorUltimoParcial = i
            calificacionMayorUltimoParcial = Calificaciones[alumnoMayorUltimoParcial][n-1]
    print(f'En el ultimo paricial, el alumno {alumnoMayorUltimoParcial} tiene la calificacion más alta: {calificacionMayorUltimoParcial}')

    # Se cuentan los alumnos aprobados del ultimo parcial
    aprobadosUltimoParcial = 0
    for i in range(m):
        if Calificaciones[i][n-1] >= 6:
            aprobadosUltimoParcial += 1
    print(f'En el ultimo paricial, aprobaron {aprobadosUltimoParcial} alumnos')
        
    # Se cuentan los alumnos reprobados del ultimo parcial
    reprobadosUltimoParcial = 0
    for i in range(m):
        if Calificaciones[i][n-1] < 6:
            reprobadosUltimoParcial += 1
    print(f'En el ultimo paricial, reprobaron {reprobadosUltimoParcial} alumnos\n')
