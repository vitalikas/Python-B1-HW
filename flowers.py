flowers = {
    "iris_setosa": {
        "sepal_length": [3.6, 4.9, 4.8, 4.7],
        "sepal_width": [2.9, 3.3, 3.2, 3.1],
        "petal_length": [1.3, 1.2, 1.5, 1.4],
    },
    "iris_virginica": {
        "sepal_length": [7.2, 7.0, 7.9],
         "sepal_width": [3.1, 2.7, 2.8],
        "petal_length": [5.5, 5.5, 6.5],
    },
    "iris_versicolor": {
        "sepal_length": [6.5, 6.0, 6.1, 6.2, 6.3],
         "sepal_width": [2.8, 2.9, 2.4, 2.7, 2.7],
        "petal_length": [4.8, 4.7, 5.0, 4.9, 4.8],
    },
}


measure_sum = 0
measure_count = 0
for flower, measure_param in flowers.items():
    for measure in measure_param['sepal_length']:
        measure_sum += measure
        measure_count += 1
mean = measure_sum / measure_count
print(f"Sepal length's measure sum is: {measure_sum}")
print(f"Sepal length's measure count is: {measure_count}")
print(f"Sepal length's mean value is: {round(mean, 2)}")

# или

sum_ = 0
count = 0
for flower in flowers:
   sum_ += sum(flowers[flower]['sepal_length'])
   count += len(flowers[flower]['sepal_length'])
mean = sum_ / count
print(f"Sepal length's measure sum is: {sum_}.\nSepal length's measure count is: {count}.\nSepal length's mean value is: {round(mean, 2)}")