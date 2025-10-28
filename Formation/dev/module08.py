classeur_1 = {
	'positif':[],
	'negatif':[]
}

# classeurAdd
def classeurAdd(classeur, nombre):
	
	if isinstance(nombre, bool):
		return

	if isinstance(nombre, (int, float)):
		if nombre >= 0 :
			classeur['positif'].append(nombre)
		else :
			classeur['negatif'].append(nombre)

# FIBONACCI
def fiboStr(n):
	ret = "1"
	min2 = 0
	min1 = 1
	while(n > 0) :
		cur = min1 + min2
		ret += f" {cur}"
		min2 = min1
		min1 = cur
		n -= 1
	return ret

