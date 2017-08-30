#funcion que toma una lista y un elemento como argumento y lo "despeja" del resto:

def despejar(lista, idx):
    l_out = []
    for (i, j) in enumerate(lista):
        if j != lista[idx]:
            l_out.append(j if (i == len(lista) - 1) else -j)
        else:
            l_out.append(0) #el despejado, se agrega para no perder la referencia por indice de las demas
    return l_out

#funcion que calcula una iteracion de Xn para dadas Xn anteriores y la matriz a resolver
def calc_iter(matrix, x_ant):
    x_act = list(x_ant)
    for i, row in enumerate(matrix):
        despejado = despejar(row, i)
        num_list = [d * x for d, x in zip(x_act, despejado[0:-1])]
        num = despejado[-1] + sum(num_list)
        den = row[i]
        x_act[i] = num/den
    return x_act

def error_aproximado(act, ant):
    Ea = abs((act-ant)/act * 100)
    return Ea

#imprime error aproximado
def printable_Ea(var, act, ant):
    Ea = abs((act-ant)/act * 100)
    return "Ea({}) = {}%".format(var, Ea)
	
def gauss_seidel(matrix, max_error):
    x_ant = [0,0,0]
    x_act = [0,0,0]
    error = 100.0
    iters = 0
    while error >= max_error:
        x_act = calc_iter(matrix, x_ant)
        errors = [error_aproximado(xac, xan) for xac, xan in zip(x_act, x_ant)]
        error = max(errors)
        x_ant = x_act
        iters+=1
    return x_act, error, iters

"""
#Prueba de escritorio:
R1 = [3.0, -0.1, -0.2, 7.85]
R2 = [0.1, 7.0, -0.3, -19.3]
R3 = [0.3, -0.2, 10, 71.4]
matrix = [R1, R2, R3]
gs = gauss_seidel(matrix, .1)
print(gs)
"""