""" 
    Programa de astrología: el usuario debe ingresar el día y mes de su cumpleaños
    y el programa le debe decir a qué signo corresponde.
        Aries: 21 de marzo al 20 de abril               Tauro: 21 de abril al 20 de mayo.
        Geminis: 21 de mayo al 21 de junio              Cancer: 22 de junio al 23 de julio.
        Leo: 24 de julio al 23 de agosto                Virgo: 24 de agosto al 23 de septiembre.
        Libra: 24 de septiembre al 22 de octubre        Escorpio: 23 de octubre al 22 de noviembre.
        Sagitario: 23 de noviembre al 21 de diciembre   Capricornio: 22 de diciembre al 20 de enero.
        Acuario: 21 de enero al 19 de febrero           Piscis: 20 de febrero al 20 de marzo.
""" 

def cantidad_dias(mes):
    # Dado un mes y un año, devolver la cantidad de días correspondientes.

    if mes==2:
        dias=28
    elif mes==4 or mes==6 or mes==9 or mes==11:
        # print(f"El mes {mes} del año {año} tiene 30 días.")
        dias=30
    else:
        # print(f"El mes {mes} del año {año} tiene 31 días.")
        dias=31
    
    return dias

def dias_transcurridos(dia,mes):
    # Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha.

    sumador= dia
    
    for i in range(1,mes):
        sumador = sumador + cantidad_dias(i)
    
    return sumador
    
def calcular_signo(dia,mes):
    # El usuario ingresa día y mes de cumpleaños y retorna a que signo corresponde.

    dias=dias_transcurridos(dia,mes)

    if dias>=21 and dias<=50:
        signo=0
    elif dias>=51 and dias<=79:
        signo=1
    elif dias>=80 and dias<=110:
        signo=2
    elif dias>=111 and dias<=140:
        signo=3
    elif dias>=141 and dias<=172:
        signo=4
    elif dias>=173 and dias<=204:
        signo=5
    elif dias>=205 and dias<=235:
        signo=6
    elif dias>=236 and dias<=266:
        signo=7
    elif dias>=267 and dias<=295:
        signo=8
    elif dias>=296 and dias<=326:
        signo=9
    elif dias>=327 and dias<=355:
        signo=10
    else:
        signo=11

    return signo

def astrología(dia,mes):
    # El usuario ingresa día y mes de cumpleaños y muestra a que signo corresponde.

    signos=["Acuario","Piscis","Aries","Tauro","Geminis","Cancer","Leo","Virgo","Libra","Escorpio","Sagitario","Capricornio"]
    i=calcular_signo(dia,mes)

    print(f"Fecha: {dia}/{mes}. Tu signo es {signos[i]}.")



astrología(19,10)
astrología(19,12)
astrología(7,5)
astrología(19,2)
astrología(27,8)
astrología(1,4)

