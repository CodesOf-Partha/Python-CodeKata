start,end=input().split() 
start=int(start)
end=int(end)
string=""
for i in range(start,end):	
	sum = 0  
	temp = i  
	while temp > 0:  
	   digit = temp % 10  
	   sum += digit ** 3  
	   temp //= 10  
	if i == sum:  
	   string+=str(i)+" "
print(string.strip())
