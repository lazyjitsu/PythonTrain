import difflib
list_of_words = ["dear","bears","bear","robot","pear","island"]

# return 4 words and 0 thru 1 is the zoom aspect where 1 is absolutely identical and anything less is 'close'
#x = difflib.get_close_matches('ear',list_of_words,4,0-1)
x = difflib.get_close_matches('ear',list_of_words,4,.8)