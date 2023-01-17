import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import tensorflow as tf
from tensorflow import keras

from sklearn.model_selection import train_test_split

from scipy.stats import reciprocal
from sklearn.model_selection import RandomizedSearchCV

from sklearn.preprocessing import MinMaxScaler

from numpy import mean
from numpy import std

import sklearn.model_selection as model_selection
from sklearn.metrics import accuracy_score

from geneticalgorithm import geneticalgorithm as ga
import matplotlib
matplotlib.use('Agg')

def build_model(n_hidden=6, n_neurons=111, learning_rate=0.0513, input_shape=[12], act_function="tanh"):
    model = keras.models.Sequential()
    initializer = tf.keras.initializers.he_normal()
    model.add(keras.layers.InputLayer(input_shape=input_shape))
    for layer in range(n_hidden):
        model.add(keras.layers.Dense(n_neurons, activation=act_function,kernel_initializer=initializer))
    model.add(keras.layers.Dense(7, activation="softmax",kernel_initializer=initializer))
    optimizer = keras.optimizers.SGD(lr=learning_rate)
    model.compile(loss="sparse_categorical_crossentropy", optimizer=optimizer, metrics=["accuracy"])
    return model


def fitfunc(k):
    if k[2]==1:
        act="relu"
    if k[2]==2:
        act="tanh"
    if k[2]==3:
        act="sigmoid"
    if k[3]==0:
        lr=1e-2
    if k[3]==1:
        lr=1e-3
    if k[3]==2:
        lr=1e-4
    if k[3]==3:
        lr=1e-5
    if k[3]==4:
        lr=1e-6
    if k[3]==5:
        lr=1e-7
    if k[3]==6:
        lr=1e-8
    fitness = 0
    for i in range(1, 11): # to jest 21 kroków czasowych
        X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, train_size=0.80, test_size=0.20, random_state=21)
        model = build_model(int(k[0]),k[1],lr,[12],act)
        model.fit(X_train, y_train, epochs=200,validation_split=0.2,callbacks=[keras.callbacks.EarlyStopping(patience=30)])
        check = model.evaluate(X_test, y_test)
        print(check)
        #y_pred = model.predict(X_test)
        #accuracy = accuracy_score(y_test, y_pred)
        #print(accuracy)
        fitness = fitness+1-check[1]
        keras.backend.clear_session()
    fitness=fitness/10
    return fitness

df = pd.read_csv('DANE.csv')

#df = df.sample(frac=1).reset_index(drop=True)
df = df.drop(df[df.WAR == 0].index)

df = df.sample(frac=1).reset_index(drop=True)

#target = df.pop('stabilnosc')

target = df.pop('stabilnosc')
war = df.pop('WAR')

X = df.values
X = np.nan_to_num(X) 
y = target.values

plik = open("zapis_MLP_A.txt","w+")
plik.write("numer solution fitness\n")


varbound=np.array([[0,10],[1, 50],[1, 3],[0, 6]])


model=ga(function=fitfunc,dimension=4,variable_type='int',variable_boundaries=varbound)
model.run()
solution=model.output_dict
plik.write("1")
plik.write(" ")
plik.write(str(solution['variable']))
plik.write(" ")
plik.write(str(solution['function']))
plik.write("\n")
plt.savefig('convergence_MLP_A.png')
plt.close()

plik.close()
