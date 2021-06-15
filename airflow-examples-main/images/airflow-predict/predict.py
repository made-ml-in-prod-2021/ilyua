import os
import pandas as pd
import pickle
import click

from airflow.models import Variable
# my_var = Variable.set("my_key", "my_value")

@click.command("predict")
@click.option("--input-dir")
@click.option("--output-dir")
def predict(input_dir: str, output_dir):
    X = pd.read_csv(os.path.join(input_dir, "data.csv"))
    with open(Variable.get("model_name"),'rb') as f:
        model = pickle.load(f)
    os.makedirs(output_dir, exist_ok=True)
    predictions = model.predict(X)
    predictions.to_csv(output_dir)







if __name__ == '__main__':
    predict()
