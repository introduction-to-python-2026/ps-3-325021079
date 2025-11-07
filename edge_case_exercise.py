def move(my_list, direction=None):
    index_of_one = my_list.index(1)
    
    # אם הרשימה היא [1] – אין מה להזיז
    if len(my_list) == 1 and my_list[0] == 1:
        return my_list

    # אם הכיוון שמאלה וה-1 כבר ראשון – לא מזיזים
    elif index_of_one == 0 and direction == "left":
        return my_list
  
    # אם הכיוון ימינה וה-1 כבר אחרון – לא מזיזים
    elif index_of_one == len(my_list) - 1 and direction == "right":
        return my_list
        
    # אם הכיוון ימינה, מזיזים ימינה
    elif direction == 'right':
        my_list[index_of_one] = 0
        my_list[index_of_one + 1] = 1
    
    # אם הכיוון שמאלה, מזיזים שמאלה
    elif direction == 'left':
        my_list[index_of_one] = 0
        my_list[index_of_one - 1] = 1

    # אם הכיוון None או לא חוקי – הרשימה נשארת כמו שהיא
    return my_list
