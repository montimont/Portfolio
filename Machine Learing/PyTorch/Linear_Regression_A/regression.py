import torch
from torch import nn
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

device ='cuda' if torch.cuda.is_available() else 'cpu'

placement = pd.read_csv('placement.csv')

weight = 0.8
bias = 0.3

X = placement['placement_exam_marks']
y = placement['cgpa']

y = weight * X + bias

train_split = int((0.8)*len(X))
X_train, y_train = X[:train_split], y[:train_split]
X_test, y_test = X[train_split:], y[train_split:]
len(X_train), len(y_train), len(X_test), len(y_test)

def plot_predictions(train_data=X_train, train_labels=y_train,test_data=X_test,test_labels=y_test,predictions=None):
  plt.figure(figsize=(10,7))

  plt.scatter(train_data, train_labels, c="b", s=4, label="Training Data" )

  plt.scatter(train_data, train_labels, c="g", s=4, label="Testing Data" )

  if predictions is not None:
    plt.scatter(test_data,predictions, c="r", s=4, label="Predictions" )

  plt.legend(prop={"size":14})

plot_predictions(X_train, y_train, X_test, y_test)

class LinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        # Use nn.Linear() for creating the model parameters
        self.linear_layer = nn.Linear(in_features=1, 
                                      out_features=1)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.linear_layer(x)

model = LinearRegressionModel()
model,model.state_dict()

loss_fn = nn.L1Loss()
optimizer = torch.optim.SGD(params=model.parameters(),
                            lr=0.01)

epochs = 1000
for epoch in range(epochs):
  y_pred = model(X_train_tensor)

  loss = loss_fn(y_pred, y_train_tensor)

  optimizer.zero_grad()

  loss.backward()

  optimizer.step()

  if epoch % 100 == 0:
    print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch, num_epochs, loss.item()))
    
X_test_tensor = torch.tensor([[90], [85], [75]], dtype=torch.float32)
with torch.inference_mode():
  test_pred = model(X_test_tensor)
  test_loss = loss_fn(test_pred, torch.tensor([[9.1], [8.7], [8.0]], dtype=torch.float32))
print('Test Loss: {:.4f}'.format(test_loss.item()))

from pprint import pprint
print("The model learned the following values for weights and bias:")
pprint(model.state_dict())
print("\nAnd the original values for weights and bias are:")
print(f"weights: {weight}, bias: {bias}")


model.eval()

with torch.inference_mode():
    y_preds = model(X_test)
y_preds


plot_predictions(predictions=y_preds.cpu())

