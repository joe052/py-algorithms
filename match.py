boxGroups = [[140,120,150,100,170,200,90,180],[170,150,140,90,100,120,180,200],[120,90,200,150,180,140,100,170]]

def matchBox(arrays):
    for i in range(len(arrays[0])):        
        target = arrays[0][i]
        box = 0
        for array in arrays:
            if(box == 0):
                boxName = 'A'
            elif(box == 1):
                boxName = 'B'
            elif(box == 2):
                boxName = 'C'      
            for i in range(len(array)):                 
                if(array[i] == target):
                    start = ''
                    if(box != 0 & box != 1):                       
                        start = ' with ' 
                        print(start+boxName+'['+str(i+1)+']', end = "")
                    else:
                        print('\n',start+boxName+'['+str(i+1)+']', end = "")                    
            box += 1
            
matchBox(boxGroups)