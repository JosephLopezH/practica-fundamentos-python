tuEdad = input("Introduce tu edad: ")
tuEdad = int(tuEdad)

#Estructura de control IF
if tuEdad >= 18 and tuEdad < 100:
    print("Eres mayor de edad")
elif tuEdad >= 100:
    print("Eres inmortal?")
elif tuEdad <= 0:
    print("No existes")
else:
    print("Eres menor de edad")


#Estructura de control for
for i in range(0, 10):
    print(i)

#Estructura de control Switch
dia = input("Introduce un dia: ")
dia = int(dia)

with switch(dia) as s:
    if s.case(15):
        print("Es quincena")