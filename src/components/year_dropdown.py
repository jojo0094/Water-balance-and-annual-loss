import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from typing import Dict, Tuple

from ..data.loader import DataSchema
from . import ids


# def render(app: Dash, data: pd.DataFrame, data_dict: Dict[str,pd.DataFrame]) -> html.Div:
#     unique_years = []
#     @app.callback(
#         Output(ids.YEAR_DROPDOWN, "value"),
#         [Input(ids.SELECT_ALL_YEARS_BUTTON, "n_clicks"),
#         Input(ids.ZONE_DROPDOWN, "value"),
#         ]   
#     )
#     def select_all_years(_: int, zone: str) -> list[str]:
#         data = data_dict[zone]
#         all_years: list[str] = data[DataSchema.YEAR].tolist()
#         unique_years = sorted(set(all_years), key=int)
        
#         return  unique_years

#     return html.Div(
#         children=[
#             html.H6("Year"),
#             dcc.Dropdown(
#                 id=ids.YEAR_DROPDOWN,
#                 options=[{"label": year, "value": year} for year in unique_years],
#                 value=unique_years,
#                 multi=True,
#             ),
#             html.Button(
#                 className="dropdown-button",
#                 children=["Select All"],
#                 id=ids.SELECT_ALL_YEARS_BUTTON,
#                 n_clicks=0,
#             ),
#         ]
#     )

def render(app: Dash, data: pd.DataFrame, data_dict: Dict[str,pd.DataFrame]) -> html.Div:
    unique_years = []
    
    @app.callback(
        Output(ids.YEAR_DROPDOWN, "options"),
        [Input(ids.ZONE_DROPDOWN, "value"),]   
    )
    def update_options(zone: str) -> list[dict]:
        data = data_dict[zone]
        all_years: list[str] = data[DataSchema.YEAR].tolist()
        unique_years = sorted(set(all_years), key=int)
        return [{"label": year, "value": year} for year in unique_years]

    @app.callback(
        Output(ids.YEAR_DROPDOWN, "value"),
        [Input(ids.SELECT_ALL_YEARS_BUTTON, "n_clicks"),
        Input(ids.ZONE_DROPDOWN, "value"),
        ]   
    )
    def select_all_years(_: int, zone: str) -> list[str]:
        data = data_dict[zone]
        all_years: list[str] = data[DataSchema.YEAR].tolist()
        unique_years = sorted(set(all_years), key=int)
        return unique_years

    return html.Div(
        children=[
            html.H6("Year"),
            dcc.Dropdown(
                id=ids.YEAR_DROPDOWN,
                options=[{"label": year, "value": year} for year in unique_years],
                value=[],
                multi=True,
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_YEARS_BUTTON,
                n_clicks=0,
            ),
        ]
    )


