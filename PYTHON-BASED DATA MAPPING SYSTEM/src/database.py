from sqlalchemy import create_engine

class Database:

    def __init__(self, db_name="assignment.db"):
        self.engine = create_engine(f"sqlite:///{db_name}")

    def save_table(self, dataframe, table_name):
        dataframe.to_sql(table_name, self.engine, if_exists='replace', index=False)