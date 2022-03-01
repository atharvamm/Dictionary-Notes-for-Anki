'''1.Here you do all the import and initialization work'''
from time import sleep
from pandas import DataFrame
import meanings as m
from os import system
import sents
from pickle import load,dump
import empty_pickles
error_words=[]
column_names=['wordorphrase','meaning','sentences']
data_studied_today=DataFrame(columns=column_names)
word_studied_today=set()

'''If you want to start new'''
# empty_pickles.empty()

'''Loading Stored Values'''
with open('Output\\words_studied_data.pkl','rb') as f:
    words_studied_data=load(f)

with open('Output\\words_studied_list.pkl','rb') as f:
    words_studied_list=load(f)

'''If word already_studied'''
def already_studied(word):
    df = words_studied_data[words_studied_data['wordorphrase']== word]
    m=df['meaning'].values[0]
    s=df['sentences'].values[0]
    return m,s


'''2.Load the doubt words'''
with open('Input\\doubts.txt','r')  as f:
    temp=f.read()
doubt_words=temp.split('\n')
for word in doubt_words:
    system('cls')
    print("Current word studied today: ",word_studied_today)
    if word in word_studied_today:
        continue
    '''3.Get data on the words'''
    try:
        word_meaning,word_sentences="",""
        if word in words_studied_list:
            print('Already Studied:',word)
            word_meaning,word_sentences=already_studied(word)
            print("Information retrieved for",word)
        else:
            print("Studying",word,".....")
            meaning=m.get_mean(word)
            if meaning=="Nothing":
                print("No meanings for",word)
                raise Exception
            print("Meaning Done for",word)
            explain=m.get_explaination(word)
            print("Explaination found for",word)
            word_forms,all_forms=m.get_wordforms(word)
            print("Word forms found for",word)
            word_meaning="Meaning:<br><br> "+meaning+"<hr>Explaination: "+explain+"<hr>"+word_forms
            #'''For the get_sentences you can give a second argument for number of sentences,default is 15'''
            print("Finding sentences for",word)
            word_sentences=sents.get_sentences(word,n=15)
            temp_word_data=[word,word_meaning,word_sentences]
            words_studied_data.loc[len(words_studied_data.index)] = temp_word_data
            words_studied_list.add(word)
        word_studied_today.add(word)
        temp_word_data=[word,word_meaning,word_sentences]
        data_studied_today.loc[len(data_studied_today.index)] = temp_word_data
        # print("Word Meaning: ",word_meaning)
        # print("Sentences for the word: ",word_sentences)
        print("Studied",word)
        
    except:
        # '''4.Store the error words'''
        error_words.append(word)
    
    print()
    waiting=10
    for i in range(waiting):
        print(waiting-i,""*waiting,end='\r')
        sleep(1)
# 5.Store variables for future reference
# Use pickle here to store the words studied till now
with open('Output\\words_studied_list.pkl','wb') as f:
    dump(words_studied_list,f)

# Use pickle here to store the data of the words studied till now
with open('Output\\words_studied_data.pkl','wb') as f:
    dump(words_studied_data,f)

# Use text file to store error_words
with open('Output\\errors.txt','w') as f:
    f.write("\n".join(error_words))

'''6.Store for anki'''

# with open('Output\\today_for_anki.pkl','wb') as f:
#     dump(data_studied_today,f)

data_studied_today.index += 1
data_studied_today.to_csv('Output\\anki_upload.csv',encoding='utf-8')
data_studied_today.to_html('Output\\anki_read.html',encoding='utf-8')
'''To read what you have saved'''
empty_pickles.read_em()
