import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from typing import Dict, Tuple

from ..data.loader import DataSchema
from . import ids


unique_years = ['wah']
def render(app: Dash, data: pd.DataFrame, data_dict: Dict[str,pd.DataFrame]) -> html.Div:
    unique_years = []
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
        
        return  unique_years

    print(unique_years,'unique years *********************************************************************************************************')
    return html.Div(
        children=[
            html.H6("Year"),
            dcc.Dropdown(
                id=ids.YEAR_DROPDOWN,
                options=[{"label": year, "value": year} for year in unique_years],
                value=unique_years,
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

# def render(app: Dash, data: pd.DataFrame, data_dict: Dict[str,pd.DataFrame]) -> html.Div:
#     unique_years = []
    
#     @app.callback(
#         Output(ids.YEAR_DROPDOWN, "options"),
#         [Input(ids.SELECT_ALL_YEARS_BUTTON, "n_clicks"),
#          Input(ids.ZONE_DROPDOWN, "value")],
#     )
#     def select_all_years(n_clicks, zone: str) -> list[dict]:
#         data = data_dict[zone]
#         all_years: list[str] = data[DataSchema.YEAR].tolist()
#         unique_years = sorted(set(all_years), key=int)
#         return [{"label": year, "value": year} for year in unique_years]
    
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

# def render(app: Dash, data: pd.DataFrame, data_dict: Dict[str,pd.DataFrame]) -> html.Div:
#     unique_years = []
    
#     @app.callback(
#         [Output(ids.YEAR_DROPDOWN, "options"),
#          Output(ids.SELECT_ALL_YEARS_BUTTON, "n_clicks")],
#         [Input(ids.SELECT_ALL_YEARS_BUTTON, "n_clicks"),
#          Input(ids.ZONE_DROPDOWN, "value")],
#         [State(ids.SELECT_ALL_YEARS_BUTTON, "n_clicks")]
#     )
#     def select_all_years(n_clicks, zone: str, current_n_clicks) -> Tuple[list[dict], int]:
#         data = data_dict[zone]
#         all_years: list[str] = data[DataSchema.YEAR].tolist()
#         unique_years = sorted(set(all_years), key=int)
#         return [{"label": year, "value": year} for year in unique_years], current_n_clicks + 1
    
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


# def render(app: Dash, data: pd.DataFrame, data_dict: Dict[str,pd.DataFrame]) -> html.Div:
#     unique_years = []
    
#     @app.callback(
#         Output(ids.YEAR_DROPDOWN, "options"),
#         [Input(ids.SELECT_ALL_YEARS_BUTTON, "n_clicks"),
#          Input(ids.ZONE_DROPDOWN, "value")]
#     )
#     def select_all_years(n_clicks, zone: str) -> list[dict]:
#         data = data_dict[zone]
#         all_years: list[str] = data[DataSchema.YEAR].tolist()
#         unique_years = sorted(set(all_years), key=int)
#         return [{"label": year, "value": year} for year in unique_years]
    
#     return html.Div(
#         children=[
#             html.H6("Year"),
#             dcc.Dropdown(
#                 id=ids.YEAR_DROPDOWN,
#                 options=[],
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

