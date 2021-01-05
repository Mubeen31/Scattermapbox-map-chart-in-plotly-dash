import dash

app = dash.Dash(__name__,
                suppress_callback_exceptions=True,
                meta_tags=[{"name": "viewport", "content": "width=device-width"}])

server = app.server