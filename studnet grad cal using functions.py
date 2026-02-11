def calculate_grade(*score,**adjustments):
    if not score:
        raise ValueError("At least one score is required.")
    #using it if the score has empty value, then it will raise an error
    #not will check 
    avg=sum(score)/len(score)#finds aberage of scores
    final_total=avg+sum(adjustments.values())
    '''as ** stors in dictionary, so we are adding the
      values which are stored in dictionary by using 
    the function called sum(adjustment.values()) 
    '''
    return(final_total)   

pk= calculate_grade(90,80,70,60,50,att=5)
print(f"final grade is {pk:.2f}")
#rounfing off to 2 decimal places


