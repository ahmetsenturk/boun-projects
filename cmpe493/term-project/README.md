# Term Project: TREC-COVID Challenge

TREC-COVID followed the TREC model for building IR test collections through community evaluations of search systems. The document set used in the challenge is the COVID-19 Open Research Dataset (CORD-19) [1]

The results of the TREC-COVID Challenge identify answers for some of today's questions and create infrastructure to improve tomorrow's search systems [1]

In this project, we have implemented some different information retrieval models to get better results for TREC-COVID Challenge

## Preprocessing Steps

We have applied following steps in order to process the raw data:

1 - **Mark-up removal:** Removing HTML tags from the content
2 - **Tokenization:** Splitting the content into words using whitespace as delimiter
3 - **Punctuation removal**
4 - **Lowercasing**
5 - **Stop-word removal:** Stopwords feature of python nltk library and built-in function of TfidfVectorizer
6 - **Removing duplicates:** Rows with duplicate document ids are removed from the data set

## Ranking Algorithms (Document Scoring Methods)

We have tried the following statistical measures that evaluates how relevant a query is to a document in a collection of documents (i.e., retrieve relevant documents to a query from the Covid-19 related scientific literature) 

1 - TF-IDF + Cosine Similarity
2 - BM25

## Additional Research

- **Using a query generator with SciSpaCy:** As shown by Schoegje et al (2020) University of Delaware’s query generator (udel) can be used. [2, 3] We have expanded queries with biomedical entities selected using SciSpaCy. We have experimented with different weightings and saw minor improvements

- **Document clustering:** We have clustered documents to let the  documents in the same clusters have closer cosine similarity scores. This approach has reduced the performance remarkably


## Notebooks and Files

### We have 4 different jupyter notebook files for each of the models we have tried:
- BM25_baseline.ipynb : Baseline model with rank BM 25 approach
- TF-IDF_Baseline.ipynb : Baseline model using TF-IDF algorithm
- BM25_with_SciSpacy.ipynb : Uses rank BM 25, with query genarator
- BM25_with_BERT.ipynb : Uses rank BM 25, with BERT reranking method

### For the preprocessing and extracting data we have use the following scripts:
- Preprocessing.ipynb
- file_filter.py

## Document files:
- all_documents.pickle
- topics.pickle 

## References

1 - https://ir.nist.gov/covidSubmit/
2 - Schoegje, Thomas, Chris Kamphuis, Koen Dercksen, Djoerd Hiemstra, Toine Pieters, and Arjen de Vries. 2020. “Exploring Term Expansion for Task-Based Retrieval at the TREC-COVID Track.” ArXiv:2010.12674 [Cs], October. http://arxiv.org/abs/2010.12674.
3 - https://scispacy.apps.allenai.org/
