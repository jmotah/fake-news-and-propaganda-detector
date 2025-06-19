# Fake News and Propaganda Detector
Project by Julien Motaharian and Spencer Karofsky



# Importance of detectors to detect statement validity

Misinformation is one of the world's most critical hinderances. It is a direct cause of many public crises, social unrest, and it even distorts elections. The addition of social media in today's day and age allows these falsehoods to spread much quicker than we may anticipate, with information being able to reach millions of users in mere seconds. 

Reliable detection methods will allow citizens to break down the truth of a speaker's narrative, or a users post, allowing them to truly understand the validity behind the actual statement.

# Where does the data come from?

## FakeNewsNet
Where is it from?: Public Kaggle Repository by Steven Peutz

How did the author collect the data?: He scraped full-length news articles from a various source of online outlets.

What is the types of data in it?: The data types includes long news stories and op-eds

Who wrote the data in it: Professional journalists and bloggers; the labels were added by Steven Peutz (again, the repository author)


## LIAR
Where is it from?: A Kaggle dataset by William Wang

How did the autor collect the data?: It was about 12 years of political claims coming from PolitiFact API

What is the types of data in it?: It mainly consists of single sentence political claims or quotes

Who wrote the data in it?: Politicians and public figures are responsible for writing the data, while labels were assigned by PolitiFact editors


## Misinformation Fake News
Where is it from?: Comes from ASU through a GitHub repository

How did the author collect the data?: The data was crawled through articles by PolitiFact and Gossipcop. This helps us include social media context in our model

What is the types of data in it?: The types of data include politics and entertainment. Tweets are also included

Who wrote the data in it?: The data was primarily written by news reporters and regular social media users while the labels were assigned by PolitiFact and GossipCop editors



# Repository Layout
```
fake-news-and-propaganda-detector:
    - chat_gpt_citations.txt
    - fake_news_transformer.ipynb
    - lr_baseline_model.ipynb
    - LSTM - train.ipynb
    - model_utils.py
    - README.md
    - RNN - train.ipynb
    - BERT_model.ipynb
    - datasets
        - fakenewsnet-dataset
            - gossipcop_fake.csv
            - gossipcop_real.csv
            - politifact_fake.csv
            - politifact_real.csv
        - liar-dataset
            - README
            - test.tsv
            - train.tsv
            - valid.tsv
        - misinfo-dataset
            - DataSet_Misinfo_FAKE.csv
            - DataSet_Misinfo_TRUE.csv
            - EXTRA_RussianPropaganda_Subset.csv
    - bert_fakenews_detection_finetuned
        - config.json
        - model.safetensors
        - speak_tokens_maps.json
        - tokenizer_config.json
        - vocab.txt
```



# Data Normalization

With datasets coming from three different places, we utilized a model_utils.py class to create centralized functions to make it easy to normalize our data to only contain text and labels rows. We ensured text consisted of gramatically correct sentences, while the labels were that of either '1' representing true or '0' representing fake information.



# Quick Start

Gives you the opportunity to 

```
git clone https://github.com/jmotah/fake-news-and-propaganda-detector.git

# ENTER THE BERT_model.ipynb CLASS AND ADD A NEW CODE CELL FIRST

example_string = "SENTENCE YOU WANT HERE"
predict(example_string)
```


# Model Information

## Baseline - Logistic Regression Model

Vectorizer: CountVectorizer

Classifier: PyTorch Logistic Regression of solver "saga" with 100 max iterations

Train/Test Split: 80/20

Evaluation Metrics: Accuracy with 79.8%, Precision with 79.9%, Recall with 79.7%, and F1 with 79.7%

Train Time: About 3 minutes on Mac OS M2 Pro Chip CPU

## Model 1 - BERT

Model: Bert Base Uncased from HuggingFace

Optimizer: Adam

Epochs: 3

Max Tokens: 256

Batch Size: 32

Train/Test Split: 90/10

Evaluation Metrics: Accuracy with 93.4%, Precision with 93.4%, Recall with 93.4%, and F1 with 93.4%

Train time: about 5.9 hours on Mac OS M2 Pro Chip CPU

## Model 2 - LSTM

Architecture: Embedding -> 1 tanh layer with 256 hidden -> FC classifier

Optimizer: Adam

Epochs: 10

Embedding Size: 128

Batch Size: 64

Train/Test Split: 80/20

Evaluation Metrics: Accurracy: 88.4%, Precision: 86.9%, Recall: 91.1%, F1: 88.4%

## Model 3 - RNN

Architecture: Embedding layer → Single-layer RNN with ReLU activation (hidden size 256) → Fully connected output layer for binary classification  

Tokenizer: Custom word-level vocabulary with fixed-length sequence encoding (padded/truncated to 20 tokens)  

Optimizer: Adam

Loss Function: CrossEntropyLoss

Epochs: 6

Embedding Size: 128

Train/Test Split: 80/20

Batch Size: 64

Evaluation Metrics: Accuracy: 86.2%, Precision: 86.4%, Recall: 85.9%, F1 Score: 86.1%



# Results

All models outperform the baseline Logistic Regression model, but the RNN, despite being the simplest model compared to the LSTM and BERT, outperforms the more complex models with respect to all four evaluation metrics.  

Despite being the simplest model and taking the least amount of training time, the RNN outperformed its heavier counterparts that took longer to train. One possible explanation for this seemingly unlikely result is that we trained the RNN for twice the number of epochs. 

Nevertheless, we found this result especially interesting as it breaks the assumption that more training and more complex model architectures on the same dataset guarantee better results. 

The RNN’s high accuracy, precision, recall, and F1 scores are strong indicators on the efficacy of building a fake news and propaganda detector. These results further indicate that we can build a classification model that effectively classifies articles and headlines as either truthful or fake news, however there are practical considerations that are addressed in the ‘Future Work’ section. 



# Future Work

First, we were very surprised by the RNN outperforming BERT, which is a much more “state-of-the-art” model architecture for sequential data modelling. In the previous section, we claimed that more training and more complex model architectures do not guarantee better results. We intend to rigorously test this hypothesis further, by training models on different types of datasets. This validation process will help uncover any discrepancies or problems with our models, thus increasing the reliability of our system. 

Lastly, we want to add more datasets to our model. Even though we trained our models on a large dataset, the information that these datasets cover is still somewhat limited in scope. We hope to ultimately develop a more comprehensive disinformation and propaganda classifier that can be integrated into social media platforms. 