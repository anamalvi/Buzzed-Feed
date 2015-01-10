import tweepy
import random

#list articles = 'number' + 'adjective' + 'noun' + 'phrase' + 'were _________'
#phrase examples = 'you'll never guess', ' that were always secretly', 'you always knew' 
# 'you totally forgot'
# 'number' + 'signs' + 'you are/you have/you need' + 'a slob/diabetes/Jesus'

#quizzes = 'how well do you know' + 'noun'
#'take this quiz to find out if you are' + 'noun'
#'Which' + 'noun' + 'are you?'
#'which' + 'noun' + 'should you' + 'verb'


#'number' + 'signs you are a' + ('adjective' + ) ''noun'

#'number' + 'noun' + 'every' + 'person noun' + 'should know'



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
            
        
        