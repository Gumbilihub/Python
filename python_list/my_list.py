#Creating a list called My_list
My_list=[]
#adding values to the list 
My_list.append(10 )
My_list.append(20)
My_list.append(30)
My_list.append(40)
#replacing and inserting  15 in the list on the index 1 
My_list.insert(1,15)
#extending My_list 
My_list.extend([50,60,70])
#removing a lst value in a list
My_list.pop()
#sorting the list 
My_list.sort()
#find and print the index of value 30 in the list
Index_of_30=My_list.index(30)
#printing the final sorted state of My_list and the index of 30
print("final state of My_list:",My_list)
print("index of value 30 in My_list:",Index_of_30)