import numpy as np
#from helper import plot_confusion_matrix


y_true = [1,1,1,1,0,2,0,3,4,2,1,2,2,1,2,1,0,1,1,0]
y_predicted = [1,0,1,1,0,2,1,3,4,2,2,0,2,1,2,1,0,3,1,1]

def confusion_matrix_masterclass(true, pred):
  '''Computes a confusion matrix using numpy for two np.arrays
  true and pred.

  Results are identical (and similar in computation time) to: 
    "from sklearn.metrics import confusion_matrix"

  However, this function avoids the dependency on sklearn.'''

  K = len(np.unique(true)) # Number of classes 
  result = np.zeros((K, K))

  for i in range(len(true)):
    result[true[i]][pred[i]] += 1

  return result


result_matrix= confusion_matrix_masterclass(y_true, y_predicted)
print(result_matrix)
plot_confusion_matrix(result_matrix)
plt.show()
