'''1. Get meaning of words from vocabulary api'''
'''Imports and initialization'''
from PyDictionary import PyDictionary
dictionary=PyDictionary()
import urllib.request
import notwords
# '''2.Extra functions'''
def clean_meanings(mean):
    cleaned_meaning=""
    for i in list(mean.keys()):
        cleaned_meaning=cleaned_meaning+i+":"+str(mean[i])+"<br>"
    # print(cleaned_meaning)
    return cleaned_meaning
# '''3.If word not in main dictionary go for urban dictionary'''
def get_mean(word):
    try:
        if not(word.isalpha()):
            mean = notwords.urban_dictionary(word)
            return mean
        mean_dict=dictionary.meaning(word)
        # clean_meanings(mean_dict)
        return (clean_meanings(mean_dict))
    except Exception as e:
        # print(e)
        print("No meanings found")

# '''4.Get explanation of words from vocabulary.com'''
def get_explaination(word):
    try:
        link="https://www.vocabulary.com/dictionary/ "[:-1]+word
        data=urllib.request.urlopen(link).read().decode('utf-8')
        og_data=data
        start_1=og_data.index('<meta name="description" content=')
        end_1=og_data.index("/>",start_1)
        start_2=og_data.index(',"description":')
        end_2=og_data.index(',"inDefinedTermSet":"https://www.vocabulary.com/dictionary/"}</script>',start_2)
        txt1=og_data[start_1+len('<meta name="description" content=')+1:end_1-2]
        txt2=og_data[start_2+len(',"description":')+1:end_2-1]
        temp=txt1+txt2
        final=[]
        for t in temp:
            if t.isalpha() or t in [" ",".",'"',"'",",",";",":","?"]:
                final.append(t)
        # print("".join(final))
        return ("".join(final))
    except:
        return "Not on vocabulary.com"

# '''5.Get antonyms of words from wordhippo.com'''
def get_ant(word):
    try:
        return dictionary.antonym(word)
    except:
        return "No antonyms"

# '''6.Get synonyms of words from wordhippo.com'''
def get_syn(word):
    try:
        return dictionary.synonym(word)
    except:
        return "No synonyms"

# '''7.Get Word Forms'''
def get_wordforms(word):
    from word_forms.word_forms import get_word_forms
    try:
        allwords=[]
        temp=get_word_forms(word)
        if len(temp['n'])==0 and len(temp['v'])==0 and len(temp['a'])==0 and len(temp['r'])==0:
            raise Exception
        temp["Noun"]=temp["n"]
        del temp["n"]
        temp["Adjective"]=temp["a"]
        del temp["a"]
        temp["Adverb"]=temp["r"]
        del temp["r"]
        temp["Verb"]=temp["v"]
        del temp["v"]
        in_str=""
        for key in temp.keys():
            if len(temp[key])>0:
                # print("Temporary Information: ",list(temp[key]))
                for i in list(temp[key]):
                    if i not in allwords:
                        allwords.append(i)
                in_str=in_str+key+" Forms: "+" ".join(temp[key])+"<br>"
        # print(in_str)
        # print("All words: ",allwords)
        return [in_str,allwords]
    except :
        return [" No word forms"," "]


