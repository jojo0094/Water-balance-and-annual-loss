import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from typing import Dict
import numpy as np

from ..data.loader import DataSchema
from . import ids


def render(app: Dash, data_dict: Dict[str,pd.DataFrame]) -> html.Div:
    @app.callback(
        Output(ids.BAR_CHART, "children"),
        [
            Input(ids.ZONE_DROPDOWN, "value"),
            Input(ids.MONTH_DROPDOWN, "value"),
            Input(ids.YEAR_DROPDOWN, "value"),
        ],
    )
    def update_line_chart(
        zone: str, months: list[str], years: list[str]
    ) -> html.Div:
        data = data_dict[zone]
        #print(filtered_data)
        filtered_data = data.query("year in @years and month in @months")
        filtered_data.replace(0,np.nan, inplace=True)
        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.", id=ids.BAR_CHART)

        fig = px.line(
            filtered_data,
            x=DataSchema.DAY,
            y=[DataSchema.USAGE,DataSchema.LIMIT,DataSchema.RESTRICTION],
            #color=DataSchema.CATEGORY,
        )

        

        specific_dates = filtered_data[~(filtered_data[DataSchema.RESTRICTION].isnull())]['Day '].tolist()
        specific_dates_values = filtered_data[~(filtered_data[DataSchema.RESTRICTION].isnull())][DataSchema.RESTRICTION].tolist()
        for date,value in zip(specific_dates,specific_dates_values):
            #print(value)
            fig.add_shape(type='line', x0=date, x1=date, y0=0, y1=value, yref='y',
                        line={'color': '#00CC96', 'width': 1, 'dash': 'dot'},#dict(color='#00CC96', width=1, dash='dot'),
                        name= DataSchema.RESTRICTION)#"Restriction On")
        fig.update_layout(
            title=f"{zone} Daily Water Usage :month year format to be integrated later",#"User Input for title",
            xaxis_title="",
            yaxis_title= DataSchema.USAGE ,#"Usage (m3/day)",
            legend_title="",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="RebeccaPurple"
            )
        )

        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

    return html.Div(id=ids.BAR_CHART)
