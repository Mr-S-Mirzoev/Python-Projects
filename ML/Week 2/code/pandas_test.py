import pandas as pd
from scipy.spatial.distance import cdist
import numpy

d = {'col1': [1, 2], 'col2': [3, None]}
df = pd.DataFrame(data=d)
print(df)
df.fillna('', inplace=True)
print(df.info())

a = numpy.array([6, 3, -5])
b = numpy.array([-1, 0, 7])

print(cdist(a[:, numpy.newaxis], b[:, numpy.newaxis], metric='euclidean'))
print(numpy.linalg.norm(a, ord=2) - numpy.linalg.norm(b, ord=2))

print(a[:, numpy.newaxis])