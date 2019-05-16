start,end=input().split()
start=int(start)
end=int(end)
for i in range(start+1,end):
	if i%2==0:
		print(i)