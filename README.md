IDF Generation

**IDF** refers to **Inverse Document Frequency**. It generates the score
against each document based on the occurrence of the document.

The documents may be: *Words, Sentences, Paragraphs*.

Given a list of documents, they are rearranged by descending order of
the IDF score. The score is so calculated that the least occurring
document in the list gets the highest score and the most occurring
document gets the lowest score. The IDF score has mathematical formulae:

> L1= Total number of documents
>
> L2= Frequency of an individual document
>
> IDF = log (L1/ L2)

idf.idf\_generator.**idf**(*documents*)

> **Pre-requisite Libraries**: Pandas, Numpy
>
> **INPUT**: (List of documents)
>
> **OUTPUT**: (Dataframe with documents, frequency, idf)
>
> **Examples**:
>
> Document 1 = \['car', 'truck', 'car', 'truck', 'rabbit', 'car',
> 'train'\]
>
> Document 2 = \['one-month duration\|block\|opioid agonist challenge
> effect',
>
> 'opioid treatment sample\|find\|fatal dose error', 'atypical-opioid
> receptor agonist\|be\|morphine-resistant interactive pain', 'one-month
> duration\|block\|opioid agonist challenge effect'\]

![\_images/ex1.idf1.jpg](media/image1.jpeg){width="6.125in"
height="0.8881944444444444in"}![\_images/ex2.idf1.jpg](media/image2.jpeg){width="6.268055555555556in"
height="1.025495406824147in"}

**Author**

Jyoti Vinayak (Jyoti.vinayak\@chubb.com)

**Version History**

\* 0.1

\* Initial Release

**License**

This code is for exclusive use by Chubb users
