**Text Cleaner**

**Description**

This code will clean raw uncleaned data including email chain
conversations and other filenotes data, clean the noise like html tags,
punctuation, non-ascii values, timestamps, non-informative email tags
and repetetive sentences like confidentiality notice, company into etc.
Output will be list of clean sentences.

**Dependencies**

python library : pandas,re, nltk, fuzzywuzzy

Input data: Uncleaned raw text with html tags, email headers etc.

**Executing program**

**Usage:-**
![image](https://drive.google.com/uc?export=view&id=1Vee2saqB_N01ERFBBAGqfpqIdPpK9c_k)

\*\* cleaned\_data is the function that will be called to clean the
data. While applying in dataframe, This function will be called.

df\[\'cleaned\_data\] = df\[\'filenotes\'\].apply(lambda fn**:
cleaned\_data(fn, stop\_sents, threshold, spell\_correction\_dict,
spell\_correct\_flag=False)**)

As we can see it requires \"stop\_sents\" and \"threshold\" ,
\"spell\_correction\_dict\" as prerequisites. So this data cleaning
should be done in following process.

**Pipeline:-**

**Step 1)** Create stop\_sents:-

Finds duplicate sentences with a given frequency threshold in the whole
corpus and returns sentences which satisfies the frequency threshold.

\* stop\_sents = stop\_phrases(df\[\'filenotes\'\].values)

\* threshold should be choosed based on manual validation. default value
is 10.

**Step 2)** If Spell correction is requried, This process should be
followed

\* spell\_correction\_dict should be created and passed on
cleaned\_data.

\* If spell correction is not required then pass a empty dictionary.

\* spell\_correction\_dict =
create\_spell\_correction\_dict(to\_be\_corrected\_list, corpus\_words)

to\_be\_corrected\_list = list of words to be corrected.

corpus\_words = list of all the words in all filenotes column. These two
list has to created by the user.

Note that this function only corrects targeted words and not all the
words. So use this only when required.

**Step 3)** Apply cleaned\_data on filenotes column

\* df\[\'cleaned\_data\] = df\[\'filenotes\'\].apply(lambda fn:
cleaned\_data(fn, stop\_sents, threshold, spell\_correction\_dict,
spell\_correct\_flag))

**Output:** cleaned filenotes (string)

**Author**

Rajeev Ranjan(rajeev.ranjan\@chubb.com)

**Version History**

\* 0.1

\* Initial Release

**License**

This code is for exclusive use by Chubb users
