#2 BUGS
def get_average(scores): # function to get average of scores
    total = 0 # variable of total and set it to 0
    for score in scores: # for each score in scores
        total += score # count the total and set equal to variable total
    average = total/len(scores) # should be plural #create average variable 
    return average # should return 70
        
scores = [90, 80, 70, 60, 50]
print("The average score is: ", get_average(scores)) # should be plural
    