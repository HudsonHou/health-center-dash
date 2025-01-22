import dash
from dash import html

import feffery_antd_components as fac


from feffery_dash_utils.style_utils import style

from components import home, fire_maps, dashboard, timeline, about


def render():
    return html.Div(
        [
            html.Div(
                [
                    fac.AntdFlex(
                        fac.AntdTitle("个人健康数据中心", level=4, style={"margin": "0px"}),
                        justify="center",
                    ),
                    fac.AntdFlex(
                        fac.AntdTitle("self-health-data-center", level=4, style={"margin": "0px"}),
                        justify="center",
                    ),
                ],
                # style=style(height="15%"),
            ),
            fac.AntdTabs(
                items=[
                    {
                        "key": "base",
                        "label": "基础数据",
                        "children": home.render(),
                    },
                    {
                        "key": "behavior",
                        "label": "行为数据",
                        # "children": timeline.render(),
                    },
                    {
                        "key": "medical",
                        "label": "医疗检测数据",
                        # "children": fire_maps.render(),
                    },
                    {
                        "key": "stats",
                        "label": "健康风险评估",
                        # "children": dashboard.render(),
                    },
                    {
                        "key": "about",
                        "label": "关于",
                        # "children": about.render(),
                    },
                ],
                defaultActiveKey="base",
                tabPosition="top",
                centered=True,
                style=style(width="100%", overflowY="auto"),
            ),
        ],
        style=style(width="100%"),
    )
