#Even numbers
start,end=input().split()
string=""
start=int(start)
end=int(end)
for i in range(start+1,end+1):
	if i%2==0:
		string=string+str(i)+" "
print(string)
