'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    th = word.find('th')
    if th == -1: ## -1 means there is no 'th' in the string 
        return 0

    return 1 + count_th(word[th+2:]) ##skip the first occurance index +2 and then move till the rest
    
print(count_th('aihfdthkfjdthTHth'))

    
    
    


