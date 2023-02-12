import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from typing import Dict
import dash_table 
import copy

from ..data.loader import DataSchema
from . import ids


# def render(app: Dash, data: pd.DataFrame, data_dict: Dict[str,pd.DataFrame]) -> html.Div:
#     @app.callback(
#         Output(ids.TABLE_CHART, "children"),
#         [
#             Input(ids.ZONE_DROPDOWN, "value"),
#         ],
#     )
#     def update_table_chart(
#         zone: str
#     ) -> html.Div:

#         HardCodeDict = {
#             "2015-2016": {"start_date": "2015-09-01","end_date":"2016-08-31"},
#             "2016-2017": {"start_date": "2016-09-01","end_date":"2017-08-31"},
#             "2017-2018": {"start_date": "2017-09-01","end_date":"2018-08-31"},
#             "2018-2019": {"start_date": "2018-09-01","end_date":"2019-08-31"},
#             "2019-2020": {"start_date": "2019-09-01","end_date":"2020-08-31"},
            
#         }
#         filtered_data = data_dict[zone]

#         if filtered_data.shape[0] == 0:
#             return html.Div("No data selected.", id=ids.TABLE_CHART)

#         cal_dict = {}
#         interim = copy.deepcopy(filtered_data)
#         for year_period in HardCodeDict:
#             valCal = interim[(interim['Day ']>=HardCodeDict[year_period]['start_date'])&(interim['Day ']<=HardCodeDict[year_period]['end_date'])]['Usage (m3/day)']
#             cal_dict[year_period]=[valCal.max(),valCal.mean()]
#         interim_df = pd.DataFrame(cal_dict).T
#         interim_df.rename(columns={0:'Peak Day',1:'Average Day'},inplace=True)

#         interim_df.columns = pd.MultiIndex.from_tuples(
#             zip([f"    {zone}", '', ''], 
#                 interim_df.columns))


#         table_ = dash_table.DataTable(
#             id='table',
#             columns=[{"name": i, "id": i} for i in interim_df.columns],
#             data=interim_df.to_dict("records"),
#             style_cell={'textAlign': 'left'}
#         )       


#         return html.Div(table_, id=ids.TABLE_CHART)

#     return html.Div(id=ids.TABLE_CHART)

def render(app: Dash, data: pd.DataFrame, data_dict: Dict[str,pd.DataFrame]) -> html.Div:
    @app.callback(
        Output(ids.TABLE_CHART, "children"),
        [
            Input(ids.ZONE_DROPDOWN, "value"),
        ],
    )
    def update_table_chart(
        zone: str
    ) -> html.Div:

        HardCodeDict = {
            "2015-2016": {"start_date": "2015-09-01","end_date":"2016-08-31"},
            "2016-2017": {"start_date": "2016-09-01","end_date":"2017-08-31"},
            "2017-2018": {"start_date": "2017-09-01","end_date":"2018-08-31"},
            "2018-2019": {"start_date": "2018-09-01","end_date":"2019-08-31"},
            "2019-2020": {"start_date": "2019-09-01","end_date":"2020-08-31"},
            
        }
        filtered_data = data_dict[zone]

        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.", id=ids.TABLE_CHART)

        cal_dict = {}
        interim = copy.deepcopy(filtered_data)
        for year_period in HardCodeDict:
            valCal = interim[(interim['Day ']>=HardCodeDict[year_period]['start_date'])&(interim['Day ']<=HardCodeDict[year_period]['end_date'])]['Usage (m3/day)']
            cal_dict[year_period]=[valCal.max(),valCal.mean()]
        interim_df = pd.DataFrame(cal_dict).T
        interim_df.rename(columns={0:'Peak Day',1:'Average Day'},inplace=True)

        interim_df.columns = pd.MultiIndex.from_tuples(
            zip([f"    {zone}", '', ''], 
                interim_df.columns))


        table_ = dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in interim_df.columns],
            data=interim_df.to_dict("records"),
            style_cell={'textAlign': 'left'}
        )       


        return html.Div(table_, id=ids.TABLE_CHART)

    return html.Div(id=ids.TABLE_CHART)


