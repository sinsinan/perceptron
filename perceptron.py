import numpy as np
from typing import List
from .validations import _is_greater_than_zero_with_error, _validate_int_with_error


class Perceptron:
    _hidden_layer_sizes: List[int] = []
    _input_size: int = 0
    _output_size: int = 0

    def __init__(self, input_size: int, output_size: int):
        _is_greater_than_zero_with_error(input_size)
        _is_greater_than_zero_with_error(output_size)
        _validate_int_with_error(input_size, "input_size should be of size int")
        _validate_int_with_error(output_size, "output_size should be of size int")
        self._input_size = input_size
        self._output_size = output_size

    def add_hidden_layer(self, size: int):
        _is_greater_than_zero_with_error(size)
        _validate_int_with_error(size, "Expected size of hidden layer to be of type int")
        self._hidden_layer_sizes.append(size)

    def view_model(self):
        print("\n**********Model**********")
        print("Input: " + str(self._input_size))
        for i in range(len(self._hidden_layer_sizes)):
            print(
                "Hidden layer " + str(i + 1) + ": " + str(self._hidden_layer_sizes[i])
            )
        print("Output: " + str(self._output_size))
        print("*************************\n")

    def _build_model(self):
        weight_matrix_array = []
        for hidden_layer_size in self._hidden_layer_sizes:
            weight_matrix_array.append(np.random.rand(hidden_layer_size + 1))
        weight_matrix_array.append(np.random.rand(self._output_size + 1))
        self._weight_matrix_array = np.array(weight_matrix_array, dtype=object)

    def train(self, training_input, training_output, validation_input, validation_output):
        if len(training_input) != len(training_output):
            raise Exception("Training input and training output should be of same length")
        for i in range(len(training_input)):
            if len(training_input[i]) != self._input_size:
                raise Exception("Training input should be of same length as input layer")
        if len(validation_input) != len(validation_output):
            raise Exception("Validation input and validation output should be of same length")
        for i in range(len(validation_input)):
            if len(validation_input[i]) != self._input_size:
                raise Exception("Validation input should be of same length as input layer")
        

if __name__ == "__main__":
    p = Perceptron(input_size=2, output_size=1)
    p.add_hidden_layer(size=6)
    p.add_hidden_layer(size=4)
    p.add_hidden_layer(size=4)
    p.view_model()
    p._build_model()
    print(p._weight_matrix_array)
