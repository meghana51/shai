num1,num2,num3=map(int,raw_input().split())
if (num1 >= num2)and(num1 >=num3):
	    largest=num1
elif(num2 >= num1)and(num2 >= num3):
	     largest=num2
else:
	     largest=num3
print("the largest number between",num1,num2,"and",num3,"is",largest)
