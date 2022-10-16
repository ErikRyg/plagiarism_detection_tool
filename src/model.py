from sklearn.metrics import roc_auc_score
from keras import backend as K
from pickletools import optimize
from sklearn import metrics
import tensorflow as tf
from keras.utils.vis_utils import plot_model
from keras.layers import Input, Concatenate, Conv2D, Flatten, Dense, Embedding, LSTM, Dropout
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

import constants


class Model:
    def __init__(self) -> None:
        self.model = build_first_attempt_model()


# TODO early stopping, to avoid overfitting
# TODO batch normalization
"""
    1 input layer gets 2 x 256 integers each of which is a token for a single word
    4 fullyconnected hidden layers (activation='relu')
    1 output layer outputs a value between 0 and 1 (activation='sigmoid')
"""


def build_model_from_quora_siamese():
    model = tf.keras.Sequential([
        # 1 Input layer
        # 2 * inputsize
        tf.keras.layers.Embedding(
            constants.VOCABULARY_SIZE, constants.EMBEDDING_DIM, constants.MAXLEN),
        tf.keras.layers.GlobalAveragePooling1D(),
        # 4 hidden layer
        tf.keras.layers.Dense(24, activation='relu'),
        # 1 output layer (wichtig sigmoid aktivierungsfunktion)
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(loss='binary_crossentropy',
                  optimizer='adam', metrics=['accuracy'])
    return model


def build_first_attempt_model():
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(constants.MAXLEN*2, activation='relu')),
    model.add(tf.keras.layers.Dense(constants.MAXLEN*2, activation='relu')),
    model.add(tf.keras.layers.Dense(constants.MAXLEN*2, activation='relu')),
    model.add(tf.keras.layers.Dense(constants.MAXLEN*2, activation='relu')),
    # model.add(tf.keras.layers.Dense(4, activation='relu')),
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy',
                  optimizer='adam', metrics=['accuracy'])
    model.build(input_shape=(1, 256))
    plot_model(model, to_file='model_plot.png',
               show_shapes=True, show_layer_names=True)
    return model

# https://medium.com/@prabhnoor0212/siamese-network-keras-31a3a8f37d04


def cosine_distance(vests):
    x, y = vests
    x = K.l2_normalize(x, axis=-1)
    y = K.l2_normalize(y, axis=-1)
    return -K.mean(x * y, axis=-1, keepdims=True)


def cos_dist_output_shape(shapes):
    shape1, shape2 = shapes
    return (shape1[0], 1)


def auroc(y_true, y_pred):
    return tf.py_func(roc_auc_score, (y_true, y_pred), tf.double)


def build_siamese_network_for_text_similarity(shape):
    # tokenizer =
    input_1 = Input(shape=shape)
    input_2 = Input(shape=shape)
    embedding = Embedding(name="synopsis_embedd", input_dim=len(
        tokenizer.word_index)+1,
        output_dim=len(embeddings_index['no']),
        weights=[embedding_matrix],
        input_length=shape,
        trainable=False)
    lstm_1 = embedding(input_1)
    lstm_2 = embedding(input_2)

    common_lstm = LSTM(64, return_sequences=True, activation='relu')
    vector_1 = common_lstm(lstm_1)
    vector_1 = Flatten()(vector_1)
    vector_2 = common_lstm(lstm_2)
    vector_2 = Flatten()(vector_2)

    x3 = Subtract()([vector_1, vector_2])
    x3 = Multiply()([x3, x3])

    x1_ = Multiply()([vector_1, vector_1])
    x2_ = Multiply()([vector_2, vector_2])
    x4 = Subtract()([x1_, x2_])

    # https://stackoverflow.com/a/51003359/10650182
    x5 = Lambda(cosine_distance, output_shape=cos_dist_output_shape)(
        [vector_1, vector_2])

    conc = Concatenate(axis=-1)([x5, x4, x3])

    x = Dense(100, activation="relu", name='conc_layer')(conc)
    x = Dropout(0.01)(x)
    out = Dense(1, activation="sigmoid", name='out')(x)

    model = Model([input_1, input_2], out)

    model.compile(loss="binary_crossentropy", metrics=[
                  'acc', auroc], optimizer=Adam(0.00001))

    return model


# def build_infinitemonkey_baseline():
    # n grams
    # tf-idf weighting
    # cosine simularity
    # grid search


# def build_infinitemonkey_model():
    # 2x encoder
    # embedding (32)
    # BatchNorm
    # LSTM(128)
    # 2x comparison module
    # Concat the output of the two encoders as input
    # BatchNorm
    # Dense (128)
    # ReLu
    # 1x network
    # Sum the output of the two comparison moduels as input
    # BatchNorm
    # Dense (128)
    # ReLu
    # BatchNorm
    # Dense(1)
    # Sigmoid

    # model = tf.keras.Sequential()
    # model.add(tf.keras.layers.Dense(constants.MAXLEN*2, activation='relu')),
    # model.add(tf.keras.layers.Dense(constants.MAXLEN*2, activation='relu')),
    # model.add(tf.keras.layers.Dense(constants.MAXLEN*2, activation='relu')),
    # model.add(tf.keras.layers.Dense(constants.MAXLEN*2, activation='relu')),
    # # model.add(tf.keras.layers.Dense(4, activation='relu')),
    # model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
    # model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # model.build(input_shape=(1,256))
    # plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)
    # return NULL


def write_summary_to_file(file='model_summary.txt'):
    with open(file, mode='a') as file:
        model.summary(print_fn=lambda x: file.write(x + '\n'))


def plot_model_structure(self, to_file='model_plot.png'):
    from keras.utils.vis_utils import plot_model
    plot_model(self.model, to_file=to_file,
               show_shapes=True, show_layer_names=True)


if __name__ == '__main__':
    model = Model()
