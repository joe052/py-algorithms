ages = [11, 10, 7, 13, 14, 12,9,5,8]
# ages = [1,2,3,4,5,6,7,8,9,10]

def checkAgeDifferences(ages):
    n = len(ages)
    print(n)
    diffArr = []
    for i in range(n):
        for j in range(i,n-1):
            # print(ages[j])            
            if(ages[j+1] > ages[i]):        
                diff = ages[j+1]-ages[i]
                diffArr.append(diff)                                       
                break
            if(ages[j+1]==ages[n-1]):
                # print("yes")         
                diffArr.append(-1)    
    print(diffArr)

checkAgeDifferences(ages)