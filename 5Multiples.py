num=int(input())
string=""
for i in range(1,6):
	fact=num*i
	string+=str(fact)+" "
print(string.strip())
