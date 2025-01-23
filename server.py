import dash

from config import AppConfig
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    compress=True,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.LUX],
    
)


app.title = AppConfig.app_title
