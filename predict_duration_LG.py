import numpy as np
from io import StringIO

def fit_model(input_file):
  file_content = np.genfromtxt(StringIO(input_file.read()), skip_header = 1)
  x_train = file_content[:,:-1]
  y_train = file_content[:, -1]
  coeff = np.linalg.lstsq(x_train, y_train, rcond=None)[0]
  return coeff

def predict(x_test, coeff):
  return x_test @ coeff

def main():
  train_file = open('training_data.txt', 'r')
  test_file = open('testing_data.txt', 'r')
  c = fit_model(train_file)
  print("\nActual coefficient values:\t[%s]" % (' '.join('%s' % str(i) for i in c)))
  test_data = np.genfromtxt(StringIO(test_file.read()), skip_header = 1)
  x_test = test_data[:,:-1]
  y_test = test_data[:, -1]
  y_pred = predict(x_test, c)
  print ('The predicted values are:\t[%s]' % (' '.join('%03s' % round(i) for i in y_pred)))
  print ('The real values are:\t\t[%s]\n' % (' '.join('%03s' % round(i) for i in y_test)))

main()
