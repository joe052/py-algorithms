# ages = [11, 10, 7, 13, 14, 12,9,15,8]
ages = [8,5,9,4,10]

# function to check age difference
def checkAgeDifferences(ages):
    n = len(ages)
    print(n)
    # array to store the differences
    diffArr = []
    # loop through the array
    for i in range(n):
        # loop through the remaining range and substract higher age differences is any
        for j in range(i,n-1):
            # substract higher age differences if any and push the difference           
            if(ages[j+1] > ages[i]):        
                diff = ages[j+1]-ages[i]
                diffArr.append(diff)                                       
                break
            # if there is no difference append '-1'   
            if(ages[j+1]==ages[n-1]):                      
                diffArr.append(-1)  

        # connect the starting point of the array to the end of the array
        if(ages[0] > ages[n-1]):
            lastNumber = ages[0] - ages[n-1]
        else:
            lastNumber = -1
    # append last number
    diffArr.append(lastNumber)

    print(diffArr)

checkAgeDifferences(ages)