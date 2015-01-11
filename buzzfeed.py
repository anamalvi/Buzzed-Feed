import tweepy
import random
import time

auth = tweepy.OAuthHandler(' ', ' ')
auth.set_access_token(' ', ' ')


def makeIntoList(fileName):
    f = open(fileName)
    list_of_words = []
    for line in f:
        list_of_words.append(line.strip())
    return list_of_words

def chooseWord(fileName):
    list_of_words = makeIntoList(fileName)
    index = random.randint(0,len(list_of_words)-1)
    return list_of_words[index]

def chooseArticle():
    article_types = ['q','lst','sgn','knw']
    return article_types[random.randint(0,4)]

def createArticle():
    article_type = chooseArticle()
    if (article_type == 'q'):
        if random.randint(1,2)%2 == 0:
            article_name = 'How Well Do You Know '
            article_name += chooseWord('nouns.txt')
        else:
            if random.randint(1,2)%2 == 0:
                article_name = 'Which ' + chooseWord('nouns.txt') + ' Are You?'
            else:
                article_name = 'Which ' + chooseWord('nouns.txt') + \
                    ' Should You ' + chooseWord('verbs.txt')
            
    elif (article_type == 'lst'):
        article_name = str(random.randint(2,30)) + ' ' + chooseWord('adjectives.txt') + \
            ' ' + chooseWord('nouns.txt') + ' ' + chooseWord('phrases.txt')  + ' ' + chooseWord('were.txt')
    
    elif (article_type == 'sgn'):
        if random.randint(1,2)%2 == 0:
            article_name = str(random.randint(2,30)) + ' Signs You Are A ' + \
                chooseWord('adjectives.txt') + ' ' + chooseWord('nouns.txt')
        else:
            article_name = str(random.randint(2,30)) + ' Signs You Are A ' + chooseWord('nouns.txt')            
    else:
        article_name = str(random.randint(2,30)) + ' ' + chooseWord('nouns.txt') + \
            ' Every ' + chooseWord('nouns.txt') + ' Should Know'
    
    return article_name
            
##MAIN##

while True:
    api.update_status(createArticle())
    time.sleep(3600)
    
        