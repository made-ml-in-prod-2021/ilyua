from typing import Tuple, NoReturn


from sklearn.model_selection import train_test_split

from enities import SplittingParams
import os
import logging
from pathlib import Path

import pandas as pd
from sklearn.datasets import load_wine

DATA_SAVE_PATH=os.path.join(Path(__file__).parents[2],'data')

def read_data(path) -> pd.DataFrame:
    df = load_wine()
    X = df['data']
    y = df['target']
    X = pd.DataFrame(X)
    X['target'] = y
    return pd.read_csv(path)


def split_train_val_data(
    data: pd.DataFrame, params: SplittingParams
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    :rtype: object
    """
    train_data, val_data = train_test_split(
        data, test_size=params.val_size, random_state=params.random_state
    )
    return train_data, val_data
