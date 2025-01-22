# dash
import dash
from dash import html

import feffery_antd_components as fac
import feffery_leaflet_components as flc
from feffery_dash_utils.style_utils import style

from dash.dependencies import Input, Output


# 配置
from server import app
from config import MapConfig

# 地图组件
from maps.legend import Legend
from maps.basemap import Basemap
from maps import tile_selector, symbol_style
import dash_bootstrap_components as dbc

# 数据
from models.gpd_data import cbsdata, arcgisdata


def render():
    return dbc.Container([
        dbc.Row([
            ## 添加人体图片assets\human-body.svg
            dbc.Col([
                 html.Img(src='/assets/human-body.svg', width="100%",height=400)
            ],align="center",width="auto"
            )
        ])
            
    ], fluid=True
    )


# 图层控制
@app.callback(
    Output("cbs_fire", "hidden"),
    Input("burned_area_check", "checked"),
)
def cbs_fire_check(checked):
    if checked:
        return False
    else:
        return True


@app.callback(
    Output("cbs_evac_order", "hidden"),
    Input("cbs_evac_order_check", "checked"),
)
def cbs_evac_order_check(checked):
    if checked:
        return False
    else:
        return True


@app.callback(
    Output("cbs_evac_warning", "hidden"),
    Input("cbs_evac_warning_check", "checked"),
)
def cbs_evac_warning_check(checked):
    if checked:
        return False
    else:
        return True
