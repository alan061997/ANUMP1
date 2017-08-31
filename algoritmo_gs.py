#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#Matriz dominante
def fila_dominante(r):
	return max(r) > (sum(r) - max(r))
	
def mat_dominante(m):
	for r in m:
		if not fila_dominante(r):
			return False
	return True
	
def fila_dom_index(f):
	assert fila_dominante(f) == True, "Fila debe ser dominante"
	mx = max(f)
	for i, e in enumerate(f):
		if e == mx:
			return i
	return -1
	
def mat_dom_index(m):
	return [fila_dom_index(f) for f in m]

def mat_ordenada(m):
	indices = mat_dom_index(m)
	if indices == sorted(indices):
		return True
	else:
		return False

#Bubble sort de filas
def mat_ordenar(m, r):
	assert mat_dominante(m), "Matriz debe ser dominante"
	indices = mat_dom_index(m)
	for j in range(len(m)):
		for i, f in enumerate(m):
			if indices[i] != i:
				ii = indices[i]
				m[i], m[ii] = m[ii], m[i]
				indices[i], indices[ii] = indices[ii], indices[i]
				r[i], r[ii] = r[ii], r[i]
			
	return m, r

def datos_dominante(d):
	m = list(d["matrix"])
	res = []
	res_salvados = False
	if len(m) != len(m[0]):
		res = [r[-1] for r in m] #salva columna de resultados
		#retira columna de resultados
		m = [r[0:-1] for r in m]
		res_salvados = True

	print ("matriz = {}".format(m))
	if(mat_dominante(m)):
		if(mat_ordenada(m)):
			print("Matriz dominante y ordenada")
		else:
			print("Matriz dominante, ordenando...")
			print("antes: \n{}".format(m))
			m, res = mat_ordenar(m, res)
			if (res_salvados):
				m = [f+[r] for f, r in zip(m, res)]
			d["matrix"] = m
			print("Matriz ordenada!")
			print("despues: \n{}".format(m))
	else:
		print("Matriz no dominante :(")
		print("Hare mi mejor esfuerzo!!!!")
	return d
		
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

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
    x_ant = [0.1 for i in range(len(matrix))]
    x_act = [0.1 for i in range(len(matrix))]
    error = 100.0
    iters = 0
    while error >= max_error:
        x_act = calc_iter(matrix, x_ant)
        errors = [error_aproximado(xac, xan) for xac, xan in zip(x_act, x_ant)]
        error = max(errors)
        x_ant = x_act
        iters+=1
    return {"valores": x_act, "ea": error, "iters": iters}

"""
#Prueba de escritorio:
R1 = [3.0, -0.1, -0.2, 7.85]
R2 = [0.1, 7.0, -0.3, -19.3]
R3 = [0.3, -0.2, 10, 71.4]
matrix = [R1, R2, R3]
gs = gauss_seidel(matrix, .1)
print(gs)
"""