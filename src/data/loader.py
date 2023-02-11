import pandas as pd
from datetime import datetime
from typing import Dict

class DataSchema:
    USAGE= "Usage (m3/day)"
    LIMIT= "Consent limit"
    RESTRICTION= "Restrictions on"
    AMOUNT = "amount"
    DAY = "Day "
    CATEGORY = "category"
    DATE = "date"
    MONTH = "month"
    YEAR = "year"

READER_DICT = {'Waipukurau':'./data/waipuk.csv','Waipawa-Otane':'./data/Wiapawa.csv',
                'Takapua':'./data/Takapau.csv',
                'Porangahau-Te Paerahi': './data/Porangahau.csv',
                'Kiarakau': './data/Kiarakau.csv'
                }

class ZoneSchema:
    WAIPUK= 'Waipukurau'
    WAIPAWAOTANE= 'Waipawa-Otane'
    TAKAPUA= 'Takapua'
    PORANGAHAU= 'Porangahau-Te Paerahi'
    KIARAKAU= 'Kiarakau' ## the average dame dataschema... that is Q/30 TO DO:

def load_data(path: str) -> pd.DataFrame:
    # load the data from the CSV file
    data = pd.read_csv(
        path,
        # dtype={
        #     DataSchema.USAGE: str,
        #     DataSchema.RESTRICTION: float,
        #     DataSchema.LIMIT: float,
        #     #DataSchema.DAY: pd.Timestamp, to find out
        # },
        parse_dates=[DataSchema.DAY],
        date_parser= lambda x: datetime.strptime(x, '%d/%m/%Y')
    )
    data[DataSchema.YEAR] = data[DataSchema.DAY].dt.year.astype(str)
    data[DataSchema.MONTH] = data[DataSchema.DAY].dt.month.astype(str)
    return data

def load_data_dict(path_list: list[str]): ### do the autmated list... ZoneSChema need mnual input, thereby need teh coupled code belwo.
    # give hardocee lsit of zones in the main.py shoud be enough? so desin my code that way?
    data_dict = {}
    data_dict[ZoneSchema.WAIPUK]=load_data(READER_DICT[ZoneSchema.WAIPUK])
    data_dict[ZoneSchema.WAIPAWAOTANE]=load_data(READER_DICT[ZoneSchema.WAIPAWAOTANE])
    data_dict[ZoneSchema.PORANGAHAU]= load_data(READER_DICT[ZoneSchema.PORANGAHAU])
    data_dict[ZoneSchema.TAKAPUA]= load_data(READER_DICT[ZoneSchema.TAKAPUA])
    data_dict[ZoneSchema.KIARAKAU]= load_data(READER_DICT[ZoneSchema.KIARAKAU])
    return data_dict

def load_transaction_data(path: str) -> pd.DataFrame:
    # load the data from the CSV file
    data = pd.read_csv(
        path,
        dtype={
            DataSchema.AMOUNT: float,
            DataSchema.CATEGORY: str,
            DataSchema.DATE: str,
        },
        parse_dates=[DataSchema.DATE],
    )
    data[DataSchema.YEAR] = data[DataSchema.DATE].dt.year.astype(str)
    data[DataSchema.MONTH] = data[DataSchema.DATE].dt.month.astype(str)
    return data
