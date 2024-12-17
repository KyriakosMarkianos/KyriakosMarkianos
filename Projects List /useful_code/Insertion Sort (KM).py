######################## INSERTION SORT #######################

def ins_sort(data):
    
    for i in range(1, len(data)):
        temp=data[i]
        j = i-1
        while (j>=0 and data[j]>temp):
            data[j+1] = data[j]
            data[j] = temp
            j -= 1
        
    return data 

my_data=[1,7,8,2,6,3,5,4,9]

print(ins_sort(my_data))