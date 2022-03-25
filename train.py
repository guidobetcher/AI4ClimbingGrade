import numpy as np

x_train = [[]]
y_train = []

def fit_model:
  file_content = np.genfromtxt(input_file, skip_header = 1)
  x_train = file_content[:,:-1]
  y_train = file_content[:, -1]
  c = np.linalg.lstsq(x_train, y_train)[0]

input_file = open('training_data.txt', 'r')
fit_model(input_file)
