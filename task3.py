import ArrayAggregation
import MatrixAggregation


print("Input array")
raw = input()
array = list(map(int, raw.split(' ')))
sample = ArrayAggregation(array)

print(f"Sum: Expected: {sum(array)}, Result: {sample.sum()}")
print(f"Product: Result: {sample.product()}")
print(f"Average: Result: {sample.average()}")
print(f"Max: Expected: {max(array)}, Result: {sample.max()}")
print(f"Min: Expected: {min(array)}, Result: {sample.min()}")

print("----------------------------------------------")

print("Input matrix length")
length = int(input())
matrix = []

for i in range(1, length):
    raw = input()
    array = list(map(int, raw.split(' ')))
    matrix.append(array)

matrix_sample = MatrixAggregation(matrix)
print(f"Sum: Result: {matrix_sample.sum()}")
print(f"Product: Result: {matrix_sample.product()}")
print(f"Average: Result: {matrix_sample.average()}")
print(f"Max: Result: {matrix_sample.max()}")
print(f"Min: Result: {matrix_sample.min()}")
