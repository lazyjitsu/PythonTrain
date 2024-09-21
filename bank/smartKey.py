import difflib
list_of_words = ["dear","bears","bear","robot","pear","island"]

# return 4 words and 0 thru 1 is the zoom aspect where 1 is absolutely identical and anything less is 'close'
#x = difflib.get_close_matches('ear',list_of_words,4,0-1)
x = difflib.get_close_matches('bear',list_of_words,4,.8)
print(type(x))
def get_word(w):
    print("func called")
    x = difflib.get_close_matches(w,list_of_words,4,.7)
    print(f"Length {len(x)}")
    if w in list_of_words:
        return w
    if len(x) == 0:
        print(f"Congrats!! You found {i} !!!!!!!!!!!!!!!")
    elif len(x) >= 0:
        for i in x:
            #print(f"did u mean {i}")
            resp = input(f"did u mean {i} ?")
            answer = resp.lower()
            print(f"ans {answer}")

            if answer == 'y' or answer == 'yes':
                #print(f"Found u  {i}  !")
                return w
            elif answer == 'n':
                return 'sorry'
            else:
                return 'not found'
    return
word = input("Please enter a word: ")
resp = get_word(word)

if resp == word:
    print(f"Glad to be of assistance in getting you the def for {word}")
elif resp == 'not found':
    print(f"Learn how to spell loser!!")
else:
    print(f"sorry bro!")