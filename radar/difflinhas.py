import os
oi=[]
oc = {}
for filename in os.listdir("."):
    if filename.endswith(".Txt"):
        #print(os.path.join(".", file))	
	f = open(filename, "r")
	c = 0
	for line in f:		
		if c ==1: # 0 para primeira linha e 1 para segunda linha
			oi.append([filename, line])
		c=c+1
		if c==2:
			break
	f.close()

for o in oi:
	if o[1] in oc:
		oc[o[1]].append(o[0])
	else:
		oc[o[1]] = [o[0]]

print("qtd tipos de cabecalho:")
print(len(oc.keys()))

print("\n\n---------------------------------------------------\n\n")

for chave, valor in oc.items():
	print(chave)
	print(len(valor))
	for v in valor:		
		print(v)
	print("\n\n---------------------------------------------------\n\n")
