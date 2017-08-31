# coding: utf-8

# # Analisis Numerico - Proyecto 1
# 

# ## Metodo Gauss-Seigel 

# In[4]:


import algoritmo_gs as gs
import string 
import os

n_points = "!#$%&'*,/:;<>?@[\]^_`{|}~"
p_points = "+-"

cont_1 = 0
cont_2 = 0

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

#----------------------------------------------------------------------------#

def eliminar_char(ecuacion, matriz):
    while ecuacion == "Error":
        ecuacion = input("\tEscribe la ecuacion: ")
        if len(ecuacion) == 0:
            print("\tEcuacion vacia")
            ecuacion = "Error"
        else:
            if any(char in n_points for char in ecuacion):
                print ("\tContiene caracteres especiales. Escriba la ecuacion correctamente.")
                ecuacion = "Error"
            for i in range(len(ecuacion)-1):
                if (ecuacion[i] in p_points) and (ecuacion[i+1] in p_points) and (ecuacion[i] == ecuacion[i+1]):
                    print ("\tContiene mas de un signo. Escriba la ecuacion correctamente.")
                    ecuacion = "Error"
                    break
                elif (ecuacion[i] in string.ascii_letters) and (ecuacion[i+1] in string.ascii_letters):
                    print("\tTiene una variable de mas de una letra")
                    ecuacion = "Error"
                    break
                elif "=" not in ecuacion:
                    print("\tFalta un simbolo de igualdad en la ecuacion.")
                    ecuacion = "Error"
                    break
                elif (ecuacion[i] in string.digits) and (ecuacion[i+1] in p_points):
                    print("\tFalta variable(s) en la ecuacion.")
                    ecuacion = "Error"
                    break
                elif (ecuacion[i] in ".") and (ecuacion[i+1] in "="):
                    print("\tError de formato.")
                    ecuacion = "Error"
                    break
                elif (ecuacion[i] in "=") and (ecuacion[i+1] in "."):
                    print("\tError de formato.")
                    ecuacion = "Error"
                    break
                elif (ecuacion[i] in "=") and (ecuacion[i+1] in "="):
                    print("\tError de formato.")
                    ecuacion = "Error"
                    break
                elif (ecuacion[i] in ".") and (ecuacion[i+1] in "-"):
                    print("\tError de formato.")
                    ecuacion = "Error"
                    break       
                elif (ecuacion[i] in "-") and (ecuacion[i+1] in "."):
                    print("\tError de formato.")
                    ecuacion = "Error"
                    break       
                elif (ecuacion[i] in "=") and (ecuacion[i+1] in string.ascii_letters):
                    print("\tError de formato.")
                    ecuacion = "Error"
                    break
                elif (ecuacion[i] in string.ascii_letters) and (ecuacion[i+1] in "."):
                    print("\tError de formato.")
                    ecuacion = "Error"
                    break       
                elif (ecuacion[i] in ".") and (ecuacion[i+1] in "."):
                    print("\tNo debes poner 2 o mas puntos decimales en un termino")
                    ecuacion = "Error"
                    break
                for i in range(len(ecuacion)-2):
                    if (ecuacion[i] in string.ascii_letters) and (ecuacion[i+1] in "-") and (ecuacion[i+2] in string.ascii_letters):
                        ecuacion = ecuacion.replace("-", "+-")
                    if (ecuacion[i] in string.ascii_letters) and (ecuacion[i+1] in "-") and (ecuacion[i+2] in string.digits):
                        ecuacion = ecuacion.replace("-","+-")

        if ecuacion != "Error":
            if "-" not in ecuacion[0] and "-" not in ecuacion[1]:
                ecuacion = ecuacion.replace("-", "+-")
            ecuacion = ecuacion.replace("(", "")
            ecuacion = ecuacion.replace(")", "")
            ecuacion = ecuacion.split("=")
            ecuacion[0] = ecuacion[0].split("+")
            ecuacion[0].append(ecuacion[1])
            ecuacion = ecuacion[0]
            
            while '' in ecuacion:
                ecuacion.remove('')

            for item in ecuacion:
                for i in range(len(item)-1):
                    if (item[i] in string.ascii_letters) and (item[i+1] in string.digits):
                        print("\tError en el formato.")
                        ecuacion = "Error"
                        break
            
            for char in ecuacion[len(ecuacion)-1]:
                if char in string.ascii_letters:
                    print ("El resultado no debe tener variables.")
                    ecuacion = "Error"
                    break
                if len(ecuacion) is not len(matriz[0]) and len(matriz) > 1:
                    print("\tNo concuerdan el nivel de las ecuaciones con la original")
                    ecuacion = "Error"
                    break
    return ecuacion


def n_eq(cont_1, cont_2, eq, variables, matriz, ecuacion):
    for i in range(len(eq)):
        try:
            #print ("{}[{}] in {}[{}]".format(variables[cont_1], cont_1, eq[i], i))
            #print (eq)
            if variables[cont_1] in eq[i]:
                eq[i] = eq[i].replace(variables[cont_1], "")
                if eq[i] == "":
                    eq[i] = 1
                elif eq[i] == "-":
                    eq[i] = -1  
                else:
                    eq[i] = float(eq[i])
                cont_1+=1
                cont_2=1
            else:
                print("\tNo concuerdan las variables")
                cont_2=0
                break  
        except:
            break
        
    if cont_2 == 0:
        eq = "Error"
        eq = eliminar_char(ecuacion, matriz)
        n_eq(0,0,eq, variables, matriz, ecuacion)
    else:
        matriz += [eq]
    eq[len(eq)-1] = eq[len(eq)-1].replace("+", "")
    eq[len(eq)-1] = float(eq[len(eq)-1]) 
    return matriz
            
#----------------------------------------------------------------------------#

def datos_usuario():
    ecuacion = "Error"
    matriz = [[1]]
    variables = [ ] 
            
    print ("{}{}\n{}{}{}\n{}\n\n".format('\n'*0,'-'*160, '-'*34, " Gauss-Seidel ", '-'*32, '-'*160))
    
    while (1):
        eq = eliminar_char(ecuacion, matriz)

        for i in range(len(eq)):
            for c in eq[i]:
                if c in string.ascii_letters:
                    variables.append(c)
                    eq[i] = eq[i].replace(c, "")
                    if eq[i] == "":
                        eq[i] = 1
                    elif eq[i] == "-":
                        eq[i] = -1
                    else:
                        eq[i] = float(eq[i])
        eq[len(eq)-1] = float(eq[len(eq)-1].replace("+", ""))
        
        if len(variables) == len(set(variables)):
            break;
        else:
            variables = []
            print("\tNo repitas variables en una misma ecuacion")
        
    matriz = [eq]
          
    for i in range(len(matriz[0])-2):
        eq = eliminar_char(ecuacion, matriz)
        matriz = n_eq(cont_1, cont_2, eq, variables, matriz, ecuacion)
        
    while (1):
        m_error = input("\tMargen de error deseado(%): ")
        if is_number(m_error) is not 0:
            break
    
    return {"matrix": matriz,"vars": variables,"ea": float(m_error)}

#----------------------------------------------------------------------------#

def imprimeResultados(r, vars):
    print("\n\n{}\n\n".format("-"*80))
    print("\t\tResultados:")
    for var, val in zip(vars,r["valores"]):
        print("\t\t\t{}: {}".format(var, val))
    print("\t\t\tEa = {}".format(r["ea"]))
    print("\t\t\tIteraciones = {}".format(r["iters"]))
    #print("\n\n{}".format("-"*80))
    print ("\n{}".format("-"*(80*4)))

#----------------------------------------------------------------------------#

#Solucion del sistema:
primer_pantalla()
d = datos_usuario() #adquiere datos
d = gs.datos_dominante(d) #preprocesa datos (trata de hacer dominante la matriz)
r = gs.gauss_seidel(d["matrix"], d["ea"]) #procesa datos

imprimeResultados(r, d["vars"])#despliega resultados

os.system("pause")
