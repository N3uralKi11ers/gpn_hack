import pandas as pd


def _filtering_df(df: pd.DataFrame, product_title: str, place_title: str):
    df_filtered = df.loc[
        (df['product'] == product_title)
        & (df['place'] == place_title)
    ]
    return df_filtered


# Принимает на вход столбец отсортированных
def compare_prices_1_2(
    df: pd.DataFrame,
    product_title: str,
    place_title: str,
    competitor: str
):
    df_filtered = _filtering_df(df, product_title, place_title)
    our_prices = df_filtered['Our_company']
    competitor_prices = df_filtered[competitor]
    result = (our_prices < competitor_prices * 1.2).all()
    return result


# check that prices diff <= 1
def compare_prices_1(
    df: pd.DataFrame,
    product_title: str,
    place_title: str
):
    df_filtered = _filtering_df(df, product_title, place_title).copy()
    df_filtered['date'] = pd.to_datetime(df_filtered[['year', 'month', 'day']])
    df_filtered.sort_values('date')

    _prices = df_filtered['Our_company']
    prev = None
    flag = True

    for _price in _prices:
        if prev is not None and _price - prev > 1:
            flag = False

        prev = _price

    return flag
