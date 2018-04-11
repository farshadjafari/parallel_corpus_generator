# Multilingual Parallel Corpus Generator
Python application, generating parallel corpus for any language pairs, can be used for training nmt (Neural Machine Translation) systems

# Manual

Using the described method in this article we implemented a small version of working framework to examine its results. 
The code is open-source and available to [use](https://github.com/farshadjafari/parallel_corpus_generator/). 
It's written in python language, using mongodb as database. 
Therefore working with it needs a fair knowledge of python language.


For running project do the following steps: 

- Install python on your system if dont have it. More information about installing python can be found [here](https://www.python.org/downloads/).

- Install and run mongodb. More information about installing mongodb can be found [here](https://docs.mongodb.com/manual/installation/).

- clone the project from github. 
```
git clone https://github.com/farshadjafari/parallel_corpus_generator.git
```
- create a virtual environment for python somewhere near the code:
```
virtualen venv
source venv/bin/activate
```
- install required python packages with pip:
```
pip install requirements.txt
```
you can run all steps with default by running following commanf but it may take hours to days to get done. I recommend to run each step separately.

    python main.py {source language code} {destination language code}
replace  source and destination language code with your desired alpha2 language codes. For example:

    python main.py en fa

## initializing videos

in order to storing movie dataset in database run following command:

    python movies/reader.py {source language code} {destination language code}


## filters

edit movies/filter.py file for desired movie filters. 
The number of videos after filtering will show by running:

    python movies/filter.py

## crawl

in order to crawl and download synchronized subtitles for desired filters and languages run:

    python downloader/main.py {source language code} {destination language code}

## store dialogues

in order to storing synchronous dialogues in database run:

    python subtitle/main.py {source language code} {destination language code}

## match sentence pairs

in order to extract sentence pairs from stored dialogues run:

    python matcher/main.py {source language code} {destination language code}

## generate corpus

finally after running all commands above for generating parallel corpus run:

    python generator/main.py {source language code} {destination language code}


