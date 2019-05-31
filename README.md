::: {.document}
::: {.documentwrapper}
::: {.bodywrapper}
::: {.body role="main"}
::: {#idf-generation-documentation .section}
IDF Generation [¶](file:///C:/Users/jyoti.vinayak/idf/_build/html/index.html#idf-generation-documentation "Permalink to this headline"){.headerlink}
=================================================================================================================================================================

 `idf`{.descname}[(]{.sig-paren}*documents*[)]{.sig-paren}[¶](file:///C:/Users/jyoti.vinayak/idf/_build/html/index.html#idf "Permalink to this definition"){.headerlink}

:   

[]{#module-idf.idf_generator .target}

IDF refers to **Inverse Document Frequency**. It generates the score
against each document based on the occurance of the document. It takes
the exact match of the documents.

The documents may be : *Words, Sentences, Paragraphs*.

Given a list of documents, they are rearraged by descending order of the
IDF score. The score is so calculated that the least occuring document
in the list gets the highest score and the most occuring document gets
the lowest score. The IDF score has mathematical formulae:

> <div>
>
> L1= Total number of documents
>
> L2= Frequency of an individual document
>
> IDF = log (L1/ L2)
>
> </div>

 `idf.idf_generator.`{.descclassname}`idf`{.descname}[(]{.sig-paren}*documents*[)]{.sig-paren}[¶](file:///C:/Users/jyoti.vinayak/idf/_build/html/index.html#idf.idf_generator.idf "Permalink to this definition"){.headerlink}

:   **Pre-requisite Libraries**: Pandas, Numpy

    **INPUT**: (List of documents)

    **OUTPUT**: (Dataframe with documents, frequency, idf)

    Examples:

    Documents=\['car','truck','car','truck','rabbit','car','train'\]

    Documents=\['one-month duration\|block\|opioid agonist challenge effect',
    :   'opioid treatment sample\|find\|fatal dose error',
        'atypical-opioid receptor agonist\|be\|morphine-resistant
        interactive pain', 'one-month duration\|block\|opioid agonist
        challenge effect'\]

![\_images/ex1.idf1.jpg](file:///C:/Users/jyoti.vinayak/idf/_build/html/_images/ex1.idf1.jpg){.align-center}
![\_images/ex2.idf1.jpg](file:///C:/Users/jyoti.vinayak/idf/_build/html/_images/ex2.idf1.jpg){.align-center}
:::
:::
:::
:::

::: {.sphinxsidebar role="navigation" aria-label="main navigation"}
::: {.sphinxsidebarwrapper}
[IDF Generator](file:///C:/Users/jyoti.vinayak/idf/_build/html/index.html#) {#idf-generator .logo}
===========================================================================

### Navigation

::: {.relations}
### Related Topics

-   [Documentation
    overview](file:///C:/Users/jyoti.vinayak/idf/_build/html/index.html#)
:::

::: {#searchbox style="" role="search"}
### Quick search

<div>

</div>

<div>

</div>
:::
:::
:::

::: {.clearer}
:::
:::

::: {.footer}
©2019, JyotiVinayak. \| Powered by [Sphinx
1.6.3](http://sphinx-doc.org/) & [Alabaster
0.7.10](https://github.com/bitprophet/alabaster) \| [Page
source](file:///C:/Users/jyoti.vinayak/idf/_build/html/_sources/index.rst.txt)
:::
