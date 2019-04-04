"""
Activation function
"""
import math


def linear(value):
    """
    Identity function
    """
    return 0.3 * value


def step_function(value):
    """
    Step function
    """
    if value >= 1:
        return 1
    return 0


def sigmoid(value):
    """
    Implementation of sigmoid function
    """
    if value < 0:
        return 1 - 1/(1 + math.exp(value))
    else:
        return 1/(1 + math.exp(-value))


def sigmoid_derivative(value):
    """
    Returns value of the derivative of the sigmoid function
    """
    return value * (1 - value)


def hyperbolic_tangent(value):
    """
    Return the hyperbolic tangent of x
    """
    return math.tanh(value)


def hyperbolic_tangent_derivative(value):
    """
    Returns derivative value of the hyberbolic tangent
    """
    return 1.0 - math.tanh(value) ** 2


def ReLU(value):
    """
    Rectified linear unit
    """
    return value * (value > 0)


def PReLU(value):
    """
    Parametric rectifier
    """
    if value < 0:
        return 0.2 * value
    else:
        return value


def softmax(value, vector):
    """Compute softmax values for each sets of scores in x."""
    e_x = math.exp(value)
    return e_x / sum(map(lambda x: math.exp(x), vector))
