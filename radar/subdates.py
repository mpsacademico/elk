import csv
d = {}
cal = {}
dt = []
with open('dates.csv', 'rb') as csvfile:
	# linha csv: DATA-CALENDARIO	DATA-ANALISE	LEGENDA
	f = csv.reader(csvfile, delimiter='	')
	for r in f:
		cal[r[0]] = 0
		dt.append([r[1], r[2]])
	for k, v in cal.items():
		for x in dt:
			if k == x[0]:
				cal[k] = x[1]
for k, v in cal.items():
	print("%s,%s"%(k, v))
