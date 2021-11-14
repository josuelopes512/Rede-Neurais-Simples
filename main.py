def backprop(self, x, y):
    nabla_b (np.zeros(b.shape) for b in self.biases]
nabla_w = [np.zeros(w.shape) for w in self.weights]
# Feedforward
activation = x
# Lista para armazenar todas as ativações, camada por camada
activations = [x]
# Lista para armazenar todos os vetores z, camada por camada
ZS = []
for b, w in zip(self.biases, self.weights):
z = np. dot(w, activation)+b
zs.append(z)
activation = sigmoid(z)
activations.append(activation)
# Backward pass
delta = self.cost_derivative(activations [-1], y) * sigmoid_prime(zs [-1])
nabla_b[-1] = delta
nabla_w[-1] = np.dot(delta, activations [-2].transpose()).
for l in range(2, self.num_layers):
z = zs[-1]
sp sigmoid_prime(z)
delta np.dot (self.weights[-2+1].transpose(), delta) * sp
nabla_b[-2] = delta
nabla_w[-1] = np.dot(delta, activations [-1-1].transpose())
return (nabla_b, nabla_w)