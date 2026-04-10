import numpy as np

class FunctionSelector:

    def __init__(self, train_df, ideal_df):
        self.train = train_df
        self.ideal = ideal_df

    def select_best_functions(self):

        best_functions = {}
        max_deviations = {}

        for i in range(1,5):

            train_y = self.train[f"y{i}"]

            min_error = float("inf")
            best_func = None
            max_dev = 0

            for j in range(1,51):

                ideal_y = self.ideal[f"y{j}"]

                error = np.sum((train_y - ideal_y) ** 2)

                if error < min_error:

                    min_error = error
                    best_func = j

                    max_dev = np.max(abs(train_y - ideal_y))

            best_functions[f"y{i}"] = best_func
            max_deviations[f"y{i}"] = max_dev

        return best_functions, max_deviations