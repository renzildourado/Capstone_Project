import pandas as pd
import scipy
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from sklearn.neural_network import MLPClassifier
from sklearn.feature_selection import RFE



def open_file():
    file_name = "cleaned_dataset_3.csv"
    data_frame = pd.read_csv(file_name, low_memory=False)
    return data_frame


def build_decision_tree(data_frame):
    X = data_frame.drop(["MALWARE_DETECTION"], axis=1)
    Y = data_frame['MALWARE_DETECTION']
    train_data_x, test_data_x, train_data_y, test_data_y = train_test_split(X, Y, test_size=0.30)


##############################################################################################################

    # neural_network = MLPClassifier()
    # neural_network = neural_network.fit(train_data_x, train_data_y)
    #
    # predicted_y = neural_network.predict(test_data_x)
    #
    # print("FOR Neural Network")
    # acc = accuracy_score(predicted_y.round(), test_data_y)
    # print("ACCURACY: " + str(acc))
    # print("CONFUSION MATRIX")
    # print(confusion_matrix(test_data_y, predicted_y.round()))

##############################################################################################################

    # linear_regression = LinearRegression()
    # linear_regression = linear_regression.fit(train_data_x, train_data_y)
    #
    # predicted_y = linear_regression.predict(test_data_x)
    #
    # print("FOR Linear Regression")
    # acc = accuracy_score(predicted_y.round(), test_data_y)
    # print("ACCURACY: " + str(acc))
    # print("CONFUSION MATRIX")
    # print(confusion_matrix(test_data_y, predicted_y.round()))

##############################################################################################################

    # naive_bayes = GaussianNB()
    # naive_bayes = naive_bayes.fit(train_data_x, train_data_y)
    #
    # predicted_y = naive_bayes.predict(test_data_x)
    #
    # print("FOR Naive Bayes Classifier")
    # acc = accuracy_score(predicted_y, test_data_y)
    # print("ACCURACY: " + str(acc))
    # print("CONFUSION MATRIX")
    # print(confusion_matrix(test_data_y, predicted_y))

##############################################################################################################

    # knn_classifier = KNeighborsClassifier()
    # knn_classifier = knn_classifier.fit(train_data_x, train_data_y)
    #
    # predicted_y = knn_classifier.predict(test_data_x)
    #
    # print("FOR K NEAREST NEIGHBORS")
    # acc = accuracy_score(predicted_y, test_data_y )
    # print("ACCURACY: "+str(acc))
    # print("CONFUSION MATRIX")
    # print(confusion_matrix(test_data_y, predicted_y))

##############################################################################################################

    # random_forest = RandomForestClassifier()
    # random_forest = random_forest.fit(train_data_x, train_data_y)
    #
    # predicted_y = random_forest.predict(test_data_x)
    #
    # print("FOR RANDOM FOREST")
    # acc = accuracy_score(predicted_y, test_data_y )
    # print("ACCURACY: "+str(acc))
    # print("CONFUSION MATRIX")
    # print(confusion_matrix(test_data_y, predicted_y))

###############################################################################################################

    # decision_tree = tree.DecisionTreeClassifier()
    # decision_tree = decision_tree.fit(train_data_x, train_data_y)
    #
    # predicted_y = decision_tree.predict(test_data_x)
    #
    # print("FOR DECISION TREE")
    # acc = accuracy_score(predicted_y, test_data_y)
    # print("ACCURACY: " + str(acc))
    # print("CONFUSION MATRIX")
    # print(confusion_matrix(test_data_y, predicted_y))

##################################################################################################################

    # test_sample = list(train_data_frame.iloc[807])
    # test_sample = [int(num) for num in test_sample]
    # # print(test_sample)
    # print(decision_tree.predict([test_sample]))


def main():
    data_frame = open_file()
    build_decision_tree(data_frame)

if __name__ == '__main__':
    main()
