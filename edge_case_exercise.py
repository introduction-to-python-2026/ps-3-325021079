def move(my_list, direction=None):
    # Finds the index of the one in the list
    index_of_one = my_list.index(1)
    if my_list[0] == 1 and len(my_list) == 1 :
      return my_list

    elif index_of_one == 0 and direction == "left" :
        return my_list
  
    elif index_of_one == len(my_list) -1 and direction == "right" :
        return my_list
        
    elif  direction == 'right':
           my_list[index_of_one] = 0
           my_list[index_of_one + 1] = 1
    
    elif  direction == 'left' :
          my_list[index_of_one] = 0
          my_list[index_of_one - 1] = 1

    return my_list
