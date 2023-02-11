import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from typing import Dict

from ..data.loader import DataSchema
from . import ids


# def render(app: Dash, data: pd.DataFrame, data_dict: Dict[str,pd.DataFrame]) -> html.Div:

#     unique_months = []
#     @app.callback(
#         Output(ids.MONTH_DROPDOWN, "options"),
#         [Input(ids.YEAR_DROPDOWN, "value"),]   
#     )
#     def update_options(zone: str) -> list[dict]:
#         filtered_data = data.query("year in @years")
#         return sorted(set(filtered_data[DataSchema.MONTH].tolist()))

#     @app.callback(
#         Output(ids.MONTH_DROPDOWN, "value"),
#         [
#             Input(ids.YEAR_DROPDOWN, "value"),
#             Input(ids.SELECT_ALL_MONTHS_BUTTON, "n_clicks"),
#         ],
#     )
#     def select_all_months(years: list[str], _: int) -> list[str]:
#         filtered_data = data.query("year in @years")
#         return sorted(set(filtered_data[DataSchema.MONTH].tolist()))

#     return html.Div(
#         children=[
#             html.H6("Month"),
#             dcc.Dropdown(
#                 id=ids.MONTH_DROPDOWN,
#                 options=[{"label": month, "value": month} for month in unique_months],
#                 value=unique_months,
#                 multi=True,
#             ),
#             html.Button(
#                 className="dropdown-button",
#                 children=["Select All"],
#                 id=ids.SELECT_ALL_MONTHS_BUTTON,
#                 n_clicks=0,
#             ),
#         ]
#     )

def render(app: Dash, data: pd.DataFrame, data_dict: Dict[str,pd.DataFrame]) -> html.Div:

    @app.callback(
        Output(ids.MONTH_DROPDOWN, "options"),
        [Input(ids.YEAR_DROPDOWN, "value"),
        Input(ids.ZONE_DROPDOWN, "value")] 
    )
    def update_options(years: list[str], zone: str) -> list[dict]:
        data = data_dict[zone]
        filtered_data = data.query("year in @years")
        unique_months = sorted(set(filtered_data[DataSchema.MONTH].tolist()))
        return [{"label": month, "value": month} for month in unique_months]

    @app.callback(
        Output(ids.MONTH_DROPDOWN, "value"),
        [
            Input(ids.YEAR_DROPDOWN, "value"),
            Input(ids.SELECT_ALL_MONTHS_BUTTON, "n_clicks"),
            Input(ids.ZONE_DROPDOWN, "value")
        ],
    )
    def select_all_months(years: list[str], _: int, zone: str) -> list[str]:
        data = data_dict[zone]
        filtered_data = data.query("year in @years")
        unique_months = sorted(set(filtered_data[DataSchema.MONTH].tolist()))
        return unique_months

    return html.Div(
        children=[
            html.H6("Month"),
            dcc.Dropdown(
                id=ids.MONTH_DROPDOWN,
                options=[],
                value=[],
                multi=True,
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_MONTHS_BUTTON,
                n_clicks=0,
            ),
        ]
    )
