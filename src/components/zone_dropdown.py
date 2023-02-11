import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from typing import Dict

from ..data.loader import DataSchema
from . import ids


def render(app: Dash, data_dict: Dict[str,pd.DataFrame]) -> html.Div:


    @app.callback(
        Output(ids.ZONE_DROPDOWN, "value"),
        [
            Input(ids.ZONE_DROPDOWN, "value"),
            
        ],
    )
    def select_zone(zone: str) -> str:
        print(zone)
        print(type(zone))
        return zone

    return html.Div(
        children=[
            html.H6("ZONE"),
            dcc.Dropdown(
                id=ids.ZONE_DROPDOWN,
                options=[{"label": zone, "value": zone} for zone in list(data_dict.keys())],
                value=list(data_dict.keys()),
                multi=False,
            ),

        ]
    )
