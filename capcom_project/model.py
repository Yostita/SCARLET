import torch
import torch.nn as nn
class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_tags):
        super(NeuralNet, self).__init__()
        # Primera columna de la red nº de patrones
        self.l1 = nn.Linear(input_size, hidden_size)
        # Segunda columna de la red
        self.l2 = nn.Linear(hidden_size, hidden_size)
        # Tercera columna de la red nº de tags
        self.l3 = nn.Linear(hidden_size, num_tags)
        self.relu = nn.ReLU()

    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        # no se aplica el softmax aqui
        return out