#DSA-Assgn-1

def merge_list(list1, list2):
    merged_data=""
    resultant_data=[]
    #write your logic here
    list2.reverse()
    for i in range(min(len(list1),len(list2))):
        if(list1[i] is None):
            merged_data=list2[i]
        elif(list2[i] is None):
            merged_data=list1[i]
        else:
            merged_data=list1[i]+list2[i]
        resultant_data.append(merged_data)
        
    return ' '.join(map(str,resultant_data))

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)