import pandas as pd
from dash import Dash, html
from src.components import (
    bar_chart,
    category_dropdown,
    month_dropdown,
    pie_chart,
    year_dropdown,
    zone_dropdown,
    timeseries_chart_v2,
    table_chart
)


def create_layout(app: Dash, data: pd.DataFrame, data_dict: dict[str, pd.DataFrame]) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    year_dropdown.render(app, data, data_dict),
                    month_dropdown.render(app, data, data_dict),
                    category_dropdown.render(app, data),
                    zone_dropdown.render(app,data_dict)
                ],
            ),
            #bar_chart.render(app, data),
            #pie_chart.render(app, data),
            timeseries_chart_v2.render(app,data_dict),
            table_chart.render(app,data,data_dict)

        ],
    )
