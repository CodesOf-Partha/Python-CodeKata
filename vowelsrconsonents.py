v=input()
if (ord(v)>=65 and ord(v)<=90) or (ord(v)>=97 and ord(v)<=122 ) :
	if v=='a' or v=='e' or v=='i' or v=='o' or v=='u' or v=='A' or v=='E' or v=='I' or v=='O' or v=='U':
		print("Vowel")
	else:
		print("Consonant")
else:
	print("invalid")
