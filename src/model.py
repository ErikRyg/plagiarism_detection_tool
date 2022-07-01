from pickletools import optimize
from sklearn import metrics
import tensorflow as tf
from keras.utils.vis_utils import plot_model
import constants

class Model:
    def __init__(self) -> None:
        self.model = build_first_attempt_model()


#TODO early stopping, to avoid overfitting
#TODO batch normalization
"""
    1 input layer gets 2 x 256 integers each of which is a token for a single word
    4 fullyconnected hidden layers (activation='relu')
    1 output layer outputs a value between 0 and 1 (activation='sigmoid')
"""
def build_model_from_quora_siamese():
    model = tf.keras.Sequential([
        # 1 Input layer
        # 2 * inputsize
        tf.keras.layers.Embedding(constants.VOCABULARY_SIZE, constants.EMBEDDING_DIM, constants.MAXLEN),
        tf.keras.layers.GlobalAveragePooling1D(),
        # 4 hidden layer
        tf.keras.layers.Dense(24, activation='relu'),
        # 1 output layer (wichtig sigmoid aktivierungsfunktion)
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


def build_first_attempt_model():
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(constants.MAXLEN*2, activation='relu')),
    model.add(tf.keras.layers.Dense(constants.MAXLEN*2, activation='relu')),
    model.add(tf.keras.layers.Dense(constants.MAXLEN*2, activation='relu')),
    model.add(tf.keras.layers.Dense(constants.MAXLEN*2, activation='relu')),
    # model.add(tf.keras.layers.Dense(4, activation='relu')),
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.build(input_shape=(1,256))
    plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)
    return model



if __name__ == '__main__':
    model = Model()

