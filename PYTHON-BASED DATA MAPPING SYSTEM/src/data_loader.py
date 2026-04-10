import pandas as pd

class DataLoader:

    def __init__(self, train_path, ideal_path, test_path):
        self.train_path = train_path
        self.ideal_path = ideal_path
        self.test_path = test_path

    def load_train(self):
        return pd.read_csv(self.train_path)

    def load_ideal(self):
        return pd.read_csv(self.ideal_path)

    def load_test(self):
        return pd.read_csv(self.test_path)