import requests
import csv
import pickle
import xmltodict
from nltk.corpus import stopwords

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&1234567890*_~'''

all_documents = []
topics = []


def preprocess_topics():
    counter = 1
    for element in topics:
        print(counter)
        counter +=1
        no_punc_query = ""
        no_punc_question = ""
        no_punc_narrative = ""
        for char in element["query"]:
            if char not in punctuations:
                no_punc_query= no_punc_query + char
        for char in element["question"]:
            if char not in punctuations:
                no_punc_question= no_punc_question + char
        for char in element["narrative"]:
            if char not in punctuations:
                no_punc_narrative= no_punc_narrative + char
        no_punc_query = no_punc_query.lower()
        no_punc_question = no_punc_question.lower()
        no_punc_narrative = no_punc_narrative.lower()
        removed_query =[]
        removed_question=[]
        removed_narrative=[]
        for word in no_punc_query.split():
            if word not in stopwords.words('english'):
                removed_query.append(word)
        for word in no_punc_question.split():
            if word not in stopwords.words('english'):
                removed_question.append(word)
        for word in no_punc_narrative.split():
            if word not in stopwords.words('english'):
                removed_narrative.append(word)
        query = ""
        question =""
        narrative =""
        for word in removed_query:
            query = query + " " + word
        for word in removed_question:
            question = question + " " + word
        for word in removed_narrative:
            narrative = narrative + " " + word
        element['query'] = query
        element['question'] = question
        element['narrative'] =narrative


def preprocess_all_docs():
    counter = 1
    for element in all_documents:
        print(counter)
        counter += 1
        no_punc_abstract = ""
        no_punc_title = ""
        for char in element["abstract"]:
            if char not in punctuations:
                no_punc_abstract = no_punc_abstract + char
        for char in element["title"]:
            if char not in punctuations:
                no_punc_title = no_punc_title + char
        no_punc_abstract = no_punc_abstract.lower()
        no_punc_title = no_punc_title.lower()
        removed_abstract = []
        removed_title = []
        for word in no_punc_abstract.split():
            if word not in stopwords.words('english'):
                removed_abstract.append(word)
        for word in no_punc_title.split():
            if word not in stopwords.words('english'):
                removed_title.append(word)
        abstract = ""
        title = ""
        for word in removed_abstract:
            abstract = abstract + " " + word
        for word in removed_title:
            title = title + " " + word
        element['title'] = title
        element['abstract'] = abstract


def get_experiment_files():
    with open("metadata.csv", 'r') as data:
        dict_data = csv.DictReader(data)
        for data in dict_data:
            element = {'document_id' : data['cord_uid'], 'title' : data['title'], 'abstract' : data['abstract'] }
            all_documents.append(element)
        preprocess_all_docs()
        with open('all_documents_pre_process.pickle', 'wb') as handle:
            pickle.dump(all_documents, handle, protocol=pickle.HIGHEST_PROTOCOL)

def get_topics():
    response = requests.get('https://ir.nist.gov/covidSubmit/data/topics-rnd5.xml')
    data = response.text
    data = xmltodict.parse(data)
    for element in data['topics']['topic']:
        new_topic = {
            'number' : element['@number'],
            'query': element['query'],
            'question': element['question'],
            'narrative': element['narrative'],
        }
        topics.append(new_topic)
    preprocess_topics()
    with open('topics.pickle_pre_process', 'wb') as handle:
        pickle.dump(topics, handle, protocol=pickle.HIGHEST_PROTOCOL)
get_experiment_files()
get_topics()
