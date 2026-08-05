def calc2(n1, n2):
   list1=[]
   sum1 = n1 + n2
   dif1 = n1 - n2
   prd1 = n1 * n2
   div1 = n1 / n2
   div2 = n1 // n2
   rem1 = n1 % n2 
   exp1 = n1 ** n2 
   list1.append(sum1)
   list1.append(dif1)
   list1.append(prd1)
   list1.append(div1)
   list1.append(div2) 
   list1.append(rem1)
   list1.append(exp1)
   return list1
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
result=calc2(n1,n2)
print("The list is:")
print(result)