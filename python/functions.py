def print_lyrics():
    print("I'm a lumberjack, and I'm okay")
    print("I sleep all night and I work all day.")
print_lyrics()


spam = 'Spam, '
def repeat(word, n): # repeat a word n times
    print(word * n)
def first_two_lines(): # display the first two lines
    repeat(spam, 4)
    repeat(spam, 4)
def last_three_lines(): # display the last three lines
    repeat(spam, 2)
    print('(Lovely Spam, Wonderful Spam')
    repeat(spam, 2)
def print_verse(): # display the whole verse
    first_two_lines()
    last_three_lines()
print_verse()

def print_n_verses(n):
    for i in range(1, n+1):
        print("Verse",i)
        print_verse()
        print()
print_n_verses(3)



