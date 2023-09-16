import tensorflow
import inspect
lst=inspect.getmembers(tensorflow.keras.Model)
for elem in lst:
    print(elem)