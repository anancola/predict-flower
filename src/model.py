from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB

class gaussianNb():
    def predict(data_matrix):
        # Loading Iris Dataset
        iris = load_iris()

        # Getting features and targets from the dataset
        X = iris.data
        Y = iris.target

        # Fitting our Model on the dataset
        clf = GaussianNB()
        clf.fit(X,Y)
        class_idx = clf.predict(data_matrix)[0]
        target_name = iris.target_names[class_idx]
        return target_name