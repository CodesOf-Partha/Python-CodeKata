#Longest Common string
def longest(str1,str2):
        if(str1 in str2):
            return str1
inputSize = int(input())
inputList= []
for _ in range(0,inputSize):
    inputList.append(input())
inputList.sort()
print(longest(inputList[0],inputList[inputSize-1]))
