

class QuadraticTransformer():
    def __init__(self):
        pass
    def func(self,x):
        return x**2

    def transform(self, input_df, **transform_params):
        return self.func(input_df)

    def fit(self, X, y=None, **fit_params):
        return self
