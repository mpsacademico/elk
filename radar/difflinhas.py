import os

fl = [] #[filename, line] - fl
lf = {} #{line: filenames} - lf

diretorio = "."
extensao = ".Txt"

for filename in os.listdir(diretorio):
    if filename.endswith(extensao):        
	f = open(filename, "r")
	c = 0
	for line in f:		
		if c == 1: # 0 - primeira linha e 1 - segunda linha
			fl.append([filename, line])
		c = c + 1
		if c == 2:
			break
	f.close()

for x in fl:
	if x[1] in lf:
		lf[x[1]].append(x[0])
	else:
		lf[x[1]] = [x[0]]

print("DIFFLINHAS v1.0.0.0 - Marcos Paulo da Silva")
print("%s %s - %d linhas"%(diretorio, extensao, len(lf.keys())))
print("\n\n---------------------------------------------------\n\n")

for key, value in lf.items():
	print(key)
	print("%d arquivos\n"%(len(value)))
	for v in value:		
		print(v)
	print("\n\n---------------------------------------------------\n\n")
