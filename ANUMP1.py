# coding: utf-8
# # Analisis Numerico - Proyecto 1
# ## Metodo Gauss-Seigel 

#------------------------------ Librerias -----------------------------------#
import string 
import os
#----------------------------------------------------------------------------#
#------------------------------- Variables ----------------------------------#
ecuacion = "Error" 
ec_num = 1
n_points = "!#$%&'*,/:;<>?@[\]^_`{|}~"
p_points = "+-="
eq = "Error"
matriz = [[1]]
m_error = 0.00
variables = [ ]
cont_1 = 0
cont_2 = 0
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#
def is_number(num):
    try:
        float(num)
        if float(num) >= 0:
            return 1
        else:
            print ("No es un numero positivo")
            return 0
    except ValueError:
        print ("No es un numero")
        return 0
#----------------------------------------------------------------------------#
def primer_pantalla():
    os.system("cls")
    print ("{}{}\n{}{}{}\n{}".format('\n'*0,'-'*160, '-'*35, " Bienvenidos ", '-'*32, '-'*160))
    print ("\n\n\n\t\t\t{}\n\n\t\t\t{}\n\t\t{}\n".format("Analisis Numerico - 5to Semestre", "Proyecto #1 - Metodo Gauss-Seidel", ""))
    print ("{}\t{}\n\n\t\t{}\t\t\t{}\n".format("\n"*1,"Integrantes: ", "Alberto Alan Zul Rabasa", "1635501", ))
    print ("\t\t{}\t\t{}\n".format("Rafael Baruc Almager Lopez", "1443335"))
    print ("\t\t{}\t\t{}\n\t".format("Luis Alberto Rodriguez Matrinez", "1791361"))
    print ("\n\n\n{}".format("-"*(80*4)))
    os.system("pause")
    os.system("cls")
#----------------------------------------------------------------------------#
def eliminar_char(ecuacion, matriz, ec_num):
    while ecuacion == "Error":
        ecuacion = input("Escribe la ecuacion [{}]: ".format(ec_num))
        ecuacion = ecuacion.replace(" ", "")
        if any(char in n_points for char in ecuacion):
            print ("Contiene caracteres especiales. Escriba la ecuacion correctamente.")
            ecuacion = "Error"
        else:
            try:
                for i in range(len(ecuacion)-1):
                    if (ecuacion[i] in p_points) and (ecuacion[i+1] in p_points):
                        print ("Contiene mas de un signo o simbolo de igual. Escriba la ecuacion correctamente.")
                        ecuacion = "Error"
                        break
                    elif (ecuacion[i] in string.ascii_letters) and (ecuacion[i+1] in string.ascii_letters):
                        print("Tiene una variable de mas de una letra")
                        ecuacion = "Error"
                        break
                    elif "=" not in ecuacion:
                        print("Falta un simbolo de igualdad en la ecuacion.")
                        ecuacion = "Error"
                        break
                    elif (ecuacion[i] in string.digits) and (ecuacion[i+1] in p_points):
                        print("Falta variable(s) en la ecuacion.")
                        ecuacion = "Error"
                        break
            except:
                ecuacion = "Error"
                print("")
        try:
            if ecuacion != "Error":
                if "-" not in ecuacion[0] and "-" not in ecuacion[1]:
                    ecuacion = ecuacion.replace("-", "+-")
                ecuacion = ecuacion.replace("(", "")
                ecuacion = ecuacion.replace(")", "")
                ecuacion = ecuacion.split("=")
                ecuacion[0] = ecuacion[0].split("+")
                ecuacion[0].append(ecuacion[1])
                ecuacion = ecuacion[0]

                for item in ecuacion:
                    for i in range(len(item)-1):
                        if (item[i] in string.ascii_letters) and (item[i+1] in string.digits):
                            print("Error en el formato.")
                            ecuacion = "Error"
                            break

                for char in ecuacion[len(ecuacion)-1]:
                    if char in string.ascii_letters:
                        print ("El resultado no debe tener variables.")
                        ecuacion = "Error"
                        break
                if len(ecuacion) is not len(matriz[0]) and len(matriz) > 1:
                    print("No concuerdan el nivel de las ecuaciones con la original")
                    ecuacion = "Error"
        except:
            ecuacion = "Error"
    return ecuacion
#----------------------------------------------------------------------------#
def n_eq(cont_1, cont_2, eq, variables, matriz):
    for i in range(len(eq)):
        try:
            if variables[cont_1] in eq[i]:
                eq[i] = eq[i].replace(variables[cont_1], "")
                if eq[i] == "":
                    eq[i] = 0
                else:
                    eq[i] = float(eq[i])
                    
                cont_1+=1
                cont_2=1
            else:
                print("No concuerdan las variables")
                cont_2=0
                break  
        except:
            break
        
    if cont_2 == 0:
        eq = "Error"
        eq = eliminar_char(ecuacion, matriz)
        n_eq(0,0,eq, variables, matriz)
    else:
        matriz += [eq]
    eq[len(eq)-1] = float(eq[len(eq)-1])
    return matriz
            
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#
primer_pantalla()
#----------------------------------------------------------------------------#
print ("{}{}\n{}{}{}\n{}\n\n\t\t".format('\n'*0,'-'*160, '-'*31, " Metodo Gauss-Seidel ", '-'*28, '-'*160))
while eq == "Error":
    eq = ""
    ec_num += 1
    eq = eliminar_char(ecuacion, matriz, ec_num)
    for i in range(len(eq)):
        for c in eq[i]:
            if c in string.ascii_letters:
                variables.append(c)
                eq[i] = eq[i].replace(c, "")
                if eq[i] == "":
                    eq[i] = 1
                else:
                    eq[i] = float(eq[i])
    eq[len(eq)-1] = float(eq[len(eq)-1])

    for item in variables:
        for i in range(len(variables)):
            if item in variables[i]:
                cont_1 += 1
        if cont_1 > 1:
            print ("No puedes tener dos o mas variables variables iguales")
            eq = "Error"
            cont_1 = 0
            variables = []
            break
        cont_1 = 0
            
cont_1 = 0
matriz = [eq]

for i in range(len(matriz[0])-2):
    eq = eliminar_char(ecuacion, matriz, ec_num)
    ec_num += 1
    matriz = n_eq(cont_1, cont_2, eq, variables, matriz)
        
while (1):
    m_error = input("Margen de error deseado(%): ")
    if is_number(m_error) is not 0:
        break
   
for i in range(len(matriz)):
    if  i == int(len(matriz)/2):
        print ("\tmatriz = {}".format(matriz[i]))
    else:
        print ("\t\t {}".format(matriz[i]))
           
print ("\n\tvariables = {}\n\n\tError deseado(%) = {}%".format(variables,m_error))
os.system("pause")
os.system("cls")