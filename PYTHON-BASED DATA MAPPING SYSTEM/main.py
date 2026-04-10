from src.data_loader import DataLoader
from src.database import Database
from src.function_selector import FunctionSelector
from src.mapper import Mapper
from src.visualization import Visualizer


loader = DataLoader(
    "data/train.csv",
    "data/ideal.csv",
    "data/test.csv"
)

train = loader.load_train()
ideal = loader.load_ideal()
test = loader.load_test()

db = Database()

db.save_table(train, "training_data")
db.save_table(ideal, "ideal_functions")


selector = FunctionSelector(train, ideal)

best_funcs, max_devs = selector.select_best_functions()

print("Best Functions:", best_funcs)


mapper = Mapper(test, ideal, best_funcs, max_devs)

results = mapper.map_points()

db.save_table(results, "test_results")

print(results.head())


viz = Visualizer()
viz.plot(train, ideal, results)