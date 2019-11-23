### Please read the following instructions carefully:###

The TapSearch takes in multiple paragraphs of text, assigns a unique ID to each paragraph and stores the words to paragraph mappings on an inverted index.

Given a word to search for, it lists out the top 10 paragraphs in which the word is present.

It mainly consists of three API endpoints:

1) clear - Clear the index and all indexed documents.

2) index - Index a given document.

3) Search - Given a word, search for it and retrieve the top 10 paragraphs (Documents) that contain it.

####Note: Use clear button before entering any data! ####

The code is deployed on Heroku. Try to play around with the deployment.

If you want to setup a local development server in Linux/macOS, follow below mentioned steps:

- `sudo apt install virtualenv`

- `virtualenv -p python .`

- `source bin/activate`

- `pip install -r requirements.txt`

- `python manage.py runserver`

#### After last step you will be able to run the server locally. ####