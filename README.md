# English Dictionary Notes in CSV format
## dictionary.py


The main code file, run this to generate a .csv and .html file of the words studied when you ran the code, and two pickle files which store data from all the previous runs

## empty_pickles.py

Run this file before starting, empty() stores one empty dataframe and one empty list before you start, while read_em() can be used to read the data stored in the pickle files

## Important files

- doubts.txt : To store the words that are meant to be studied
- errors.txt : To store the words that had errors while studying them, usually are words that are spelled incorrectly
- anki_read.html : Data of the words studied when the program was executed in html file
- anki_upload.csv : Data of the words studied when the program was executed in csv format for uploading to anki. (Encoding: 'utf-8')
- word_studied_data.pkl : Data of all the words studied till date 
- word_studied_list.pkl : List of all the words studied till date

##### Note : There is a function for synonyms and antonyms which can be used if needed in the meanings.py
