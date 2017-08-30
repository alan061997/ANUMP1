r1 = [5, 2, 1]
r2 = [1, 4, 1]
r3 = [2, 1, 7]

r4 = [2, 1, 3]
r5 = [5, 2, 3]
r6 = [3, 4, 5]

#i = [3, 2, 0, 1]
f0 = [1, 2, 3, 7]
f1 = [2, 4, 9, 1]
f2 = [15, 3, 6, 2]
f3 = [4, 20, 5, 1]
m = [r1, r2, r3]

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
def mat_ordenar(m):
	indices = mat_dom_index(m)
	for j in range(len(m)):
		for i, f in enumerate(m):
			if indices[i] != i:
				ii = indices[i]
				m[i], m[ii] = m[ii], m[i]
				indices[i], indices[ii] = indices[ii], indices[i]
			
	return m