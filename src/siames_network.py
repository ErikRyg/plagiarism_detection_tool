

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %matplotlib inline

import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))
stemmer = SnowballStemmer("english")

from tqdm import tqdm

import re



"""Only necessary for real text"""
def decontracted(phrase):
    # specific
    phrase = re.sub(r"won\'t", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)

    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    return phrase


def striphtml(data):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, ' ', str(data))
    return cleantext


def stripunc(data):
    return re.sub('[^A-Za-z]+', ' ', str(data), flags=re.MULTILINE|re.DOTALL)


def compute(sent):

    sent = decontracted(sent)
    sent = striphtml(sent)
    sent = stripunc(sent)

    words=word_tokenize(str(sent.lower()))

    #Removing all single letter and and stopwords from question
    sent1=' '.join(str(stemmer.stem(j)) for j in words if j not in stop_words and (len(j)!=1))
    sent2=' '.join(str(j) for j in words if j not in stop_words and (len(j)!=1))
    return sent1, sent2


def cosine_distance(vests):
    x, y = vests
    x = K.l2_normalize(x, axis=-1)
    y = K.l2_normalize(y, axis=-1)
    return -K.mean(x * y, axis=-1, keepdims=True)


def cos_dist_output_shape(shapes):
    shape1, shape2 = shapes
    return (shape1[0],1)

from sklearn.metrics import roc_auc_score

def auroc(y_true, y_pred):
    return tf.py_func(roc_auc_score, (y_true, y_pred), tf.double)

if __name__ == '__main__':
    # import nltk
    # nltk.download('punkt')
    train_data = pd.read_csv("../data/question_pairs/train.csv")
    test_data = pd.read_csv("../data/question_pairs/test.csv")
    test_data.fillna(value = " ",inplace = True)
    clean_stemmed_q1 = []
    clean_stemmed_q2 = []
    clean_q1 = []
    clean_q2 = []
    combined_stemmed_text = []
    for _, row in tqdm(train_data.iterrows()):
        csq1, cq1 = compute(row['question1'])
        csq2, cq2 = compute(row['question2'])
        clean_stemmed_q1.append(csq1)
        clean_q1.append(cq1)
        clean_stemmed_q2.append(csq2)
        clean_q2.append(cq2)
        combined_stemmed_text.append(csq1+" "+csq2)

    clean_stemmed_q1_t = []
    clean_stemmed_q2_t = []
    clean_q1_t = []
    clean_q2_t = []
    combined_stemmed_text_t = []
    for _, row in tqdm(test_data.iterrows()):

        csq1_t, cq1_t = compute(row['question1'])
        csq2_t, cq2_t = compute(row['question2'])
        clean_stemmed_q1_t.append(csq1_t)
        clean_q1_t.append(cq1_t)
        clean_stemmed_q2_t.append(csq2_t)
        clean_q2_t.append(cq2_t)
        combined_stemmed_text_t.append(csq1_t+" "+csq2_t)

    train_data['clean_stemmed_q1'] = clean_stemmed_q1
    train_data['clean_stemmed_q2'] = clean_stemmed_q2
    train_data['clean_q1'] = clean_q1
    train_data['clean_q2'] = clean_q2
    train_data['combined_stemmed_text'] = combined_stemmed_text

    test_data['clean_stemmed_q1_t'] = clean_stemmed_q1_t
    test_data['clean_stemmed_q2_t'] = clean_stemmed_q2_t
    test_data['clean_q1_t'] = clean_q1_t
    test_data['clean_q2_t'] = clean_q2_t
    test_data['combined_stemmed_text_t'] = combined_stemmed_text_t


    from google.colab import drive
    drive.mount('/content/drive')
    data= pd.read_csv("drive/My Drive/data.csv")

    from sklearn.model_selection import train_test_split
    X_temp, X_test, y_temp, y_test = train_test_split(data[['clean_q1', 'clean_q2']], data['is_duplicate'], test_size=0.2, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.2, random_state=42)

    X_train['text'] = X_train[['clean_q1','clean_q2']].apply(lambda x:str(x[0])+" "+str(x[1]), axis=1)


    import tensorflow as tf
    import keras
    import keras.backend as K
    from keras.preprocessing.text import Tokenizer
    from keras.preprocessing.sequence import pad_sequences

    from keras.layers import Input, Concatenate, Conv2D, Flatten, Dense, Embedding, LSTM
    from keras.models import Model

    t = Tokenizer()
    t.fit_on_texts(X_train['text'].values)

    X_train['clean_q1'] = X_train['clean_q1'].astype(str)
    X_train['clean_q2'] = X_train['clean_q2'].astype(str)

    X_val['clean_q1'] = X_val['clean_q1'].astype(str)
    X_val['clean_q2'] = X_val['clean_q2'].astype(str)

    X_test['clean_q1'] = X_test['clean_q1'].astype(str)
    X_test['clean_q2'] = X_test['clean_q2'].astype(str)

    train_q1_seq = t.texts_to_sequences(X_train['clean_q1'].values)

    train_q2_seq = t.texts_to_sequences(X_train['clean_q2'].values)
    val_q1_seq = t.texts_to_sequences(X_val['clean_q1'].values)
    val_q2_seq = t.texts_to_sequences(X_val['clean_q2'].values)
    test_q1_seq = t.texts_to_sequences(X_test['clean_q1'].values)
    test_q2_seq = t.texts_to_sequences(X_test['clean_q2'].values)

    len_vec = [len(sent_vec) for sent_vec in train_q1_seq]
    sns.distplot(len_vec)
    len_vec = [len(sent_vec) for sent_vec in train_q2_seq]

    sns.distplot(len_vec)

    max_len = 30
    train_q1_seq = pad_sequences(train_q1_seq, maxlen=max_len, padding='post')
    train_q2_seq = pad_sequences(train_q2_seq, maxlen=max_len, padding='post')

    val_q1_seq = pad_sequences(val_q1_seq, maxlen=max_len, padding='post')
    val_q2_seq = pad_sequences(val_q2_seq, maxlen=max_len, padding='post')
    test_q1_seq = pad_sequences(test_q1_seq, maxlen=max_len, padding='post')
    test_q2_seq = pad_sequences(test_q2_seq, maxlen=max_len, padding='post')

    import joblib
    embeddings_index = {}
    f = open('drive/My Drive/movie_plot/glove.6B.300d.txt')
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        embeddings_index[word] = coefs
    f.close()

    print('Found %s word vectors.' % len(embeddings_index))

    not_present_list = []
    vocab_size = len(t.word_index) + 1
    print('Loaded %s word vectors.' % len(embeddings_index))
    embedding_matrix = np.zeros((vocab_size, len(embeddings_index['no'])))
    for word, i in t.word_index.items():
        if word in embeddings_index.keys():
            embedding_vector = embeddings_index.get(word)
        else:
            not_present_list.append(word)
        if embedding_vector is not None:
            embedding_matrix[i] = embedding_vector
        else:
            embedding_matrix[i] = np.zeros(300)

    from keras.regularizers import l2
    from keras.models import Sequential
    from keras.optimizers import Adam
    from keras.layers import Conv2D, ZeroPadding2D, Activation, Input, concatenate
    from keras.models import Model

    from keras.layers.normalization import BatchNormalization
    from keras.layers.pooling import MaxPooling2D
    from keras.layers.merge import Concatenate
    from keras.layers.core import Lambda, Flatten, Dense
    from keras.initializers import glorot_uniform
    from keras.layers import Input, Dense, Flatten, GlobalMaxPool2D, GlobalAvgPool2D, Concatenate, Multiply, Dropout, Subtract, Add, Conv2D

    from keras import backend as K

    input_1 = Input(shape=(train_q1_seq.shape[1],))
    input_2 = Input(shape=(train_q2_seq.shape[1],))


    common_embed = Embedding(name="synopsis_embedd",input_dim =len(t.word_index)+1,
                        output_dim=len(embeddings_index['no']),weights=[embedding_matrix],
                        input_length=train_q1_seq.shape[1],trainable=False)
    lstm_1 = common_embed(input_1)
    lstm_2 = common_embed(input_2)


    common_lstm = LSTM(64,return_sequences=True, activation="relu")
    vector_1 = common_lstm(lstm_1)
    vector_1 = Flatten()(vector_1)

    vector_2 = common_lstm(lstm_2)
    vector_2 = Flatten()(vector_2)

    x3 = Subtract()([vector_1, vector_2])
    x3 = Multiply()([x3, x3])

    x1_ = Multiply()([vector_1, vector_1])
    x2_ = Multiply()([vector_2, vector_2])
    x4 = Subtract()([x1_, x2_])

        #https://stackoverflow.com/a/51003359/10650182
    x5 = Lambda(cosine_distance, output_shape=cos_dist_output_shape)([vector_1, vector_2])

    conc = Concatenate(axis=-1)([x5,x4, x3])

    x = Dense(100, activation="relu", name='conc_layer')(conc)
    x = Dropout(0.01)(x)
    out = Dense(1, activation="sigmoid", name = 'out')(x)

    model = Model([input_1, input_2], out)

    model.compile(loss="binary_crossentropy", metrics=['acc',auroc], optimizer=Adam(0.00001))
    model.summary()
    model.fit([train_q1_seq,train_q2_seq],y_train.values.reshape(-1,1), epochs = 5,
          batch_size=64,validation_data=([val_q1_seq, val_q2_seq],y_val.values.reshape(-1,1)))

    model.save('../data/model/siames_network_model')

