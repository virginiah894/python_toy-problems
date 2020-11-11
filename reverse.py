# first try ..incorrrect
def reverse():
    words = list(input('Enter a word')).split(' ')
    rev_words = words.reverse().join(list)
    return(rev_words)
reverse()


def reverse():
      quiz = input('Write something: ')
      x = quiz.split(" ")
      x.reverse()
      newone = " ".join(x)
      print (newone)
reverse()


# try 2 refactored..not
def reverse_word():

   a= input('write your sentence')

   break_word= a.split(" ")

   revword= break_word[::-1]
   
   print(revword)
reverse_word()

#  samething just joined the words for clarity

def reverse_words():

   a= input('write your sentence')

   break_word= a.split(" ")

   revword= break_word[::-1]
   revword1 = ' '.join(revword)
   
   print(revword1)
reverse_words()