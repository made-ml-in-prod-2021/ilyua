import os
import pandas as pd
import click


@click.command("predict")
@click.option("--input-dir")
@click.option("--output-dir")
def preprocess(input_dir: str, output_dir):
    X = pd.read_csv(os.path.join(input_dir, "data.csv"))

    y = pd.read_csv(os.path.join(input_dir, "target.csv"))
    # do something instead
    X=X**2

    os.makedirs(output_dir, exist_ok=True)
    X.to_csv(os.path.join(output_dir, "data.csv"))
    y.to_csv(os.path.join(output_dir, "target.csv"))


if __name__ == '__main__':
    preprocess()
