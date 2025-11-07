def move(my_list, direction=None):
   
    index_of_one = my_list.index(1)
  
    #אם אין ערך לכיוון
    if direction is None:
        return my_list
   #אם יש רק ערך 1 שהוא 1 
    if my_list[0] == 1 and len(my_list) == 1 :
        return my_list

    #אם קצה שמאל הוא 1
    if index_of_one == 0 and direction == "left" :
        return my_list
  
    #אם קצה ימין הוא 1
    if index_of_one == len(my_list) -1 and direction == "right" :
        return my_list
        
    if  direction == 'right':
           my_list[index_of_one] = 0
           my_list[index_of_one + 1] = 1
    
    elif  direction == 'left' :
          my_list[index_of_one] = 0
          my_list[index_of_one - 1] = 1

    return my_list
