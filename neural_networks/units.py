"""
Contains structural units of networks: neuron and input neuron
"""


class Neuron:
    """
    Basic structural unit of networks
    """

    def __init__(self, weights, bias=0):
        self.weights = list(weights)
        self.bias_w = bias
        self.value = 0

    def calculate(self, inputs, activation_function, bias):
        """
        Calculates its value
        """
        if len(inputs) != len(self.weights):
            raise ValueError('Different number of inputs and weights')
        neuron_base_value = 0
        for i, value in enumerate(inputs):
            neuron_base_value += value * self.weights[i]
        self.value = activation_function(
            neuron_base_value + bias * self.bias_w)

    def get_weights(self):
        """
        Returns weights
        """
        return self.weights

    def get_value(self):
        """
        Returns neuron value
        """
        return self.value

    def get_bias_w(self):
        """
        Returns neuron value
        """
        return self.bias_w

    def update_weights(self, corrections):
        """
        Adds each weights_sum to each weight
        """
        for i, value in enumerate(corrections):
            self.weights[i] += value


class InputNeuron(Neuron):
    """
    Input neuron
    """

    def __init__(self, value):
        super(InputNeuron, self).__init__([])
        self.value = value

    def set_value(self, value):
        """
        Sets value
        """
        self.value = value
