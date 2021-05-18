from sklearn.datasets import load_iris
import pickle
from sklearn import linear_model
iris = load_iris()

X = iris.data
y = iris.target

clf = linear_model.LogisticRegression(penalty='l1', solver='liblinear',
                                      tol=1e-6, max_iter=int(1e6),
                                      warm_start=True)
clf.fit(X, y)

with open('model.pkl','wb') as f:
    pickle.dump(clf,f)
