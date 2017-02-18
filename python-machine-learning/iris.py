
import pandas
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plot
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names = names)

# Shape of the dataset
print(dataset.shape)

# Print the first 20 rows of data
print(dataset.head(20))

# Description
print(dataset.describe())

# Group by class distribution
print(dataset.groupby('class').size())

# Box-and-whisker plots
dataset.plot(kind = 'box', subplots = True, layout = (2, 3), sharex = False, sharey = False)
plot.show()

# Histogram
dataset.hist()
plot.show()

# Scatter plot matrix
scatter_matrix(dataset)
plot.show()
