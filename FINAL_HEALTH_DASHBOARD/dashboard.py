
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
import webbrowser
from threading import Timer

# Load the classified data
df = pd.read_csv("classified_patient_data.csv")

# Initialize Dash app
app = Dash(__name__)
app.title = "Health Data Dashboard"

# Auto-open browser
def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050")

Timer(1, open_browser).start()

# Layout with multiple charts
app.layout = html.Div([
    html.H1("📊 Health Monitoring Dashboard", style={'textAlign': 'center'}),

    dcc.Graph(
        id='health-distribution',
        figure=px.histogram(df, x='health_label', title='Health Category Distribution')
    ),

    dcc.Graph(
        id='steps-box',
        figure=px.box(df, x='health_label', y='steps', color='health_label',
                      title='Steps by Health Category')
    ),

    dcc.Graph(
        id='sleep-box',
        figure=px.box(df, x='health_label', y='sleep_duration', color='health_label',
                      title='Sleep Duration by Health Category')
    ),

    dcc.Graph(
        id='active-minutes-box',
        figure=px.box(df, x='health_label', y='active_minutes', color='health_label',
                      title='Active Minutes by Health Category')
    ),

    dcc.Graph(
        id='heart-rate-box',
        figure=px.box(df, x='health_label', y='heart_rate_mean', color='health_label',
                      title='Heart Rate by Health Category')
    )
])

# Run the Dash app (Dash 3+ uses app.run())
if __name__ == '__main__':
    app.run(debug=True)
