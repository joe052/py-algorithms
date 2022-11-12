# define boxes
boxes = [[2, 1, 3], [6, 3, 8], [4, 2, 5], [3, 1, 6]]
#boxes = [[12, 4, 37], [67, 3, 84], [41, 2, 35], [33, 1, 64],[1,34,2]]

#method to arrange our stack
def stackSorter(boxes):    
    stackHeight = 0
    print("These are the unsorted boxes ", boxes)
    # loop through every box
    # calculate the area and push for sorting
    for box in boxes:
        area = box[0] * box[2]
        stackHeight += box[1]
        # store area in every box
        box.append(area)
        # print(box)
    
    n = len(boxes)
    # second loop to sort boxes in respect to area from largest to smallest
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            # if box area after is larger than current boxarea then swap them
            if boxes[j][3] < boxes[j + 1][3]:
                boxes[j], boxes[j + 1] = boxes[j + 1], boxes[j]
                already_sorted = False
        if already_sorted:
            break
    #trim off the areas
    for box in boxes:
        box.pop()       

    print("These are the sorted boxes ", boxes)
    print("the boxes stack to a height of ", stackHeight)



stackSorter(boxes)
