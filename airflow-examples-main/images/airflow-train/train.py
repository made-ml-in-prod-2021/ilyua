import os
import pandas as pd
import click
from sklearn.linear_model import LinearRegression
import pickle
from sklearn.model_selection import train_test_split

@click.command("train")
@click.option("--input-dir")
@click.option("--output-dir")
def train(input_dir: str, output_dir):
    X = pd.read_csv(os.path.join(input_dir, "data.csv"))
    y = pd.read_csv(os.path.join(input_dir, "target.csv"))

    os.makedirs(output_dir, exist_ok=True)
    X_train,X_test,y_train,y_test = train_test_split(X,y)
    model=LinearRegression()
    model.fit(X_train,y_train)
    with open(os.path.join(output_dir,'my_model.pickle'),'wb') as f:
        pickle.dump(model,f)


if __name__ == '__main__':
    train()
