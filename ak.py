
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, session, render_template
import dash
import flask
import pandas as pd
from datetime import datetime, timedelta
import plotly.io as pio
import plotly.express as px
from dash import dcc, html, dash_table, ctx
import numpy as np
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import ast
import pytz

app = Flask(__name__)

@app.route("/")
def mode_page():
    return render_template('main.html')

@app.route("/dkexample/")
def mode_page():
    return render_template('dkgearexample.html')
