import numpy as np
import pandas as pd
from src.exceptions import MappingError

class Mapper:

    def __init__(self, test_df, ideal_df, best_funcs, max_devs):

        self.test = test_df
        self.ideal = ideal_df
        self.best_funcs = best_funcs
        self.max_devs = max_devs

    def map_points(self):

        results = []

        for _, row in self.test.iterrows():

            x = row["x"]
            y = row["y"]

            for train_func, ideal_index in self.best_funcs.items():

                ideal_y = self.ideal.loc[self.ideal["x"] == x, f"y{ideal_index}"]

                if len(ideal_y) == 0:
                    continue

                ideal_y = ideal_y.values[0]

                deviation = abs(y - ideal_y)

                if deviation <= self.max_devs[train_func] * np.sqrt(2):

                    results.append({
                        "x": x,
                        "y": y,
                        "delta_y": deviation,
                        "ideal_function": ideal_index
                    })

        return pd.DataFrame(results)