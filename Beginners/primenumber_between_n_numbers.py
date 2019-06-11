start,end=input().split()
start=int(start)
end=int(end)
for i in range(start,end+1):
	for j in range(2, i):
		if i % j  == 0:
			break
	else:
		print(i)

