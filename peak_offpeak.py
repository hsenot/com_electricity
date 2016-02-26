'''
PyCon Presentation Example
'''

import pandas as pd
import numpy as np
import seaborn

import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.cross_validation import train_test_split

def cm_inch(cm):
    return float(cm) * 0.0610237441

def grm_pd(grm):
    return float(grm) * 0.00220462

def load_data(filename, incols):
    return pd.read_csv(filename, sep=r"\s*",  converters={'Head_Size': cm_inch, 'Brain_Weight': grm_pd}, names=incols)

def create_datasets(X, y, random):
    return  train_test_split(X, y, test_size=0.30, random_state=random)

def build_model(X_train, y_train):
    model = linear_model.LinearRegression()# Create regression object
    return model.fit(X_train, y_train) # Train the model

def predict_eval(model, X_test, y_test):
    # R squared / proportion of variance explained by model: 1 is perfect prediction
    print('Accuracy: %.2f' % model.score(X_test, y_test))

    # The mean square error - how much the values can fluctuate
    print('Root Mean Squared Error: %.2f' % ((np.mean((model.predict(X_test) - y_test) ** 2))**(0.5)))


def design_plot(fn):
    plt.xlabel('Head Size (in^3)', fontsize=18)
    plt.ylabel('Brain Weight (lb)', fontsize=18)
    plt.xlim(180,280)
    plt.ylim(2.4,3.8)
    plt.tick_params(labelsize=14)
    plt.savefig(fn)
    plt.show()

def scatter_plot(model, X, y, title, fn, color):
    plt.scatter(X, y,  color=color, s=30)
    plt.title(title, fontsize=24)
    design_plot(fn)
    
def scatter_split_plot(model, dataset, title, fn):
    X_train, X_test, y_train, y_test = dataset
    train = plt.scatter(X_train, y_train,  color='#fc4e2a', s=30)
    test = plt.scatter(X_test, y_test,  color='#0c2c84', s=30)
    plt.title(title, fontsize=24)
    plt.legend([train,test],['Train Data', 'Test Data'], fontsize=16, loc='lower right')
    design_plot(fn)

def model_plot(model, X, y, title, fn, color):
    plt.scatter(X, y,  color=color, s=30)

    plt.plot(X, model.predict(X), linewidth=3)

    design_plot(fn)

def model_ex_predict(model, X, y, title, fn):
    plt.plot(X, model.predict(X), linewidth=3)

    plt.title(title, fontsize=24)


    plt.plot([240,240],[2.4,3.03], color='r')
    plt.plot([180,240],[3.03,3.03], color='r')
    design_plot(fn)

def main():
    cols = ['Gender', 'Age_Range', 'Head_Size', 'Brain_Weight']
    data = load_data('brainhead.dat', incols=cols)
    
    X, y = np.array(data['Head_Size']), np.array(data['Brain_Weight'])
    # 6 overfits
    X_train, X_test, y_train, y_test = create_datasets(X[:,np.newaxis], y, 1)

    model = build_model(X_train, y_train)
    predict_eval(model, X_test, y_test)

    scatter_plot(model, X, y, 'Brain Weight by Head Size Data', 'full_scatter_ex.png', 'black')
    
    scatter_split_plot(model, [X_train, X_test, y_train, y_test], 'Train & Test Data Split', 'split_scatter_ex.png')

    model_plot(model, X_train, y_train,'Fit Model with Training Data', 'train_model_ex.png', '#fc4e2a')

    model_plot(model, X_test, y_test, 'Evaluate Model with Test Data', 'body_brain_lr_ex.png', '#0c2c84')

    model_ex_predict(model, X_train, y_train, 'Example Brain Weight Prediction', 'body_brain_predict_ex.png')

    return model

if __name__ == '__main__':
    main()