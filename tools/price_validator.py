import pandas as pd


def filtering_df():
    pass


# Принимает на вход столбец отсортированных
def compare_prices(our_prices: pd.Series, copetitors_prices: pd.Series):
    result = (our_prices < copetitors_prices * 1.2).all()
    return result
