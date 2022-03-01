import pickle
from pandas import DataFrame


def empty():
    ''' Empty pickle for word studied'''
    words_studied=set()
    with open('Output\\words_studied_list.pkl','wb') as f:
        pickle.dump(words_studied,f)

    ''' Empty pickle for data on word studied'''
    column_names=['wordorphrase','meaning','sentences']
    words_studied_data=DataFrame(columns=column_names)
    with open('Output\\words_studied_data.pkl','wb') as f:
        pickle.dump(words_studied_data,f)


def read_em():
    '''Reading them to see whats inside the pickles'''
    with open('Output\\words_studied_list.pkl','rb') as f:
        temp=pickle.load(f)

    print(temp)

    with open('Output\\words_studied_data.pkl','rb') as f:
        temp=pickle.load(f)

    print(temp.head())

# empty()
read_em()
