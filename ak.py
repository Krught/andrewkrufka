

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
def main_page():
    return render_template('main.html')

@app.route("/dkexample/")
def dkgear_page():
    return render_template('dkgearexample.html')



external_stylesheets = ['/static/css/dash_css.css']


server = dash.Dash(server=app, routes_pathname_prefix="/frontpagedata/",title="Frontpage", update_title='Loading Frontpage...', external_stylesheets=external_stylesheets)


def all_dash_stuff():
    data_rot = ['Main hand', 'Rune of Razoricce', 'Off hand', 'Icy Touch', 'Ghoul - Claw', 'Ghoul - Main hand', 'Frost Fever', 'OH - Plague Strike', 'Plague Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Hyperspeed Acceleration', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Darkmoon Card: Greatness', 'Off hand', 'Blood Plague', 'Unbreakable Armor', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Blood Strike', 'Blood Strike', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Horn of Winter', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'Off hand', 'Main hand', 'Rune of Razoricce', 'Ghoul - Claw', 'Ghoul - Main hand', 'Blood Plague', 'Ghoul - Main hand', 'Main hand', 'Off hand', 'Ghoul - Main hand', 'Main hand', 'Rune of Razoricce', 'Ghoul - Main hand', 'Frost Fever', 'Off hand', 'Ghoul - Main hand', 'Main hand', 'Rune of Razoricce', 'Ghoul - Main hand', 'OH - Obliterate', 'Obliterate', 'Ghoul - Claw', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Grim Toll', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Blood Strike', 'Blood Strike', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'Pestilence', 'Ghoul - Main hand', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Empowered Rune Weapon', 'Main hand', 'Rune of Razoricce', 'OH - Obliterate', 'Obliterate', 'Shattering Throw', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Blood Strike', 'Blood Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'OH - Obliterate', 'Obliterate', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'Blood Plague', 'OH - Blood Strike', 'Blood Strike', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Pestilence', 'Ghoul - Claw', 'Ghoul - Main hand', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'Blood Tap', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Blood Strike', 'Blood Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Blood Strike', 'Blood Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'Pestilence', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'OH - Blood Strike', 'Blood Strike', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Frost Fever', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'OH - Blood Strike', 'Blood Strike', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Darkmoon Card: Greatness', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Rune of the Fallen Crusader', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'Horn of Winter', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Rune of Razoricce', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'Pestilence', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Ghoul - Claw', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Grim Toll', 'Main hand', 'Rune of Razoricce', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Hyperspeed Acceleration', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'Howling Blast', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'Main hand', 'Rune of Razoricce', 'OH - Obliterate', 'Obliterate', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'Pestilence', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'Unbreakable Armor', 'Main hand', 'Rune of Razoricce', 'Off hand', 'OH - Frost Strike', 'Frost Strike', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Rune of Razorice', 'Blood Plague', 'Howling Blast', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'OH - Obliterate', 'Obliterate', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Blood Strike', 'Blood Strike', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Rune of the Fallen Crusader', 'Blood Plague', 'OH - Blood Strike', 'Blood Strike', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Blood Plague', 'Horn of Winter', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'Off hand', 'Main hand', 'Rune of Razoricce', 'Icy Touch', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Plague Strike', 'Plague Strike', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate']
    data_time = [0, 0, 0, 0, 0, 0, 0, 1.1846804511278197, 1.1846804511278197, 0.7338357794525984, 0.7338357794525984, 1.4676715589051967, 2.3693609022556394, 2.3693609022556394, 1.5335669270263035, 2.3693609022556394, 2.3693609022556394, 1.5949096041073558, 1.1846804511278197, 2.3693609022556394, 2.201507338357795, 2.201507338357795, 2.8004760015866728, 2.8115393662148898, 3.554041353383459, 3.1898192082147117, 3, 3.554041353383459, 3.554041353383459, 3.39944466481555, 3.9984133280444274, 4.624681217483119, 3.966490675923261, 4.624681217483119, 4.18468045112782, 4.624681217483119, 4.624681217483119, 4.597381991273305, 5.6953210815827795, 5.121441985631632, 5.6953210815827795, 4.631198442730759, 5.6953210815827795, 5.196350654502182, 5.795319317731059, 6.009866070022687, 6.76596094568244, 5.739951700050796, 6, 6.848704957370832, 6.898290154413742, 6.965960945682439, 6.394287980959937, 6.394287980959937, 7.18468045112782, 6.993256644188814, 7.786714238804796, 7.957458214690869, 7.592225307417691, 8.675138323195851, 8.765960945682433, 8.19119397064657, 9, 9.066211472010906, 8.790162633875447, 9.563562407586906, 9.56596094568243, 9.389131297104324, 10.065960945682429, 10.065960945682429, 9.988099960333201, 9.988099960333201, 11.13660080978209, 10.45198649197796, 11.13660080978209, 10.174964729330943, 10.18468045112782, 11.13660080978209, 11.13660080978209, 10.587068623562079, 11.186037286790956, 12.207240673881751, 12.207240673881751, 11.340410576369015, 12.207240673881751, 11.28371798665098, 12, 12.207240673881751, 12.207240673881751, 11.785005950019833, 12.518841729472431, 13.277880537981412, 12.22883466076007, 13.277880537981412, 12.392471243971018, 13.18468045112782, 13.277880537981412, 13.252677508925029, 13.211890383212829, 14.462560989109232, 13.619324785592061, 14.462560989109232, 14.194946105665588, 14.462560989109232, 14.462560989109232, 14.462560989109232, 15.647241440237051, 13.986513288377626, 13.986513288377626, 14.720349067830224, 15.647241440237051, 15.178001828118347, 15.647241440237051, 14.846178327213105, 15, 15.647241440237051, 15.647241440237051, 15.454184847282821, 16.83192189136487, 16.161057550571105, 16.83192189136487, 16.073031868834146, 16.184680451127818, 16.83192189136487, 16.83192189136487, 16.38635462118207, 18.236639573385673, 17.326701631577496, 18.236639573385673, 17.527755681930124, 18, 18.236639573385673, 18.236639573385673, 17.318524395081315, 17.318524395081315, 18.250694168980562, 19.641357255406476, 18.492345712583887, 19.641357255406476, 18.9824794950261, 19.184680451127818, 19.641357255406476, 19.641357255406476, 19.18286394287981, 21.046074937427278, 19.65798979359028, 21.046074937427278, 20.43720330812208, 21, 21.046074937427278, 21.046074937427278, 20.115033716779056, 21.047203490678303, 22.45079261944808, 20.82363387459667, 22.45079261944808, 21.891927121218057, 22.184680451127818, 22.45079261944808, 22.45079261944808, 21.97937326457755, 21.97937326457755, 22.911543038476797, 23.855510301468883, 21.98927795560306, 23.855510301468883, 23.346650934314034, 23.855510301468883, 23.855510301468883, 23.843712812376044, 25.260227983489685, 23.154922036609452, 25.260227983489685, 24.801374747410012, 24, 25.184680451127818, 25.260227983489685, 25.260227983489685, 24.77588258627529, 25.708052360174538, 26.664945665510487, 24.320566117615844, 26.664945665510487, 26.25609856050599, 26.664945665510487, 26.640222134073785, 26.640222134073785, 25.486210198622235, 28.06966334753129, 27.710822373601967, 27, 28.06966334753129, 28.06966334753129, 28.06966334753129, 27.57239190797303, 28.50456168187228, 29.47438102955209, 26.651854279628626, 29.47438102955209, 29.165546186697945, 28.184680451127818, 29.47438102955209, 29.47438102955209, 29.436731455771525, 30.879098711572894, 27.817498360635017, 30.879098711572894, 30.620269999793923, 30, 30.879098711572894, 30.879098711572894, 30.368901229670772, 30.368901229670772, 31.30107100357002, 32.283816393593696, 28.98314244164141, 32.283816393593696, 32.0749938128899, 31.184680451127818, 32.283816393593696, 32.283816393593696, 32.23324077746926, 33.6885340756145, 30.1487865226478, 33.6885340756145, 33.529717625985874, 33, 33.6885340756145, 33.6885340756145, 33.16541055136851, 33.16541055136851, 34.09758032526776, 35.0932517576353, 31.31443060365419, 35.0932517576353, 34.98444143908185, 34.18468045112782, 35.0932517576353, 35.0932517576353, 35.029750099167, 36.4979694396561, 32.8297679089625, 36.4979694396561, 36, 36.4979694396561, 36.4979694396561, 35.96191987306625, 36.8940896469655, 37.902687121676905, 34.34510521427081, 37.902687121676905, 36.875582396106616, 37.18468045112782, 37.902687121676905, 37.902687121676905, 37.826259420864744, 37.826259420864744, 39.30740480369771, 35.86044251957912, 39.30740480369771, 38.76672335313138, 39, 39.30740480369771, 38.75842919476399, 39.69059896866324, 37.375779824887424, 40.71212248571851, 40.65786431015615, 40.18468045112782, 40.71212248571851, 40.71212248571851, 40.622768742562485, 42.11684016773931, 38.89111713019573, 42.11684016773931, 42, 42.11684016773931, 42.11684016773931, 41.55493851646173, 41.55493851646173, 42.48710829036098, 43.521557849760114, 40.40645443550404, 43.521557849760114, 42.54900526718092, 43.18468045112782, 43.521557849760114, 43.521557849760114, 43.419278064260226, 44.92627553178092, 41.921791740812345, 44.92627553178092, 44.440146224205684, 44.92627553178092, 44.92627553178092, 44.35144783815947, 45.28361761205872, 46.33099321380172, 43.43712904612065, 46.33099321380172, 45, 46.18468045112782, 46.33099321380172, 46.33099321380172, 46.21578738595797, 46.21578738595797, 47.73571089582252, 44.95246635142896, 47.73571089582252, 46.33128718123045, 47.73571089582252, 47.73571089582252, 47.147957159857214, 48.08012693375646, 49.14042857784332, 49.14042857784332, 46.46780365673727, 49.14042857784332, 48.22242813825522, 49.14042857784332, 48, 49.14042857784332, 49.14042857784332, 49.01229670765571, 50.545146259864126, 47.983140962045574, 50.545146259864126, 50.113569095279985, 49.18468045112782, 50.545146259864126, 49.944466481554954, 49.944466481554954, 50.8766362554542, 49.49847826735388, 51.94986394188493, 51, 51.94986394188493, 51.94986394188493, 51.80880602935345, 53.35458162390573, 51.01381557266219, 53.35458162390573, 52.00471005230475, 52.18468045112782, 53.35458162390573, 52.740975803252695, 53.67314557715194, 52.529152877970496, 54.75929930592653, 53.89585100932952, 54, 54.75929930592653, 54.75929930592653, 54.60531535105119, 54.60531535105119, 56.164016987947335, 54.0444901832788, 56.164016987947335, 55.786991966354286, 55.18468045112782, 56.164016987947335, 56.164016987947335, 55.537485124950436, 56.46965489884968, 57.56873466996814, 57.56873466996814, 55.55982748858711, 57.56873466996814, 57, 57.56873466996814, 57.56873466996814, 57.40182467274893, 58.97345235198894, 57.07516479389542, 58.97345235198894, 57.67813292337905, 58.18468045112782, 58.97345235198894, 58.97345235198894, 60.37817003400974, 60.37817003400974, 58.590502099203725, 60.37817003400974, 59.56927388040382, 60, 60.37817003400974, 60.10583940451203, 61.782887716030544, 61.46041483742859, 61.18468045112782, 61.62117670982034, 61.882887716030545, 62.28288771603055, 62.28288771603055, 63.68760539805135, 63.13651401512865, 63.68760539805135, 63.351555794453354, 63, 63.68760539805135, 63.68760539805135, 65.09232308007216, 64.65185132043696, 65.09232308007216, 64.18468045112782, 65.09232308007216, 65.09232308007216, 66.49704076209296, 66.16718862574527, 66.49704076209296, 65.24269675147812, 66, 66.49704076209296, 67.44516106493386, 67.68172121322078, 66.83760635558548, 67.18468045112782, 67.68172121322078, 68.72313350412244, 68.8664016643486, 68.43251595969284, 68.8664016643486, 68.8664016643486, 70.05108211547642, 70.00110594331103, 70.05108211547642, 70.0274255638002, 69, 70.05108211547642, 70.05108211547642, 71.23576256660424, 70.18468045112782, 71.23576256660424, 71.27907838249962, 72.42044301773205, 71.62233516790755, 72, 72.42044301773205, 72.42044301773205, 73.60512346885987, 72.55705082168821, 73.60512346885987, 73.21724477201491, 73.18468045112782, 73.60512346885987, 73.60512346885987, 74.78980391998769, 73.8350232608768, 74.78980391998769, 74.78980391998769, 74.78980391998769, 75.97448437111551, 75.11299570006538, 75.97448437111551, 74.81215437612227, 75, 75.97448437111551, 75.97448437111551, 77.15916482224333, 76.39096813925397, 77.15916482224333, 76.40706398022962, 77.15916482224333, 76.18468045112782, 77.15916482224333, 77.15916482224333, 78.34384527337114, 77.66894057844256, 78.34384527337114, 78.00197358433698, 78, 78.34384527337114, 78.34384527337114, 79.52852572449896, 78.94691301763115, 79.52852572449896, 79.18468045112782, 79.52852572449896, 80.22488545681973, 80.71320617562678, 79.59688318844434, 81, 81.1917927925517, 81.50285789600832, 81.51320617562673, 82.31320617562669, 83.32126266237829, 83.71792385764749, 83.08293374957647, 82.31320617562669, 83.71792385764749, 83.71792385764749, 85.1226415396683, 84.8365999676866, 85.1226415396683, 84.97407470660124, 83.71792385764749, 85.1226415396683, 85.1226415396683]
    data_dam = [770.2097112429549, 15.404194224859099, 0.0, 2698.5016254719812, 306.7479904351805, 154.15002907223868, 441.2536343947696, 1094.3101540007804, 1930.8906821479484, 286.42521844514476, 143.93722901885258, 111.28116554547591, 0, 38.61781364295897, 2600.565137888517, 52.01130275777034, 0, 2131.291573816107, 643.9181361586739, 0, 0, 0.0, 0.0, 1477.5883377028604, 29.55176675405721, 2234.639014825437, 503.4093879403697, 2004.9094220179222, 2035.8213443951463, 167.57552053721517, 129.55646964572776, 40.71642688790293, 1495.1654366939783, 29.903308733879566, 768.8495110667276, 5086.704075330188, 4201.342545277327, 99.02582314619849, 84.02685090554654, 1455.5830913033287, 29.111661826066577, 2464.4988842418493, 0, 100.1877684801807, 77.45745646120872, 1590.351552990541, 31.80703105981082, 2510.414404895002, 566.0738440628281, 745.0192164943606, 3270.5028798361886, 65.41005759672377, 240.26384010120324, 185.75347286553517, 768.8495110667276, 159.16278332771722, 0.0, 1233.1232043315013, 159.63480055600525, 1026.377502442731, 20.527550048854618, 306.82878541716457, 566.0738440628281, 739.9653991810903, 152.63710213520656, 3146.148344733898, 62.922966894677955, 168.87219236466225, 5213.752411947229, 7483.0147513453785, 250.98889047639932, 194.04525473754438, 149.66029502690756, 1043.5298521120123, 20.87059704224025, 780.3959376872542, 768.8495110667276, 5561.816930399944, 7328.319409810836, 166.5527903713985, 83.69775280806215, 146.56638819621674, 0, 3167.1929583665924, 63.34385916733185, 1196.3681693258977, 566.0738440628281, 5169.761355463422, 5115.515446979516, 207.09567128318088, 126.46998183034982, 102.31030893959033, 1803.2102373763737, 36.06420474752748, 977.942807385628, 768.8495110667276, 129.93827, 346.54634592274016, 1146.776251452986, 22.93552502905972, 0.0, 0, 1309.8050226977764, 26.196100453955527, 6447.596877146089, 9291.02795491855, 0, 591.3659451339718, 367.05817120060516, 350.5097677250871, 185.820559098371, 3777.2399519775277, 75.54479903955055, 3042.2324989108424, 566.0738440628281, 2828.0800294281353, 9517.535539706056, 342.6784867911552, 190.3507107941211, 1206.4345571899707, 24.128691143799415, 0.0, 768.8495110667276, 6442.902997184658, 2578.6587741819926, 116.33607077780226, 51.57317548363985, 1808.3274117284375, 36.16654823456875, 2802.9780600310423, 566.0738440628281, 2389.867414206597, 4714.6818132387025, 310.0067051298525, 592.0608052553007, 1130.7368238139434, 94.29363626477405, 1690.1478041800478, 33.80295608360096, 1357.1826750324813, 706.6384014271235, 5306.38686914769, 1708.6274310668684, 113.85328730089668, 34.17254862133737, 3766.547008618154, 75.33094017236309, 2645.2010139415106, 503.9180905172281, 2154.906019195037, 1728.9392904518152, 128.74997845848569, 245.89086191153226, 34.578785809036304, 3837.437212730687, 76.74874425461374, 2592.0333608571104, 706.6384014271235, 6381.658940546699, 3354.015473913585, 246.16745991756017, 202.57350800680064, 166.69963674290668, 67.0803094782717, 2592.9068500637677, 51.85813700127535, 2124.9770422789184, 5145.172757656757, 6867.3875609662355, 177.27818948843915, 137.34775121932472, 1455.850534542491, 29.11701069084982, 670.6308846927004, 441.2536343947696, 643.9181361586739, 4878.084564380847, 5029.329428867573, 139.49345785633835, 107.84558437059316, 100.58658857735146, 1288.6060647485554, 25.772121294971107, 0.0, 236.3695257, 478.78395808480195, 740.3176685188874, 2841.6216213175726, 56.83243242635145, 1845.7544297543072, 441.2536343947696, 0, 1638.067930987947, 3404.7142636407134, 165.00651278648476, 127.57031096568818, 68.09428527281428, 766.5342077423946, 15.330684154847892, 0.0, 643.9181361586739, 1798.342214066025, 1839.0968364153334, 158.04840676958997, 36.78193672830667, 2428.381935439189, 48.56763870878378, 2099.724653367063, 441.2536343947696, 1565.3638706213096, 1275.9299075383196, 0, 0, 0.0, 25.518598150766394, 1247.138845767875, 24.9427769153575, 608.9231925407488, 643.9181361586739, 4598.0091225735705, 2538.4931444574404, 153.40966939088207, 50.76986288914881, 1207.5565003772251, 24.151130007544502, 1052.017809791793, 441.2536343947696, 5059.572940521736, 2670.0275775644745, 228.9548197275019, 115.0566367758536, 88.95291879269445, 53.40055155128949, 846.7827008379619, 16.935654016759237, 652.5697966099027, 643.9181361586739, 4449.910122976278, 1833.7320149597083, 167.3258812563029, 36.67464029919417, 1275.4119496183391, 25.508238992366785, 441.2536343947696, 1676.3673913596583, 1423.9346018561178, 95.69604607792454, 73.98480308558814, 28.478692037122357, 889.0509910944057, 17.781019821888115, 1054.8451201768396, 643.9181361586739, 4007.6726976883683, 1343.4408207359118, 241.71134725423403, 121.46717295024496, 26.868816414718236, 1346.094709244499, 26.92189418488998, 952.3551187189073, 441.2536343947696, 114.75068000000002, 160.36777528059767, 123.9839968492269, 2700.0487659703485, 54.00097531940697, 0.0, 643.9181361586739, 4138.072623103101, 3505.599802644706, 0, 70.11199605289413, 2684.7435924192982, 53.694871848385965, 441.2536343947696, 5019.217634034464, 6255.107691767179, 227.7951353331726, 176.1136318814688, 136.15747890804408, 125.10215383534359, 1359.288824374716, 27.18577648749432, 1898.8442505095159, 643.9181361586739, 4797.263448354472, 6520.780126141717, 138.72033453370318, 130.41560252283435, 2724.919672990808, 54.498393459816164, 676.4605693635449, 4489.824394606132, 4600.874425939881, 331.55927091149226, 166.61843873098465, 92.01748851879762, 1344.2098356544684, 26.88419671308937, 441.2536343947696, 643.9181361586739, 1664.6828102293057, 3492.720797665473, 0, 0.0, 69.85441595330947, 1306.5123638538494, 26.13024727707699, 678.298321113825, 1877.4733305365016, 1944.6049917093028, 99.21375518230046, 49.857875919644684, 38.892099834186055, 0, 2560.3890573170065, 51.20778114634013, 1903.1488305707496, 0, 441.2536343947696, 3870.833269784018, 1269.8712358411003, 157.27528373500894, 25.397424716822005, 1483.2316675860752, 29.664633351721506, 0.0, 753.1694447496152, 0, 235.9129256020492, 182.3896813019838, 141.00963633317033, 1539.7778752870038, 30.795557505740078, 550.4077300322135, 4721.982998096833, 1526.8044734134342, 0, 30.536089468268685, 3255.8430620165523, 65.11686124033105, 710.0793380422497, 753.1694447496152, 109.68815, 0, 0.0, 3156.3594339347187, 63.127188678694374, 744.9966212975728, 550.4077300322135, 5293.766476612805, 3011.5460691280914, 254.46787480590802, 196.73493713410815, 60.23092138256183, 2974.6104980159857, 59.49220996031971, 1217.538235372534, 753.1694447496152, 5770.825652376234, 8315.905923072296, 0, 0.0, 166.31811846144592, 0, 1610.460634913164, 32.20921269826328, 550.4077300322135, 5432.865813635859, 4433.178579709697, 114.45960157548119, 88.66357159419395, 1859.7146544572229, 37.19429308914446, 966.7489950783986, 753.1694447496152, 6400.539293334943, 5118.506224697219, 0, 102.37012449394439, 1934.8887141792381, 38.697774283584764, 2781.9956013428605, 542.5612161433247, 4237.830372273173, 3860.402215788906, 77.20804431577811, 876.2705084495831, 745.3159427327467, 1873.0442909462306, 37.460885818924616, 7139.176842204848, 10076.901730993219, 201.5380346198644, 3634.8876717368394, 72.69775343473678, 2651.2204147147286, 542.5612161433247, 7025.976169669419, 0, 0.0, 1938.3245154699612, 38.766490309399224, 745.3159427327467, 2939.56091623068, 3729.4557854866366, 74.58911570973274, 1628.5146913696879, 32.570293827393755, 727.1027064006977, 433.40712050588087, 124.87574000000001, 1582.704007493386, 31.65408014986772, 2507.9366881524725, 636.0646341418058, 0, 781.015010885806, 15.62030021771612, 972.1070232144399, 1833.666695234946, 3850.1425495292724, 77.00285099058544, 853.6985169060382, 17.073970338120766, 0.0, 496.07157662833924, 2029.392808927466, 1684.4149914899565, 33.68829982979913, 698.7848994102553, 0, 2792.433819210415, 55.848676384208304, 692.1463156982135, 496.07157662833924, 5775.304097428584, 7500.781213814411, 150.0156242762882, 1355.7919894772936, 27.115839789545873, 649.4185875041996, 698.7848994102553, 2057.747392470455, 4271.1083351439065, 85.42216670287813, 1398.2016452529895, 27.96403290505979, 5566.263609824516, 7271.025002213544, 145.42050004427088, 902.7052302468428, 18.054104604936857, 2048.2722443373314, 496.07157662833924, 1919.4423272301115, 4789.266828851215, 95.7853365770243, 1295.4760345963032, 25.909520691926065, 2186.0188062967927, 0, 698.7848994102553, 1936.877996960895, 4846.920776761004, 96.93841553522009, 1451.219678249838, 29.024393564996757, 2440.5437189704676, 554.038203804209, 2228.0582161566062, 4538.264411394935, 90.76528822789871, 1563.3696568566786, 31.267393137133574, 756.8031518320597, 0, 1606.7217494273903, 32.1344349885478, 2248.272476235387, 554.038203804209, 0.0, 3227.208510847737, 64.54417021695474, 3562.324082465886, 1592.5851975021585, 31.85170395004317, 0.0, 554.038203804209, 2506.1956947815106, 2047.0174272061183, 40.940348544122365, 1044.3691371278037, 20.887382742556074, 0.0, 756.8031518320597, 2371.040518237284, 8141.560268742911]
    data_sta = ['Glance', 'Active', 'Miss', 'Crit', 'Hit', 'Glance', 'DOT', 'Hit', 'Crit', 'Hit', 'Glance', 'Hit', 'Active', 'Active', 'Crit', 'Active', 'Proc', 'Crit', 'DOT', 'Active', 'Dodge', 'Hit', 'Hit', 'Hit', 'Active', 'Crit', 'DOT', 'Hit', 'Hit', 'Hit', 'Hit', 'Active', 'Hit', 'Active', 'DOT', 'Crit', 'Crit', 'Glance', 'Active', 'Hit', 'Active', 'Crit', 'Active', 'Glance', 'Hit', 'Hit', 'Active', 'Crit', 'DOT', 'Glance', 'Crit', 'Active', 'Hit', 'Hit', 'DOT', 'Hit', 'Dodge', 'Hit', 'Hit', 'Glance', 'Active', 'Crit', 'DOT', 'Glance', 'Hit', 'Crit', 'Active', 'Hit', 'Crit', 'Crit', 'Hit', 'Hit', 'Active', 'Glance', 'Active', 'Glance', 'DOT', 'Crit', 'Crit', 'Hit', 'Glance', 'Active', 'Proc', 'Crit', 'Active', 'Hit', 'DOT', 'Crit', 'Crit', 'Hit', 'Glance', 'Active', 'Hit', 'Active', 'Glance', 'DOT', 'Hit', 'Crit', 'Glance', 'Active', 'Miss', 'Active', 'Glance', 'Active', 'Crit', 'Crit', 'Active', 'Crit', 'Glance', 'Hit', 'Active', 'Crit', 'Active', 'Crit', 'DOT', 'Hit', 'Crit', 'Crit', 'Active', 'Glance', 'Active', 'Miss', 'DOT', 'Crit', 'Hit', 'Glance', 'Active', 'Hit', 'Active', 'Crit', 'DOT', 'Hit', 'Crit', 'Hit', 'Crit', 'Crit', 'Active', 'Hit', 'Active', 'Hit', 'DOT', 'Crit', 'Hit', 'Glance', 'Active', 'Crit', 'Active', 'Crit', 'DOT', 'Hit', 'Hit', 'Glance', 'Crit', 'Active', 'Crit', 'Active', 'Crit', 'DOT', 'Crit', 'Hit', 'Hit', 'Hit', 'Hit', 'Active', 'Crit', 'Active', 'Crit', 'Crit', 'Crit', 'Hit', 'Active', 'Hit', 'Active', 'Glance', 'DOT', 'DOT', 'Crit', 'Crit', 'Hit', 'Hit', 'Active', 'Hit', 'Active', 'Miss', 'Crit', 'Crit', 'Crit', 'Crit', 'Active', 'Crit', 'DOT', 'Active', 'Hit', 'Crit', 'Hit', 'Hit', 'Active', 'Glance', 'Active', 'Miss', 'DOT', 'Hit', 'Hit', 'Hit', 'Active', 'Crit', 'Active', 'Crit', 'DOT', 'Hit', 'Hit', 'Miss', 'Dodge', 'Hit', 'Active', 'Hit', 'Active', 'Glance', 'DOT', 'Crit', 'Hit', 'Hit', 'Active', 'Hit', 'Active', 'Hit', 'DOT', 'Crit', 'Hit', 'Hit', 'Glance', 'Hit', 'Active', 'Glance', 'Active', 'Glance', 'DOT', 'Crit', 'Hit', 'Hit', 'Active', 'Hit', 'Active', 'DOT', 'Hit', 'Hit', 'Glance', 'Hit', 'Active', 'Glance', 'Active', 'Hit', 'DOT', 'Crit', 'Hit', 'Hit', 'Glance', 'Active', 'Hit', 'Active', 'Hit', 'DOT', 'Hit', 'Hit', 'Hit', 'Crit', 'Active', 'Miss', 'DOT', 'Crit', 'Crit', 'Miss', 'Active', 'Crit', 'Active', 'DOT', 'Crit', 'Crit', 'Hit', 'Hit', 'Hit', 'Active', 'Hit', 'Active', 'Crit', 'DOT', 'Crit', 'Crit', 'Hit', 'Active', 'Crit', 'Active', 'Glance', 'Crit', 'Crit', 'Crit', 'Glance', 'Active', 'Hit', 'Active', 'DOT', 'DOT', 'Hit', 'Crit', 'Dodge', 'Glance', 'Active', 'Hit', 'Active', 'Glance', 'Hit', 'Hit', 'Glance', 'Glance', 'Active', 'Proc', 'Crit', 'Active', 'Crit', 'Proc', 'DOT', 'Crit', 'Hit', 'Hit', 'Active', 'Hit', 'Active', 'Miss', 'DOT', 'Active', 'Hit', 'Hit', 'Hit', 'Hit', 'Active', 'DOT', 'Crit', 'Hit', 'Dodge', 'Active', 'Crit', 'Active', 'Glance', 'DOT', 'Hit', 'Dodge', 'Glance', 'Crit', 'Active', 'Glance', 'DOT', 'Crit', 'Hit', 'Hit', 'Hit', 'Active', 'Crit', 'Active', 'Hit', 'DOT', 'Crit', 'Crit', 'Dodge', 'Hit', 'Active', 'Proc', 'Hit', 'Active', 'DOT', 'Crit', 'Crit', 'Glance', 'Active', 'Hit', 'Active', 'Glance', 'DOT', 'Crit', 'Crit', 'Active', 'Active', 'Hit', 'Active', 'Crit', 'DOT', 'Hit', 'Crit', 'Active', 'Glance', 'DOT', 'Hit', 'Active', 'Crit', 'Crit', 'Active', 'Crit', 'Active', 'Crit', 'DOT', 'Crit', 'Dodge', 'Active', 'Hit', 'Active', 'DOT', 'Hit', 'Hit', 'Active', 'Hit', 'Active', 'Glance', 'DOT', 'Hit', 'Hit', 'Active', 'Crit', 'DOT', 'Active', 'Glance', 'Active', 'Hit', 'Hit', 'Crit', 'Active', 'Glance', 'Active', 'Miss', 'DOT', 'Hit', 'Hit', 'Active', 'DOT', 'Miss', 'Crit', 'Active', 'Glance', 'DOT', 'Crit', 'Crit', 'Active', 'Hit', 'Active', 'Glance', 'DOT', 'Hit', 'Crit', 'Active', 'Hit', 'Active', 'Crit', 'Crit', 'Active', 'Glance', 'Active', 'Crit', 'DOT', 'Hit', 'Crit', 'Active', 'Hit', 'Active', 'Crit', 'Proc', 'DOT', 'Hit', 'Crit', 'Active', 'Hit', 'Active', 'Crit', 'DOT', 'Hit', 'Crit', 'Active', 'Hit', 'Active', 'DOT', 'Active', 'Hit', 'Active', 'Crit', 'DOT', 'Miss', 'Crit', 'Active', 'Crit', 'Hit', 'Active', 'Dodge', 'DOT', 'Crit', 'Crit', 'Active', 'Glance', 'Active', 'Miss', 'DOT', 'Hit', 'Crit']
    
    rotation = data_rot
    rotation_time = data_time
    rotation_damage = data_dam
    rotation_status = data_sta
    all_data = pd.DataFrame()
    all_data2 = pd.DataFrame()
    ability_order = rotation
    timeline_order = rotation_time
    damage_order = rotation_damage
    status_order = rotation_status
    timeline_order_data = []
    timeline_order_data_end = []
    for i in timeline_order:
        if i < 1:
            i = .000001
        i = round(i, 6)
        iz = i + 0.5
        if type(i) == int or i.is_integer() == True:
            i += .000001
        if type(iz) == int or iz.is_integer() == True:
            iz += .000001
        i = timedelta(seconds=i)
        iz = timedelta(seconds=iz)
        total = "1970-01-01 " + str(i)
        total_end = "1970-01-01 " + str(iz)
        finished_converted_time = datetime.strptime(total, '%Y-%m-%d %H:%M:%S.%f')
        finished_converted_time_end = datetime.strptime(total_end, '%Y-%m-%d %H:%M:%S.%f')
        timeline_order_data.append(finished_converted_time)
        timeline_order_data_end.append(finished_converted_time_end)
    x = 0
    for i in ability_order:
        if damage_order[x] == 0:
            damage_scale = 0
        elif damage_order[x] < 150:
            damage_scale = "Under 150"
        elif damage_order[x] < 300:
            damage_scale = "Under 300"
        elif damage_order[x] < 500:
            damage_scale = "Under 500"
        elif damage_order[x] < 750:
            damage_scale = "Under 750"
        elif damage_order[x] < 1000:
            damage_scale = "Under 1000"
        elif damage_order[x] < 2000:
            damage_scale = "Under 2000"
        elif damage_order[x] >= 2000:
            damage_scale = "Over 2000"
        data = pd.DataFrame(dict(Ability=i, index=[0],Start=timeline_order_data[x], Finish=timeline_order_data_end[x], Damage=damage_order[x], Status=status_order[x]))
        all_data = pd.concat([all_data, data])
        data2 = pd.DataFrame(dict(Ability=i, index=[0],Start=timeline_order_data[x], Finish=timeline_order_data_end[x], Damage=damage_order[x], Status=status_order[x], DamageScale=damage_scale))
        all_data2 = pd.concat([all_data2, data2])
        x += 1
    unique_ability_df_table = []
    unique_miss_count_df_table = []
    unique_dodge_count_df_table = []
    unique_parry_count_df_table = []
    unique_glance_count_df_table = []
    unique_block_count_df_table = []
    unique_crit_count_df_table = []
    unique_hit_count_df_table = []
    unique_dot_count_df_table = []
    unique_active_count_df_table = []
    unique_proc_count_df_table = []
    unique_damage_per_cast_df_table = []
    unique_damage_df_table = []
    for i in np.unique(np.array(ability_order)):
        search_data = all_data.loc[all_data['Ability'] == i]
        miss_search = search_data.loc[search_data['Status'] == "Miss"]
        dodge_search = search_data.loc[search_data['Status'] == "Dodge"]
        parry_search = search_data.loc[search_data['Status'] == "Parry"]
        glance_search = search_data.loc[search_data['Status'] == "Glance"]
        block_search = search_data.loc[search_data['Status'] == "Block"]
        crit_search = search_data.loc[search_data['Status'] == "Crit"]
        hit_search = search_data.loc[search_data['Status'] == "Hit"]
        dot_search = search_data.loc[search_data['Status'] == "DOT"]
        active_search = search_data.loc[search_data['Status'] == "Active"]
        proc_search = search_data.loc[search_data['Status'] == "Proc"]
        if miss_search.empty:
            unique_miss_count_df_table.append(0)
        else:
            unique_miss_count_df_table.append(len(miss_search.index))

        if dodge_search.empty:
            unique_dodge_count_df_table.append(0)
        else:
            unique_dodge_count_df_table.append(len(dodge_search.index))
        if parry_search.empty:
            unique_parry_count_df_table.append(0)
        else:
            unique_parry_count_df_table.append(len(parry_search.index))
        if glance_search.empty:
            unique_glance_count_df_table.append(0)
        else:
            unique_glance_count_df_table.append(len(glance_search.index))
        if block_search.empty:
            unique_block_count_df_table.append(0)
        else:
            unique_block_count_df_table.append(len(block_search.index))
        if crit_search.empty:
            unique_crit_count_df_table.append(0)
        else:
            unique_crit_count_df_table.append(len(crit_search.index))
        if hit_search.empty:
            unique_hit_count_df_table.append(0)
        else:
            unique_hit_count_df_table.append(len(hit_search.index))
        if dot_search.empty:
            unique_dot_count_df_table.append(0)
        else:
            unique_dot_count_df_table.append(len(dot_search.index))
        if active_search.empty:
            unique_active_count_df_table.append(0)
        else:
            unique_active_count_df_table.append(len(active_search.index))
        if proc_search.empty:
            unique_proc_count_df_table.append(0)
        else:
            unique_proc_count_df_table.append(len(proc_search.index))
        unique_damage_per_cast_df_table.append(round((sum(search_data['Damage'])) / len(search_data['Damage']), 4))
        unique_damage_df_table.append(round(sum(search_data['Damage']), 4))
        unique_ability_df_table.append(i)



    colors = {'Main hand': '#45515E',
              'Off hand': '#576778',
              'Icy Touch': '#ACFDFC',
              'Obliterate': '#6AAEF7',
              'OH - Obliterate': '#55BDE0',
              'Frost Strike': '#2087f5',
              'OH - Frost Strike': '#12AADE',
              'Howling Blast': '#60FCFA',
              'Frost Fever': '#9AE3E2',
              'Blood Plague': '#E67F63',
              'Blood Strike': '#F2463D',
              'OH - Blood Strike': '#E6443A',
              'Blood Boil': '#FF3320',
              'Pestilence': '#D7F507',
              'Plague Strike': '#36C219',
              'OH - Plague Strike': '#2EA816',
              'Unbreakable Armor': '#F5A720',
              'Horn of Winter': '#CDD1C9',
              'Empowered Rune Weapon': '#7C9FC4',
              'Blood Tap': '#F54638',
              'Bloody Vengeance': '#DB7F8E',
              'Dancing Rune Weapon': '#FF3864',
              'Heart Strike': '#BC4B51',
              'Bone Shield': '#79B473',
              'Wandering Plague': '#98E02B',
              'Crypt Fever': '#8CB369',
              'Desolation': '#EFF7F6',
              'Scourge Strike': '#5C0029',
              'Blood-Caked Blades': '#91AEC1',
              'Necrosis': '#EAF2EF',
              'Death Coil': '#E2F89C',
              'Unholy Blight': '#0A8754',
              'Death and Decay': '#912F56',
              'Death Strike': '#A0A4B8',
              'Sudden Doom': '#D5E1A3',
              }
    colors_status = {'Hit': '#39CCCC',
              'Crit': '#FFDC00',
              'DOT': '#01FF70',
              'Proc': '#723BFF',
              'Active': '#381D7F',
              'Miss': '#FF4136',
              'Dodge': '#85144b',
              'Parry': '#FF283E',
              'Glance': '#80201B',
              'Block': '#40100D',
              }
    # fig = px.timeline(all_data,x_start="Start", x_end="Finish", y="Ability", color="Ability",opacity=1, color_discrete_map=colors, hover_data=["Status", "Damage"], template="plotly_dark")
    # fig.update_layout(xaxis=dict(
    #                       title='Timeline',
    #                       linecolor = "#BCCCDC",
    #                       showgrid=False,
    #                       tickformat = '%H:%M:%S',
    #                                   ),
    #                         yaxis=dict(
    #                         title=None,
    #                         linecolor="#BCCCDC",
    #                         showgrid=False,
    #                         ))
    # fig.update_layout(
    #     hoverlabel=dict(
    #         font_size=12,
    #         font_family="Rockwell",
    #     )
    # )
    all_data_no_zero = all_data.copy()
    all_data_no_zero = all_data_no_zero[all_data_no_zero.Damage != 0]
    fig3 = px.treemap(all_data, path=[px.Constant("All Damage"),'Ability', 'Status'], values='Damage',color="Ability",color_discrete_map=colors, template="plotly_dark")

    fig3.update_layout(
        hoverlabel=dict(
            font_size=12,
            font_family="Rockwell",
        )
    )
    fig3.update_layout(margin = dict(t=50, l=25, r=25, b=25))



    return html.Div(children=[
        # html.Div([
        #     dcc.Graph(
        #         id='graph1',
        #         figure=fig
        #     ),
        # ]),
        html.Div([
            dcc.Graph(
                id='graph3',
                figure=fig3
            ),
        ]),
    ])

server.layout = html.Div(children=[
all_dash_stuff()
])


#Angry Dread Data: Souled
serverad = dash.Dash(server=app, routes_pathname_prefix="/angrydread/",title="Angry Dread", update_title='Loading Angry Dread...', external_stylesheets=external_stylesheets)


def all_angrydread_stuff():
    dash_username = "Angry Dread"
    t_damage = 623452.4734856863
    fight_length = 80.75
    rotation = ['Main hand', 'Rune of Razoricce', 'Off hand', 'Icy Touch', 'Ghoul - Claw', 'Ghoul - Main hand', 'Frost Fever', 'OH - Plague Strike', 'Plague Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Hyperspeed Acceleration', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Darkmoon Card: Greatness', 'Grim Toll', 'Off hand', 'Blood Plague', 'Unbreakable Armor', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Blood Strike', 'Blood Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Shattering Throw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Ghoul - Main hand', 'Off hand', 'Frost Fever', 'Main hand', 'Rune of Razoricce', 'Ghoul - Main hand', 'Main hand', 'Off hand', 'Ghoul - Claw', 'Ghoul - Main hand', 'Blood Plague', 'Ghoul - Main hand', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Ghoul - Main hand', 'Main hand', 'Rune of Razoricce', 'Ghoul - Main hand', 'Frost Fever', 'Off hand', 'Ghoul - Main hand', 'Main hand', 'Rune of Razoricce', 'OH - Obliterate', 'Obliterate', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Blood Strike', 'Blood Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'Pestilence', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Empowered Rune Weapon', 'Main hand', 'Rune of Razoricce', 'OH - Obliterate', 'Obliterate', 'Ghoul - Claw', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Blood Strike', 'Blood Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Blood Strike', 'Blood Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Ghoul - Claw', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'OH - Obliterate', 'Obliterate', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'Blood Plague', 'Pestilence', 'Ghoul - Main hand', 'Main hand', 'Rune of Razoricce', 'Off hand', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Blood Strike', 'Blood Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Ghoul - Claw', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Blood Strike', 'Blood Strike', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Rune of the Fallen Crusader', 'Blood Plague', 'Pestilence', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Rune of Razoricce', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Rune of the Fallen Crusader', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Ghoul - Claw', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Rune of the Fallen Crusader', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Blood Strike', 'Blood Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Darkmoon Card: Greatness', 'Off hand', 'Frost Fever', 'OH - Blood Strike', 'Blood Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'Blood Tap', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Pestilence', 'Ghoul - Claw', 'Ghoul - Main hand', 'Main hand', 'Rune of Razoricce', 'Frost Fever', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Grim Toll', 'Main hand', 'Rune of Razoricce', 'Off hand', 'OH - Obliterate', 'Obliterate', 'Ghoul - Claw', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Rune of the Fallen Crusader', 'Frost Fever', 'OH - Blood Strike', 'Blood Strike', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'Horn of Winter', 'Hyperspeed Acceleration', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'Pestilence', 'Main hand', 'Rune of Razoricce', 'Blood Plague', 'Unbreakable Armor', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Rune of the Fallen Crusader', 'Blood Plague', 'OH - Blood Strike', 'Blood Strike', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'OH - Frost Strike', 'Frost Strike', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'Blood Plague', 'Off hand', 'Main hand', 'Rune of Razoricce', 'OH - Blood Strike', 'Blood Strike', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'OH - Frost Strike', 'Frost Strike', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'Pestilence', 'Main hand', 'Off hand', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Rune of Razorice', 'Off hand', 'Frost Fever', 'Main hand', 'Rune of Razoricce', 'Blood Plague', 'Horn of Winter', 'Main hand', 'Rune of Razoricce', 'Off hand']
    rotation_time = [0, 0, 0, 0, 0, 0, 0, 1.1929022082018927, 1.1929022082018927, 0.7425624752082507, 0.7425624752082507, 1.4851249504165014, 2.3858044164037855, 2.3858044164037855, 1.5442099782548775, 2.3858044164037855, 2.3858044164037855, 2.3858044164037855, 1.5442099782548775, 1.1929022082018927, 2.3858044164037855, 2.227687425624752, 2.227687425624752, 2.8353827846092816, 2.8310516268006087, 3.5787066246056782, 3.088419956509755, 3, 3.5787066246056782, 3.5787066246056782, 3.4430781435938114, 4.656057051956106, 3.9932419475669816, 4.656057051956106, 4.483048341429402, 4.192902208201893, 4.656057051956106, 4.656057051956106, 5.733407479306533, 4.050773502578341, 4.658468861562871, 5.733407479306533, 5.155432268333355, 5.733407479306533, 5.266164220547401, 5.8776767263490495, 6, 6.049424822769026, 6.133407479306531, 5.87385957953193, 6.943417377204698, 6.950467791671855, 6.48155493851646, 6.48155493851646, 7.192902208201893, 7.08925029750099, 7.837409931640369, 7.933407479306525, 8.02325885699466, 7.69694565648552, 8.73140248607604, 8.733407479306523, 8.30464101547005, 9, 9.096049922317466, 8.912336374454581, 9.625395040511712, 9.63340747930652, 10.033407479306518, 10.033407479306518, 9.520031733439112, 9.520031733439112, 10.127727092423642, 11.110757906656946, 10.519387594947384, 11.110757906656946, 10.168840987640271, 10.192902208201893, 11.110757906656946, 11.110757906656946, 10.735422451408173, 11.343117810392704, 12.188108334007374, 11.413380149383055, 12.188108334007374, 11.241632052963077, 12, 12.188108334007374, 12.188108334007374, 11.950813169377234, 13.265458761357802, 12.307372703818727, 13.265458761357802, 12.314423118285882, 13.192902208201893, 13.265458761357802, 12.693375644585485, 13.435938119793736, 13.297250895007751, 14.458360969559696, 13.50227694771271, 14.458360969559696, 14.287129086196776, 14.458360969559696, 14.458360969559696, 14.458360969559696, 14.178500595001987, 14.178500595001987, 15.651263177761589, 15.2770072773858, 15.651263177761589, 14.690130777139538, 15, 15.651263177761589, 15.651263177761589, 14.921063070210238, 15.861959539865136, 16.844165385963482, 16.266885468574824, 16.844165385963482, 15.877984606566367, 16.192902208201893, 16.844165385963482, 16.844165385963482, 16.802856009520035, 18.260457520794944, 17.442134107552054, 18.260457520794944, 17.288282973339044, 18, 18.260457520794944, 18.260457520794944, 17.743752479174933, 17.743752479174933, 18.68464894882983, 19.676749655626406, 18.617382746529284, 19.676749655626406, 18.69858134011172, 19.192902208201893, 19.676749655626406, 19.676749655626406, 19.62554541848473, 21.093041790457868, 19.792631385506514, 21.093041790457868, 20.108879706884395, 21, 21.093041790457868, 21.093041790457868, 20.56644188813963, 21.507338357794527, 22.50933392528933, 20.967880024483744, 22.50933392528933, 21.51917807365707, 22.192902208201893, 22.50933392528933, 22.50933392528933, 22.448234827449426, 22.448234827449426, 23.92562606012079, 22.143128663460974, 23.92562606012079, 22.929476440429745, 23.92562606012079, 23.92562606012079, 23.389131297104324, 24.330027766759223, 25.341918194952253, 23.318377302438204, 25.341918194952253, 24.33977480720242, 24, 25.192902208201893, 25.341918194952253, 25.27092423641412, 24.493625941415434, 26.758210329783715, 25.750073173975096, 26.758210329783715, 26.758210329783715, 26.21182070606902, 26.21182070606902, 27.152717175723918, 28.174502464615177, 25.668874580392664, 28.174502464615177, 27.16037154074777, 27, 28.174502464615177, 28.174502464615177, 28.093613645378817, 29.59079459944664, 26.844123219369894, 29.59079459944664, 28.570669907520447, 28.192902208201893, 29.59079459944664, 29.59079459944664, 29.034510115033715, 29.034510115033715, 29.975406584688614, 31.0070867342781, 28.019371858347125, 31.0070867342781, 29.980968274293122, 30, 31.0070867342781, 31.0070867342781, 30.916303054343512, 32.42337886910956, 29.194620497324355, 32.42337886910956, 31.391266641065798, 31.192902208201893, 32.42337886910956, 32.42337886910956, 31.85719952399841, 32.79809599365331, 33.83967100394102, 30.369869136301585, 33.83967100394102, 32.80156500783848, 33, 33.83967100394102, 33.83967100394102, 33.738992463308215, 33.738992463308215, 35.25596313877248, 31.545117775278815, 35.25596313877248, 34.211863374611156, 34.19290220820189, 35.25596313877248, 35.25596313877248, 34.67988893296312, 35.62078540261802, 36.67225527360394, 33.07294100594922, 36.67225527360394, 36.045251251415635, 36, 36.67225527360394, 36.67225527360394, 36.56168187227292, 38.088547408435396, 34.60076423661962, 38.088547408435396, 37.878639128220115, 38.088547408435396, 37.19290220820189, 38.088547408435396, 37.50257834192782, 37.50257834192782, 38.443474811582725, 36.12858746729002, 39.504839543266854, 39, 39.504839543266854, 39.504839543266854, 39.38437128123763, 40.92113167809831, 37.65641069796042, 40.92113167809831, 39.712027005024595, 40.92113167809831, 40.19290220820189, 40.92113167809831, 40.92113167809831, 40.32526775089253, 41.26616422054743, 42.33742381292977, 39.18423392863082, 42.33742381292977, 41.545414881829075, 42, 42.33742381292977, 42.33742381292977, 42.20706069020233, 42.20706069020233, 43.75371594776123, 40.71205715930122, 43.75371594776123, 43.378802758633555, 43.75371594776123, 43.19290220820189, 43.75371594776123, 43.75371594776123, 43.147957159857235, 44.08885362951214, 45.17000808259269, 42.23988038997162, 45.17000808259269, 45, 45.17000808259269, 45.17000808259269, 45.02975009916704, 46.586300217424146, 43.76770362064202, 46.586300217424146, 45.212190635438034, 46.19290220820189, 46.586300217424146, 46.586300217424146, 45.97064656882194, 45.97064656882194, 46.91154303847684, 48.002592352255604, 45.29552685131242, 48.002592352255604, 48.002592352255604, 47.045578512242514, 48, 48.002592352255604, 48.002592352255604, 47.852439508131745, 49.41888448708706, 46.82335008198282, 49.41888448708706, 48.878966389046994, 49.19290220820189, 49.41888448708706, 49.41888448708706, 49.41888448708706, 48.79333597778665, 49.73423244744155, 50.83517662191852, 48.351173312653216, 50.83517662191852, 50.712354265851474, 50.83517662191852, 50.67512891709645, 50.67512891709645, 49.878996543323616, 52.25146875674998, 51, 52.19290220820189, 52.25146875674998, 52.25146875674998, 51.61602538675135, 52.556921856406255, 53.66776089158144, 53.66776089158144, 51.406819773994016, 53.66776089158144, 52.54574214265595, 53.66776089158144, 53.66776089158144, 53.49781832606116, 53.49781832606116, 55.084053026412896, 52.934643004664416, 55.084053026412896, 54.37913001946043, 55.084053026412896, 54, 55.084053026412896, 55.084053026412896, 54.43871479571606, 55.37961126537096, 56.500345161244354, 54.462466235334816, 56.500345161244354, 56.21251789626491, 55.19290220820189, 56.500345161244354, 56.500345161244354, 56.32050773502586, 57.91663729607581, 55.990289466005216, 57.91663729607581, 57, 57.91663729607581, 57.91663729607581, 57.261404204680765, 57.261404204680765, 58.20230067433567, 59.33292943090727, 57.518112696675615, 59.33292943090727, 58.04590577306939, 58.19290220820189, 59.33292943090727, 60.74922156573873, 59.045935927346015, 60.74922156573873, 59.87929364987387, 60, 60.74922156573873, 60.74922156573873, 62.16551370057019, 60.573759158016415, 62.16551370057019, 61.71268152667835, 61.19290220820189, 62.16551370057019, 62.16551370057019, 63.581805835401646, 62.101582388686815, 63.581805835401646, 63.54606940348283, 63, 63.581805835401646, 63.629405619357215, 64.9980979702331, 64.1929022082019, 64.9980979702331, 65.15722885002762, 66.41439010506457, 65.37945728028731, 66, 66.68505208069803, 66.71439010506455, 67.21284515709179, 67.21439010506452, 67.1929022082019, 67.5143901050645, 67.5143901050645, 68.7072923132664, 67.97189372924376, 68.7072923132664, 68.7072923132664, 68.7072923132664, 69.90019452146828, 69.25873537778949, 69.90019452146828, 68.75705513534668, 69, 70.1929022082019, 70.30126511360156, 70.54557702633522, 70.60019452146824, 71.10019452146821, 71.10019452146821, 72.2930967296701, 71.83241867488096, 72.2930967296701, 71.84547509185644, 72, 72.2930967296701, 72.2930967296701, 73.48599893787198, 73.11926032342669, 73.48599893787198, 73.38968507011133, 73.1929022082019, 73.48599893787198, 73.48599893787198, 74.67890114607387, 74.40610197197242, 74.67890114607387, 74.67890114607387, 74.67890114607387, 75.87180335427576, 75.69294362051815, 75.87180335427576, 74.93389504836621, 75, 75.87180335427576, 76.97978526906388, 76.4781050266211, 76.1929022082019, 77.06470556247764, 77.06470556247764, 78.25760777067953, 78.02231500487598, 78, 78.26662691760961, 78.35760777067952, 79.1929022082019, 79.35760777067946, 79.55346856615535, 80.55050997888135, 79.56652498313086] 
    rotation_damage = [861.810187676137, 17.23620375352274, 605.008226375799, 1316.3806582280445, 239.3919785768231, 185.07941676977296, 445.56139828297773, 1126.1333473884963, 988.6501729074445, 232.43387262510922, 179.69994583252003, 138.93014029110233, 0, 19.77300345814889, 1292.8765393685155, 25.85753078737031, 0, 0, 673.4644790737351, 648.2297365538686, 0, 283.8673280158771, 266.6972195764136, 162.86768480019472, 1762.9891656176637, 35.25978331235328, 885.6981505965052, 507.7171518285777, 2339.862145004764, 5799.772995566088, 185.48683088318776, 115.99545991132176, 3703.0818932694265, 74.06163786538853, 0.0, 775.7744558481074, 5857.472315143968, 4635.234180710539, 0, 178.97856577226133, 170.90951908633363, 92.70468361421078, 3803.9618339352305, 76.07923667870462, 137.43971418868392, 891.3816390084272, 572.9926269561385, 1267.198142618909, 25.343962852378183, 119.43954516913371, 0.0, 2957.534426517409, 272.7649712360035, 260.46767028439336, 775.7744558481074, 199.03180446778148, 4052.077548329097, 81.04155096658195, 2736.002538665743, 118.19815420226817, 3825.228895168991, 76.50457790337983, 188.52772705584235, 572.9926269561385, 0.0, 191.39247544091666, 1308.8126713056583, 26.176253426113167, 2899.24343817421, 3671.5244620744725, 281.35921639122637, 268.67445359417917, 256.561569014882, 73.43048924148945, 3763.7907182714616, 75.27581436542924, 1435.0877088409243, 775.7744558481074, 2882.9261865273256, 9184.23901441661, 173.24906900211272, 330.87666042628615, 183.68478028833218, 3711.8045685889374, 74.23609137177876, 3058.552967377769, 572.9926269561385, 6381.815339569169, 6286.789708353725, 377.0554541116847, 125.73579416707449, 1283.087326299304, 25.661746525986082, 992.3914495480835, 775.7744558481074, 121.50071999999999, 111.4865851206596, 91.7433549143908, 3616.139076307024, 72.32278152614047, 1296.8900399063089, 0, 1113.5388521591349, 22.270777043182697, 6081.4035970209625, 2998.290198191807, 246.16745847278025, 202.5735068178777, 59.965803963836144, 3227.1968325093812, 64.54393665018763, 1199.0852046594355, 572.9926269561385, 2375.3397915765763, 7503.753257042632, 158.82152950102497, 0, 150.07506514085264, 3152.477844447651, 63.04955688895302, 722.1432828374012, 775.7744558481074, 5180.174737642043, 0, 108.76182279286115, 0.0, 3085.517710161803, 61.71035420323606, 2324.1823027642295, 572.9926269561385, 5084.823977637392, 4980.5402915257855, 234.75324127568052, 181.49310281160436, 91.20570614049882, 99.61080583051572, 894.5392016212148, 17.890784032424296, 0.0, 713.5633462085036, 0, 3468.681601693292, 166.55275833626263, 69.37363203386585, 1472.3427094319086, 29.446854188638174, 1027.2128240814168, 510.83687341053854, 1820.2185437420512, 1487.8109625685993, 168.09900410331016, 129.96118676982442, 29.756219251371988, 2721.0151630033774, 54.42030326006755, 683.3092255303022, 713.5633462085036, 2164.024035024653, 6900.122534728801, 416.1610035882212, 321.7435951042697, 138.00245069457603, 2490.6191063463875, 49.81238212692775, 985.9144392404032, 1879.614019635637, 6090.828163259419, 317.64305900204994, 159.62512650953335, 121.81656326518838, 2710.6309761427488, 54.21261952285498, 2010.0154717804846, 445.56139828297773, 648.2297365538686, 121.50071999999999, 149.54405489873977, 2460.0087592442856, 49.200175184885715, 0.0, 1654.4913354718808, 3439.38037862537, 212.7192390952532, 164.45811151030344, 127.14632938971874, 68.78760757250741, 784.6246141643699, 15.692492283287397, 1834.9625492903363, 445.56139828297773, 4657.575339195026, 1939.9257103698058, 146.45156336464473, 38.79851420739612, 866.7108590102172, 17.334217180204345, 2116.195113290903, 648.2297365538686, 1665.526773206103, 1401.5608438440315, 239.3919785768231, 185.07941676977296, 143.0891323739436, 28.03121687688063, 1373.9261037398458, 27.478522074796917, 1829.223109208692, 445.56139828297773, 1635.0170335879602, 1360.8811910198417, 143.35907183054965, 27.217623820396835, 1251.4093203878344, 25.02818640775669, 644.5198890068224, 648.2297365538686, 4969.151980661825, 6316.145291146683, 297.54186403043207, 230.03642388824377, 126.32290582293366, 2482.9665195708617, 49.659330391417235, 2124.8042734133696, 445.56139828297773, 4689.187041906379, 2453.26704792132, 225.47576667339533, 0, 49.065340958426404, 1217.4815957672777, 24.349631915345554, 655.0869615709335, 648.2297365538686, 4587.725363842781, 4717.882461247459, 0, 0.0, 94.35764922494918, 1342.825689504335, 26.8565137900867, 1935.4027507191097, 445.56139828297773, 4138.555775663153, 3486.6033968825586, 105.24411367282801, 69.73206793765118, 1338.113505529258, 26.76227011058516, 964.7096113525554, 0, 648.2297365538686, 226.0925898, 255.6275591308222, 197.6315156233631, 99.31574070203926, 2992.477380186732, 59.849547603734635, 494.5180046286483, 4297.894887973291, 3475.8451765279497, 101.72640455279489, 69.51690353055899, 2759.0734835332005, 55.18146967066401, 1039.153297153404, 0, 697.2299437948449, 1773.9181662035285, 3611.074728809895, 165.77963545273886, 128.16802979074012, 72.2214945761979, 1476.011661859357, 29.520233237187142, 633.6407908308388, 494.5180046286483, 5070.010029521999, 2885.822803691198, 228.95481964925227, 177.01021036389358, 57.716456073823956, 2730.3762831249796, 54.6075256624996, 1090.0448840842396, 0, 697.2299437948449, 4966.599556648365, 6531.3333026014625, 97.20363568418085, 75.15035510914748, 130.62666605202926, 1387.4226031279027, 27.748452062558055, 494.5180046286483, 1805.0770492178017, 3714.106768643759, 99.21375518134266, 74.28213537287519, 1298.8335443964486, 25.97667088792897, 2230.0094349359383, 697.2299437948449, 4930.2962956712945, 2024.5635296281703, 226.63545099868097, 175.21705338480928, 88.05180381101084, 40.4912705925634, 3057.5243677786993, 61.150487355573986, 0, 2010.4758518130475, 494.5180046286483, 4852.685211946577, 1982.8371405288603, 150.31717778226354, 39.65674281057721, 1492.5280013258307, 29.850560026516614, 718.8780798325118, 759.4410534344488, 0, 4787.374792779902, 3845.0951296631342, 138.72033452940707, 107.24786503475656, 76.90190259326269, 1047.9413582903173, 20.958827165806348, 2268.0693019573446, 118.1257, 469.50648255136105, 362.9862056232087, 3198.1887517530004, 63.96377503506001, 556.6737581742483, 759.4410534344488, 5708.189192214337, 2944.164612856198, 330.0130251384302, 510.28124319084804, 58.88329225712396, 0, 3119.749737303863, 62.394994746077266, 2180.542840712271, 6175.656793313663, 8550.594660611758, 265.5468125198169, 249.4848458307018, 171.01189321223515, 1233.2793713827673, 24.665587427655346, 3000.3145842769227, 0, 556.6737581742483, 6239.367065980499, 2497.9733814387146, 186.42634449837033, 113.84755777520805, 49.95946762877429, 1801.1504429101765, 36.02300885820353, 2995.0835768117977, 759.4410534344488, 6557.465008604949, 5288.856776573718, 203.33758957165662, 105.77713553147436, 3786.5293626841085, 75.73058725368217, 556.6737581742483, 6688.931825331273, 5464.145865542149, 286.68586886142475, 269.34527707575387, 506.107109995586, 109.28291731084299, 3514.5169744975956, 70.29033948995192, 961.2501796703339, 759.4410534344488, 0, 0, 1916.8224196978395, 38.33644839395679, 2651.580753268572, 556.6737581742483, 6526.789418035474, 2116.1112859466743, 42.32222571893349, 1280.1780590011317, 25.603561180022634, 0.0, 759.4410534344488, 3109.6610359802044, 3829.0020121949537, 76.58004024389908, 1270.500552032263, 25.41001104064526, 0.0, 556.6737581742483, 133.31329, 3564.4437025095, 71.28887405019, 697.2299437948449, 0, 1493.9179609646508, 29.878359219293017, 2099.4371730785324, 494.5180046286483, 1615.216449073397, 32.30432898146794, 2440.513863448903, 0, 773.99902581455, 2108.2116896715856, 2087.7009215547746, 41.754018431095496, 3215.7555507209104, 64.3151110144182, 5530.968338547114, 4457.710887183102, 89.15421774366204, 947.589177798779, 18.95178355597558, 1215.6533023826175, 571.2187767187362, 773.99902581455, 2218.11056028519, 3079.92213545533, 61.59844270910661, 2132.8004546765364, 5258.805135072209, 105.17610270144418, 1004.559482057464, 20.09118964114928, 2312.81132163232, 571.2187767187362, 6257.281068454813, 3421.8420342532017, 68.43684068506404, 3292.281418476166, 65.84562836952333, 2209.501400162724, 773.99902581455, 6079.314166845946, 8211.21409008133, 164.2242818016266, 1632.1803113836754, 32.64360622767351, 2256.402630500988, 4544.257800643547, 90.88515601287094, 1627.4681274085983, 32.54936254817197, 2420.4258231631484, 571.2187767187362, 131.62578, 0.0, 768.1216255453394, 773.99902581455, 5512.9377315761885, 4433.670077888533, 88.67340155777067, 0.0, 571.2187767187362, 1049.8906918977082, 20.997813837954165, 773.99902581455, 0, 1541.7063790621905, 30.834127581243813, 708.394693661234] 
    rotation_status = ['Glance', 'Active', 'Glance', 'Hit', 'Hit', 'Hit', 'DOT', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Active', 'Active', 'Hit', 'Active', 'Proc', 'Proc', 'Glance', 'DOT', 'Active', 'Hit', 'Hit', 'Glance', 'Hit', 'Active', 'Glance', 'DOT', 'Hit', 'Crit', 'Hit', 'Active', 'Crit', 'Active', 'Miss', 'DOT', 'Crit', 'Crit', 'Active', 'Hit', 'Hit', 'Active', 'Crit', 'Active', 'Glance', 'Glance', 'DOT', 'Glance', 'Active', 'Glance', 'Dodge', 'Crit', 'Hit', 'Hit', 'DOT', 'Hit', 'Crit', 'Active', 'Crit', 'Glance', 'Crit', 'Active', 'Hit', 'DOT', 'Miss', 'Hit', 'Glance', 'Active', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Active', 'Crit', 'Active', 'Hit', 'DOT', 'Hit', 'Crit', 'Hit', 'Crit', 'Active', 'Crit', 'Active', 'Crit', 'DOT', 'Crit', 'Crit', 'Crit', 'Active', 'Glance', 'Active', 'Glance', 'DOT', 'Hit', 'Glance', 'Hit', 'Crit', 'Active', 'Hit', 'Active', 'Glance', 'Active', 'Crit', 'Hit', 'Hit', 'Hit', 'Active', 'Crit', 'Active', 'Hit', 'DOT', 'Hit', 'Crit', 'Hit', 'Dodge', 'Active', 'Crit', 'Active', 'Glance', 'DOT', 'Crit', 'Dodge', 'Glance', 'Active', 'Crit', 'Active', 'Crit', 'DOT', 'Crit', 'Crit', 'Hit', 'Hit', 'Glance', 'Active', 'Glance', 'Active', 'Miss', 'DOT', 'Dodge', 'Crit', 'Hit', 'Active', 'Hit', 'Active', 'Hit', 'DOT', 'Hit', 'Hit', 'Hit', 'Hit', 'Active', 'Crit', 'Active', 'Glance', 'DOT', 'Hit', 'Crit', 'Crit', 'Hit', 'Active', 'Crit', 'Active', 'Hit', 'Hit', 'Crit', 'Crit', 'Glance', 'Active', 'Crit', 'Active', 'Crit', 'DOT', 'DOT', 'Hit', 'Hit', 'Crit', 'Active', 'Miss', 'Hit', 'Crit', 'Hit', 'Hit', 'Hit', 'Active', 'Glance', 'Active', 'Crit', 'DOT', 'Crit', 'Hit', 'Hit', 'Active', 'Glance', 'Active', 'Crit', 'DOT', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Active', 'Hit', 'Active', 'Crit', 'DOT', 'Hit', 'Hit', 'Hit', 'Active', 'Hit', 'Active', 'Glance', 'DOT', 'Crit', 'Crit', 'Crit', 'Hit', 'Active', 'Crit', 'Active', 'Crit', 'DOT', 'Crit', 'Hit', 'Hit', 'Dodge', 'Active', 'Hit', 'Active', 'Glance', 'DOT', 'Crit', 'Crit', 'Dodge', 'Glance', 'Active', 'Hit', 'Active', 'Crit', 'DOT', 'Crit', 'Crit', 'Glance', 'Active', 'Hit', 'Active', 'Hit', 'Proc', 'DOT', 'Crit', 'Hit', 'Hit', 'Glance', 'Crit', 'Active', 'DOT', 'Crit', 'Crit', 'Glance', 'Active', 'Crit', 'Active', 'Hit', 'Proc', 'DOT', 'Hit', 'Crit', 'Hit', 'Hit', 'Active', 'Hit', 'Active', 'Glance', 'DOT', 'Crit', 'Hit', 'Hit', 'Hit', 'Active', 'Crit', 'Active', 'Hit', 'Proc', 'DOT', 'Crit', 'Crit', 'Glance', 'Hit', 'Active', 'Hit', 'Active', 'DOT', 'Hit', 'Crit', 'Glance', 'Active', 'Hit', 'Active', 'Crit', 'DOT', 'Crit', 'Hit', 'Hit', 'Hit', 'Glance', 'Active', 'Crit', 'Active', 'Proc', 'Crit', 'DOT', 'Crit', 'Hit', 'Hit', 'Active', 'Hit', 'Active', 'Glance', 'DOT', 'Active', 'Crit', 'Crit', 'Hit', 'Hit', 'Active', 'Glance', 'Active', 'Crit', 'Hit', 'Crit', 'Hit', 'Crit', 'Active', 'DOT', 'DOT', 'Crit', 'Hit', 'Crit', 'Crit', 'Active', 'Proc', 'Crit', 'Active', 'Crit', 'Crit', 'Crit', 'Hit', 'Hit', 'Active', 'Glance', 'Active', 'Crit', 'Proc', 'DOT', 'Crit', 'Hit', 'Hit', 'Glance', 'Active', 'Hit', 'Active', 'Crit', 'DOT', 'Crit', 'Crit', 'Hit', 'Active', 'Crit', 'Active', 'DOT', 'Crit', 'Crit', 'Hit', 'Hit', 'Crit', 'Active', 'Crit', 'Active', 'Glance', 'DOT', 'Active', 'Active', 'Hit', 'Active', 'Crit', 'DOT', 'Crit', 'Hit', 'Active', 'Glance', 'Active', 'Miss', 'DOT', 'Hit', 'Hit', 'Active', 'Glance', 'Active', 'Miss', 'DOT', 'Hit', 'Crit', 'Active', 'DOT', 'Active', 'Hit', 'Active', 'Crit', 'DOT', 'Hit', 'Active', 'Crit', 'Proc', 'DOT', 'Hit', 'Hit', 'Active', 'Crit', 'Active', 'Crit', 'Crit', 'Active', 'Glance', 'Active', 'Hit', 'DOT', 'DOT', 'Crit', 'Crit', 'Active', 'Hit', 'Crit', 'Active', 'Glance', 'Active', 'Crit', 'DOT', 'Crit', 'Hit', 'Active', 'Crit', 'Active', 'Crit', 'DOT', 'Crit', 'Crit', 'Active', 'Hit', 'Active', 'Hit', 'Crit', 'Active', 'Hit', 'Active', 'Crit', 'DOT', 'Hit', 'Dodge', 'Glance', 'DOT', 'Crit', 'Crit', 'Active', 'Miss', 'DOT', 'Glance', 'Active', 'DOT', 'Active', 'Hit', 'Active', 'Glance'] 
    rune_0_tracker = [0, 0, 0, 0, 0, 0, 0, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 20.765458761357802, 20.765458761357802, 0, 0, 0, 0, 0, 17.844165385963482, 17.844165385963482, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 35.67450246461517, 35.67450246461517, 35.67450246461517, 35.67450246461517, 35.67450246461517, 35.67450246461517, 35.67450246461517, 35.67450246461517, 35.67450246461517, 35.67450246461517, 35.67450246461517, 35.67450246461517, 35.67450246461517, 35.67450246461517, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 55.502592352255604, 55.502592352255604, 10000, 10000, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 78.60019452146821, 78.60019452146821, 78.60019452146821, 78.60019452146821, 78.60019452146821, 78.60019452146821, 78.60019452146821, 78.60019452146821, 78.60019452146821, 78.60019452146821, 78.60019452146821, 78.60019452146821, 78.60019452146821, 78.60019452146821, 78.60019452146821, 78.60019452146821, 78.60019452146821, 78.60019452146821, 78.60019452146821, 78.60019452146821, 78.60019452146821, 78.60019452146821, 78.60019452146821, 78.60019452146821, 78.60019452146821, 78.60019452146821]
    rune_1_tracker = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19.688108334007374, 19.688108334007374, 19.688108334007374, 19.688108334007374, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 42.75596313877248, 42.75596313877248, 42.75596313877248, 42.75596313877248, 42.75596313877248, 42.75596313877248, 42.75596313877248, 42.75596313877248, 42.75596313877248, 42.75596313877248, 42.75596313877248, 42.75596313877248, 42.75596313877248, 42.75596313877248, 42.75596313877248, 42.75596313877248, 54.086300217424146, 54.086300217424146, 54.086300217424146, 54.086300217424146, 54.086300217424146, 54.086300217424146, 54.086300217424146, 54.086300217424146, 54.086300217424146, 54.086300217424146, 54.086300217424146, 54.086300217424146, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 75.0143901050645, 75.0143901050645, 75.0143901050645, 75.0143901050645, 75.0143901050645, 75.0143901050645, 75.0143901050645, 75.0143901050645, 75.0143901050645, 75.0143901050645, 75.0143901050645, 75.0143901050645, 75.0143901050645, 75.0143901050645, 75.0143901050645, 75.0143901050645, 75.0143901050645, 75.0143901050645, 75.0143901050645, 75.0143901050645, 75.0143901050645, 75.0143901050645, 75.0143901050645, 75.0143901050645, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
    rune_2_tracker = [0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 0, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969]
    rune_3_tracker = [0, 0, 0, 0, 0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 0, 0, 0, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159]
    rune_4_tracker = [0, 0, 0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 0, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969]
    rune_5_tracker = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 0, 0, 0, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159]
    rune_6_tracker = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 24.344165385963482, 24.344165385963482, 27.844165385963482, 27.844165385963482, 27.844165385963482, 27.844165385963482, 27.844165385963482, 27.844165385963482, 27.844165385963482, 27.844165385963482, 27.844165385963482, 27.844165385963482, 27.844165385963482, 27.844165385963482, 27.844165385963482, 27.844165385963482, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 45.67450246461517, 45.67450246461517, 45.67450246461517, 45.67450246461517, 45.67450246461517, 45.67450246461517, 45.67450246461517, 45.67450246461517, 45.67450246461517, 45.67450246461517, 45.67450246461517, 45.67450246461517, 45.67450246461517, 45.67450246461517, 10000, 10000, 49.41888448708706, 49.41888448708706, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
    rune_7_tracker = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 32.84191819495226, 32.84191819495226, 32.84191819495226, 32.84191819495226, 32.84191819495226, 32.84191819495226, 32.84191819495226, 32.84191819495226, 32.84191819495226, 32.84191819495226, 32.84191819495226, 32.84191819495226, 32.84191819495226, 32.84191819495226, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 85.0143901050645, 85.0143901050645, 85.0143901050645, 85.0143901050645, 85.0143901050645, 85.0143901050645, 85.0143901050645, 85.0143901050645, 85.0143901050645, 85.0143901050645, 85.0143901050645, 85.0143901050645, 85.0143901050645, 85.0143901050645, 85.0143901050645, 85.0143901050645, 85.0143901050645, 85.0143901050645]
    rune_8_tracker = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
    rune_9_tracker = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
    rune_10_tracker = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
    rune_11_tracker = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000] 
    rune_time_tracker = [0, 0.0, 1.1929022082018927, 1.1929022082018927, 2.3858044164037855, 2.3858044164037855, 3.5787066246056782, 3.5787066246056787, 4.656057051956106, 4.656057051956106, 5.733407479306533, 5.8334074793065325, 5.933407479306532, 6.033407479306532, 6.133407479306531, 6.233407479306531, 6.333407479306531, 6.43340747930653, 6.53340747930653, 6.63340747930653, 6.733407479306529, 6.833407479306529, 6.933407479306529, 7.033407479306528, 7.133407479306528, 7.2334074793065275, 7.333407479306527, 7.433407479306527, 7.533407479306526, 7.633407479306526, 7.733407479306526, 7.833407479306525, 7.933407479306525, 8.033407479306526, 8.133407479306525, 8.233407479306525, 8.333407479306524, 8.433407479306524, 8.533407479306524, 8.633407479306523, 8.733407479306523, 8.833407479306523, 8.933407479306522, 9.033407479306522, 9.133407479306522, 9.233407479306521, 9.333407479306521, 9.43340747930652, 9.53340747930652, 9.63340747930652, 9.73340747930652, 9.83340747930652, 9.933407479306519, 10.033407479306518, 10.033407479306518, 11.110757906656946, 11.110757906656946, 12.188108334007374, 12.188108334007374, 13.265458761357802, 13.265458761357802, 14.458360969559696, 14.458360969559696, 14.458360969559696, 15.651263177761589, 15.651263177761589, 16.844165385963482, 16.844165385963482, 18.260457520794944, 18.260457520794944, 19.676749655626406, 19.676749655626406, 21.093041790457868, 21.093041790457868, 22.50933392528933, 22.50933392528933, 23.92562606012079, 23.92562606012079, 25.341918194952253, 25.341918194952253, 26.758210329783715, 26.758210329783715, 28.174502464615177, 28.174502464615177, 29.59079459944664, 29.59079459944664, 31.0070867342781, 31.0070867342781, 32.42337886910956, 32.42337886910956, 33.83967100394102, 33.83967100394102, 35.25596313877248, 35.25596313877248, 36.67225527360394, 36.67225527360394, 38.088547408435396, 38.088547408435396, 39.504839543266854, 39.504839543266854, 40.92113167809831, 40.92113167809831, 42.33742381292977, 42.33742381292977, 43.75371594776123, 43.75371594776123, 45.17000808259269, 45.17000808259269, 46.586300217424146, 46.586300217424146, 48.002592352255604, 48.002592352255604, 49.41888448708706, 49.41888448708706, 50.83517662191852, 50.83517662191852, 52.25146875674998, 52.25146875674998, 53.66776089158144, 53.66776089158144, 55.084053026412896, 55.084053026412896, 56.500345161244354, 56.500345161244354, 57.91663729607581, 57.91663729607581, 59.33292943090727, 59.33292943090727, 60.74922156573873, 60.74922156573873, 62.16551370057019, 62.16551370057019, 63.581805835401646, 63.581805835401646, 64.9980979702331, 64.9980979702331, 66.41439010506457, 66.51439010506456, 66.61439010506456, 66.71439010506455, 66.81439010506455, 66.91439010506454, 67.01439010506454, 67.11439010506453, 67.21439010506452, 67.31439010506452, 67.41439010506451, 67.5143901050645, 67.5143901050645, 68.7072923132664, 68.7072923132664, 69.90019452146828, 70.00019452146827, 70.10019452146827, 70.20019452146826, 70.30019452146826, 70.40019452146825, 70.50019452146825, 70.60019452146824, 70.70019452146823, 70.80019452146823, 70.90019452146822, 71.00019452146822, 71.10019452146821, 71.10019452146821, 72.2930967296701, 72.2930967296701, 73.48599893787198, 73.48599893787198, 74.67890114607387, 74.67890114607387, 75.87180335427576, 75.87180335427576, 77.06470556247764, 77.06470556247764, 78.25760777067953, 78.35760777067952, 78.45760777067952, 78.55760777067951, 78.6576077706795, 78.7576077706795, 78.8576077706795, 78.95760777067949, 79.05760777067948, 79.15760777067948, 79.25760777067947, 79.35760777067946, 79.35760777067946, 80.55050997888135, 80.65050997888135]
    runic_power_tracker = [10, 25, 25, 35, 35, 25, 25, 35, 35, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 28, 28, 53, 53, 63, 63, 73, 73, 98, 123, 123, 130, 130, 130, 130, 130, 130, 98, 98, 66, 66, 91, 91, 116, 116, 126, 126, 94, 94, 104, 104, 72, 72, 40, 40, 65, 65, 90, 90, 100, 100, 68, 68, 78, 78, 46, 46, 14, 14, 39, 39, 64, 64, 32, 32, 42, 42, 52, 52, 20, 20, 30, 30, 55, 55, 80, 80, 90, 90, 58, 58, 26, 26, 36, 36, 4, 4, 29, 29, 39, 39, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 39, 39, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 17, 17, 42, 42, 67, 67, 35, 35, 45, 45, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 23, 23, 23]
    number_of_targets_in_fight = 1
    gear_currently_worn = "Spiked Titansteel Helm*&*Pendant of the Dragonsworn*&*Valorous Scourgeborne Shoulderplates*&*Aged Winter Cloak*&*Valorous Scourgeborne Battleplate*&*Wristbands of the Sentinel Huntress*&*Valorous Scourgeborne Gauntlets*&*Girdle of Razuvious*&*Valorous Scourgeborne Legplates*&*Melancholy Sabatons*&*Ruthlessness*&*Greatring of Collision*&*Darkmoon Card: Greatness*&*Grim Toll*&*Sigil of Awareness*&*Angry Dread*&*Angry Dread"
    current_gear_split_list = gear_currently_worn.replace("*&*",", ")
    current_gear_split_list = current_gear_split_list.split(", ")
    extra_sim_stats_info = "406.156*^*12.39*^*33.86*^*946.0*^*1575.288*^*1243.1760000000002*^*20372.760000000002*^*14623.0*^*626.076*^*5520.728044444444*^*88.0*^*44.0*^*17*^*141.5*^*5.91*^*149.0*^*False"
    extra_stats_split_list = extra_sim_stats_info.replace("*^*",", ")
    extra_stats_split_list = extra_stats_split_list.split(", ")
    extra_future_stats_info = 6004*[8274, 7709, 8177, 7251, 8182, 8747, 8125, 8599, 7765, 7833, 7627, 8207, 7692, 7067, 8150, 7843, 7555, 7751, 7664, 7578, 7953, 7590, 7578, 7242, 8197, 8158, 7700, 7969, 7735, 8297, 7851, 7123, 8198, 7984, 8100, 7574, 7603, 7490, 7449, 7966, 7973, 7821, 8209, 7277, 7453, 7925, 8032, 7829, 7743, 7679, 7470, 8390, 7733, 7752, 7895, 8075, 7731, 7874, 7644, 7476, 7912, 8031, 7938, 8162, 7561, 8027, 7867, 7867, 7952, 8092, 7587, 7614, 7621, 7415, 7799, 8082, 7578, 7672, 7575, 7606, 8011, 8423, 8342, 8334, 7761, 7718, 8156, 7787, 7157, 8102, 7683, 8028, 7530, 7638, 7297, 7815, 7912, 7780, 7818, 7431, 7738, 8042, 7551, 7594, 7313, 7631, 8161, 8104, 8297, 7484, 8501, 7751, 7634, 8077, 7690, 7409, 7971, 7889, 7917, 7493, 8515, 7890, 7567, 7634, 7625, 7513, 7337, 7573, 7697, 8237, 8070, 8286, 7665, 7853, 7925, 7933, 7963, 7788, 7893, 7282, 7280, 7825, 7676, 7768, 7184, 7764, 7535, 7436, 7976, 7922, 7781, 7779, 7812, 7839, 7922, 7632, 7713, 7968, 7756, 7502, 7610, 7701, 7600, 7659, 7890, 8035, 7316, 8494, 7559, 7875, 7825, 7523, 8039, 7660, 8043, 7999, 7854, 8056, 7282, 7618, 7822, 8062, 7842, 7585, 7417, 8010, 8217, 8033, 7413, 7879, 7536, 7878, 7678, 7546, 7675, 7753, 8293, 7774, 8132, 8203, 7891, 8065, 7680, 7955, 8209, 7446, 7786, 8279, 7799, 7621, 7866, 7762, 8156, 7651, 7549, 8197, 8108, 8210, 7243, 7432, 7897, 7451, 7742, 8222, 7678, 8331, 7821, 8136, 8247, 7434, 7726, 7769, 8046, 7440, 7488, 7172, 7615, 7258, 7850, 8131, 7451, 8323, 7791, 7494, 7790, 7911, 7293, 8188, 7681, 7205, 7812, 7505, 8059, 7711, 8028, 7910, 7836, 8049, 7399, 7864, 7871, 7988, 8227, 8186, 8692, 7772, 7776, 7884, 7679, 7683, 7264, 7897, 7617, 8188, 8310, 8141, 7676, 7444, 7716, 7660, 8229, 8125, 8145, 7437, 8276, 7709, 7830, 7891, 8354, 7701, 7285, 7780, 7696, 7615, 8278, 7321, 7916, 8270, 7323, 8057, 7622, 7832, 7507, 7575, 7679, 7344, 7334, 7356, 7997, 7408, 7844, 7242, 8595, 8273, 7586, 7626, 7679, 7751, 7757, 7454, 7978, 7841, 7533, 8093, 7569, 7802, 7478, 8122, 7646, 7883, 7701, 7995, 7612, 7890, 7657, 7834, 7779, 7774, 7215, 7372, 7937, 8190, 7570, 7694, 8043, 7655, 7880, 7755, 8031, 7544, 7579, 7166, 7582, 7528, 7328, 7323, 7461, 7539, 7371, 8121, 7704, 7679, 8249, 7358, 8034, 7651, 7524, 7034, 8077, 7250, 8045, 7710, 7832, 8069, 7441, 7340, 7490, 7927, 7436, 8119, 8020, 7903, 8034, 7566, 7187, 7157, 8137, 8019, 7641, 7911, 7848, 7924, 7714, 7962, 7774, 8104, 7532, 7463, 8024, 8369, 7804, 8074, 7672, 7497, 7853, 7541, 7854, 8043, 7949, 7486, 7744, 7779, 7302, 8335, 7582, 8226, 7791, 7888, 7897, 7499, 8363, 7739, 7726, 7199, 7512, 7766, 7796, 7736, 8253, 7827, 8191, 8448, 7267, 8188, 7272, 7565, 7587, 7515, 7781, 7392, 7861, 7558, 7974, 8111, 7302, 7893, 7721, 7809, 7398, 8142, 7582, 8122, 7144, 7502, 8443, 7943, 7767, 8166, 7687, 7325, 7567, 7656, 7774, 7986, 7997, 7841, 7765, 7898, 7744, 7740, 7658, 7545, 7516, 7767, 7328, 8131, 7685, 7791, 7697, 8142, 7884, 7714, 7155, 7761, 8250, 7651, 8630, 8110, 8215, 7719, 7766, 8132, 7780, 8201, 7639, 7654, 7875, 8243, 7430, 7758, 8408, 7340, 7727, 7181, 7729, 7676, 7630, 7474, 7654, 7626, 7613, 7946, 8104, 7468, 8143, 7578, 7786, 7626, 7764, 7530, 7636, 7660, 7404, 7114, 7659, 7499, 7170, 7430, 7411, 8027, 7772, 8117, 7921, 7690, 8823, 7515, 8000, 8283, 7743, 7788, 7380, 7207, 7662, 7602, 8200, 8343, 7246, 8072, 8169, 7880, 8078, 7573, 7617, 7704, 7941, 7953, 7660, 7701, 7227, 7960, 7954, 7547, 7761, 7999, 7940, 7434, 8252, 7737, 8057, 8188, 8324, 7320, 8044, 7516, 8189, 7402, 7567, 8236, 7582, 7628, 7602, 7120, 7946, 7503, 7549, 7639, 7915, 7967, 7825, 7324, 7643, 8181, 7117, 7949, 7491, 7448, 7650, 8026, 8136, 7481, 8147, 8431, 8385, 7316, 7721, 8166, 7783, 7311, 8228, 7099, 7700, 7670, 7858, 7185, 8054, 7354, 8147, 6888, 7730, 7580, 7810, 7770, 8050, 7148, 7854, 7696, 7456, 7652, 7640, 7804, 7697, 7900, 7310, 8100, 8459, 7359, 8310, 7242, 7925, 8051, 7571, 7777, 7755, 8161, 7834, 8055, 7821, 7947, 7961, 7333, 8062, 7650, 7900, 7963, 7778, 8261, 7547, 7792, 7539, 7578, 8022, 7634, 8493, 8270, 7159, 7947, 7630, 8045, 7949, 8332, 7511, 7495, 7759, 7709, 7509, 7530, 7408, 7959, 7505, 7796, 7398, 8103, 7481, 7859, 7810, 7703, 8046, 8106, 7312, 7832, 7538, 7956, 7733, 8014, 7951, 8156, 7980, 8600, 7320, 7520, 7594, 7929, 7677, 7660, 7566, 7621, 8073, 7836, 7533, 7939, 7775, 7957, 7838, 8117, 7593, 8363, 7442, 7387, 7696, 8444, 8435, 7690, 7562, 7750, 7341, 7618, 7661, 8137, 7739, 7538, 8244, 7897, 7348, 7950, 8053, 8215, 7561, 7809, 7614, 7625, 7759, 7362, 7312, 8026, 7631, 7779, 7894, 7981, 8041, 7858, 7560, 7687, 7777, 7808, 8245, 8041, 7748, 8129, 8324, 8163, 7933, 7723, 7875, 7688, 7591, 8274, 7715, 8174, 7794, 7658, 7573, 7618, 7941, 8042, 7505, 8209, 7945, 7778, 7604, 8023, 8572, 7574, 7398, 8002, 8265, 7559, 7820, 8367, 8025, 8252, 7706, 7510, 7850, 7457, 7856, 7567, 7957, 7304, 7810, 8074, 8261, 7530, 7527, 8326, 7355, 7818, 7916, 8069, 8227, 7245, 7543, 7958, 7940, 8540, 7513, 7198, 7659, 8149, 7445, 7229, 7899, 7298, 7625, 8398, 7363, 8093, 7828, 7828, 7563, 7647, 8267, 7937, 7902, 8338, 8384, 7798, 8092, 8143, 7974, 7811, 7817, 7759, 7474, 8255, 8054, 7706, 7960, 7551, 7782, 8001, 7599, 7997, 8024, 7578, 7828, 7628, 7526, 7556, 7942, 7713, 7361, 7531, 8211, 7425, 8115, 7725, 7434, 7639, 7800, 7922, 8224, 8448, 7926, 7904, 7795, 8019, 7845, 8148, 7743, 7660, 7922, 8261, 7642, 8178, 7841, 8051, 7904, 7684, 7519, 7901, 7714, 7766, 7940, 7553, 7783, 7915, 7865, 7794, 8354, 8507, 7588, 7574, 7538, 7746, 7699, 8125, 8098, 7951, 8365, 8026, 8101, 7490, 7995, 7676, 7234, 7966, 8028, 7867, 7557, 7926, 8060, 7332, 8269, 7683, 7805, 8064, 7407, 7585, 7284, 7226, 7754, 7945, 7024, 8508, 7761, 7822, 7769, 7389, 7903, 8099, 7805, 7571, 7201, 7736, 7949, 7847, 8160, 7720, 7671, 8360, 7990, 7473, 7422, 7688, 7996, 7890, 7941, 7747, 8334, 8039, 7776, 8608, 7458, 7855, 7863, 7742, 8565, 7640, 8106, 7849, 7642, 8217, 7696, 7888, 8400, 8427, 7398, 7815, 7322, 7531, 8126, 8143, 7501, 7961, 7663, 8166, 8285, 7480, 7892, 7398, 7621, 8364, 7901, 7458, 8207, 7110, 7791, 7535, 7693, 8424, 8271, 7716, 7600, 7592, 8144, 7677, 7686, 7731, 7529, 7989, 7350, 8059, 8035, 8055, 7782, 7545, 7491, 7487, 7590, 7818, 7852, 7925, 7970, 7956, 7294, 8613, 7962, 8127, 7640, 8526, 7446, 7650, 7667, 7792, 7744, 7973, 7755, 7614, 8510, 7874, 7520, 8339, 7215, 7617, 7771, 7715, 8052, 8023, 7224, 7552, 7865, 7938, 8325, 7598, 7518, 7876, 8326, 7703, 8525, 7931, 7661, 7765, 7649, 8194, 7694, 7720, 7933, 8122, 8200, 8520, 8173, 7776, 7930, 7823, 8208, 7924, 8451, 8051, 7714, 7500, 7917, 7683, 8244, 7800, 8435, 7539, 7505, 7601, 7705, 7367, 7697, 7242, 8160, 8120, 7782, 7944, 7614, 7410, 7699, 7877, 7271, 7775, 8387, 8055, 7436, 7620, 7824, 7665, 7593, 7143, 7976, 8119, 7695, 7941, 7925, 8114, 7569, 7554, 7827, 7621, 7890, 7411, 7854, 8636, 7750, 7893, 8495, 7661, 7861, 7592, 7679, 7877, 7425, 7750, 7386, 8571, 7767, 6842, 8192, 8093, 7787, 8255, 7207, 8109, 7807, 8339, 8110, 8144, 7783, 7562, 7645, 7903, 8273, 7607, 7374, 7708, 7922, 7275, 7551, 7962, 7758, 7849, 8091, 7748, 7378, 7435, 7779, 7992, 7797, 7468, 8359, 7656, 8271, 7713, 8076, 7603, 7971, 7999, 7293, 8720, 7709, 7968, 7498, 8144, 8186, 7636, 7987, 7155, 8211, 7954, 7956, 7632, 7810, 8040, 7539, 7488, 8284, 7316, 7545, 7605, 7488, 7355, 7683, 7339, 7767, 7813, 7214, 7978, 7435, 7667, 7615, 8027, 7488, 7474, 7379, 7839, 8339, 8032, 7851, 7899, 7660, 7973, 7501, 8057, 7822, 7217, 7316, 7764, 7846, 8198, 7986, 7800, 7338, 7668, 8149, 7789, 8346, 7880, 7947, 7888, 7407, 7654, 7640, 7349, 7576, 7370, 8227, 8472, 7741, 7893, 8207, 7611, 7889, 7807, 7975, 7563, 7500, 8057, 7957, 7694, 7439, 7613, 7929, 7336, 7763, 7696, 7888, 7577, 7703, 7338, 7972, 7856, 8484, 7695, 7568, 7540, 8263, 7231, 7435, 7610, 7387, 7603, 7997, 7605, 7538, 8193, 7500, 7628, 7665, 7480, 7760, 7517, 7813, 8326, 7498, 8469, 7639, 7803, 7816, 7752, 8185, 7684, 7819, 7369, 7897, 7570, 7712, 7855, 7174, 7733, 7522, 7445, 7195, 7916, 7957, 7757, 8439, 7796, 7609, 8013, 7665, 7547, 7957, 7719, 7673, 7602, 7490, 7910, 7869, 8006, 7530, 8025, 7737, 7592, 7100, 8074, 8075, 7894, 7541, 7550, 7761, 7747, 7649, 7209, 8148, 8326, 8195, 7861, 7446, 7643, 7735, 8465, 8101, 8185, 7621, 7751, 7247, 7691, 7558, 7575, 8038, 7935, 7592, 7434, 7202, 7722, 8180, 7254, 8350, 7847, 7520, 8265, 7434, 7466, 7690, 7768, 8194, 7257, 7982, 7462, 7866, 7765, 7169, 7314, 7553, 8100, 7931, 7775, 7566, 7861, 7720, 7225, 7317, 7925, 7543, 7914, 7958, 8226, 8118, 7777, 7921, 7361, 7526, 8087, 7546, 8028, 7558, 7668, 7651, 7786, 7554, 7917, 8423, 7709, 7135, 7752, 7971, 8016, 8616, 7508, 7730, 8009, 7686, 7107, 7093, 7901, 7662, 7564, 8162, 8381, 8115, 7657, 8949, 7756, 8370, 7728, 7589, 8265, 7974, 8209, 7978, 8009, 7872, 7779, 7910, 7942, 7985, 7946, 7736, 7522, 8038, 8116, 7725, 7397, 7533, 7666, 7519, 7395, 7754, 8272, 7955, 7933, 7871, 8137, 7861, 8257, 7849, 7513, 7907, 8181, 8285, 8191, 7793, 7787, 8255, 8476, 7666, 8380, 8434, 7776, 8013, 8076, 7406, 7554, 7902, 7884, 7792, 7424, 8059, 7719, 7578, 7727, 7223, 7332, 7920, 7506, 8151, 7168, 8060, 8000, 6846, 7929, 7871, 7792, 7800, 8159, 7442, 7413, 7636, 7993, 7364, 7614, 7928, 7636, 7458, 7377, 7289, 7698, 7082, 7416, 8083, 8349, 7737, 7853, 8244, 7597, 7340, 7672, 7947, 7551, 7713, 7424, 7883, 7550, 8513, 7767, 8107, 7408, 7712, 7695, 7781, 7943, 8097, 7365, 8033, 7603, 7437, 7602, 7908, 7838, 7724, 7765, 8309, 7590, 7736, 8023, 7760, 7502, 7890, 7761, 8269, 7718, 7627, 7775, 7389, 7480, 8180, 7961, 7895, 7703, 7639, 8080, 7950, 7694, 7492, 7787, 7467, 7982, 7130, 7769, 8126, 7721, 7980, 7921, 7639, 8093, 7766, 7367, 7212, 7820, 7533, 7418, 7854, 7856, 7806, 8054, 7666, 8027, 7802, 7735, 7940, 7788, 7482, 7571, 7676, 7559, 7762, 7990, 7342, 8023, 7675, 7616, 7938, 7918, 7963, 7679, 7362, 7282, 7706, 7562, 7844, 7181, 7838, 7671, 8084, 8071, 7997, 8312, 7418, 7606, 7461, 7718, 7865, 8072, 7727, 7840, 7914, 8030, 8288, 8040, 7688, 7550, 7536, 7507, 7429, 7617, 7409, 7796, 7474, 7400, 7838, 7647, 7981, 7897, 8290, 7310, 8192, 7341, 8166, 7568, 7533, 7979, 7560, 8124, 8059, 7606, 7771, 7450, 7882, 7742, 7891, 7940, 8180, 7636, 7793, 7593, 7864, 8198, 7330, 8164, 7962, 7524, 7861, 7752, 7467, 7686, 7818, 7727, 7811, 8227, 7956, 7837, 7587, 7728, 7617, 8010, 7339, 7506, 7439, 7862, 7490, 8092, 7301, 8267, 7795, 7814, 8183, 7776, 7914, 7897, 8121, 8321, 7673, 7400, 8068, 7954, 8239, 7604, 8456, 7826, 7782, 7363, 7289, 7649, 7868, 8247, 7260, 8208, 7959, 7649, 8230, 8381, 7828, 7439, 7944, 7469, 7286, 7934, 8153, 7915, 7711, 7968, 7807, 7504, 8228, 7683, 8118, 8139, 7867, 7839, 8331, 7848, 7580, 7537, 8072, 7789, 7523, 7606, 7968, 7756, 7249, 8070, 8323, 7841, 8039, 7751, 7831, 7592, 7601, 7588, 7738, 7685, 7966, 7453, 7516, 7756, 8057, 8019, 8015, 7562, 8352, 8211, 7804, 7388, 7774, 7210, 7800, 7539, 7975, 7733, 8246, 7597, 7486, 7689, 7433, 7642, 7909, 8039, 7640, 7480, 8098, 7502, 7496, 7563, 8293, 7336, 8220, 7960, 7725, 7912, 7654, 8152, 7604, 8008, 7714, 7533, 7652, 7769, 8122, 6858, 7390, 7782, 7506, 7775, 8007, 7635, 6996, 7584, 8109, 7806, 7868, 7845, 7615, 8191, 7835, 8311, 7752, 8046, 8161, 8150, 7811, 7646, 7534, 7777, 7697, 8200, 6962, 8080, 7927, 8119, 7347, 7897, 7482, 7865, 7641, 7653, 7901, 8530, 7196, 7349, 7674, 7489, 7604, 8117, 7915, 7773, 7901, 7746, 7978, 8117, 7921, 8056, 8245, 8301, 7756, 7493, 7893, 7925, 7682, 7815, 8116, 8103, 7543, 7783, 7809, 7446, 7703, 7830, 7395, 7776, 7598, 7806, 7671, 8550, 7658, 7769, 7755, 7727, 7962, 8167, 7868, 7939, 7775, 8203, 7857, 7768, 7680, 7541, 7841, 7871, 8452, 7319, 7275, 7973, 7787, 7420, 8173, 7714, 8309, 7607, 7500, 7274, 7911, 7672, 7847, 8185, 7281, 7481, 7328, 7975, 8116, 7546, 7957, 7928, 7651, 7697, 7942, 7508, 8055, 7542, 7568, 8052, 8006, 7159, 7892, 7803, 8013, 7530, 7399, 7881, 7902, 8121, 7546, 8324, 7918, 7475, 8033, 8252, 7605, 7627, 7844, 8229, 7441, 7743, 7883, 7287, 7962, 7729, 7512, 7763, 7548, 7632, 7542, 7691, 7652, 7991, 7981, 8155, 8198, 7692, 7435, 7456, 7983, 7591, 8034, 7832, 6949, 7619, 7540, 8390, 7455, 7222, 7899, 8341, 8249, 7970, 7742, 7767, 7452, 7769, 7264, 7352, 7568, 7877, 7482, 7765, 7630, 7762, 7890, 8111, 7633, 7952, 8438, 7455, 7591, 7915, 7879, 7415, 7701, 8008, 8683, 7685, 8175, 7541, 8169, 8087, 8075, 7490, 8755, 7911, 8030, 7603, 7391, 7948, 7426, 7343, 7575, 8021, 8526, 8291, 7549, 8030, 7910, 7830, 7584, 8028, 7187, 7792, 7898, 7603, 7396, 7541, 8003, 7498, 7234, 7559, 7763, 7661, 7802, 7680, 7666, 8016, 7966, 7692, 7257, 7994, 8037, 7668, 7952, 8211, 7996, 7847, 7812, 7638, 7156, 7917, 7628, 7429, 7525, 7918, 7689, 7601, 7708, 7485, 7998, 7499, 7527, 7220, 7484, 7931, 7137, 7327, 7516, 7755, 7891, 7109, 7560, 7324, 7885, 7837, 7655, 7842, 7611, 7768, 7659, 7284, 7538, 8224, 7715, 7585, 7315, 7992, 7566, 7288, 7830, 7724, 7767, 8001, 7593, 7307, 7967, 7922, 7525, 7455, 7393, 7604, 8123, 7737, 8168, 7639, 8213, 7872, 8046, 7810, 7597, 7468, 8432, 7450, 7856, 8090, 7692, 8128, 7775, 7829, 8079, 7332, 7992, 7804, 7501, 7435, 7568, 7432, 7519, 7981, 7727, 7621, 8421, 7758, 7916, 7719, 7303, 7507, 7754, 7544, 7429, 8064, 8211, 8501, 7297, 8654, 8072, 7610, 8110, 8074, 7750, 7983, 7754, 8312, 7911, 7766, 7493, 7919, 7967, 7738, 7245, 7478, 8004, 7800, 7479, 7963, 7552, 8061, 7407, 7985, 8278, 7668, 7390, 7604, 7671, 7850, 8055, 7784, 8237, 7872, 8076, 8241, 7802, 7511, 7937, 7949, 7837, 7844, 7757, 8068, 7072, 7602, 8201, 7997, 7937, 7773, 8049, 8223, 7653, 7462, 7732, 8375, 7627, 7474, 7813, 7494, 7463, 7926, 7847, 7972, 7261, 8185, 7862, 7801, 8126, 7303, 7263, 7562, 7876, 7943, 7873, 7712, 8007, 7776, 8184, 8026, 8248, 8245, 7792, 7824, 7905, 7283, 7757, 7998, 7430, 7505, 7635, 7998, 7466, 8020, 7637, 7713, 7928, 7656, 7587, 8049, 8397, 7721, 8281, 8118, 7211, 7351, 7650, 7641, 7883, 8099, 8181, 7919, 7433, 7823, 7307, 7956, 7692, 7875, 8218, 8052, 8235, 7399, 7909, 7680, 8649, 7899, 7923, 7356, 7682, 7480, 7740, 7703, 7520, 8491, 7794, 7777, 7598, 7553, 7446, 7754, 8284, 7791, 7614, 8029, 7908, 7708, 7975, 7658, 7424, 7979, 8081, 8125, 7657, 7813, 7957, 7697, 7710, 7620, 8179, 8078, 7861, 7923, 7543, 8450, 7653, 8181, 7987, 7925, 7677, 7890, 8218, 7790, 7562, 7454, 6993, 7494, 7928, 7592, 7888, 7649, 7791, 7705, 7873, 7559, 8198, 8304, 7625, 8136, 7827, 7261, 7447, 7687, 8097, 7379, 8352, 7777, 7659, 8006, 8141, 7905, 8143, 7457, 8023, 8150, 7950, 7089, 8572, 7308, 6925, 7476, 7787, 7773, 7562, 7205, 8648, 7471, 7823, 7419, 7855, 7666, 8075, 8011, 7725, 7900, 7612, 8329, 7927, 7772, 7911, 7263, 8447, 7715, 7687, 7603, 7757, 7929, 7414, 7304, 7616, 7598, 7997, 8655, 8395, 7678, 7858, 7821, 7819, 7650, 7593, 7492, 7897, 7367, 7759, 7951, 7561, 7197, 7813, 8270, 7591, 7789, 8261, 8430, 7064, 7735, 7951, 7146, 7586, 7649, 7860, 8065, 7547, 8368, 7707, 7845, 8066, 7834, 8110, 7696, 7413, 7962, 7597, 7985, 7823, 7951, 8213, 8055, 7416, 8140, 7219, 8338, 7734, 7610, 8113, 8043, 7796, 7595, 7647, 7832, 7527, 7973, 8016, 7911, 7886, 7876, 7671, 7725, 7340, 7547, 7366, 7560, 7896, 7031, 7238, 7476, 7958, 7598, 7543, 7283, 8045, 8039, 7734, 6927, 7972, 8068, 8270, 7960, 8867, 7730, 8280, 7756, 7492, 6999, 7770, 7537, 7257, 7680, 7650, 7798, 8751, 7244, 7534, 7345, 8531, 7957, 8758, 7764, 7549, 7739, 7796, 7425, 7659, 8313, 8591, 7422, 8147, 7794, 8027, 7585, 7868, 8038, 7545, 7838, 7663, 7222, 7725, 7636, 7884, 7947, 7286, 7485, 7462, 7646, 8300, 7617, 7826, 7829, 8090, 7853, 8689, 7572, 7798, 7715, 7598, 7634, 7512, 7928, 7879, 8017, 8711, 7566, 8113, 7348, 8118, 7965, 7318, 7356, 8020, 7460, 7840, 7684, 7419, 8153, 7641, 7746, 7241, 8387, 7807, 7810, 8237, 7908, 7345, 7553, 7721, 8159, 7305, 7609, 8009, 7975, 7490, 7866, 7618, 7775, 7864, 7740, 7830, 7803, 7797, 7407, 7764, 7861, 7809, 7647, 7349, 7944, 7677, 7237, 8154, 7474, 7768, 7871, 7658, 7583, 8353, 7772, 8022, 7864, 7665, 8005, 7580, 7376, 7944, 7805, 7672, 7898, 7690, 7552, 7962, 7999, 7688, 7867, 7836, 7877, 8042, 8119, 7733, 7886, 7700, 7393, 7191, 7762, 8243, 7821, 8036, 7422, 7699, 7760, 8246, 7566, 8134, 8305, 7985, 7086, 7632, 7906, 8050, 7788, 7342, 7456, 7831, 7571, 8200, 7968, 8216, 8310, 7891, 8198, 7689, 7808, 7424, 7457, 8051, 7738, 7599, 8416, 7881, 7887, 7952, 8302, 7407, 8100, 7523, 7434, 8241, 6996, 8343, 7343, 7696, 7634, 7549, 7967, 7800, 7333, 7913, 7214, 8210, 7664, 7730, 7869, 7904, 8310, 7344, 7948, 7731, 7444, 7754, 7859, 7727, 7835, 7757, 7895, 8207, 8169, 7837, 7666, 8243, 7877, 7964, 7596, 8070, 7449, 7751, 7674, 7828, 7673, 7792, 7129, 7726, 8156, 7478, 8069, 7533, 8086, 7641, 7753, 7473, 7478, 7779, 7507, 7654, 7726, 7776, 7775, 7583, 8315, 7656, 7499, 8147, 7641, 7912, 7451, 7810, 8369, 7392, 7716, 7908, 7764, 7473, 7590, 7871, 7948, 8007, 7463, 7601, 8024, 7782, 8216, 7607, 7658, 7426, 7217, 8040, 7568, 8094, 8031, 7814, 8271, 7604, 7702, 8091, 7842, 7819, 8252, 7984, 7692, 8380, 7521, 8179, 8163, 7891, 7493, 7773, 7970, 8006, 7990, 8032, 7560, 7902, 7952, 8007, 7926, 8111, 7379, 8087, 8055, 7747, 7539, 7133, 8311, 8572, 8150, 8329, 8129, 7436, 7253, 7436, 7620, 7608, 7304, 7418, 7258, 7869, 7569, 8352, 7606, 7836, 7672, 8127, 7494, 8338, 7503, 7711, 7782, 7303, 8127, 7832, 7409, 7774, 7784, 8153, 8072, 7676, 7289, 7817, 8232, 8026, 7707, 7552, 7519, 7400, 7909, 8058, 7506, 8240, 8173, 7902, 7196, 7898, 7943, 7282, 7655, 8261, 7672, 7731, 7661, 8118, 7911, 7810, 7629, 7589, 8026, 8202, 7634, 7708, 7629, 7674, 7933, 7726, 7209, 7462, 7543, 7675, 8157, 7560, 7584, 7133, 7754, 7929, 7297, 8151, 7650, 8221, 8115, 8173, 7348, 7951, 7474, 7132, 7979, 7005, 7305, 7845, 7431, 7689, 8214, 7571, 7995, 7247, 7808, 7583, 7929, 7850, 7972, 7246, 7014, 8180, 7830, 8085, 7390, 7822, 7542, 7972, 8018, 7585, 7607, 7882, 7310, 7856, 8018, 8297, 7371, 8147, 7259, 7457, 7535, 7803, 7505, 8131, 8420, 7676, 7061, 7434, 7855, 7615, 7501, 7674, 7542, 8037, 7656, 7619, 7352, 7558, 7872, 7525, 7449, 7574, 7603, 7659, 7533, 7548, 7995, 8018, 7308, 8135, 7609, 7582, 7929, 7899, 8099, 8206, 7790, 7456, 7358, 7683, 7969, 8099, 7434, 7826, 7779, 7689, 7361, 7351, 7831, 7906, 8200, 7957, 7737, 7745, 7310, 7811, 7799, 7889, 7128, 7400, 8007, 7389, 7435, 7969, 7973, 7830, 8055, 7884, 8008, 7091, 8189, 8281, 7855, 8287, 7897, 7572, 8031, 7998, 7571, 7865, 8527, 7811, 7594, 7871, 7357, 7743, 7828, 7791, 7431, 7657, 7870, 7536, 7101, 8313, 7924, 8182, 7695, 7739, 8262, 7207, 7659, 7316, 7879, 7504, 7998, 7706, 8180, 7483, 7611, 7988, 7572, 8179, 7915, 7726, 7323, 8129, 8042, 7577, 7971, 7627, 7216, 7781, 8194, 7934, 8168, 7737, 7593, 7346, 7718, 8014, 7755, 7901, 8106, 7591, 7870, 6960, 7576, 7714, 7252, 7797, 7881, 8217, 7875, 7465, 8083, 7966, 8066, 7829, 8010, 8378, 7790, 7442, 7917, 7652, 7634, 8147, 8352, 7576, 7551, 8060, 7328, 8083, 7445, 7581, 7832, 7630, 7378, 8215, 7899, 7951, 7586, 7890, 7619, 7546, 7744, 7542, 7305, 7894, 7474, 7877, 7687, 7742, 7857, 7624, 6885, 7231, 7485, 7390, 7686, 7497, 7904, 7672, 8003, 7917, 8566, 7673, 8243, 7492, 7324, 7993, 7769, 7991, 7704, 7851, 7298, 8298, 7473, 7964, 7985, 7751, 8171, 8024, 7708, 7361, 7048, 7972, 7867, 8017, 7307, 7676, 7386, 8237, 7543, 7968, 8010, 8261, 7557, 8263, 8138, 7503, 7940, 7991, 7555, 7774, 7997, 7604, 7861, 7875, 7954, 7875, 7689, 7772, 7865, 7490, 7781, 7351, 7489, 7813, 7839, 7898, 7760, 8134, 8035, 7810, 7956, 7714, 7772, 7823, 8281, 7476, 8779, 7546, 8204, 8201, 7866, 8187, 7949, 7391, 7790, 7978, 7994, 7431, 8328, 8780, 7652, 7475, 7834, 8014, 7997, 7827, 7853, 8391, 7523, 7707, 7443, 7690, 7713, 8140, 7525, 7355, 7832, 7730, 7448, 8177, 7697, 8188, 8093, 7623, 8024, 7228, 7510, 7636, 7961, 8185, 7867, 7962, 7643, 8228, 7482, 7748, 7310, 7333, 8032, 8021, 7748, 7289, 8029, 8003, 7879, 7156, 7769, 7611, 7999, 7456, 7794, 7738, 8076, 7877, 7757, 7598, 8143, 7713, 7068, 7936, 7937, 7612, 8026, 7668, 7628, 7577, 7936, 7493, 8097, 8257, 8060, 7198, 7835, 7992, 8121, 7466, 7559, 8051, 8153, 7360, 8393, 7430, 7691, 8020, 8140, 8277, 7842, 7656, 7982, 7568, 7257, 7664, 8115, 8063, 8128, 7717, 7622, 7352, 8018, 7575, 7212, 8551, 7924, 7932, 7833, 7512, 8201, 7803, 8411, 7885, 7451, 8366, 8150, 7830, 8067, 7671, 7873, 7661, 7737, 7549, 8034, 7829, 7977, 7636, 7509, 7816, 6900, 7417, 7783, 7392, 8091, 8052, 8319, 7422, 7151, 7897, 7780, 7745, 7851, 6880, 7547, 7687, 7299, 7919, 8122, 7523, 7957, 7004, 7897, 8211, 8117, 8270, 8126, 7499, 8371, 7888, 7290, 7167, 8039, 7862, 8515, 7673, 8603, 7594, 8176, 7954, 7646, 7926, 7690, 8097, 7484, 7967, 8070, 7562, 8114, 7862, 7581, 7370, 7917, 7483, 7468, 7610, 7482, 7720, 7547, 7743, 8366, 7609, 7440, 7767, 8288, 7697, 7939, 7697, 8265, 8030, 7518, 8085, 7106, 7733, 8131, 8593, 7594, 8031, 7189, 7837, 8296, 7589, 7156, 7275, 8333, 7963, 7822, 7974, 8105, 7669, 7266, 8154, 7210, 7959, 7849, 7994, 7609, 7432, 8029, 8131, 7287, 7672, 8000, 7655, 8240, 7454, 7864, 7743, 7374, 7630, 8203, 7327, 7372, 7660, 7587, 7894, 7543, 7899, 7661, 7811, 7575, 8148, 8368, 8511, 7898, 7965, 7653, 7924, 7956, 7438, 7739, 7556, 7882, 7791, 7579, 7596, 7322, 7421, 7976, 7653, 7893, 7937, 7831, 7858, 7986, 7805, 7565, 7664, 7698, 7873, 7880, 8203, 7812, 8078, 7527, 7446, 7352, 8291, 7923, 7244, 7318, 7280, 7486, 7404, 7785, 7146, 7521, 7633, 7711, 7824, 7767, 7596, 7380, 7824, 8073, 7872, 7150, 7481, 7209, 7530, 8038, 7425, 7461, 7986, 7845, 7752, 7734, 7670, 7386, 7871, 7612, 7584, 8455, 7410, 8153, 7934, 7635, 7800, 7996, 7912, 8207, 8053, 7892, 7957, 7684, 7959, 7903, 8479, 6981, 7708, 8415, 7348, 7630, 8265, 7219, 7741, 7616, 7909, 8000, 8169, 7860, 8106, 7612, 8237, 7660, 7956, 7975, 7131, 8367, 7639, 7677, 7302, 8012, 7996, 7607, 7512, 7571, 7798, 7955, 7600, 7346, 7866, 7258, 8439, 7531, 7768, 7369, 7843, 8184, 7431, 7707, 7971, 7159, 7567, 8133, 7573, 7167, 7784, 7676, 8084, 7747, 7661, 7653, 7653, 7718, 7914, 7875, 7903, 7419, 7764, 7669, 7893, 7781, 7817, 8231, 7765, 8144, 7670, 7328, 7097, 7251, 8050, 7837, 8128, 7469, 7787, 8196, 6952, 7747, 8184, 7618, 7843, 7674, 8251, 7707, 7691, 7776, 7300, 7897, 7676, 7261, 7725, 8065, 7151, 7504, 7585, 7627, 8360, 8002, 7901, 7778, 7786, 7823, 8363, 7469, 7572, 7829, 8088, 7833, 7781, 7516, 7548, 7923, 7937, 8040, 7824, 7874, 7242, 8058, 7420, 8160, 7676, 7521, 7516, 7020, 7705, 7893, 8066, 8006, 7288, 7268, 7114, 8004, 7088, 7853, 8160, 7327, 7498, 8044, 8522, 6879, 7584, 7926, 7604, 7345, 7745, 8061, 7706, 7681, 8011, 7520, 7886, 7867, 7639, 7771, 7456, 7312, 7849, 8267, 8004, 8085, 7334, 7561, 8173, 8124, 7814, 7577, 7324, 7668, 7615, 7766, 7631, 8064, 7792, 7870, 7952, 7777, 7943, 7782, 7252, 7811, 7237, 7355, 8332, 8106, 8346, 8168, 7888, 7850, 7944, 7754, 7806, 7265, 8121, 8220, 7488, 7438, 7564, 7177, 8168, 7420, 7787, 8237, 8371, 7706, 7587, 7855, 8435, 7803, 7425, 7947, 7854, 7601, 7581, 8037, 7333, 7316, 7541, 8132, 7552, 8303, 7841, 7602, 7631, 7784, 7863, 7598, 7893, 8004, 8217, 7590, 7942, 8063, 8136, 8306, 7492, 7679, 7626, 7701, 6901, 8125, 7602, 7901, 7867, 7405, 7484, 8088, 8016, 7379, 7691, 8212, 8271, 7113, 7526, 7788, 7835, 7931, 7696, 7533, 7634, 8100, 7746, 7361, 7551, 7363, 7722, 7983, 7937, 8308, 7888, 7882, 7636, 7977, 7881, 7971, 7860, 7911, 7022, 7773, 7225, 7392, 8224, 7206, 7574, 7508, 8032, 8022, 7809, 7639, 7967, 8051, 7922, 7430, 8004, 8240, 7889, 8391, 7430, 7831, 7710, 7887, 7898, 7256, 8124, 7996, 7372, 8037, 7495, 7692, 7631, 8304, 7641, 7740, 7670, 7689, 8074, 7946, 8018, 7450, 7442, 7565, 7812, 7528, 7768, 7713, 7923, 7976, 7833, 7500, 8333, 8181, 8266, 8186, 7518, 7984, 8032, 7636, 8184, 7498, 8521, 7945, 8115, 7565, 7686, 7860, 7850, 7473, 7653, 7556, 7923, 7677, 7733, 7320, 7993, 8072, 7429, 7556, 7815, 8063, 7688, 7765, 7505, 7430, 8262, 7652, 7659, 7753, 7761, 6981, 8061, 7350, 7449, 7700, 7905, 8237, 7804, 7668, 7650, 7973, 8005, 7555, 8185, 8117, 8058, 7242, 8285, 7763, 7533, 7230, 7642, 7557, 7515, 7606, 8012, 8106, 8330, 7680, 7969, 7850, 7587, 7846, 7800, 7277, 7566, 8217, 8066, 7078, 7505, 7597, 8023, 7833, 7573, 7721, 7654, 7535, 8523, 7456, 8107, 8387, 8139, 7978, 7205, 8140, 7884, 8261, 7820, 7736, 7954, 7505, 7507, 7891, 7185, 7855, 7862, 7661, 7926, 7192, 8275, 7725, 8046, 7983, 7858, 7587, 7318, 7163, 7774, 7437, 7710, 8095, 7636, 8095, 7481, 7044, 7890, 7762, 7869, 7642, 7859, 7882, 8349, 7973, 7740, 7531, 7790, 7886, 7787, 7349, 8444, 7914, 7521, 7888, 8276, 7777, 7789, 8083, 7582, 7668, 7627, 8132, 7908, 7868, 8516, 8579, 7738, 7661, 7691, 8095, 7333, 8252, 7916, 7759, 7801, 7915, 7660, 7838, 7960, 8414, 7719, 7491, 7609, 7905, 8031, 8021, 8030, 7733, 7899, 7994, 7605, 8050, 7880, 8069, 7386, 7968, 8118, 7789, 7051, 7516, 7740, 7939, 7449, 7295, 7484, 7151, 8435, 7623, 7402, 8205, 7764, 7442, 8096, 7994, 7647, 7809, 8457, 7390, 8377, 8129, 7742, 7608, 7655, 7567, 7648, 7077, 8188, 7941, 7339, 7440, 7448, 7875, 7627, 7774, 7480, 7548, 7882, 7729, 7659, 7677, 7741, 8104, 7773, 7629, 8199, 7794, 7795, 7263, 7811, 7912, 7927, 7756, 8073, 7926, 7517, 8136, 7583, 7751, 7748, 7838, 7431, 7609, 7964, 7840, 7803, 7489, 7870, 7589, 7707, 7958, 8093, 7798, 7566, 8165, 7510, 7355, 7622, 7274, 7901, 7495, 7732, 7748, 7885, 7441, 7785, 7780, 7786, 7925, 7443, 7723, 7819, 7725, 7525, 7435, 7745, 7975, 8405, 7804, 8183, 7762, 7366, 7502, 7613, 8347, 7845, 7664, 7695, 7298, 7730, 8075, 7205, 7619, 7639, 7240, 8296, 7573, 7659, 7955, 8241, 7518, 7655, 7210, 7920, 7436, 7679, 8150, 7386, 7399, 7441, 8149, 7938, 7282, 7510, 7906, 8198, 7858, 7764, 8005, 7809, 7038, 8008, 8011, 8143, 7963, 7561, 8741, 7528, 7639, 8260, 7617, 7634, 8115, 8066, 7705, 7881, 8062, 8513, 7596, 7513, 7940, 7162, 7240, 7181, 7951, 7927, 7740, 7707, 8038, 8030, 8347, 8158, 7313, 7788, 8081, 7195, 7058, 8300, 7600, 7711, 7999, 8005, 7466, 7113, 8343, 7908, 7943, 7644, 7895, 7820, 7705, 7771, 7541, 8020, 7511, 7657, 7800, 7869, 7599, 7315, 8008, 7238, 7273, 7997, 7669, 8098, 7609, 8016, 7615, 7572, 7666, 7774, 8002, 7366, 7660, 8069, 7247, 7694, 8070, 7446, 7975, 7880, 7734, 7530, 7648, 7926, 7203, 7542, 8477, 7923, 8035, 8045, 7583, 7569, 7401, 7450, 8263, 7792, 7593, 7874, 7861, 7745, 7549, 7930, 7731, 8236, 7963, 7937, 8083, 7969, 7639, 7841, 7910, 7603, 7650, 8063, 7700, 7678, 7467, 7716, 8123, 7756, 7959, 7399, 7828, 8037, 8047, 7685, 8290, 7542, 8069, 7796, 7433, 7609, 7646, 7919, 7545, 8232, 7902, 7825, 7643, 7930, 7723, 7914, 8358, 7212, 8549, 7937, 7325, 7469, 7600, 8062, 8571, 7872, 7495, 7500, 7700, 7895, 7817, 7769, 7920, 7054, 8027, 7638, 7684, 7672, 7947, 7503, 7806, 7573, 7532, 7563, 8289, 8206, 7657, 7702, 7760, 8028, 7460, 7437, 7839, 8268, 7919, 8199, 7686, 8275, 7372, 7891, 7894, 8251, 7679, 7790, 7517, 7585, 7942, 7818, 8222, 7451, 7354, 7634, 7915, 8131, 8473, 7504, 7853, 8432, 7897, 8122, 7892, 8118, 7772, 7864, 7675, 7789, 7784, 8256, 7749, 7373, 7333, 7897, 7328, 7671, 7981, 6889, 7483, 7812, 7332, 7481, 7844, 8197, 7739, 8021, 8030, 7680, 7499, 7318, 7903, 8145, 7295, 7739, 7345, 7816, 8046, 7877, 7591, 7498, 8493, 8022, 7606, 7523, 8019, 7618, 7911, 8073, 8275, 7756, 8335, 8063, 7714, 7899, 7777, 7271, 8267, 8359, 7774, 7375, 7869, 7974, 7273, 7808, 7785, 8471, 7666, 7698, 7210, 7759, 7783, 7367, 7533, 7509, 7629, 7832, 7925, 7504, 7461, 7824, 7772, 7688, 7793, 7918, 8506, 8362, 7662, 7783, 7711, 8525, 8016, 8612, 8008, 7762, 7443, 7680, 7843, 7606, 8286, 7985, 7069, 7781, 7261, 7484, 8227, 7577, 8542, 7823, 7556, 7800, 7917, 7354, 8252, 7776, 7772, 7167, 7385, 8094, 7437, 7234, 8090, 7646, 7625, 7312, 7061, 7590, 7492, 7753, 8362, 7899, 7748, 8044, 7476, 7978, 8092, 7783, 7585, 8140, 7734, 7821, 7906, 7922, 8377, 7765, 7671, 8463, 7410, 7830, 8017, 7288, 7766, 7323, 8134, 7722, 8072, 7856, 7997, 7830, 7610, 8062, 8283, 7212, 7584, 7853, 7735, 7636, 8131, 7719, 8127, 7988, 7718, 7349, 8014, 7903, 8080, 8023, 7948, 8161, 7546, 7564, 7216, 7833, 7191, 7372, 7714, 7515, 7736, 7922, 7739, 7823, 7820, 7236, 7346, 7941, 8258, 7614, 7973, 7879, 7681, 7324, 7766, 8140, 7206, 7875, 7589, 7337, 8027, 8069, 7669, 8261, 7831, 8146, 7877, 7373, 7387, 7695, 7644, 7963, 7742, 7836, 7828, 7478, 7619, 7168, 7577, 8036, 8020, 7749, 8123, 7865, 8422, 7406, 7853, 7434, 7892, 7347, 8118, 7510, 7357, 7492, 8272, 8326, 7839, 8046, 7786, 7711, 7693, 7278, 7999, 7668, 7631, 6967, 7812, 7476, 7140, 7252, 7469, 7647, 7942, 7931, 8091, 8266, 7694, 7420, 7257, 8010, 8116, 7301, 7809, 7657, 7453, 7661, 8303, 8339, 7139, 8036, 7495, 7828, 7583, 7887, 7225, 8175, 7606, 7630, 8102, 7676, 8176, 7855, 7858, 7278, 7560, 7793, 7687, 7709, 7925, 8181, 7706, 7675, 7730, 7807, 8099, 8090, 8090, 7818, 8146, 7996, 7582, 8337, 7859, 7931, 7258, 8204, 7742, 7964, 8129, 7464, 7826, 7610, 7301, 7466, 7617, 7582, 8087, 7732, 7081, 8060, 7648, 7495, 7968, 8272, 8085, 7690, 7929, 7887, 8035, 7400, 7658, 7425, 7720, 7569, 7728, 8174, 7604, 7512, 7208, 7731, 7657, 7246, 7419, 7623, 7879, 7731, 8403, 7771, 7686, 7680, 7850, 7439, 7925, 8098, 7258, 7707, 7715, 7789, 7648, 7620, 7785, 8201, 7737, 7664, 7986, 8062, 8211, 7326, 7855, 7719, 7753, 8507, 8707, 7574, 7618, 7666, 7616, 7360, 7693, 7388, 7975, 7517, 7976, 7972, 7338, 8306, 7432, 7060, 8432, 7723, 7460, 8399, 7895, 7313, 7551, 7671, 7068, 7884, 7498, 7615, 7840, 7635, 8226, 8118, 7954, 7505, 7602, 7245, 8103, 8409, 7731, 8205, 7404, 7858, 7697, 7858, 7574, 8053, 7757, 8021, 8384, 8197, 8474, 8174, 7572, 7722, 8030, 7839, 7759, 7612, 8052, 8060, 8068, 7163, 7409, 7679, 7303, 8039, 8014, 7977, 7479, 7358, 7776, 7460, 7957, 7435, 7715, 7899, 8138, 8060, 8041, 7706, 7131, 8027, 7440, 7831, 7592, 7936, 7270, 7737, 7405, 7545, 7487, 8389, 7390, 7664, 7712, 7564, 7804, 7696, 8290, 8022, 7480, 7397, 8277, 8460, 7931, 7330, 7676, 7585, 7717, 7968, 7536, 8542, 7420, 7447, 7643, 7955, 7667, 7367, 7647, 8121, 7754, 7918, 8472, 8144, 7310, 7716, 7764, 8335, 7519, 7600, 7898, 8057, 7688, 7815, 8373, 7881, 8318, 8202, 8429, 8162, 7855, 7694, 7585, 7739, 8192, 8116, 7847, 8315, 7970, 7909, 7255, 7766, 8036, 7442, 8035, 8065, 7718, 7761, 7588, 8226, 7596, 7396, 7945, 8519, 7814, 7713, 7718, 7862, 8073, 7837, 7663, 7652, 8297, 7894, 7628, 7962, 7751, 7794, 8057, 8126, 7749, 7397, 7757, 7408, 8156, 8337, 7439, 8130, 7650, 7728, 7842, 7547, 7469, 7600, 7712, 7710, 7282, 8172, 7914, 7851, 7518, 7919, 7684, 8042, 7800, 7085, 7372, 7721, 7972, 7785, 8188, 7617, 7160, 8509, 8576, 7681, 8091, 7394, 8103, 7888, 7916, 8074, 7847, 7967, 7658, 7992, 7263, 7476, 7453, 7865, 8755, 7519, 6996, 8040, 8291, 7488, 7230, 7905, 7372, 7571, 8310, 7594, 7916, 7477, 7893, 7589, 7542, 7332, 7774, 7334, 7455, 8100, 7960, 7770, 7830, 7612, 8142, 7485, 7199, 7643, 7893, 7792, 7748, 7735, 8021, 7607, 7532, 7862, 7438, 7786, 8215, 7836, 7705, 7299, 7218, 8031, 7642, 8048, 7892, 7623, 7581, 7873, 7912, 7163, 7934, 7806, 8021, 8189, 7556, 8228, 7675, 7692, 7952, 7520, 7986, 7900, 7906, 8076, 8321, 8150, 8279, 8203, 7949, 7585, 8479, 7461, 7726, 7664, 7520, 8059, 7396, 8135, 7714, 7429, 8224, 7511, 8690, 8185, 7745, 7854, 7933, 6982, 7714, 8285, 7453, 8008, 7494, 8262, 7718, 8202, 7696, 8093, 7333, 7553, 7639, 7614, 7852, 7682, 7580, 7805, 8043, 7710, 7992, 7774, 8199, 8217, 7935, 7848, 8196, 7866, 8027, 7760, 7834, 7415, 8458, 7579, 7709, 7750, 7536, 8363, 7288, 7839, 7598, 7891, 8055, 8078, 7953, 7431, 7504, 7629, 7563, 7867, 8124, 7764, 7216, 7870, 8294, 7646, 7831, 8209, 7787, 7756, 8348, 7567, 7262, 7643, 7631, 7941, 8044, 7868, 7458, 7345, 7924, 7612, 7912, 7618, 7691, 7649, 7078, 7744, 8201, 8055, 7530, 7982, 7587, 8003, 7811, 7600, 7811, 7875, 7789, 7695, 7473, 8035, 7869, 7684, 7321, 7861, 7606, 7543, 7571, 7467, 8066, 7850, 7911, 7983, 7858, 7306, 7231, 7516, 7609, 7900, 7751, 7739, 7655, 7686, 7661, 7936, 8032, 7102, 7516, 7554, 8037, 8117, 7936, 7807, 8186, 7142, 7421, 8098, 7770, 7921, 7532, 7570, 7776, 7798, 7753, 8212, 7779, 8299, 7877, 7226, 7659, 7821, 8336, 7100, 7605, 6976, 7786, 8018, 7169, 8188, 7478, 7818, 7939, 8229, 8275, 7348, 7564, 7367, 7769, 7732, 8007, 7212, 7786, 7830, 7484, 7851, 7957, 8159, 7371, 7862, 7531, 7806, 8134, 7686, 7463, 7468, 8056, 8338, 8364, 7638, 7754, 7754, 8143, 7202, 7292, 7793, 7764, 7670, 7247, 7449, 8502, 7518, 8028, 7817, 8094, 7500, 8258, 7871, 8082, 7543, 7505, 8027, 7729, 8182, 7941, 7527, 7481, 7856, 7623, 7974, 7634, 7830, 7688, 7553, 7524, 8188, 7679, 8037, 8118, 7809, 7373, 8085, 7295, 7568, 7566, 7797, 7076, 7528, 7783, 7964, 8127, 8481, 7587, 7569, 7284, 7398, 8296, 7890, 7753, 7743, 7788, 7826, 7885, 7520, 7539, 7873, 7810, 8127, 7371, 8105, 7491, 7267, 7787, 7681, 7016, 7955, 8091, 7583, 7574, 8036, 7204, 7735, 8243, 7666, 7748, 7848, 7568, 8100, 7610, 7646, 7370, 7748, 7922, 8030, 7863, 7518, 7845, 7302, 8047, 8239, 7724, 7693, 7972, 7445, 7716, 8081, 7781, 7999, 7789, 8603, 7909, 8160, 7583, 8105, 7685, 8091, 7982, 7972, 7440, 7307, 7714, 7794, 7505, 7660, 7391, 7901, 8453, 7727, 7216, 7505, 7660, 7945, 7763, 7806, 7648, 8250, 7710, 8024, 7782, 7864, 7416, 8195, 8161, 7534, 7736, 7678, 8073, 7482, 7973, 7477, 7331, 7298, 7664, 7709, 8104, 7812, 8151, 7972, 7764, 7699, 7838, 7291, 7777, 7768, 7460, 7610, 7649, 8651, 8185, 7195, 8343, 7947, 7563, 7457, 8209, 8122, 7425, 7549, 8158, 7998, 8102, 7795, 7465, 7736, 8427, 7630, 7674, 7910, 7682, 7721, 7835, 7903, 7926, 7830, 7438, 7535, 7482, 7575, 7842, 7773, 7974, 7952, 7408, 7880, 7599, 7916, 7462, 7674, 7777, 7033, 7781, 7764, 7810, 8161, 7918, 7707, 7732, 7439, 8018, 8341, 7785, 7329, 7858, 7450, 7767, 7720, 7460, 7545, 7544, 7247, 7528, 7569, 8068, 7546, 8278, 7876, 7996, 7697, 7730, 8286, 7767, 8317, 7898, 7808, 8248, 8017, 7697, 7894, 7493, 7911, 8278, 7574, 7488, 8091, 7849, 7678, 7417, 7520, 7379, 7928, 7765, 7861, 7366, 7579, 8060, 7928, 7366, 8033, 8026, 7692, 7669, 8376, 7440, 8576, 7622, 7595, 7771, 7917, 8026, 7535, 8177, 8139, 8139, 7637, 8125, 7906, 7632, 8425, 8007, 7785, 7376, 7577, 7382, 7632, 8009, 7779, 7699, 7613, 8760, 8011, 7262, 8229, 8002, 7426, 7701, 8001, 7584, 7505, 8133, 7591, 7916, 8008, 7415, 7414, 8018, 7698, 7642, 7461, 7651, 7618, 7949, 8301, 7644, 8306, 7855, 8205, 7734, 7708, 7653, 7956, 7575, 7803, 8039, 7611, 7737, 7852, 8063, 7868, 7072, 8196, 7555, 8124, 7912, 7802, 7938, 7516, 7762, 7222, 8127, 7736, 8060, 7549, 7809, 7397, 7671, 7599, 7809, 7972, 7862, 7743, 7724, 7781, 8112, 8120, 7660, 7635, 7592, 7993, 7668, 8289, 7592, 7860, 7712, 7479, 7800, 7982, 7602, 7687, 7492, 7783, 7621, 7495, 7988, 7931, 7625, 7890, 7345, 7569, 7995, 7780, 7734, 7442, 7750, 7733, 7717, 7958, 7865, 7916, 8314, 7198, 8046, 8473, 7484, 7854, 7962, 7809, 7939, 7626, 7782, 8012, 8091, 7358, 7816, 7457, 8385, 7647, 7516, 7810, 7391, 7199, 7862, 7456, 7806, 8285, 7960, 7482, 7622, 7773, 7698, 8097, 7922, 7979, 7526, 8021, 7365, 7788, 8152, 8345, 7783, 7989, 7959, 8827, 7908, 8104, 7843, 7479, 8072, 7311, 7474, 7641, 7433, 7493, 7516, 7418, 7781, 7958, 8104, 7770, 7801, 7886, 7344, 7113, 7596, 8069, 7921, 7313, 8053, 8470, 7958, 8280, 7683, 7752, 7106, 8127, 8045, 7689, 7285, 7316, 7791, 7741, 7792, 7788, 7927, 7867, 7645, 7760, 7793, 8134, 8074, 7837, 7916, 7983, 7386, 7710, 7796, 7058, 7630, 8233, 7888, 7976, 7845, 7427, 7430, 8224, 7822, 7628, 7889, 7700, 7949, 7566, 7798, 7685, 7917, 7384, 8187, 7322, 7898, 7497, 7559, 8252, 7698, 7419, 7458, 7590, 8165, 7817, 8184, 8348, 7993, 8095, 7745, 7919, 7856, 8101, 7467, 7851, 8285, 7741, 7213, 8366, 8190, 8315, 7233, 7522, 8076, 8066, 7815, 7885, 7620, 7437, 7522, 8006, 8069, 7480, 7517, 7983, 7567, 7814, 7898, 7192, 7607, 7669, 7761, 7457, 7900, 7663, 7975, 7446, 7723, 8017, 7827, 8047, 7607, 7508, 7499, 7667, 8027, 7375, 7117, 7794, 8182, 8033, 8027, 7727, 7462, 7743, 7954, 7568, 7586, 7236, 8157, 7709, 7387, 7855, 7438, 8468, 7745, 8108, 8268, 7565, 7779, 7809, 7481, 8110, 8089, 7858, 7942, 7918, 7595, 7790, 7589, 7911, 8333, 7898, 7963, 7800, 7554, 7725, 7657, 7210, 8251, 7516, 8085, 7779, 7735, 7815, 7976, 7872, 7794, 7761, 7347, 7819, 7358, 7706, 8204, 8046, 7987, 7958, 8148, 7957, 8215, 7835, 7996, 7792, 8135, 8383, 7378, 7694, 7787, 7881, 7792, 8055, 7617, 7483, 7326, 8085, 7681, 7500, 8005, 7701, 7389, 8181, 7870, 8238, 7833, 7919, 7640, 7984, 7432, 7578, 7565, 7592, 7928, 7610, 6844, 7947, 7600, 7751, 7995, 8083, 7372, 7711, 7644, 7562, 8144, 7433, 7660, 7683, 7400, 7936, 7344, 8120, 7881, 8209, 8019, 8160, 8291, 7691, 7514, 7707, 7989, 8373, 7126, 8146, 7747, 7711, 7591, 8329, 7394, 8308, 7646, 8226, 7878, 8158, 7987, 7612, 8092, 7609, 7721]
    extra_future_stats_info_loc = extra_future_stats_info.find("*") + 1
    total_amount_of_simss = extra_future_stats_info[:extra_future_stats_info_loc-1]
    extra_future_stats_info = extra_future_stats_info[extra_future_stats_info_loc:]
    extra_future_stats_info = ast.literal_eval(extra_future_stats_info)
    extra_all_dps_results = extra_future_stats_info
    #extra_all_dps_results = []
    #for i in extra_future_stats_info:
        #i = round(i)
        #extra_all_dps_results.append(i)
    extra_all_dps_results_min = int(min(extra_all_dps_results))
    extra_all_dps_results_max = int(max(extra_all_dps_results))
    counts1, bins1 = np.histogram(extra_all_dps_results, bins=range(extra_all_dps_results_min, extra_all_dps_results_max, 50))
    bins1 = 0.5 * (bins1[:-1] + bins1[1:])
    fig_250_title = str("DPS Breakdown for All ") + str(total_amount_of_simss) + str(" Simulations")
    fig250 = px.bar(x=bins1, y=counts1, labels={'x':'DPS', 'y':'Occurrence'}, title=fig_250_title, template="plotly_dark", color=counts1, color_continuous_scale="sunset")
    fig250.update_layout(coloraxis_showscale=False)
    
    data_251 = pd.DataFrame(dict(DPSValue=extra_all_dps_results))
    fig251  = px.box(data_251, x="DPSValue", template="plotly_dark")
    fig251.update_layout(xaxis=dict(
                          title=None,
                          showgrid=False, ),
                            yaxis=dict(
                            title=None,
                            showgrid=False,))
    #fig251.update_traces(orientation='h') 
    #fig250 = px.histogram(x=bins1, y=counts1, labels={'x':'DPS', 'y':'Occurrence'}, title=fig_250_title, template="plotly_dark", marginal="box")
    #extra_stats_split_list = extra_sim_stats_info.replace("*^*",", ")
    #extra_stats_split_list = extra_stats_split_list.split(", ")


    # extra_stats_split_list = extra_sim_stats_info.split("*^*")
    # current_gear_split_list = gear_currently_worn.split("*&*")



    e_stats_hit = extra_stats_split_list[0]
    e_stats_hit_perc = extra_stats_split_list[1] + "%"
    e_stats_crit = extra_stats_split_list[2] + "%"
    e_stats_crit_rating = extra_stats_split_list[3]
    e_stats_strength = extra_stats_split_list[4]
    e_stats_stamina = extra_stats_split_list[5]
    e_stats_hp = extra_stats_split_list[6]
    e_stats_armor = extra_stats_split_list[7]
    e_stats_agi = extra_stats_split_list[8]
    e_stats_ap = extra_stats_split_list[9]
    e_stats_armor_pen = extra_stats_split_list[10]
    e_stats_armor_pen_perc = extra_stats_split_list[11] + "%"
    e_stats_expertise = extra_stats_split_list[12]
    e_stats_expertise_rating = extra_stats_split_list[13]
    e_stats_expertise_dodge_parry_reduc = str(float(e_stats_expertise) * .25) + "%"
    e_stats_haste = extra_stats_split_list[14] + "%"
    e_stats_haste_rating = extra_stats_split_list[15]
    c_g_head = current_gear_split_list[0]
    c_g_neck = current_gear_split_list[1]
    c_g_shoulders = current_gear_split_list[2]
    c_g_back = current_gear_split_list[3]
    c_g_chest = current_gear_split_list[4]
    c_g_wrist = current_gear_split_list[5]
    c_g_gloves = current_gear_split_list[6]
    c_g_waist = current_gear_split_list[7]
    c_g_legs = current_gear_split_list[8]
    c_g_boots = current_gear_split_list[9]
    c_g_ring1 = current_gear_split_list[10]
    c_g_ring2 = current_gear_split_list[11]
    c_g_trinket1 = current_gear_split_list[12]
    c_g_trinket2 = current_gear_split_list[13]
    c_g_sigil = current_gear_split_list[14]
    c_g_mh = current_gear_split_list[15]
    c_g_oh = current_gear_split_list[16]
    c_g_2h = extra_stats_split_list[16]
    c_g_2h = ast.literal_eval(c_g_2h)



    #Extra future stuff
    future_extra_sim_stats_info = dash_all_data["content_extra_future_stats_area"] #database 1 (version 2)
    future_extra_sim_stats_info = future_extra_sim_stats_info.to_string(index = False) #database 1 (version 2)


    # dash_all_data = dash_all_data.to_string(index = False)
    # dash_data_split = dash_all_data.split("*&*")
    # t_damage = float(dash_data_split[1])
    # fight_length = float(dash_data_split[2])
    # rotation = dash_data_split[3]
    # rotation = ast.literal_eval(rotation)
    # rotation_time = dash_data_split[4]
    # rotation_time = ast.literal_eval(rotation_time)
    # rotation_damage = dash_data_split[5]
    # rotation_damage = ast.literal_eval(rotation_damage)
    # rotation_status = dash_data_split[6]
    # rotation_status = ast.literal_eval(rotation_status)
    # rune_0_tracker = dash_data_split[7]
    # rune_0_tracker = ast.literal_eval(rune_0_tracker)
    # rune_1_tracker = dash_data_split[8]
    # rune_1_tracker = ast.literal_eval(rune_1_tracker)
    # rune_2_tracker = dash_data_split[9]
    # rune_2_tracker = ast.literal_eval(rune_2_tracker)
    # rune_3_tracker = dash_data_split[10]
    # rune_3_tracker = ast.literal_eval(rune_3_tracker)
    # rune_4_tracker = dash_data_split[11]
    # rune_4_tracker = ast.literal_eval(rune_4_tracker)
    # rune_5_tracker = dash_data_split[12]
    # rune_5_tracker = ast.literal_eval(rune_5_tracker)
    # rune_6_tracker = dash_data_split[13]
    # rune_6_tracker = ast.literal_eval(rune_6_tracker)
    # rune_7_tracker = dash_data_split[14]
    # rune_7_tracker = ast.literal_eval(rune_7_tracker)
    # rune_8_tracker = dash_data_split[15]
    # rune_8_tracker = ast.literal_eval(rune_8_tracker)
    # rune_9_tracker = dash_data_split[16]
    # rune_9_tracker = ast.literal_eval(rune_9_tracker)
    # rune_10_tracker = dash_data_split[17]
    # rune_10_tracker = ast.literal_eval(rune_10_tracker)
    # rune_11_tracker = dash_data_split[18]
    # rune_11_tracker = ast.literal_eval(rune_11_tracker)
    # rune_time_tracker = dash_data_split[19]
    # rune_time_tracker = ast.literal_eval(rune_time_tracker)
    # runic_power_tracker = dash_data_split[20]
    # runic_power_tracker = ast.literal_eval(runic_power_tracker)
    all_data = pd.DataFrame()
    all_data2 = pd.DataFrame()
    ability_order = rotation
    timeline_order = rotation_time
    damage_order = rotation_damage
    status_order = rotation_status
    timeline_order_data = []
    timeline_order_data_end = []
    for i in timeline_order:
        if i < 1:
            i = .000001
        i = round(i, 6)
        iz = i + 0.5
        if type(i) == int or i.is_integer() == True:
            i += .000001
        if type(iz) == int or iz.is_integer() == True:
            iz += .000001
        i = timedelta(seconds=i)
        iz = timedelta(seconds=iz)
        total = "1970-01-01 " + str(i)
        total_end = "1970-01-01 " + str(iz)
        finished_converted_time = datetime.strptime(total, '%Y-%m-%d %H:%M:%S.%f')
        finished_converted_time_end = datetime.strptime(total_end, '%Y-%m-%d %H:%M:%S.%f')
        timeline_order_data.append(finished_converted_time)
        timeline_order_data_end.append(finished_converted_time_end)
    x = 0
    for i in ability_order:
        if damage_order[x] == 0:
            damage_scale = 0
        elif damage_order[x] < 150:
            damage_scale = "Under 150"
        elif damage_order[x] < 300:
            damage_scale = "Under 300"
        elif damage_order[x] < 500:
            damage_scale = "Under 500"
        elif damage_order[x] < 750:
            damage_scale = "Under 750"
        elif damage_order[x] < 1000:
            damage_scale = "Under 1000"
        elif damage_order[x] < 2000:
            damage_scale = "Under 2000"
        elif damage_order[x] >= 2000:
            damage_scale = "Over 2000"
        data = pd.DataFrame(dict(Ability=i, index=[0],Start=timeline_order_data[x], Finish=timeline_order_data_end[x], Damage=damage_order[x], Status=status_order[x]))
        all_data = pd.concat([all_data, data])
        data2 = pd.DataFrame(dict(Ability=i, index=[0],Start=timeline_order_data[x], Finish=timeline_order_data_end[x], Damage=damage_order[x], Status=status_order[x], DamageScale=damage_scale))
        all_data2 = pd.concat([all_data2, data2])
        x += 1
    unique_ability_df_table = []
    unique_miss_count_df_table = []
    unique_dodge_count_df_table = []
    unique_parry_count_df_table = []
    unique_glance_count_df_table = []
    unique_block_count_df_table = []
    unique_crit_count_df_table = []
    unique_hit_count_df_table = []
    unique_dot_count_df_table = []
    unique_active_count_df_table = []
    unique_proc_count_df_table = []
    unique_damage_per_cast_df_table = []
    unique_damage_df_table = []
    for i in np.unique(np.array(ability_order)):
        search_data = all_data.loc[all_data['Ability'] == i]
        miss_search = search_data.loc[search_data['Status'] == "Miss"]
        dodge_search = search_data.loc[search_data['Status'] == "Dodge"]
        parry_search = search_data.loc[search_data['Status'] == "Parry"]
        glance_search = search_data.loc[search_data['Status'] == "Glance"]
        block_search = search_data.loc[search_data['Status'] == "Block"]
        crit_search = search_data.loc[search_data['Status'] == "Crit"]
        hit_search = search_data.loc[search_data['Status'] == "Hit"]
        dot_search = search_data.loc[search_data['Status'] == "DOT"]
        active_search = search_data.loc[search_data['Status'] == "Active"]
        proc_search = search_data.loc[search_data['Status'] == "Proc"]
        if miss_search.empty:
            unique_miss_count_df_table.append(0)
        else:
            unique_miss_count_df_table.append(len(miss_search.index))

        if dodge_search.empty:
            unique_dodge_count_df_table.append(0)
        else:
            unique_dodge_count_df_table.append(len(dodge_search.index))
        if parry_search.empty:
            unique_parry_count_df_table.append(0)
        else:
            unique_parry_count_df_table.append(len(parry_search.index))
        if glance_search.empty:
            unique_glance_count_df_table.append(0)
        else:
            unique_glance_count_df_table.append(len(glance_search.index))
        if block_search.empty:
            unique_block_count_df_table.append(0)
        else:
            unique_block_count_df_table.append(len(block_search.index))
        if crit_search.empty:
            unique_crit_count_df_table.append(0)
        else:
            unique_crit_count_df_table.append(len(crit_search.index))
        if hit_search.empty:
            unique_hit_count_df_table.append(0)
        else:
            unique_hit_count_df_table.append(len(hit_search.index))
        if dot_search.empty:
            unique_dot_count_df_table.append(0)
        else:
            unique_dot_count_df_table.append(len(dot_search.index))
        if active_search.empty:
            unique_active_count_df_table.append(0)
        else:
            unique_active_count_df_table.append(len(active_search.index))
        if proc_search.empty:
            unique_proc_count_df_table.append(0)
        else:
            unique_proc_count_df_table.append(len(proc_search.index))
        unique_damage_per_cast_df_table.append(round((sum(search_data['Damage'])) / len(search_data['Damage']), 4))
        unique_damage_df_table.append(round(sum(search_data['Damage']), 4))
        unique_ability_df_table.append(i)
    status_table_data = pd.DataFrame(dict(Ability=unique_ability_df_table, Miss=unique_miss_count_df_table, Dodge=unique_dodge_count_df_table, Parry=unique_parry_count_df_table, Glance=unique_glance_count_df_table, Block=unique_block_count_df_table, Crit=unique_crit_count_df_table, Hit=unique_hit_count_df_table, DOT=unique_dot_count_df_table, Active=unique_active_count_df_table, Proc=unique_proc_count_df_table, Avg_Damage=unique_damage_per_cast_df_table, All_Damage=unique_damage_df_table))


    statuss_sum_list = ["Miss", "Dodge", "Parry", "Glance", "Block", "Crit", "Hit", "DOT", "Active", "Proc"]
    status_table_data['Sum'] = status_table_data[statuss_sum_list].sum(axis=1)
    status_table_data['MissP'] = status_table_data["Miss"]/status_table_data["Sum"]
    status_table_data['DodgeP'] = status_table_data["Dodge"]/status_table_data["Sum"]
    status_table_data['ParryP'] = status_table_data["Parry"]/status_table_data["Sum"]
    status_table_data['GlanceP'] = status_table_data["Glance"]/status_table_data["Sum"]
    status_table_data['BlockP'] = status_table_data["Block"]/status_table_data["Sum"]
    status_table_data['CritP'] = status_table_data["Crit"]/status_table_data["Sum"]
    status_table_data['HitP'] = status_table_data["Hit"]/status_table_data["Sum"]
    status_table_data['DOTP'] = status_table_data["DOT"]/status_table_data["Sum"]
    status_table_data['ActiveP'] = status_table_data["Active"]/status_table_data["Sum"]
    status_table_data['ProcP'] = status_table_data["Proc"]/status_table_data["Sum"]
    status_table_data['MissP'] = status_table_data['MissP'].apply(lambda x: x * 100)
    status_table_data['DodgeP'] = status_table_data['DodgeP'].apply(lambda x: x * 100)
    status_table_data['ParryP'] = status_table_data['ParryP'].apply(lambda x: x * 100)
    status_table_data['GlanceP'] = status_table_data['GlanceP'].apply(lambda x: x * 100)
    status_table_data['BlockP'] = status_table_data['BlockP'].apply(lambda x: x * 100)
    status_table_data['CritP'] = status_table_data['CritP'].apply(lambda x: x * 100)
    status_table_data['HitP'] = status_table_data['HitP'].apply(lambda x: x * 100)
    status_table_data['DOTP'] = status_table_data['DOTP'].apply(lambda x: x * 100)
    status_table_data['ActiveP'] = status_table_data['ActiveP'].apply(lambda x: x * 100)
    status_table_data['ProcP'] = status_table_data['ProcP'].apply(lambda x: x * 100)
    status_table_data = status_table_data.round({'MissP': 2, 'DodgeP': 2, 'ParryP': 2, 'GlanceP': 2, 'BlockP': 2, 'CritP': 2, 'HitP': 2, 'DOTP': 2, 'ActiveP': 2, 'ProcP': 2})
    status_table_data['MissP'] = status_table_data['MissP'].astype(str) + '%'
    status_table_data['DodgeP'] = status_table_data['DodgeP'].astype(str) + '%'
    status_table_data['ParryP'] = status_table_data['ParryP'].astype(str) + '%'
    status_table_data['GlanceP'] = status_table_data['GlanceP'].astype(str) + '%'
    status_table_data['BlockP'] = status_table_data['BlockP'].astype(str) + '%'
    status_table_data['CritP'] = status_table_data['CritP'].astype(str) + '%'
    status_table_data['HitP'] = status_table_data['HitP'].astype(str) + '%'
    status_table_data['DOTP'] = status_table_data['DOTP'].astype(str) + '%'
    status_table_data['ActiveP'] = status_table_data['ActiveP'].astype(str) + '%'
    status_table_data['ProcP'] = status_table_data['ProcP'].astype(str) + '%'
    status_table_data['DPSPA'] = status_table_data["All_Damage"].apply(lambda x: x / fight_length)
    status_table_data = status_table_data.round({'DPSPA': 3})

    dps_timeline_breaks = int(fight_length / 3)
    time_each_break = fight_length / dps_timeline_breaks
    time_breaks = []
    timeline_dps_list = []
    for times in range(0, dps_timeline_breaks):
        times += 1
        timeline_current_time = times * time_each_break
        time_breaks.append(times * time_each_break)
        timeline_dps_num = []
        for timeline_time_position, timeline_time in enumerate(timeline_order):
            if timeline_time < timeline_current_time:
                timeline_dps_num.append(timeline_time_position)
        timeline_damage_list = []
        for timeline_damage in timeline_dps_num:
            timeline_damage_list.append(damage_order[timeline_damage])
        timeline_damage = sum(timeline_damage_list)
        timeline_dps = timeline_damage / timeline_current_time
        timeline_dps_list.append(timeline_dps)
    dps_table_data = pd.DataFrame(dict(DPS=timeline_dps_list, Time=time_breaks))

    stats_columns_names = ["Hit", "Hit Percentage", "Crit", "Crit Rating", "Strength", "Stamina", "Health", "Armor", "Agility", "Attack Power", "Armor Penetration", "Armor Penetration Percentage", "Expertise", "Expertise Rating", "Dodge & Parry Reduction", "Haste", "Haste Rating"]
    stats_columns_stats = [e_stats_hit, e_stats_hit_perc, e_stats_crit, e_stats_crit_rating, e_stats_strength, e_stats_stamina, e_stats_hp, e_stats_armor, e_stats_agi, e_stats_ap, e_stats_armor_pen, e_stats_armor_pen_perc, e_stats_expertise, e_stats_expertise_rating, e_stats_expertise_dodge_parry_reduc, e_stats_haste, e_stats_haste_rating]
    stats_table_data = pd.DataFrame(dict(Names=stats_columns_names, Data=stats_columns_stats))
    if c_g_2h == False:
        gear_columns_names = ["Head", "Neck", "Shoulders", "Back", "Chest", "Wrist", "Gloves", "Waist", "Legs", "Boots", "Ring1", "Ring2", "Trinket1", "Trinket2", "Sigil", "Main hand", "Off hand"]
        gear_columns_values = [c_g_head, c_g_neck, c_g_shoulders, c_g_back, c_g_chest, c_g_wrist, c_g_gloves, c_g_waist, c_g_legs, c_g_boots, c_g_ring1, c_g_ring2, c_g_trinket1, c_g_trinket2, c_g_sigil, c_g_mh, c_g_oh]
        gear_table_data = pd.DataFrame(dict(Names=gear_columns_names, Data=gear_columns_values))
    else:
        gear_columns_names = ["Head", "Neck", "Shoulders", "Back", "Chest", "Wrist", "Gloves", "Waist", "Legs", "Boots", "Ring1", "Ring2", "Trinket1", "Trinket2", "Sigil", "Main hand"]
        gear_columns_values = [c_g_head, c_g_neck, c_g_shoulders, c_g_back, c_g_chest, c_g_wrist, c_g_gloves, c_g_waist, c_g_legs, c_g_boots, c_g_ring1, c_g_ring2, c_g_trinket1, c_g_trinket2, c_g_sigil, c_g_mh]
        gear_table_data = pd.DataFrame(dict(Names=gear_columns_names, Data=gear_columns_values))



    colors = {'Main hand': '#45515E',
              'Off hand': '#576778',
              'Icy Touch': '#ACFDFC',
              'Obliterate': '#6AAEF7',
              'OH - Obliterate': '#55BDE0',
              'Frost Strike': '#2087f5',
              'OH - Frost Strike': '#12AADE',
              'Howling Blast': '#60FCFA',
              'Frost Fever': '#9AE3E2',
              'Blood Plague': '#E67F63',
              'Blood Strike': '#F2463D',
              'OH - Blood Strike': '#E6443A',
              'Blood Boil': '#FF3320',
              'Pestilence': '#D7F507',
              'Plague Strike': '#36C219',
              'OH - Plague Strike': '#2EA816',
              'Unbreakable Armor': '#F5A720',
              'Horn of Winter': '#CDD1C9',
              'Empowered Rune Weapon': '#7C9FC4',
              'Blood Tap': '#F54638',
              'Bloody Vengeance': '#DB7F8E',
              'Dancing Rune Weapon': '#FF3864',
              'Heart Strike': '#BC4B51',
              'Bone Shield': '#79B473',
              'Wandering Plague': '#98E02B',
              'Crypt Fever': '#8CB369',
              'Desolation': '#EFF7F6',
              'Scourge Strike': '#5C0029',
              'Blood-Caked Blades': '#91AEC1',
              'Necrosis': '#EAF2EF',
              'Death Coil': '#E2F89C',
              'Unholy Blight': '#0A8754',
              'Death and Decay': '#912F56',
              'Death Strike': '#A0A4B8',
              'Sudden Doom': '#D5E1A3',
              }
    colors_status = {'Hit': '#39CCCC',
              'Crit': '#FFDC00',
              'DOT': '#01FF70',
              'Proc': '#723BFF',
              'Active': '#381D7F',
              'Miss': '#FF4136',
              'Dodge': '#85144b',
              'Parry': '#FF283E',
              'Glance': '#80201B',
              'Block': '#40100D',
              }
    fig = px.timeline(all_data,x_start="Start", x_end="Finish", y="Ability", color="Ability",opacity=1, color_discrete_map=colors, hover_data=["Status", "Damage"], template="plotly_dark")
    fig.update_layout(xaxis=dict(
                          title='Timeline',
                          linecolor = "#BCCCDC",
                          showgrid=False,
                          tickformat = '%H:%M:%S',
                                      ),
                            yaxis=dict(
                            title=None,
                            linecolor="#BCCCDC",
                            showgrid=False,
                            ))
    t_dps = fight_length
    #t_dps = round(max(timeline_order),0)
    total_damage = round(sum(damage_order), 3)
    total_dps = round((t_damage / t_dps), 3)
    #t_damage = "Damage Status Map.                  Total Damage Done - " + str(t_damage) + "                  DPS - " + str(t_dps)
    total_damage = "Total Damage Done - " + str(total_damage) + "                  DPS - " + str(total_dps) + "                  Fight Length - " + str(fight_length) + "                  Number of Targets - " + str(number_of_targets_in_fight)
    fig.update_layout(
        hoverlabel=dict(
            font_size=12,
            font_family="Rockwell",
        )
    )
    all_data_no_zero = all_data.copy()
    all_data_no_zero = all_data_no_zero[all_data_no_zero.Damage != 0]
    fig2 = px.pie(all_data_no_zero, values='Damage', names='Ability', title='Damage by attack',color="Ability",color_discrete_map=colors, template="plotly_dark")
    fig3 = px.treemap(all_data, path=[px.Constant("All Damage"),'Ability', 'Status'], values='Damage',title=total_damage ,color="Ability",color_discrete_map=colors, template="plotly_dark")
    fig4 = px.pie(all_data, names='Status', title='Status Percentage',color="Status",color_discrete_map=colors_status, template="plotly_dark")
    fig5 = px.parallel_categories(all_data2, dimensions=['Ability', 'Status', 'DamageScale'],labels={'Ability':'Ability Name', 'Status':'Damage Status', 'DamageScale':'Damage Sclae'},color="Damage", color_continuous_scale=px.colors.sequential.Plotly3,range_color=(0,2000), template="plotly_dark")
    fig601 = px.line(dps_table_data, x='Time', y="DPS", template="plotly_dark")
    fig602 = px.scatter(dps_table_data,x='Time', y='DPS',color='DPS',template="plotly_dark")
    fig6 = go.Figure(data=fig601.data + fig602.data)
    rune_time_loop_num = 0
    for rune_time in rune_time_tracker:
        rune_0_tracker[rune_time_loop_num] -= rune_time
        if rune_0_tracker[rune_time_loop_num] < 0:
            rune_0_tracker[rune_time_loop_num] = 0
        rune_1_tracker[rune_time_loop_num] -= rune_time
        if rune_1_tracker[rune_time_loop_num] < 0:
            rune_1_tracker[rune_time_loop_num] = 0
        rune_2_tracker[rune_time_loop_num] -= rune_time
        if rune_2_tracker[rune_time_loop_num] < 0:
            rune_2_tracker[rune_time_loop_num] = 0
        rune_3_tracker[rune_time_loop_num] -= rune_time
        if rune_3_tracker[rune_time_loop_num] < 0:
            rune_3_tracker[rune_time_loop_num] = 0
        rune_4_tracker[rune_time_loop_num] -= rune_time
        if rune_4_tracker[rune_time_loop_num] < 0:
            rune_4_tracker[rune_time_loop_num] = 0
        rune_5_tracker[rune_time_loop_num] -= rune_time
        if rune_5_tracker[rune_time_loop_num] < 0:
            rune_5_tracker[rune_time_loop_num] = 0
        rune_6_tracker[rune_time_loop_num] -= rune_time
        if rune_6_tracker[rune_time_loop_num] < 0:
            rune_6_tracker[rune_time_loop_num] = 0
        rune_7_tracker[rune_time_loop_num] -= rune_time
        if rune_7_tracker[rune_time_loop_num] < 0:
            rune_7_tracker[rune_time_loop_num] = 0
        rune_8_tracker[rune_time_loop_num] -= rune_time
        if rune_8_tracker[rune_time_loop_num] < 0:
            rune_8_tracker[rune_time_loop_num] = 0
        rune_9_tracker[rune_time_loop_num] -= rune_time
        if rune_9_tracker[rune_time_loop_num] < 0:
            rune_9_tracker[rune_time_loop_num] = 0
        rune_10_tracker[rune_time_loop_num] -= rune_time
        if rune_10_tracker[rune_time_loop_num] < 0:
            rune_10_tracker[rune_time_loop_num] = 0
        rune_11_tracker[rune_time_loop_num] -= rune_time
        if rune_11_tracker[rune_time_loop_num] < 0:
            rune_11_tracker[rune_time_loop_num] = 0
        rune_time_loop_num += 1

    rune_table_data = pd.DataFrame(dict(Rune0=rune_0_tracker,
    Rune1=rune_1_tracker,
    Rune2=rune_2_tracker,
    Rune3=rune_3_tracker,
    Rune4=rune_4_tracker,
    Rune5=rune_5_tracker,
    Rune6=rune_6_tracker,
    Rune7=rune_7_tracker,
    Rune8=rune_8_tracker,
    Rune9=rune_9_tracker,
    Rune10=rune_10_tracker,
    Rune11=rune_11_tracker,
    RuneTime=rune_time_tracker))
    runic_power_data = pd.DataFrame(dict(Runicpower=runic_power_tracker, Time=rune_time_tracker))
    fig7 = go.Figure()
    # fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["RuneTime"], mode="lines", name="Time", line_color='#ffffff'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune0"], mode="lines", name="Blood1", line_color='#FF4136'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune1"], mode="lines", name="Blood2", line_color='#FF4136'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune2"], mode="lines", name="Frost1", line_color='#39CCCC'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune3"], mode="lines", name="Frost2", line_color='#39CCCC'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune4"], mode="lines", name="Unholy1", line_color='#2ECC40'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune5"], mode="lines", name="Unholy2", line_color='#2ECC40'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune6"], mode="lines", name="Death_Blood1", line_color='#80201B'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune7"], mode="lines", name="Death_Blood2", line_color='#80201B'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune8"], mode="lines", name="Death_Frost1", line_color='#154D4D'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune9"], mode="lines", name="Death_Frost2", line_color='#154D4D'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune10"], mode="lines", name="Death_Unholy1", line_color='#124D18'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune11"], mode="lines", name="Death_Unholy2", line_color='#124D18'))
    fig7.update_layout(yaxis_range=[0, 10])
    # fig7.update_layout(yaxis_range=[0,int(fight_length+1)])
    fig7.update_layout(title="Rune Usage Cooldowns", template="plotly_dark")
    fig7.update_traces(mode="lines", hovertemplate=None)
    fig7.update_layout(hovermode="x")
    fig7.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False)
              )
    fig8 = px.line(runic_power_data, x="Time", y="Runicpower", title='Runic Power Usage', template="plotly_dark")
    fig8.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False)
              )
    fig2.update_layout(
        hoverlabel=dict(
            font_size=12,
            font_family="Rockwell",
        )
    )
    fig3.update_layout(
        hoverlabel=dict(
            font_size=12,
            font_family="Rockwell",
        )
    )
    fig4.update_layout(
        hoverlabel=dict(
            font_size=12,
            font_family="Rockwell",
        )
    )
    fig3.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    fig6.update_layout(title="Damage Over Time", template="plotly_dark")
    fig6.update_traces(line_color='#ffffff', line_width=1)
    fig6.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False)
              )



    return html.Div(children=[
        html.Div([
            html.H1(children='Last Simulation', style={'color': '#ffffff'}),
            dcc.Graph(
                id='graph1',
                figure=fig
            ),
        ]),
        html.Div([
            dcc.Graph(
                id='graph3',
                figure=fig3
            ),
        ]),
        html.Div([
            dcc.Graph(
                id='graph250',
                figure=fig250
            ),
        ]),
         html.Div([
            dcc.Graph(
                id='graph251',
                figure=fig251
            ),
        ]),
        html.Div(children=[
            dcc.Graph(id="graph2",figure=fig2, style={'display': 'inline-block'}),
            dcc.Graph(id="graph4",figure=fig4, style={'display': 'inline-block'})
        ]),
        html.Div([
            dash_table.DataTable(id='table',
                #columns=[{"name": i, "id": i} for i in status_table_data.columns],
                columns=[{"name": "Ability", "id":"Ability"},{"name": "Miss", "id":"Miss"},
                      {"name": "Dodge", "id":"Dodge"},{"name": "Parry", "id":"Parry"},
                      {"name": "Glance", "id":"Glance"},{"name": "Block", "id":"Block"},
                      {"name": "Crit", "id":"Crit"},{"name": "Hit", "id":"Hit"},
                      {"name": "DOT", "id":"DOT"},{"name": "Active", "id":"Active"},
                      {"name": "Proc", "id":"Proc"},{"name": "Average Damage", "id":"Avg_Damage"},
                      {"name": "Total Damage", "id":"All_Damage"},
                      {"name": "Average DPS", "id":"DPSPA"},
                      


                    #  {"name": "Sum - DELETE", "id":"Sum"},{"name": "MissPercentage - DELETE", "id":"MissP"},
                         ],
                data=status_table_data.to_dict('records'),
                tooltip_data=[{
                    'Miss': {'value': '{}'.format(str(row['MissP']) + " Miss Rate"), 'type': 'markdown'},
                    'Dodge': {'value': '{}'.format(str(row['DodgeP']) + " Dodge Rate"), 'type': 'markdown'},
                    'Parry': {'value': '{}'.format(str(row['ParryP']) + " Parry Rate"), 'type': 'markdown'},
                    'Glance': {'value': '{}'.format(str(row['GlanceP']) + " Glance Rate"), 'type': 'markdown'},
                    'Block': {'value': '{}'.format(str(row['BlockP']) + " Block Rate"), 'type': 'markdown'},
                    'Crit': {'value': '{}'.format(str(row['CritP']) + " Crit Rate"), 'type': 'markdown'},
                    'Hit': {'value': '{}'.format(str(row['HitP']) + " Hit Rate"), 'type': 'markdown'},
                    'DOT': {'value': '{}'.format(str(row['DOTP']) + " DOT Rate"), 'type': 'markdown'},
                    'Active': {'value': '{}'.format(str(row['ActiveP']) + " Active Rate"), 'type': 'markdown'},
                    'Proc': {'value': '{}'.format(str(row['ProcP']) + " Proc Rate"), 'type': 'markdown'},
                    'Avg_Damage': {'value': '{}'.format(str(row['Ability'])), 'type': 'markdown'},
                    'All_Damage': {'value': '{}'.format(str(row['Ability'])), 'type': 'markdown'},
                    'DPSPA': {'value': '{}'.format(str(row['Ability'])), 'type': 'markdown'},
                 } for row in status_table_data.to_dict('records')],
                css=[{
                    'selector': '.dash-table-tooltip',
                    'rule': 'background-color: grey !important; font-family: monospace; color: white !important; textAlign: center'
                }],
                tooltip_delay=0,
                tooltip_duration=None,
                style_cell={'textAlign': 'center'},
                style_data={'color': 'white','backgroundColor': 'black'},
                style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': '#4D4B4B',
            },
            {
            "if": {"state": "selected"},
            # "backgroundColor": "#94E66C",
            "backgroundColor": "inherit !important",
            "border": "inherit !important",
            # 'fontWeight': 'bold'
            },
            {
                'if': {
                    'filter_query': '{Miss} > 0',
                    'column_id': 'Miss'
                },
                'backgroundColor': '#FF4136',
                'color': 'white'
            },
            {
                'if': {
                    'column_id': 'Dodge',
                    'filter_query': '{Dodge} > 0'
                },
                'backgroundColor': '#85144b',
            },
            {
                'if': {
                    'column_id': 'Parry',
                    'filter_query': '{Parry} > 0'
                },
                'backgroundColor': '#FF283E',
            },
            {
                'if': {
                    'column_id': 'Glance',
                    'filter_query': '{Glance} > 0'
                },
                'backgroundColor': '#80201B',
            },
            {
                'if': {
                    'column_id': 'Block',
                    'filter_query': '{Block} > 0'
                },
                'backgroundColor': '#40100D',
            },
            {
                'if': {
                    'column_id': 'Crit',
                    'filter_query': '{Crit} > 0'
                },
                'backgroundColor': '#FFDC00',
                'color': 'black'
            },
            {
                'if': {
                    'column_id': 'Hit',
                    'filter_query': '{Hit} > 0'
                },
                'backgroundColor': '#39CCCC',
                'color': 'black'
            },
            {
                'if': {
                    'column_id': 'DOT',
                    'filter_query': '{DOT} > 0'
                },
                'backgroundColor': '#01FF70',
                'color': 'black'
            },
            {
                'if': {
                    'column_id': 'Active',
                    'filter_query': '{Active} > 0'
                },
                'backgroundColor': '#381D7F',
            },
            {
                'if': {
                    'column_id': 'Proc',
                    'filter_query': '{Proc} > 0'
                },
                'backgroundColor': '#723BFF',
            }
        ],
                style_header={
        'backgroundColor': 'rgb(210, 210, 210)',
        'color': 'black',
        'fontWeight': 'bold'
    },
            )
        ]),
        html.Div([

            dcc.Graph(
                id='graph6',
                figure=fig6
            ),
        ]),
        html.Div([

            dcc.Graph(
                id='graph5',
                figure=fig5
            ),
        ]),
        html.Div([

            dcc.Graph(
                id='graph7',
                figure=fig7
            ),
        ]),
        html.Div([

            dcc.Graph(
                id='graph8',
                figure=fig8
            ),
        ]),
        html.Div(children=[
    html.Div(children=[
    html.Div([
            dash_table.DataTable(id='table2',
                columns=[{"name": "N", "id":"Names"},{"name": "D", "id":"Data"},
                          ],
                data=stats_table_data.to_dict('records'),
                style_cell={'textAlign': 'center'},
                style_data={'color': 'white','backgroundColor': 'black'},
                style_header = {'display': 'none'},
                style_data_conditional=[
                    {
            'if': {'column_id': 'Data'},
            "fontWeight": "bold",
            'textAlign': 'right'

        },
                    {
            'if': {'column_id': 'Names'},
            "fontWeight": "italic",
            'textAlign': 'right'

        },
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': '#4D4B4B',
            },]
        )
        ],style={'display': 'inline-block', 'float': 'left', 'padding-left': '250px'}),
    html.Div([
            dash_table.DataTable(id='table3',
                #columns=[{"name": "N", "id":"Names"},{"name": "D", "id":"Data"},
                #          ],
                columns=[{"name": "D", "id":"Data"},{"name": "N", "id":"Names"},
                          ],
                data=gear_table_data.to_dict('records'),
                style_cell={'textAlign': 'center'},
                style_data={'color': 'white','backgroundColor': 'black'},
                style_header = {'display': 'none'},
                style_data_conditional=[
                    {
            'if': {'column_id': 'Data'},
            "fontWeight": "bold",
            'textAlign': 'left'

        },
                    {
            'if': {'column_id': 'Names'},
            "fontWeight": "italic",
            'textAlign': 'left'

        },
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': '#4D4B4B',
            },]
        )
        ],style={'display': 'inline-block', 'float': 'right', 'padding-right': '250px'}),
    ])
        ]),
        html.Div(
        [   html.H1(
            html.I("Buff'd Stats & Gear", style={'color': '#ffffff'}), style={'textAlign': 'center'}),
            html.Br(),
        ]),
        html.Div(
        [   html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
            html.H1(
            html.I("", style={'color': '#ffffff'}), style={'textAlign': 'center'}),
            html.Br(),
        ])
    ])



serverad.layout = html.Div(children=[
all_angrydread_stuff()
])




#Last Laugh Data: Souled2
serverll = dash.Dash(server=app, routes_pathname_prefix="/lastlaugh/",title="Last Laugh", update_title='Loading Last Laugh...', external_stylesheets=external_stylesheets)

def all_lastlaugh_stuff():
    dash_username = "Last Laugh"
    t_damage = 635036.9553971434
    fight_length = 81.5
    rotation = ['Main hand', 'Rune of Razoricce', 'Off hand', 'Icy Touch', 'Ghoul - Claw', 'Ghoul - Main hand', 'Off hand', 'Darkmoon Card: Greatness', 'Grim Toll', 'Frost Fever', 'OH - Plague Strike', 'Plague Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Hyperspeed Acceleration', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'Unbreakable Armor', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Rune of the Fallen Crusader', 'Frost Fever', 'OH - Blood Strike', 'Blood Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Shattering Throw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Off hand', 'Ghoul - Main hand', 'Frost Fever', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Ghoul - Main hand', 'Off hand', 'Main hand', 'Rune of Razoricce', 'Ghoul - Claw', 'Ghoul - Main hand', 'Blood Plague', 'Off hand', 'Ghoul - Main hand', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Ghoul - Main hand', 'Main hand', 'Rune of Razoricce', 'Ghoul - Main hand', 'Off hand', 'Frost Fever', 'Ghoul - Main hand', 'Main hand', 'Rune of Razoricce', 'Off hand', 'OH - Obliterate', 'Obliterate', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Blood Strike', 'Blood Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'Pestilence', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Empowered Rune Weapon', 'Main hand', 'Rune of Razoricce', 'Off hand', 'OH - Obliterate', 'Obliterate', 'Ghoul - Claw', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Blood Strike', 'Blood Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Off hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Ghoul - Claw', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'OH - Obliterate', 'Obliterate', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Off hand', 'Frost Fever', 'Blood Plague', 'Pestilence', 'Ghoul - Main hand', 'Main hand', 'Rune of Razoricce', 'Off hand', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Blood Strike', 'Blood Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Ghoul - Claw', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Off hand', 'Blood Plague', 'OH - Blood Strike', 'Blood Strike', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'Pestilence', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'Howling Blast', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Main hand', 'Off hand', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Ghoul - Claw', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Blood Strike', 'Blood Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Grim Toll', 'Frost Fever', 'OH - Blood Strike', 'Blood Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Darkmoon Card: Greatness', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'Blood Tap', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Pestilence', 'Ghoul - Claw', 'Ghoul - Main hand', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'OH - Obliterate', 'Obliterate', 'Ghoul - Claw', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Blood Strike', 'Blood Strike', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Ghoul - Claw', 'Ghoul - Main hand', 'Ghoul - Main hand', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Hyperspeed Acceleration', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'Horn of Winter', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'Pestilence', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'Unbreakable Armor', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Blood Strike', 'Blood Strike', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'Off hand', 'Off hand', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Off hand', 'Off hand', 'Off hand', 'Off hand', 'Off hand', 'Off hand', 'Off hand', 'Off hand', 'Off hand', 'Blood Plague', 'Off hand', 'Off hand', 'Off hand', 'Main hand', 'Rune of Razoricce', 'Off hand', 'OH - Blood Strike', 'Blood Strike', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Obliterate', 'Obliterate', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Rune of the Fallen Crusader', 'Blood Plague', 'OH - Obliterate', 'Obliterate', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'OH - Frost Strike', 'Frost Strike', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'Pestilence', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Blood Plague', 'OH - Frost Strike', 'Frost Strike', 'Rune of Razorice', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Frost Fever', 'OH - Frost Strike', 'Frost Strike', 'Rune of Razorice', 'Off hand', 'Blood Plague', 'Main hand', 'Rune of Razoricce', 'Off hand', 'Off hand', 'Off hand', 'Horn of Winter']
    rotation_time = [0, 0, 0, 0, 0, 0, 0.9882943860831215, 1.1929022082018927, 1.1929022082018927, 0, 1.1929022082018927, 1.1929022082018927, 0.7425624752082507, 0.7425624752082507, 1.4851249504165014, 2.3858044164037855, 2.3858044164037855, 1.5442099782548775, 2.3858044164037855, 1.976588772166243, 1.1929022082018927, 2.3858044164037855, 2.227687425624752, 2.227687425624752, 2.8353827846092816, 2.8310516268006087, 3.5787066246056782, 2.964883158249364, 3.5787066246056782, 3, 3.5787066246056782, 3.5787066246056782, 3.4430781435938114, 4.656057051956106, 3.9932419475669816, 4.656057051956106, 3.857445324597938, 4.192902208201893, 4.656057051956106, 4.656057051956106, 5.733407479306533, 4.050773502578341, 4.658468861562871, 5.733407479306533, 5.155432268333355, 5.733407479306533, 4.750007490946512, 5.436593772753107, 5.266164220547401, 6, 6.049424822769026, 6.133407479306531, 6.123180054559702, 5.87385957953193, 6.809766336366297, 6.943417377204698, 7.033407479306528, 6.48155493851646, 6.48155493851646, 7.192902208201893, 7.496352618172892, 7.08925029750099, 7.837409931640369, 7.933407479306525, 8.182938899979488, 7.69694565648552, 8.73140248607604, 8.733407479306523, 8.30464101547005, 8.869525181786084, 9, 8.912336374454581, 9.625395040511712, 9.63340747930652, 9.55611146359268, 10.033407479306518, 10.033407479306518, 9.520031733439112, 9.520031733439112, 10.127727092423642, 11.110757906656946, 10.519387594947384, 11.110757906656946, 10.242697745399276, 10.192902208201893, 11.110757906656946, 11.110757906656946, 10.735422451408173, 11.343117810392704, 12.188108334007374, 11.413380149383055, 12.188108334007374, 10.929284027205872, 12, 12.188108334007374, 12.188108334007374, 11.950813169377234, 13.265458761357802, 12.307372703818727, 13.265458761357802, 11.615870309012468, 13.192902208201893, 13.265458761357802, 12.693375644585485, 13.435938119793736, 13.297250895007751, 14.458360969559696, 12.37609675984564, 14.458360969559696, 14.287129086196776, 14.458360969559696, 13.13632321067881, 14.458360969559696, 14.458360969559696, 14.178500595001987, 14.178500595001987, 15.651263177761589, 15.2770072773858, 15.651263177761589, 13.896549661511981, 15, 15.651263177761589, 15.651263177761589, 14.921063070210238, 15.861959539865136, 16.844165385963482, 16.266885468574824, 16.844165385963482, 14.656776112345153, 16.192902208201893, 16.844165385963482, 16.844165385963482, 16.802856009520035, 18.260457520794944, 17.442134107552054, 18.260457520794944, 15.559367067079666, 18, 18.260457520794944, 18.260457520794944, 17.743752479174933, 17.743752479174933, 18.68464894882983, 19.676749655626406, 18.617382746529284, 19.676749655626406, 16.46195802181418, 19.192902208201893, 19.676749655626406, 19.676749655626406, 19.62554541848473, 21.093041790457868, 19.792631385506514, 21.093041790457868, 17.364548976548694, 21, 21.093041790457868, 21.093041790457868, 20.56644188813963, 21.507338357794527, 22.50933392528933, 20.967880024483744, 18.267139931283207, 22.192902208201893, 22.50933392528933, 22.50933392528933, 22.448234827449426, 22.448234827449426, 23.92562606012079, 22.143128663460974, 23.92562606012079, 19.16973088601772, 23.92562606012079, 23.92562606012079, 23.389131297104324, 24.330027766759223, 25.341918194952253, 23.318377302438204, 20.072321840752235, 24, 25.192902208201893, 25.341918194952253, 25.27092423641412, 24.493625941415434, 26.758210329783715, 20.97491279548675, 26.758210329783715, 26.758210329783715, 26.21182070606902, 26.21182070606902, 27.152717175723918, 28.174502464615177, 25.668874580392664, 28.174502464615177, 21.877503750221262, 27, 28.174502464615177, 28.174502464615177, 28.093613645378817, 29.59079459944664, 26.844123219369894, 29.59079459944664, 22.780094704955776, 28.192902208201893, 29.59079459944664, 29.59079459944664, 29.034510115033715, 29.034510115033715, 29.975406584688614, 31.0070867342781, 28.019371858347125, 31.0070867342781, 23.68268565969029, 30, 31.0070867342781, 31.0070867342781, 30.916303054343512, 32.42337886910956, 29.194620497324355, 32.42337886910956, 24.585276614424803, 31.192902208201893, 32.42337886910956, 32.42337886910956, 31.85719952399841, 32.79809599365331, 33.83967100394102, 30.369869136301585, 33.83967100394102, 25.487867569159317, 33, 33.83967100394102, 33.83967100394102, 33.738992463308215, 33.738992463308215, 35.25596313877248, 31.545117775278815, 26.39045852389383, 34.19290220820189, 35.25596313877248, 35.25596313877248, 34.67988893296312, 35.62078540261802, 36.67225527360394, 33.07294100594922, 36.67225527360394, 27.5638267650487, 36, 36.67225527360394, 36.67225527360394, 36.56168187227292, 38.088547408435396, 34.60076423661962, 38.088547408435396, 28.737195006203567, 37.19290220820189, 38.088547408435396, 37.50257834192782, 37.50257834192782, 38.443474811582725, 36.12858746729002, 39.504839543266854, 29.910563247358436, 39, 39.504839543266854, 39.504839543266854, 39.38437128123763, 40.92113167809831, 37.65641069796042, 40.92113167809831, 31.083931488513304, 40.19290220820189, 40.92113167809831, 40.32526775089253, 41.26616422054743, 39.18423392863082, 32.25729972966817, 42, 42.33742381292977, 42.33742381292977, 42.20706069020233, 42.20706069020233, 43.75371594776123, 40.71205715930122, 43.75371594776123, 33.43066797082304, 43.19290220820189, 43.75371594776123, 43.75371594776123, 43.147957159857235, 44.08885362951214, 45.17000808259269, 42.23988038997162, 45.17000808259269, 34.604036211977906, 45, 45.17000808259269, 45.17000808259269, 45.02975009916704, 46.586300217424146, 43.76770362064202, 46.586300217424146, 35.777404453132775, 46.19290220820189, 46.586300217424146, 46.586300217424146, 45.97064656882194, 45.97064656882194, 46.91154303847684, 48.002592352255604, 45.29552685131242, 48.002592352255604, 36.95077269428764, 48.002592352255604, 48, 48.002592352255604, 48.002592352255604, 47.852439508131745, 49.41888448708706, 49.41888448708706, 46.82335008198282, 49.41888448708706, 38.12414093544251, 49.19290220820189, 49.41888448708706, 49.41888448708706, 49.41888448708706, 48.79333597778665, 49.73423244744155, 50.83517662191852, 48.351173312653216, 50.83517662191852, 39.29750917659738, 50.83517662191852, 50.67512891709645, 50.67512891709645, 49.878996543323616, 52.25146875674998, 40.47087741775225, 51, 52.19290220820189, 52.25146875674998, 52.25146875674998, 51.61602538675135, 52.556921856406255, 53.66776089158144, 51.406819773994016, 53.66776089158144, 41.64424565890712, 53.66776089158144, 53.66776089158144, 53.49781832606116, 53.49781832606116, 55.084053026412896, 52.934643004664416, 55.084053026412896, 42.817613900061986, 54, 55.084053026412896, 55.084053026412896, 54.43871479571606, 55.37961126537096, 56.500345161244354, 54.462466235334816, 56.500345161244354, 43.990982141216854, 55.19290220820189, 56.500345161244354, 56.500345161244354, 56.32050773502586, 57.91663729607581, 55.990289466005216, 57.91663729607581, 45.16435038237172, 57, 57.91663729607581, 57.91663729607581, 57.261404204680765, 57.261404204680765, 58.20230067433567, 59.33292943090727, 57.518112696675615, 59.33292943090727, 46.33771862352659, 58.19290220820189, 59.33292943090727, 59.33292943090727, 60.74922156573873, 60.74922156573873, 59.045935927346015, 60.74922156573873, 47.51108686468146, 60, 60.74922156573873, 60.573759158016415, 62.16551370057019, 48.68445510583633, 61.19290220820189, 62.16551370057019, 62.16551370057019, 63.581805835401646, 62.101582388686815, 63.581805835401646, 49.857823346991196, 63, 63.581805835401646, 63.629405619357215, 64.9980979702331, 51.031191588146065, 64.1929022082019, 64.9980979702331, 65.15722885002762, 66.41439010506457, 52.20455982930093, 66, 66.41439010506457, 66.41439010506457, 67.83068223989603, 66.68505208069803, 67.83068223989603, 53.3779280704558, 67.1929022082019, 67.83068223989603, 67.83068223989603, 69.02358444809792, 67.97189372924376, 69.02358444809792, 54.36622245653892, 69, 55.35451684262204, 56.34281122870516, 69.25873537778949, 69.3235844480979, 57.33110561478828, 58.3194000008714, 59.307694386954516, 60.295988773037635, 61.284283159120754, 62.27257754520387, 63.26087193128699, 64.24916631737011, 65.23746070345324, 66.22575508953636, 70.1929022082019, 67.21404947561949, 68.20234386170262, 69.19063824778574, 70.54557702633522, 70.62358444809783, 70.17893263386887, 71.1235844480978, 71.1235844480978, 72.31648665629969, 71.83241867488096, 72.31648665629969, 71.167227019952, 72, 72.31648665629969, 72.31648665629969, 73.50938886450157, 73.11926032342669, 73.50938886450157, 72.15552140603512, 73.50938886450157, 73.1929022082019, 73.50938886450157, 73.50938886450157, 74.70229107270346, 74.40610197197242, 74.70229107270346, 73.14381579211825, 74.70229107270346, 74.70229107270346, 75.89519328090535, 75.69294362051815, 75.89519328090535, 74.13211017820137, 75, 75.89519328090535, 76.97978526906388, 77.08809548910723, 75.1204045642845, 76.1929022082019, 77.08809548910723, 77.08809548910723, 78.28099769730912, 78.26662691760961, 78.28099769730912, 76.10869895036763, 78, 78.28099769730912, 78.28099769730912, 79.473899905511, 77.09699333645075, 79.1929022082019, 79.55346856615535, 79.573899905511, 78.08528772253388, 79.073582108617, 80.06187649470013, 80.77389990551093]
    rotation_damage = [2710.7621742768824, 54.21524348553765, 1355.9201020317892, 1340.0706040120765, 213.87892342053885, 165.35468999984562, 1192.3460597049288, 0, 0, 445.5923923536017, 0, 1934.4283553393534, 283.8673280158771, 173.35319272466887, 325.7353696003895, 0, 38.68856710678707, 3488.356644606673, 69.76713289213346, 1649.511593877207, 710.4718678675058, 0, 306.41565478025876, 187.12309172123827, 114.27305005165435, 3702.2467276251277, 74.04493455250255, 860.6685056943573, 0, 507.7481458992018, 2358.405405147563, 2363.2948012614547, 203.33758957165662, 47.2658960252291, 4436.545825894215, 88.73091651788431, 1075.5254941727642, 853.3467931289101, 6673.75473121745, 5294.195075869808, 0, 342.67847349079307, 327.2292011774925, 105.88390151739615, 2217.827653851529, 44.356553077030576, 1113.237542091528, 662.8850218665536, 176.11381738718703, 650.4959395624174, 2122.3761474931102, 42.447522949862204, 2208.4768124642155, 115.09467678510434, 1030.2994954081455, 4348.594695074781, 86.97189390149562, 278.4944680061521, 265.9388591575839, 853.3467931289101, 676.5043221640356, 0, 4121.7460419146755, 82.43492083829351, 2227.971618595162, 196.16705608270718, 2209.67935452825, 44.193587090564996, 121.301631619432, 1026.8073671267398, 650.4959395624174, 179.93348190061943, 2094.4391212418655, 41.88878242483731, 1990.4894348181751, 2879.943474977878, 3756.2464197300706, 304.2772034718208, 188.86348590651193, 180.34878875006126, 75.12492839460141, 4443.114967224826, 88.86229934449652, 0.0, 853.3467931289101, 6961.715704338376, 10166.331196548637, 196.16705608270718, 187.32308570590533, 203.32662393097274, 4282.43050456975, 85.648610091395, 0.0, 650.4959395624174, 6846.393561493765, 2663.563754169547, 152.59090787854288, 53.27127508339094, 3700.6128206653484, 74.01225641330697, 957.0875309201881, 853.3467931289101, 116.43818999999999, 182.21564500134164, 0, 1923.2746321585798, 38.4654926431716, 1828.3431787961622, 0, 1134.0667730767868, 22.68133546153574, 897.6522848855494, 2511.294814758681, 8014.14754846785, 263.4485551277462, 216.79428308446225, 160.28295096935702, 3596.7591325308995, 71.93518265061799, 1887.9063234615082, 650.4959395624174, 2485.321041849405, 8107.191374978411, 99.71628505563311, 0, 162.14382749956823, 3329.4113609838037, 66.58822721967607, 518.769451758981, 853.3467931289101, 2242.682258312964, 2166.6183244044423, 98.20869543276176, 43.332366488088844, 1033.8916194224919, 20.67783238844984, 543.1122694374375, 588.3401860168175, 5040.9694887378155, 4038.843019845274, 216.19829207111013, 167.1478469789299, 83.9967865302406, 80.77686039690548, 3114.134255948128, 62.28268511896256, 724.5854049829861, 791.1356834893061, 5222.885434069482, 1726.3700054922692, 164.23338968569132, 34.52740010984539, 1007.3293999451946, 20.146587998903893, 765.135392516616, 527.1625601611536, 1944.434930539058, 4026.078830630045, 288.26438942814684, 222.86379597190654, 80.52157661260091, 0.0, 1447.0452052983123, 729.90357266299, 5012.856393560574, 6784.696790965614, 209.24018611939624, 323.536752083354, 135.6939358193123, 1353.2571238722307, 27.065142477444617, 1315.7440214602798, 4369.032843760741, 6390.351415836121, 302.1806013315746, 233.62273784641235, 127.80702831672242, 0.0, 391.4338808309433, 445.5923923536017, 648.2607582279018, 113.06317, 0, 1259.0134443706838, 25.18026888741368, 412.1085880215951, 0, 3452.400696462894, 211.55955476996755, 163.5615330207613, 126.45316404257855, 69.04801392925788, 2823.6378292158843, 56.472756584317686, 675.0092129240886, 445.5923923536017, 1812.84144253966, 4595.2803565497325, 104.74158379853759, 91.90560713099465, 811.0077318398239, 16.22015463679648, 1183.7368995824627, 648.2607582279018, 1592.9081843263343, 1304.6790776797604, 246.350084528537, 123.79827700956682, 95.71128089691018, 26.09358155359521, 1350.4298134871844, 27.00859626974369, 429.56722964925666, 445.5923923536017, 4207.9923967139675, 1443.1630021876424, 316.0968132350024, 28.86326004375285, 1311.7899048915501, 26.235798097831005, 405.21701895804455, 648.2607582279018, 4444.699043424376, 6645.935023588841, 94.69098631272863, 146.41553676361232, 132.91870047177684, 859.4018612638685, 17.18803722527737, 609.2742464717596, 445.5923923536017, 4757.45266870073, 2491.3250228943343, 485.7420631053601, 375.5383044767988, 49.82650045788669, 0.0, 0.0, 648.2607582279018, 4645.525296110307, 4794.851714699003, 143.35907183054965, 110.83417899292516, 95.89703429398007, 1289.171421811179, 25.78342843622358, 635.4268675334387, 445.5923923536017, 1674.7002522388016, 3506.063217209697, 91.1732771926955, 70.12126434419395, 895.5443123527115, 17.91088624705423, 395.1093843315036, 648.2607582279018, 118.1257, 233.59355695039486, 361.19304864412436, 279.2466112764851, 2645.7151866849135, 52.91430373369827, 698.3345236007216, 445.5923923536017, 1646.7870862051818, 3413.763681525196, 107.75676304428025, 68.27527363050392, 2509.8817714193347, 50.1976354283867, 435.0804849000972, 648.2607582279018, 3299.1949416289835, 162.6871439186438, 81.75514998210802, 0.0, 424.0539743984163, 445.5923923536017, 4598.5536494071, 6780.452711879746, 231.27418829982355, 357.60673468595576, 135.60905423759493, 839.7991759275467, 16.795983518550933, 596.5513497390507, 648.2607582279018, 4608.642476028916, 2507.597323897266, 326.9205336043351, 252.7497456233116, 50.15194647794532, 860.6270290973885, 17.21254058194777, 666.5272817689494, 445.5923923536017, 1690.928837142069, 3559.7257379565017, 98.7112253070522, 71.19451475913003, 2747.1119614606287, 54.942239229212575, 437.83711252551757, 648.2607582279018, 4614.480862620423, 4753.4591367124885, 225.47576667339533, 113.30830868192362, 56.940810117990296, 95.06918273424978, 2789.2011887260196, 55.78402377452039, 446.56643333934824, 0, 445.5923923536017, 4542.413427733183, 4657.369223529506, 195.82148065019604, 93.14738447059011, 0, 1507.0717133171306, 30.141434266342614, 1677.3822422302146, 648.2607582279018, 0, 1958.608976513424, 4007.6131739043494, 168.57558580990147, 158.37905805578038, 80.152263478087, 1113.2393691243792, 22.264787382487583, 896.7444192469451, 118.1257, 598.738605332779, 562.5230716455702, 3788.267739273854, 75.76535478547709, 823.7336418190887, 507.7481458992018, 710.4718678675058, 5869.070469854024, 8454.31991833552, 191.1239125742832, 116.71628673282669, 169.0863983667104, 1852.3985383217669, 37.04797076643534, 920.7950282820038, 6377.830491857128, 9121.232202972446, 269.7746237881385, 164.747005851813, 182.42464405944892, 3488.356644606673, 69.76713289213346, 554.4096693136503, 507.7481458992018, 2436.095314458223, 6117.8657405823205, 177.97072196172718, 108.68384565149451, 122.35731481164642, 1694.351678948524, 33.88703357897048, 870.9759095665253, 710.4718678675058, 6340.885762183543, 2138.585296279209, 191.1239125742832, 42.771705925584186, 1797.425717670204, 35.94851435340408, 1785.5177879704638, 507.7481458992018, 2522.351746496546, 5189.753626942958, 305.00638435748493, 286.5576508214657, 269.2248144815003, 103.79507253885917, 1600.4397770021046, 32.008795540042094, 1619.869218241497, 710.4718678675058, 2494.9628263452287, 2056.124031307501, 0, 41.12248062615002, 921.5945309249212, 18.431890618498425, 759.8398983412586, 507.7481458992018, 0, 966.9257407651653, 19.338514815303306, 1460.687972469325, 710.4718678675058, 2166.7794824743564, 7692.126826815549, 153.84253653631097, 1535.6423392614279, 30.712846785228557, 462.1947162294852, 507.7481458992018, 118.1257, 947.9356393456035, 18.95871278691207, 1526.691533408233, 710.4718678675058, 0, 2859.9876163996314, 57.19975232799263, 1285.6119610316473, 445.5923923536017, 4559.691325066769, 3804.1826758725647, 76.0836535174513, 973.6372845233915, 19.47274569046783, 1511.61390621681, 729.90357266299, 4935.484770169814, 4925.330010580569, 98.50660021161139, 1436.6451229753663, 28.73290245950733, 1458.5240854616004, 527.1625601611536, 0.0, 1365.2581841348822, 952.1968474367897, 19.043936948735794, 774.3241512680169, 743.9305646287678, 1494.3955859718774, 465.6367874434675, 0.0, 1528.8322264617425, 1365.2581841348822, 709.2960124119493, 716.3642883745654, 1395.3902445635144, 729.90357266299, 505.1484500744911, 1536.0065265637977, 1528.8322264617425, 999.978392944074, 19.99956785888148, 0.0, 1986.9853474989286, 1981.8475266467506, 39.63695053293501, 1396.1203407897012, 27.922406815794027, 493.6625016352401, 527.1625601611536, 2213.7519422609075, 8005.641895273182, 160.11283790546364, 2836.0374384969746, 56.72074876993949, 457.82634250477685, 0, 729.90357266299, 2302.598705736916, 7854.982084387371, 157.09964168774744, 3348.530493833967, 66.97060987667933, 1581.1227902680066, 5796.325812215336, 4706.738297512286, 94.13476595024574, 1713.608112816701, 34.27216225633402, 1579.6879302475957, 591.7383297739153, 114.75068000000002, 3426.969508283105, 68.5393901656621, 1654.3006513089704, 794.5368536430693, 2217.2664504818767, 4310.064944151912, 86.20129888303823, 3449.9272686096806, 68.99854537219362, 1561.0347499822517, 591.7383297739153, 5852.220693825205, 1927.9293573892933, 38.558587147785865, 1563.904470023074, 794.5368536430693, 1113.845273330856, 22.27690546661712, 837.5449122966129, 520.5134202391562, 803.617187676056, 0]
    rotation_status = ['Crit', 'Active', 'Crit', 'Hit', 'Hit', 'Hit', 'Crit', 'Proc', 'Proc', 'DOT', 'Dodge', 'Crit', 'Hit', 'Glance', 'Crit', 'Active', 'Active', 'Crit', 'Active', 'Crit', 'DOT', 'Active', 'Hit', 'Glance', 'Glance', 'Crit', 'Active', 'Hit', 'Proc', 'DOT', 'Hit', 'Hit', 'Hit', 'Active', 'Crit', 'Active', 'Hit', 'DOT', 'Crit', 'Crit', 'Active', 'Crit', 'Hit', 'Active', 'Hit', 'Active', 'Hit', 'Glance', 'Hit', 'DOT', 'Hit', 'Active', 'Crit', 'Glance', 'Hit', 'Crit', 'Active', 'Hit', 'Hit', 'DOT', 'Glance', 'Dodge', 'Crit', 'Active', 'Crit', 'Hit', 'Hit', 'Active', 'Glance', 'Hit', 'DOT', 'Hit', 'Hit', 'Active', 'Crit', 'Hit', 'Hit', 'Hit', 'Glance', 'Hit', 'Active', 'Crit', 'Active', 'Miss', 'DOT', 'Crit', 'Crit', 'Hit', 'Hit', 'Active', 'Crit', 'Active', 'Miss', 'DOT', 'Crit', 'Hit', 'Hit', 'Active', 'Crit', 'Active', 'Hit', 'DOT', 'Hit', 'Hit', 'Dodge', 'Hit', 'Active', 'Crit', 'Active', 'Glance', 'Active', 'Hit', 'Hit', 'Crit', 'Hit', 'Hit', 'Active', 'Crit', 'Active', 'Crit', 'DOT', 'Hit', 'Crit', 'Glance', 'Dodge', 'Active', 'Crit', 'Active', 'Glance', 'DOT', 'Hit', 'Hit', 'Glance', 'Active', 'Glance', 'Active', 'Glance', 'DOT', 'Crit', 'Crit', 'Hit', 'Hit', 'Glance', 'Active', 'Crit', 'Active', 'Hit', 'DOT', 'Crit', 'Hit', 'Hit', 'Active', 'Glance', 'Active', 'Hit', 'DOT', 'Hit', 'Crit', 'Crit', 'Hit', 'Active', 'Dodge', 'Crit', 'DOT', 'Crit', 'Crit', 'Hit', 'Crit', 'Active', 'Hit', 'Active', 'Crit', 'Crit', 'Crit', 'Crit', 'Hit', 'Active', 'Dodge', 'Glance', 'DOT', 'DOT', 'Hit', 'Dodge', 'Hit', 'Active', 'Glance', 'Dodge', 'Crit', 'Hit', 'Hit', 'Hit', 'Active', 'Crit', 'Active', 'Hit', 'DOT', 'Hit', 'Crit', 'Glance', 'Active', 'Glance', 'Active', 'Crit', 'DOT', 'Hit', 'Hit', 'Hit', 'Glance', 'Hit', 'Active', 'Hit', 'Active', 'Glance', 'DOT', 'Crit', 'Hit', 'Crit', 'Active', 'Hit', 'Active', 'Glance', 'DOT', 'Crit', 'Crit', 'Glance', 'Crit', 'Active', 'Glance', 'Active', 'Hit', 'DOT', 'Crit', 'Hit', 'Crit', 'Hit', 'Active', 'Dodge', 'Miss', 'DOT', 'Crit', 'Crit', 'Hit', 'Hit', 'Active', 'Hit', 'Active', 'Hit', 'DOT', 'Hit', 'Crit', 'Glance', 'Active', 'Glance', 'Active', 'Glance', 'DOT', 'Hit', 'Hit', 'Crit', 'Hit', 'Crit', 'Active', 'Hit', 'DOT', 'Hit', 'Crit', 'Glance', 'Active', 'Crit', 'Active', 'Glance', 'DOT', 'Hit', 'Hit', 'Glance', 'Dodge', 'Glance', 'DOT', 'Crit', 'Crit', 'Hit', 'Crit', 'Active', 'Glance', 'Active', 'Hit', 'DOT', 'Crit', 'Hit', 'Crit', 'Hit', 'Active', 'Glance', 'Active', 'Hit', 'DOT', 'Hit', 'Crit', 'Glance', 'Active', 'Crit', 'Active', 'Glance', 'DOT', 'Crit', 'Crit', 'Hit', 'Glance', 'Glance', 'Active', 'Crit', 'Active', 'Glance', 'Proc', 'DOT', 'Crit', 'Crit', 'Hit', 'Active', 'Proc', 'Hit', 'Active', 'Crit', 'DOT', 'Active', 'Hit', 'Crit', 'Hit', 'Hit', 'Active', 'Glance', 'Active', 'Hit', 'Hit', 'Crit', 'Hit', 'Crit', 'Active', 'Hit', 'DOT', 'DOT', 'Crit', 'Crit', 'Hit', 'Glance', 'Active', 'Hit', 'Active', 'Hit', 'Crit', 'Crit', 'Hit', 'Glance', 'Active', 'Crit', 'Active', 'Glance', 'DOT', 'Hit', 'Crit', 'Hit', 'Glance', 'Active', 'Hit', 'Active', 'Hit', 'DOT', 'Crit', 'Hit', 'Hit', 'Active', 'Hit', 'Active', 'Crit', 'DOT', 'Hit', 'Crit', 'Hit', 'Hit', 'Hit', 'Active', 'Hit', 'Active', 'Crit', 'DOT', 'Hit', 'Hit', 'Active', 'Active', 'Glance', 'Active', 'Hit', 'DOT', 'Active', 'Glance', 'Active', 'Crit', 'DOT', 'Hit', 'Crit', 'Active', 'Hit', 'Active', 'Glance', 'DOT', 'Hit', 'Glance', 'Active', 'Crit', 'DOT', 'Active', 'Crit', 'Active', 'Crit', 'DOT', 'Crit', 'Crit', 'Active', 'Glance', 'Active', 'Crit', 'DOT', 'Crit', 'Crit', 'Active', 'Hit', 'Active', 'Crit', 'DOT', 'Miss', 'Crit', 'Glance', 'Active', 'Hit', 'Hit', 'Crit', 'Glance', 'Miss', 'Crit', 'Crit', 'Hit', 'Hit', 'Crit', 'DOT', 'Glance', 'Crit', 'Crit', 'Glance', 'Active', 'Miss', 'Hit', 'Hit', 'Active', 'Hit', 'Active', 'Glance', 'DOT', 'Hit', 'Crit', 'Active', 'Crit', 'Active', 'Glance', 'Proc', 'DOT', 'Hit', 'Crit', 'Active', 'Crit', 'Active', 'Crit', 'Crit', 'Crit', 'Active', 'Hit', 'Active', 'Crit', 'DOT', 'Hit', 'Crit', 'Active', 'Crit', 'DOT', 'Hit', 'Crit', 'Active', 'Crit', 'Active', 'Crit', 'DOT', 'Crit', 'Hit', 'Active', 'Crit', 'DOT', 'Glance', 'Active', 'Hit', 'Glance', 'Hit', 'Active']
    rune_0_tracker = [0, 0, 0, 0, 0, 0, 0, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 20.765458761357802, 20.765458761357802, 0, 0, 0, 0, 0, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 35.67450246461517, 35.67450246461517, 35.67450246461517, 35.67450246461517, 35.67450246461517, 35.67450246461517, 35.67450246461517, 35.67450246461517, 35.67450246461517, 35.67450246461517, 35.67450246461517, 35.67450246461517, 35.67450246461517, 35.67450246461517, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 55.502592352255604, 55.502592352255604, 10000, 10000, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 58.33517662191852, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 78.6235844480978, 78.6235844480978, 78.6235844480978, 78.6235844480978, 78.6235844480978, 78.6235844480978, 78.6235844480978, 78.6235844480978, 78.6235844480978, 78.6235844480978, 78.6235844480978, 78.6235844480978, 78.6235844480978, 78.6235844480978, 78.6235844480978, 78.6235844480978, 78.6235844480978, 78.6235844480978, 78.6235844480978, 78.6235844480978, 78.6235844480978, 78.6235844480978, 78.6235844480978, 78.6235844480978, 78.6235844480978, 78.6235844480978, 78.6235844480978]
    rune_1_tracker = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19.688108334007374, 19.688108334007374, 19.688108334007374, 19.688108334007374, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 42.75596313877248, 42.75596313877248, 42.75596313877248, 42.75596313877248, 42.75596313877248, 42.75596313877248, 42.75596313877248, 42.75596313877248, 42.75596313877248, 42.75596313877248, 42.75596313877248, 42.75596313877248, 42.75596313877248, 42.75596313877248, 42.75596313877248, 42.75596313877248, 54.086300217424146, 54.086300217424146, 54.086300217424146, 54.086300217424146, 54.086300217424146, 54.086300217424146, 54.086300217424146, 54.086300217424146, 54.086300217424146, 54.086300217424146, 54.086300217424146, 54.086300217424146, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 75.33068223989603, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
    rune_2_tracker = [0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 0, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969]
    rune_3_tracker = [0, 0, 0, 0, 0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 0, 0, 0, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 73.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159]
    rune_4_tracker = [0, 0, 0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 0, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 21.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 31.958360969559696, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 41.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 51.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 61.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 71.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969, 81.95836096955969]
    rune_5_tracker = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 0, 0, 0, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 23.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 33.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 43.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 53.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 63.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159, 83.15126317776159]
    rune_6_tracker = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 11.078706624605678, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 24.344165385963482, 24.344165385963482, 24.344165385963482, 24.344165385963482, 24.344165385963482, 24.344165385963482, 24.344165385963482, 24.344165385963482, 24.344165385963482, 24.344165385963482, 24.344165385963482, 24.344165385963482, 24.344165385963482, 24.344165385963482, 24.344165385963482, 24.344165385963482, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 45.67450246461517, 45.67450246461517, 45.67450246461517, 45.67450246461517, 45.67450246461517, 45.67450246461517, 45.67450246461517, 45.67450246461517, 45.67450246461517, 45.67450246461517, 45.67450246461517, 45.67450246461517, 45.67450246461517, 45.67450246461517, 10000, 10000, 49.41888448708706, 49.41888448708706, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 71.08180583540164, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
    rune_7_tracker = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 32.84191819495226, 32.84191819495226, 32.84191819495226, 32.84191819495226, 32.84191819495226, 32.84191819495226, 32.84191819495226, 32.84191819495226, 32.84191819495226, 32.84191819495226, 32.84191819495226, 32.84191819495226, 32.84191819495226, 32.84191819495226, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 64.08630021742414, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 85.33068223989603, 85.33068223989603, 85.33068223989603, 85.33068223989603, 85.33068223989603, 85.33068223989603, 85.33068223989603, 85.33068223989603, 85.33068223989603, 85.33068223989603, 85.33068223989603, 85.33068223989603, 85.33068223989603, 85.33068223989603, 85.33068223989603, 85.33068223989603, 85.33068223989603, 85.33068223989603, 85.33068223989603]
    rune_8_tracker = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
    rune_9_tracker = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
    rune_10_tracker = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
    rune_11_tracker = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
    rune_time_tracker = [0, 0.0, 1.1929022082018927, 1.1929022082018927, 2.3858044164037855, 2.3858044164037855, 3.5787066246056782, 3.5787066246056787, 4.656057051956106, 4.656057051956106, 5.733407479306533, 5.8334074793065325, 5.933407479306532, 6.033407479306532, 6.133407479306531, 6.233407479306531, 6.333407479306531, 6.43340747930653, 6.53340747930653, 6.63340747930653, 6.733407479306529, 6.833407479306529, 6.933407479306529, 7.033407479306528, 7.133407479306528, 7.2334074793065275, 7.333407479306527, 7.433407479306527, 7.533407479306526, 7.633407479306526, 7.733407479306526, 7.833407479306525, 7.933407479306525, 8.033407479306526, 8.133407479306525, 8.233407479306525, 8.333407479306524, 8.433407479306524, 8.533407479306524, 8.633407479306523, 8.733407479306523, 8.833407479306523, 8.933407479306522, 9.033407479306522, 9.133407479306522, 9.233407479306521, 9.333407479306521, 9.43340747930652, 9.53340747930652, 9.63340747930652, 9.73340747930652, 9.83340747930652, 9.933407479306519, 10.033407479306518, 10.033407479306518, 11.110757906656946, 11.110757906656946, 12.188108334007374, 12.188108334007374, 13.265458761357802, 13.265458761357802, 14.458360969559696, 14.458360969559696, 14.458360969559696, 15.651263177761589, 15.651263177761589, 16.844165385963482, 16.844165385963482, 18.260457520794944, 18.260457520794944, 19.676749655626406, 19.676749655626406, 21.093041790457868, 21.093041790457868, 22.50933392528933, 22.50933392528933, 23.92562606012079, 23.92562606012079, 25.341918194952253, 25.341918194952253, 26.758210329783715, 26.758210329783715, 28.174502464615177, 28.174502464615177, 29.59079459944664, 29.59079459944664, 31.0070867342781, 31.0070867342781, 32.42337886910956, 32.42337886910956, 33.83967100394102, 33.83967100394102, 35.25596313877248, 35.25596313877248, 36.67225527360394, 36.67225527360394, 38.088547408435396, 38.088547408435396, 39.504839543266854, 39.504839543266854, 40.92113167809831, 40.92113167809831, 42.33742381292977, 42.33742381292977, 43.75371594776123, 43.75371594776123, 45.17000808259269, 45.17000808259269, 46.586300217424146, 46.586300217424146, 48.002592352255604, 48.002592352255604, 49.41888448708706, 49.41888448708706, 50.83517662191852, 50.83517662191852, 52.25146875674998, 52.25146875674998, 53.66776089158144, 53.66776089158144, 55.084053026412896, 55.084053026412896, 56.500345161244354, 56.500345161244354, 57.91663729607581, 57.91663729607581, 59.33292943090727, 59.33292943090727, 60.74922156573873, 60.74922156573873, 62.16551370057019, 62.16551370057019, 63.581805835401646, 63.581805835401646, 64.9980979702331, 64.9980979702331, 66.41439010506457, 66.41439010506457, 67.83068223989603, 67.83068223989603, 69.02358444809792, 69.12358444809792, 69.22358444809791, 69.3235844480979, 69.4235844480979, 69.52358444809789, 69.62358444809789, 69.72358444809788, 69.82358444809788, 69.92358444809787, 70.02358444809786, 70.12358444809786, 70.22358444809785, 70.32358444809785, 70.42358444809784, 70.52358444809784, 70.62358444809783, 70.72358444809782, 70.82358444809782, 70.92358444809781, 71.02358444809781, 71.1235844480978, 71.1235844480978, 72.31648665629969, 72.31648665629969, 73.50938886450157, 73.50938886450157, 74.70229107270346, 74.70229107270346, 75.89519328090535, 75.89519328090535, 77.08809548910723, 77.08809548910723, 78.28099769730912, 78.28099769730912, 79.473899905511, 79.573899905511, 79.67389990551099, 79.77389990551099, 79.87389990551098, 79.97389990551098, 80.07389990551097, 80.17389990551096, 80.27389990551096, 80.37389990551095, 80.47389990551095, 80.57389990551094, 80.67389990551094, 80.77389990551093]
    runic_power_tracker = [10, 25, 25, 35, 35, 25, 25, 35, 35, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 28, 28, 53, 53, 63, 63, 73, 73, 98, 123, 123, 130, 130, 130, 130, 98, 98, 66, 66, 34, 34, 59, 59, 84, 84, 94, 94, 62, 62, 72, 72, 40, 40, 8, 8, 33, 33, 58, 58, 68, 68, 36, 36, 46, 46, 14, 14, 34, 34, 59, 59, 84, 84, 52, 52, 62, 62, 72, 72, 40, 40, 50, 50, 75, 75, 100, 100, 110, 110, 78, 78, 46, 46, 14, 14, 24, 24, 49, 49, 59, 59, 49, 49, 17, 17, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 37, 37, 62, 62, 87, 87, 55, 55, 65, 65, 33, 33, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    number_of_targets_in_fight = 1
    gear_currently_worn = "Spiked Titansteel Helm*&*Pendant of the Dragonsworn*&*Valorous Scourgeborne Shoulderplates*&*Aged Winter Cloak*&*Valorous Scourgeborne Battleplate*&*Wristbands of the Sentinel Huntress*&*Valorous Scourgeborne Gauntlets*&*Girdle of Razuvious*&*Valorous Scourgeborne Legplates*&*Melancholy Sabatons*&*Ruthlessness*&*Greatring of Collision*&*Darkmoon Card: Greatness*&*Grim Toll*&*Sigil of Awareness*&*Angry Dread*&*Last Laugh"
    current_gear_split_list = gear_currently_worn.replace("*&*",", ")
    current_gear_split_list = current_gear_split_list.split(", ")
    extra_sim_stats_info = "405.156*^*12.36*^*32.67*^*917.0*^*1618.46256*^*1277.958*^*20720.58*^*14623.0*^*591.294*^*5521.112076444444*^*88.0*^*44.0*^*17*^*141.5*^*5.91*^*149.0*^*False"
    extra_stats_split_list = extra_sim_stats_info.replace("*^*",", ")
    extra_stats_split_list = extra_stats_split_list.split(", ")
    extra_future_stats_info = 6004*[7632, 7578, 8010, 8094, 7844, 7754, 8043, 7267, 7835, 7360, 8225, 7366, 7840, 8019, 7895, 7649, 7484, 7820, 7608, 7758, 7596, 8228, 7678, 7436, 7481, 8123, 8021, 7726, 7616, 7162, 7459, 7817, 7738, 7886, 7674, 7592, 7298, 7530, 7592, 7683, 7135, 7455, 7545, 7550, 7944, 7669, 7204, 8082, 7569, 7844, 7811, 7840, 7526, 7799, 7404, 7601, 7884, 7242, 7893, 7673, 7380, 8570, 7765, 7598, 7585, 7587, 7621, 7535, 7461, 7896, 7965, 7434, 7477, 8017, 7520, 7628, 8067, 7550, 8213, 8190, 7751, 7948, 7582, 7708, 7917, 7194, 7781, 7621, 7057, 7960, 8200, 8427, 7618, 7654, 7689, 8083, 7241, 7824, 7630, 7883, 7631, 7015, 7646, 7741, 7565, 7927, 7966, 7852, 7383, 7498, 7882, 7736, 8032, 7785, 7471, 7555, 7533, 7801, 8163, 7733, 8007, 7741, 7391, 7753, 7822, 7435, 7646, 7391, 7667, 7555, 7276, 7485, 8010, 7827, 7450, 7211, 7301, 7726, 7849, 7555, 7589, 7914, 7831, 7636, 7409, 7266, 7851, 7863, 7440, 7930, 7693, 7712, 7727, 8130, 7900, 7538, 7557, 7922, 7948, 7612, 7818, 8104, 7343, 8001, 7833, 7708, 7677, 7946, 7766, 8132, 7534, 7625, 7580, 7617, 7792, 7419, 8106, 7468, 7934, 7612, 7653, 7710, 7292, 7771, 7092, 7777, 7873, 7702, 7376, 7907, 7714, 7322, 7147, 8057, 8282, 7300, 7781, 7711, 7705, 7497, 7468, 8077, 7072, 7392, 7487, 7812, 7950, 8041, 7890, 7657, 7192, 7056, 7768, 7931, 8318, 7695, 7919, 7663, 7931, 8008, 7458, 7169, 7211, 7453, 7538, 7736, 7493, 7754, 7607, 7329, 7911, 7510, 7500, 8079, 7868, 7530, 7580, 7910, 7855, 8097, 7345, 7338, 7503, 7742, 7990, 7645, 7497, 7642, 7710, 7892, 7773, 7816, 7685, 7653, 7631, 7943, 7184, 7422, 7774, 7974, 7960, 7657, 7693, 7911, 7692, 7576, 7682, 7368, 7912, 8123, 7218, 8137, 7866, 7469, 7445, 8102, 7718, 7564, 7525, 7943, 7554, 8093, 7782, 7835, 7926, 8176, 7190, 7673, 7538, 7574, 7514, 7528, 7579, 7669, 7396, 7169, 7645, 7758, 8005, 7670, 7943, 7359, 8012, 7562, 7307, 7741, 7131, 7614, 7356, 8028, 6951, 8032, 7679, 7902, 7826, 7666, 7778, 7682, 7355, 7740, 7810, 7722, 7421, 7498, 7819, 7487, 8325, 7574, 7393, 7653, 7364, 7288, 7611, 7497, 7819, 7558, 7606, 7270, 8002, 7714, 7102, 7863, 7995, 7780, 7182, 7890, 8058, 7586, 7292, 7516, 7267, 7968, 8231, 8262, 7724, 7858, 8264, 7652, 7789, 7655, 7989, 7208, 7427, 7470, 7526, 8072, 7643, 8016, 8247, 7437, 7943, 7551, 7837, 8344, 7635, 7378, 7968, 7501, 7901, 7590, 8005, 7510, 7886, 7368, 7464, 7556, 7807, 7671, 7517, 7715, 7671, 7241, 8135, 7771, 8176, 7537, 7650, 7824, 7616, 7534, 7665, 8303, 7231, 7443, 7994, 6804, 7657, 7749, 7519, 8160, 7727, 7460, 7623, 7782, 7069, 7584, 7532, 7862, 7620, 7252, 7785, 7982, 7741, 7791, 7798, 7335, 7516, 7640, 8291, 7489, 7877, 7740, 7722, 7423, 7923, 7889, 7698, 7952, 7826, 7208, 7675, 8066, 7721, 7533, 7910, 7940, 7443, 7429, 7597, 7835, 7502, 7180, 7545, 7772, 7978, 7685, 7595, 7233, 7882, 7550, 7773, 8087, 7863, 7142, 7908, 7659, 7758, 7703, 7917, 7416, 7832, 7942, 7919, 8080, 7595, 7870, 7673, 7935, 7774, 7926, 7298, 7671, 7234, 7791, 7773, 7240, 8481, 7760, 7540, 7981, 7338, 8085, 7130, 7712, 7644, 7475, 7694, 7765, 7374, 7840, 7611, 7600, 7534, 7876, 7733, 7398, 7687, 7629, 7762, 7475, 8064, 7921, 8039, 7724, 7152, 7614, 7852, 8035, 7481, 7330, 7777, 7912, 7880, 7409, 7791, 7563, 8097, 7478, 7765, 7688, 7911, 7909, 7347, 7887, 7795, 7835, 7811, 7500, 7535, 7295, 7910, 7533, 7551, 7614, 8122, 7945, 7427, 7571, 7760, 7806, 7671, 7827, 7847, 7250, 8103, 7687, 7540, 8208, 7827, 7604, 7749, 7055, 7937, 7760, 7425, 7737, 7638, 7284, 7579, 7793, 7488, 7451, 7799, 7488, 7639, 7412, 7285, 8023, 7841, 7097, 7877, 7894, 8005, 7318, 7822, 7931, 7371, 7626, 7381, 7398, 7682, 7674, 7752, 7359, 7254, 7740, 7621, 7975, 7840, 7465, 7934, 7663, 7450, 7717, 7488, 7974, 7511, 7653, 7644, 7431, 7943, 8232, 7713, 7662, 7551, 8232, 8099, 7869, 7488, 7760, 7380, 7615, 7599, 7634, 7102, 7962, 7753, 8007, 7393, 7476, 7477, 7414, 7376, 7517, 7729, 7787, 8118, 7810, 7673, 7573, 7881, 7991, 7633, 7443, 7896, 7685, 7826, 7345, 8099, 7134, 7797, 8155, 7917, 8180, 7594, 7790, 7719, 7622, 7815, 7606, 7963, 7293, 7491, 7403, 7941, 8279, 7471, 7600, 7817, 7530, 7659, 8215, 7856, 7267, 7462, 7731, 7326, 7883, 7851, 7308, 7320, 8396, 7743, 7488, 7292, 7258, 7398, 7973, 7735, 7402, 7978, 7921, 7558, 8017, 7790, 7645, 7578, 7710, 7432, 7301, 7980, 8139, 7433, 7617, 8294, 7986, 7486, 7858, 7093, 7320, 7573, 7626, 7858, 7671, 7803, 7690, 8150, 7811, 7378, 8114, 7679, 7464, 7774, 7750, 7855, 7815, 7227, 8303, 7668, 7177, 7358, 7890, 7713, 8097, 7543, 7261, 7403, 7693, 7994, 8174, 7838, 7933, 7976, 7730, 7356, 7880, 7688, 7768, 8083, 7599, 8161, 7704, 7375, 7300, 7847, 7712, 7839, 8020, 7701, 7645, 7539, 7688, 7576, 7618, 7765, 7799, 7200, 7479, 7289, 7251, 7113, 7862, 7782, 7825, 7548, 8083, 7432, 7505, 7635, 7864, 7708, 7571, 8045, 8163, 7531, 7830, 7266, 7878, 7793, 7617, 7430, 7652, 7737, 7930, 7760, 7608, 7485, 7481, 7510, 7785, 7308, 7430, 8164, 8069, 7624, 7784, 7459, 7729, 7350, 7856, 7968, 7716, 7082, 8058, 7992, 7829, 7747, 7858, 7808, 7574, 7881, 7429, 7529, 7414, 7706, 7745, 8205, 7811, 7256, 7471, 7699, 7737, 7650, 7353, 7386, 7365, 7612, 7517, 7760, 7466, 7622, 7686, 7619, 7721, 7323, 7935, 7853, 7774, 7154, 7531, 7436, 7373, 7891, 7660, 7563, 7841, 7598, 7808, 7193, 7622, 7555, 7258, 7766, 7767, 7848, 7990, 7536, 8117, 8175, 7657, 7764, 7910, 7429, 7517, 7602, 7392, 7810, 8034, 6982, 7721, 7222, 7552, 7830, 7322, 7130, 7602, 7781, 7117, 7461, 7586, 7414, 7114, 7953, 7572, 7790, 7785, 7094, 7153, 7569, 7427, 7511, 7798, 7695, 7694, 7612, 7167, 7801, 8076, 7338, 7726, 7965, 7875, 7808, 7755, 7094, 7134, 7641, 7951, 7046, 7465, 7337, 8131, 7732, 7521, 7722, 7579, 7051, 7583, 7931, 7532, 8153, 8019, 8412, 7764, 7523, 7459, 8006, 7359, 7743, 7116, 7516, 7944, 7392, 7408, 7638, 7408, 7665, 7523, 6958, 7835, 7950, 7680, 7337, 7845, 7824, 7665, 7693, 7747, 7510, 8269, 7699, 7410, 7638, 7604, 7825, 7764, 7649, 7761, 7289, 7387, 7561, 7630, 7417, 7389, 7816, 7534, 7496, 7560, 7395, 7490, 7797, 7581, 7364, 7767, 7725, 7132, 7538, 8062, 7723, 7295, 7476, 7631, 7539, 7631, 7824, 7562, 8489, 7509, 7930, 7626, 7556, 7693, 7825, 7557, 7503, 7384, 7708, 7716, 7677, 7643, 7401, 7701, 7803, 7999, 7937, 7483, 7888, 7187, 7415, 7633, 7765, 7476, 7799, 7120, 7532, 7671, 7447, 7735, 7937, 7059, 7781, 7766, 7310, 7544, 7976, 7398, 7909, 7926, 7731, 7623, 7535, 7407, 7818, 7588, 7756, 7349, 7250, 7722, 8119, 7435, 7160, 7732, 7678, 7501, 7849, 7877, 7765, 7849, 8098, 7916, 7660, 7586, 8136, 7766, 7717, 7593, 7926, 7917, 7786, 8263, 7754, 7594, 7904, 7820, 7902, 7562, 7600, 8161, 7594, 7268, 7628, 7249, 7776, 7399, 7486, 7884, 8347, 7622, 7726, 7627, 8037, 8103, 7638, 7378, 8058, 7394, 7921, 8191, 7494, 7880, 7406, 7782, 7350, 7875, 7722, 7894, 7955, 7638, 8187, 7457, 7554, 7259, 6807, 7678, 7660, 7628, 7942, 7846, 7700, 7783, 7572, 7590, 7518, 7364, 7530, 7186, 7404, 7555, 8057, 7222, 8043, 7759, 7058, 7834, 8072, 7166, 7552, 7593, 7775, 7676, 7967, 7796, 8069, 8172, 7130, 7491, 8047, 7158, 7657, 7766, 7538, 7151, 7353, 7756, 7225, 8223, 7387, 7594, 8137, 7365, 7794, 8227, 7339, 7150, 8211, 7624, 8094, 7016, 7605, 7743, 7491, 7553, 7704, 7718, 8047, 7585, 8119, 7555, 7854, 7471, 7557, 7887, 7546, 7474, 7590, 7747, 7557, 7767, 7849, 7692, 7202, 7651, 7451, 7552, 7441, 7513, 7736, 7599, 7552, 7565, 7677, 7401, 7550, 7359, 7752, 7712, 7519, 7618, 7801, 8087, 7544, 7881, 7647, 7777, 7652, 7556, 8105, 7462, 8118, 8265, 7888, 7654, 7725, 7584, 7869, 8136, 7689, 7760, 7553, 8049, 8013, 7230, 7094, 7595, 7118, 7297, 7784, 7340, 7794, 7670, 7712, 7624, 7697, 7571, 7929, 7521, 7812, 8160, 7541, 7516, 7834, 7541, 7725, 7208, 7450, 7101, 7551, 7548, 7886, 7341, 7903, 7796, 7377, 7987, 7906, 7647, 7539, 7523, 7651, 7374, 7971, 7643, 7130, 7858, 7576, 7917, 7234, 7697, 7408, 8248, 7855, 7630, 7489, 7675, 7325, 7247, 7889, 7595, 7605, 7576, 7986, 7975, 7877, 7584, 7457, 7830, 7965, 7746, 7581, 7402, 7532, 7545, 7896, 7436, 7539, 7555, 7831, 7288, 7652, 7764, 7226, 7699, 7704, 7053, 7693, 8227, 7840, 7602, 7607, 7396, 7906, 7475, 7125, 7705, 7551, 7604, 7610, 7967, 7624, 7970, 7818, 7392, 7790, 8000, 7742, 7765, 7917, 7158, 8085, 7931, 7443, 7628, 7968, 7431, 7117, 7038, 7602, 7607, 7572, 7286, 7985, 8068, 7541, 7776, 7595, 8035, 7704, 7361, 7075, 7584, 8052, 7864, 8156, 7955, 7772, 7588, 7770, 7951, 7700, 7665, 7853, 8077, 7914, 7570, 7773, 8413, 7156, 8155, 7888, 7950, 8025, 7891, 7634, 7597, 6998, 7332, 7878, 7741, 7901, 7954, 7752, 7208, 7442, 7735, 7522, 7744, 6964, 7407, 7796, 7760, 7325, 7552, 7233, 7512, 8142, 7870, 7681, 7759, 7516, 7776, 7192, 7203, 7000, 7648, 6962, 7662, 7592, 7569, 7801, 7061, 7450, 7227, 7292, 7825, 7854, 7631, 7689, 7870, 7802, 7324, 8074, 7993, 8129, 7597, 7611, 7654, 7293, 7618, 8397, 7933, 7853, 7828, 7696, 7427, 8237, 7467, 8025, 7624, 7046, 7114, 7863, 7600, 7807, 7924, 7298, 7772, 7294, 7719, 7530, 7282, 7240, 7569, 7625, 7569, 7915, 7643, 7286, 7219, 7351, 7765, 7185, 7450, 7748, 7606, 7248, 8171, 7279, 7286, 7286, 7512, 7560, 7401, 7855, 7201, 7717, 7863, 7745, 7165, 7807, 7208, 7279, 7306, 7654, 7794, 7256, 7706, 7680, 7312, 7606, 7560, 7897, 7313, 7631, 7564, 7694, 7880, 7627, 7674, 7781, 7829, 7697, 7403, 8107, 7704, 7607, 7929, 8119, 7707, 7454, 7701, 7728, 7692, 7778, 7307, 7709, 7865, 7843, 7515, 7343, 7836, 7154, 7731, 7840, 7553, 7434, 7743, 7379, 8102, 7931, 7355, 7839, 7426, 7434, 8029, 7650, 7576, 7634, 8228, 7886, 7381, 7972, 8165, 7740, 7317, 7653, 7542, 7831, 8120, 7632, 7155, 7787, 7329, 8049, 7372, 7668, 7406, 7523, 8093, 7299, 7762, 7953, 7399, 7932, 7586, 7254, 7321, 7656, 8139, 8293, 7880, 7704, 7386, 7615, 7378, 7494, 7662, 7195, 7775, 7500, 7467, 7454, 7695, 7983, 7337, 7608, 7805, 7538, 7343, 7949, 7576, 7305, 7371, 7660, 7513, 7808, 7629, 7739, 7647, 7663, 8094, 7521, 7283, 6991, 7785, 7275, 7266, 7703, 8255, 7509, 7930, 7947, 7654, 8130, 8136, 7003, 8077, 7254, 7743, 7848, 7370, 7517, 7407, 6996, 7423, 7956, 7586, 7691, 7350, 7666, 7074, 7401, 7684, 7855, 7735, 7645, 7787, 7290, 7531, 7871, 7606, 7707, 7406, 7905, 7666, 7649, 7327, 8279, 7635, 7441, 7173, 7553, 7762, 7584, 7676, 7836, 7618, 7648, 7360, 7229, 7838, 7893, 7992, 7758, 7021, 7257, 7696, 7908, 7343, 7243, 7281, 7703, 8129, 7648, 7909, 7939, 8021, 7421, 7759, 7052, 7486, 7753, 7785, 8229, 7881, 7464, 7889, 7897, 7246, 7617, 7594, 7277, 7504, 7530, 7567, 7356, 7595, 8052, 7842, 7522, 7747, 7199, 8198, 7682, 7599, 7616, 7618, 7700, 7596, 7452, 7491, 7922, 7859, 7401, 7476, 7537, 7907, 7696, 7860, 7710, 7036, 7571, 8106, 7659, 7964, 7608, 7647, 7123, 8094, 7776, 8005, 7768, 7575, 7681, 7724, 7840, 7630, 7690, 7525, 7708, 7683, 7398, 7562, 7421, 7424, 7449, 7432, 7998, 7937, 7948, 7837, 8092, 7992, 7981, 7806, 7470, 7768, 7294, 7638, 7613, 7707, 8072, 7099, 8025, 8007, 7870, 7825, 8056, 7698, 7924, 7466, 7547, 7007, 7650, 6949, 7625, 7981, 7675, 7749, 7521, 7625, 7628, 8018, 7685, 7392, 7722, 7697, 7891, 7703, 7886, 7679, 7746, 8184, 8240, 7606, 7741, 7950, 8102, 8231, 7489, 7977, 7984, 7273, 7931, 7644, 7723, 8229, 7186, 7920, 7858, 7366, 7151, 7816, 7620, 7767, 7310, 7578, 7571, 7946, 7973, 7982, 7685, 7455, 7605, 7771, 7439, 7154, 7485, 7625, 7408, 8232, 7643, 7129, 7634, 8113, 7397, 7576, 7366, 7096, 7093, 7417, 7073, 7764, 7251, 8202, 7563, 7717, 7501, 7906, 7311, 7872, 7862, 7153, 7535, 7142, 7688, 7915, 7352, 7538, 7868, 7792, 7963, 7568, 7428, 7922, 7776, 7477, 7257, 7424, 8007, 7592, 7420, 7739, 7874, 7534, 7792, 7344, 7381, 8197, 7998, 7601, 7978, 7843, 7525, 7265, 7636, 7376, 7492, 7561, 7611, 7633, 7743, 7413, 7404, 7713, 7762, 8197, 7662, 7968, 7423, 8413, 7458, 7776, 7536, 7780, 7642, 7205, 7183, 7634, 7971, 7456, 7243, 7565, 7719, 7465, 7979, 7369, 7628, 7474, 7787, 7577, 7348, 7964, 8172, 8287, 7257, 8046, 7752, 7721, 7865, 8058, 7585, 7329, 7919, 7363, 7434, 7794, 7554, 7414, 7686, 7408, 8228, 7512, 7935, 7468, 7818, 7945, 7674, 7514, 8080, 7617, 7355, 7794, 7953, 7555, 7828, 7546, 7869, 7907, 7819, 7289, 7385, 7466, 7454, 7276, 7392, 7909, 7343, 7773, 7841, 7629, 7534, 8119, 7785, 8163, 7157, 7849, 7343, 7605, 7656, 6799, 7862, 7271, 8124, 7645, 7906, 8117, 7963, 7844, 7506, 7681, 7552, 8292, 7415, 8228, 7714, 7336, 7589, 7515, 7441, 7524, 7402, 7392, 7979, 7585, 7322, 7586, 7481, 7723, 7370, 7965, 7333, 7292, 8020, 7602, 7304, 7633, 8013, 8250, 7834, 7808, 7035, 7789, 7590, 7983, 7207, 7367, 7720, 7376, 8584, 7691, 7807, 7937, 7500, 8126, 7539, 7398, 7437, 7767, 7677, 7623, 7826, 7900, 7483, 7708, 7470, 7822, 7338, 7847, 7465, 8000, 7249, 7246, 7026, 7534, 7795, 7632, 7544, 7722, 7672, 7310, 7855, 7793, 7896, 8438, 8301, 7949, 7721, 7793, 7768, 7567, 7895, 7802, 7287, 7917, 7777, 7632, 7562, 7274, 7936, 7747, 7545, 7919, 8553, 7528, 7470, 7809, 7700, 7439, 7528, 7536, 7010, 7218, 7178, 7534, 7537, 7650, 7647, 8004, 7403, 7354, 7848, 7340, 7813, 7680, 7586, 6796, 7318, 7956, 7396, 7808, 7611, 7551, 7496, 8272, 7557, 7654, 7533, 7590, 7290, 7859, 7621, 7706, 7319, 7487, 7389, 7284, 7320, 7349, 8063, 7979, 7510, 7378, 7700, 7770, 7568, 7442, 7456, 7495, 7856, 7554, 7489, 7125, 7409, 7386, 7272, 7766, 7250, 7355, 7510, 7674, 7465, 7473, 7698, 7301, 7999, 7972, 7612, 7015, 7275, 7856, 7688, 7497, 7332, 7464, 8093, 7571, 8028, 7997, 7773, 7624, 8386, 7365, 7836, 7485, 7464, 7463, 7162, 7370, 7790, 7784, 7453, 6903, 7892, 7857, 7437, 7642, 7935, 7349, 7769, 7982, 7171, 7674, 7630, 7795, 7863, 7571, 7800, 7611, 7413, 7770, 7350, 7595, 7206, 8267, 7765, 7464, 7728, 7926, 7606, 7426, 7828, 7809, 7684, 8234, 7917, 7139, 7685, 7448, 7868, 7977, 7231, 7522, 7261, 7885, 7708, 7748, 7952, 7830, 8066, 7444, 7582, 7559, 7577, 7769, 8022, 7988, 7187, 7899, 7239, 7523, 7612, 7815, 8173, 7330, 7314, 7935, 7809, 7762, 8046, 7557, 7452, 7659, 7676, 7846, 7104, 7542, 7753, 7545, 7777, 7872, 7932, 7583, 7261, 6950, 7644, 7457, 7527, 7786, 7628, 8046, 7864, 7562, 7599, 7558, 7389, 7585, 8060, 7559, 7593, 8007, 7827, 7211, 8146, 7824, 7925, 7957, 7490, 7768, 8072, 7489, 7655, 7760, 7684, 7850, 7661, 7770, 7374, 6976, 7508, 7737, 7432, 7358, 7710, 7424, 7825, 7433, 6969, 7903, 7834, 7448, 8143, 7561, 7664, 7944, 7766, 8289, 7503, 7876, 7822, 7710, 7690, 7886, 7676, 7484, 7360, 7451, 7659, 8087, 7789, 8413, 7114, 7572, 7126, 7399, 7192, 7769, 7325, 8004, 7801, 7468, 7446, 7594, 7448, 8224, 7627, 7489, 7770, 7509, 7664, 8050, 8020, 7298, 7880, 7484, 7243, 7576, 8145, 7356, 7687, 7574, 7846, 7275, 7523, 7157, 7444, 6936, 7612, 7609, 7314, 7198, 7682, 7592, 7823, 7258, 7766, 7704, 7683, 7533, 7551, 7596, 8138, 7785, 7446, 7789, 8024, 7563, 7164, 7558, 7762, 7599, 7737, 7902, 7854, 7457, 7486, 7503, 7453, 7975, 8051, 7548, 7611, 7762, 7527, 7535, 6961, 7393, 7730, 7388, 7839, 7951, 7589, 7931, 7880, 8026, 6984, 7616, 7501, 7547, 7828, 7852, 7725, 7660, 7277, 7711, 7594, 7857, 7399, 7666, 7384, 8232, 7687, 7299, 7422, 7639, 7899, 7554, 7730, 7527, 7459, 7993, 7826, 7126, 7554, 7615, 7811, 7514, 7233, 7767, 8014, 7466, 7620, 7402, 7783, 7877, 7823, 7735, 8105, 7764, 7879, 7615, 7651, 7495, 7744, 7944, 7529, 7864, 7664, 7597, 8199, 7906, 7380, 7808, 7544, 7690, 8047, 7872, 8173, 7683, 7696, 8005, 7946, 7383, 7524, 7440, 7656, 7843, 7626, 6846, 7984, 7541, 7551, 7863, 7532, 8042, 7812, 8011, 7580, 7346, 7040, 7628, 7825, 7994, 7574, 7912, 7348, 8126, 7574, 7461, 7363, 7994, 7453, 7717, 7925, 8209, 7929, 7419, 7614, 7774, 7620, 8083, 7523, 7554, 7861, 7424, 7971, 7875, 7795, 7566, 7165, 7911, 7722, 7274, 7668, 7103, 7416, 7374, 7363, 7722, 7514, 7486, 7787, 7828, 7701, 7251, 7783, 7848, 7918, 7673, 7928, 7107, 7483, 7707, 7835, 7657, 7698, 7624, 7794, 7725, 7355, 7693, 8067, 7683, 7661, 7404, 7454, 8101, 7628, 7695, 7616, 7906, 7816, 7021, 7767, 7462, 7321, 7732, 7367, 7763, 7713, 7905, 7649, 7598, 7391, 7669, 7736, 7560, 8229, 7913, 7662, 7708, 8023, 8468, 7318, 7487, 7972, 7619, 7429, 7187, 7554, 7926, 7989, 7778, 7954, 7605, 7697, 7898, 7936, 7601, 7882, 7228, 7305, 7316, 6965, 7345, 7628, 7685, 7816, 7513, 7592, 7600, 7708, 7643, 8026, 8055, 7534, 7647, 7801, 7566, 7737, 7562, 7849, 7388, 8110, 7579, 7947, 7810, 7575, 7411, 7369, 7823, 7035, 7729, 7904, 7743, 7797, 7689, 7232, 7854, 8458, 7569, 7776, 7545, 7638, 7942, 7543, 7753, 8065, 7500, 7607, 8156, 7992, 7715, 7931, 8037, 7864, 7220, 7985, 7579, 7371, 7167, 7851, 7753, 7614, 7107, 7472, 7820, 7578, 7521, 7849, 7847, 7754, 7228, 7789, 7270, 7653, 7561, 8108, 7759, 7158, 7535, 7803, 7503, 8144, 7459, 8087, 7728, 7556, 7518, 7766, 7539, 6950, 7812, 7682, 7448, 7851, 7885, 7632, 7269, 7407, 7300, 7222, 7687, 8316, 7267, 8192, 8037, 7744, 7495, 7716, 7772, 7297, 7580, 7464, 7647, 7928, 7244, 7472, 7754, 7315, 7944, 7837, 7347, 7429, 7569, 7531, 7945, 7515, 7945, 7376, 7808, 7866, 7767, 7240, 7908, 7465, 7456, 7474, 7425, 7771, 7903, 7763, 7987, 7761, 7254, 7964, 7541, 7692, 7226, 7943, 8072, 7289, 7639, 7903, 7646, 7787, 7699, 7907, 7993, 7682, 7865, 7454, 8697, 7235, 7593, 8083, 7277, 7774, 7550, 7718, 8039, 8251, 7455, 7699, 7576, 7173, 7704, 8331, 8561, 8000, 7667, 7782, 7463, 8031, 7895, 8056, 7515, 7912, 7713, 8094, 7219, 8193, 7381, 7488, 7913, 7648, 7652, 7600, 7602, 7645, 7256, 7205, 7808, 7615, 8246, 7728, 7805, 7274, 8336, 7691, 7639, 8048, 7880, 7973, 7922, 7765, 7748, 7621, 7524, 7553, 7181, 7637, 7625, 7399, 7645, 8357, 7549, 7806, 7635, 7848, 7378, 7574, 7659, 7689, 7692, 7639, 7637, 7343, 7811, 7182, 7181, 7150, 7604, 7141, 7604, 8038, 7555, 7653, 7902, 7465, 7559, 7781, 7706, 7688, 7183, 7578, 7845, 7235, 7468, 7666, 7304, 7365, 7991, 7737, 7564, 7857, 7545, 7939, 7561, 7473, 7792, 7406, 7397, 8019, 7961, 7604, 7643, 7875, 7537, 7360, 8037, 7704, 7438, 7677, 7467, 8198, 8100, 7685, 7494, 8275, 7692, 7907, 7517, 7230, 7707, 7702, 7802, 7750, 7395, 7425, 7398, 8002, 7750, 7658, 7606, 7856, 7682, 7559, 7221, 7526, 7191, 7412, 7613, 7702, 7656, 7428, 7298, 7926, 7863, 8094, 7516, 7765, 7609, 7506, 7900, 7610, 7022, 8335, 7305, 7777, 7500, 7879, 7356, 7659, 7706, 7599, 7460, 7921, 7552, 8187, 7729, 7802, 6987, 7428, 7341, 7050, 7414, 8042, 7525, 7729, 7827, 7884, 8046, 7439, 7730, 7494, 8153, 7707, 7642, 7169, 7461, 7465, 8056, 7929, 8080, 7364, 7430, 7460, 7606, 7491, 7490, 7748, 7676, 7385, 7220, 7925, 7597, 7378, 7956, 8271, 8023, 7538, 7345, 8023, 7593, 7865, 7540, 7490, 7683, 7402, 7627, 7928, 7580, 7767, 7291, 7704, 7906, 7798, 7661, 7449, 6826, 7160, 7751, 8370, 7388, 8344, 7713, 8005, 7152, 7606, 7868, 7704, 7696, 7722, 7728, 7550, 7752, 7218, 7677, 7620, 7550, 7598, 7692, 7509, 7636, 7552, 7639, 7267, 7894, 7539, 8108, 7673, 7363, 7344, 7803, 7646, 7727, 8467, 7740, 7657, 7469, 7750, 7492, 7507, 7546, 7560, 7657, 7984, 7213, 7531, 7496, 7431, 7054, 7723, 7175, 7722, 7562, 7399, 7537, 7305, 7590, 7492, 7154, 8021, 7337, 7337, 7419, 7801, 7081, 7844, 7286, 7583, 7294, 7845, 7693, 7600, 7749, 8122, 8153, 8118, 7504, 8183, 7568, 7213, 7602, 7809, 7521, 7244, 7763, 7377, 7886, 7555, 7781, 7643, 7527, 7634, 7401, 7574, 7632, 8029, 7554, 7692, 7855, 7552, 7931, 7783, 7984, 7473, 7797, 8338, 8362, 7621, 7979, 7404, 8259, 8073, 7778, 7460, 7229, 8019, 7707, 7675, 7422, 8356, 7581, 7772, 7202, 8177, 7811, 7554, 8013, 7227, 7350, 7815, 7714, 7762, 7460, 7441, 7561, 8225, 7311, 7402, 7894, 7414, 8158, 7149, 7725, 8169, 7686, 7554, 7054, 7524, 6934, 7791, 7848, 7769, 7657, 7084, 7397, 7316, 8102, 7681, 7800, 7825, 7636, 7680, 7616, 7995, 7636, 7393, 7747, 7698, 7559, 8051, 7355, 7485, 7571, 7675, 7787, 7613, 7499, 7881, 7354, 7799, 7676, 7316, 7906, 7917, 8157, 7857, 7341, 7772, 7933, 7815, 7682, 7587, 7300, 8303, 7566, 7757, 7712, 7480, 7725, 7841, 7683, 8169, 7509, 7613, 8006, 7645, 8014, 7588, 7598, 7778, 7604, 8073, 7732, 7830, 7428, 7493, 7934, 7194, 7858, 7423, 7644, 7302, 7291, 7456, 7703, 8513, 7864, 8354, 7833, 7835, 7645, 7337, 7934, 7828, 7339, 7198, 7664, 7443, 7447, 7711, 7608, 7935, 7281, 7980, 7604, 8100, 7088, 8023, 7565, 7454, 6873, 7788, 7606, 8367, 7770, 7700, 7683, 7993, 7742, 7813, 7211, 8191, 7791, 7709, 7688, 7673, 7473, 7726, 7880, 7394, 8016, 7655, 7617, 7907, 7676, 7443, 8025, 7309, 7118, 8252, 7941, 7875, 7316, 7970, 7902, 8053, 7152, 7464, 7743, 7430, 7620, 7555, 7973, 7432, 8029, 7738, 7811, 7359, 8039, 7889, 8222, 7891, 7744, 7817, 7593, 7740, 8176, 7884, 8042, 7436, 7748, 8168, 7210, 7708, 7286, 7439, 7790, 7731, 7444, 7984, 7649, 7747, 7611, 7084, 7660, 7839, 7274, 7523, 7446, 7832, 7676, 7625, 7501, 7158, 7866, 8229, 7353, 8024, 8082, 7896, 7811, 7805, 7237, 7836, 7280, 7733, 7384, 7613, 8051, 7304, 7229, 7826, 7096, 8007, 7830, 7532, 7306, 8021, 7428, 7431, 8231, 7152, 7688, 7380, 7482, 7497, 7134, 7139, 7628, 7721, 7443, 7555, 7861, 8016, 7848, 7419, 7427, 7348, 8034, 7579, 7653, 7434, 7418, 7476, 8270, 7718, 7226, 7660, 7761, 7286, 7038, 7695, 8241, 7888, 7905, 7889, 7683, 8054, 8126, 7967, 7972, 7868, 7859, 7816, 7250, 8401, 7111, 7311, 7331, 7408, 7550, 7395, 8237, 7517, 8344, 7085, 7929, 7299, 7465, 8087, 7596, 7383, 7630, 7619, 7182, 7315, 8308, 7781, 7965, 7378, 7227, 7902, 7729, 7904, 7509, 8035, 7131, 7578, 7815, 7660, 7271, 7627, 7885, 8077, 7746, 7626, 7821, 7849, 7509, 7945, 7594, 8218, 7299, 7574, 7781, 8017, 7809, 7631, 7670, 7523, 7293, 7419, 7880, 7729, 7407, 7357, 7691, 7189, 7787, 7297, 7733, 7636, 7772, 7996, 7627, 7989, 7702, 7531, 7832, 7482, 7837, 7401, 8167, 7719, 7536, 8132, 7725, 7555, 7876, 7770, 7807, 7362, 7955, 7311, 7805, 7854, 7628, 7866, 7391, 7632, 7659, 7399, 6993, 7703, 7228, 7213, 8332, 8043, 7426, 7855, 8015, 7529, 7530, 7687, 7940, 8019, 7832, 7568, 8315, 7718, 7814, 7990, 7698, 7825, 7844, 7753, 7845, 7670, 8160, 7555, 7513, 8066, 7305, 7262, 7559, 7217, 7634, 8063, 7911, 7762, 7638, 8017, 7970, 7800, 7339, 7717, 7374, 7358, 8071, 7954, 7328, 7299, 7593, 7643, 8127, 8032, 7240, 7498, 7237, 8065, 7433, 8182, 7238, 8013, 7150, 7297, 7420, 7757, 8052, 7402, 7586, 7450, 7478, 7720, 8038, 7913, 8294, 7558, 8066, 7125, 7518, 8106, 7610, 7938, 7084, 7919, 7573, 7147, 7549, 7634, 8062, 7588, 7794, 7102, 7648, 7685, 8141, 7712, 7761, 7525, 7814, 7107, 8299, 7656, 7785, 7000, 7262, 7655, 7640, 7643, 7663, 7428, 7463, 8034, 7499, 7616, 7510, 8171, 7658, 7744, 7605, 7824, 7497, 7810, 8204, 8482, 7829, 7760, 7037, 7521, 7410, 8276, 7521, 7593, 7443, 7868, 7788, 8033, 7215, 7518, 7814, 8361, 7935, 7644, 8246, 7547, 7672, 8436, 7693, 7281, 7838, 7317, 8148, 7396, 7616, 7804, 7569, 7632, 7208, 7514, 7790, 7967, 7831, 7414, 7523, 7611, 7512, 7428, 7528, 7770, 8088, 8196, 8372, 7660, 7491, 7746, 7353, 7808, 7621, 7846, 7595, 8109, 7579, 7693, 7946, 7847, 6863, 7502, 8138, 7707, 8003, 7788, 7654, 7377, 7303, 7485, 7852, 7532, 7556, 7170, 7519, 7559, 7796, 7637, 7721, 7249, 7784, 7826, 7599, 8133, 7836, 7410, 7983, 7848, 7798, 7617, 7905, 7294, 7362, 7830, 8165, 8276, 7813, 7505, 7390, 7623, 7324, 7645, 7958, 7180, 7929, 7775, 7601, 7315, 7746, 7643, 7682, 7503, 7971, 7962, 7705, 7492, 7680, 7520, 7699, 7923, 7623, 7662, 7531, 7972, 7826, 7842, 7353, 7545, 7797, 7528, 7799, 7798, 7286, 7455, 7358, 7634, 7588, 7368, 7612, 7738, 7829, 7784, 7916, 8159, 7813, 7484, 8104, 7546, 7626, 7618, 7859, 7647, 7659, 7200, 7642, 7437, 7892, 7645, 7195, 7861, 7911, 7283, 7877, 7746, 7818, 7313, 7996, 7899, 7796, 7307, 8149, 7867, 7466, 7587, 7587, 7936, 7604, 7706, 7256, 7695, 7561, 7289, 7634, 7852, 7055, 7129, 7399, 7092, 7332, 7309, 7603, 7549, 7605, 7342, 7312, 7836, 7673, 7600, 7444, 7886, 7736, 7857, 7679, 7718, 7969, 7811, 7806, 8062, 8146, 7400, 7548, 7969, 7099, 7906, 7613, 7537, 7870, 7313, 7542, 8161, 7124, 7282, 7991, 7402, 7738, 7339, 7788, 7727, 7724, 7635, 7823, 7784, 7203, 7794, 7320, 7268, 7550, 7637, 7644, 7323, 7691, 7139, 7391, 6633, 7144, 7702, 7441, 7462, 7320, 8077, 8103, 7463, 7538, 7840, 7675, 7651, 8259, 7652, 7682, 7439, 7395, 7761, 7878, 7948, 7239, 7993, 7518, 7624, 7755, 7218, 6925, 7988, 7728, 7392, 7176, 7689, 7888, 7631, 7605, 7715, 7721, 7569, 7814, 7521, 7861, 7856, 7537, 7336, 7665, 8280, 8040, 7474, 7668, 8165, 7349, 7563, 7383, 7298, 7703, 7398, 7175, 7509, 7809, 7387, 7453, 7643, 7652, 7330, 7771, 7268, 7422, 8028, 7473, 7764, 7816, 7689, 7952, 7964, 7769, 7954, 7593, 7810, 7221, 7620, 8068, 7764, 7615, 8008, 7549, 7601, 8117, 7447, 7832, 7189, 7777, 7945, 7527, 8062, 7644, 7465, 7744, 8124, 7328, 7439, 7611, 7719, 7668, 7665, 7706, 7811, 7349, 8062, 6965, 7548, 7657, 8087, 7608, 7682, 7523, 8048, 7628, 7652, 7488, 7651, 8193, 7963, 7694, 7612, 7664, 7918, 7109, 7752, 7668, 7750, 7409, 7529, 7402, 7258, 7470, 7549, 7279, 7541, 7492, 7630, 7741, 8070, 7415, 7583, 7257, 7937, 7450, 7858, 7991, 7798, 7436, 7403, 7696, 7745, 7716, 7989, 7273, 7529, 7681, 8184, 7519, 7467, 7821, 6823, 7886, 7882, 8421, 7767, 7708, 7686, 7397, 7657, 6913, 7085, 7503, 7579, 7785, 7448, 7785, 7736, 7233, 7763, 7367, 7588, 7782, 8017, 7793, 7513, 7556, 7460, 7744, 7321, 8114, 7179, 7134, 7692, 7977, 7545, 7647, 7391, 7952, 7327, 7884, 7454, 7337, 7510, 7245, 7489, 7873, 7325, 7894, 7802, 7454, 7953, 7593, 8033, 7596, 7907, 7223, 6984, 8006, 7682, 7522, 7918, 7886, 7775, 7263, 7911, 8226, 8183, 7584, 7968, 7314, 7449, 7604, 8151, 8136, 7618, 7052, 7581, 7564, 8017, 8037, 7667, 8417, 7438, 7575, 7319, 7365, 7986, 7396, 8134, 7843, 7299, 7575, 7381, 7769, 7475, 7550, 7622, 7919, 7518, 7603, 7757, 7415, 7529, 8087, 7883, 7652, 7866, 7510, 7555, 7250, 6963, 7902, 7572, 7804, 7523, 7895, 8257, 8002, 7134, 7361, 7219, 7636, 7649, 7499, 7584, 7475, 7531, 8011, 7531, 7627, 7674, 7645, 7456, 6974, 7866, 7653, 7361, 7476, 7556, 8109, 7725, 7825, 7716, 7999, 7546, 8417, 7541, 7832, 7602, 7531, 8070, 7543, 7853, 7988, 7500, 7498, 7741, 7613, 8090, 7992, 7596, 7941, 7242, 7877, 7472, 7757, 7974, 7766, 7046, 8075, 7725, 7482, 7837, 7826, 7356, 7410, 8625, 7478, 8009, 7791, 7792, 7504, 7805, 7738, 7904, 8079, 8081, 7829, 7216, 8208, 7667, 7227, 7708, 7615, 7155, 7957, 8183, 7564, 7494, 7481, 7453, 7489, 7340, 7272, 7802, 7897, 7558, 7369, 7764, 7156, 7487, 7289, 7457, 7746, 7596, 7034, 7655, 7446, 7201, 7018, 7628, 7823, 7673, 7740, 7839, 7677, 7444, 7535, 7711, 7809, 7115, 7620, 7783, 7872, 7331, 8012, 7551, 7479, 8156, 8304, 7601, 7426, 7397, 7177, 7745, 7599, 7800, 7791, 7195, 7831, 8496, 7716, 7672, 7753, 7857, 7788, 7453, 7468, 7819, 7418, 7884, 7970, 7889, 7642, 7852, 8003, 7742, 7896, 8130, 7668, 7973, 8191, 8023, 7735, 7574, 7632, 7652, 7621, 7899, 7709, 7933, 7446, 7543, 7302, 7953, 7542, 8466, 7184, 8066, 8183, 7562, 7435, 7694, 8426, 7833, 8129, 7671, 7855, 7978, 7752, 7589, 7399, 7593, 7287, 7141, 7640, 7621, 7763, 7883, 7335, 7369, 7103, 7269, 7717, 7580, 7971, 7734, 7781, 8161, 8006, 7601, 7748, 7420, 7570, 7951, 7704, 8006, 7739, 7562, 7108, 7555, 7793, 7695, 7846, 7717, 7681, 7484, 7044, 7326, 8128, 7672, 7661, 8229, 7387, 7364, 7976, 8116, 7572, 8080, 7593, 7834, 7302, 7934, 7775, 7574, 7619, 7820, 7395, 8001, 7240, 7673, 7716, 7723, 7849, 7341, 7881, 7326, 7928, 7697, 7856, 7374, 7397, 7859, 7826, 7657, 7744, 7545, 7985, 6957, 7383, 7160, 7452, 7781, 7898, 7874, 8436, 7662, 7016, 7655, 8380, 7055, 7745, 8068, 7284, 7630, 7626, 7777, 7433, 7965, 7420, 8094, 7610, 7615, 7289, 8145, 7492, 7808, 8025, 7440, 7428, 7959, 7403, 7705, 7579, 7944, 7414, 7778, 7681, 7946, 7494, 7421, 8213, 8189, 7828, 8006, 8034, 7631, 7431, 7908, 7839, 7201, 7209, 7564, 7749, 8187, 7933, 7613, 7720, 7184, 7701, 7867, 7685, 7884, 6719, 7829, 7602, 7920, 7917, 7689, 7361, 7865, 7622, 7622, 7684, 7448, 7808, 7564, 8135, 7254, 7496, 7318, 7611, 7772, 7384, 7956, 7515, 7749, 7296, 7492, 7796, 7588, 8202, 7505, 7199, 7730, 7576, 8021, 7449, 7203, 7992, 7542, 7891, 7891, 7263, 7979, 7343, 7665, 7735, 7722, 7585, 7970, 7737, 8246, 7732, 7770, 7739, 7916, 7742, 7676, 8323, 7781, 7499, 7500, 7540, 7953, 7789, 7566, 7753, 7684, 7414, 7546, 7630, 8195, 7983, 7959, 7827, 7671, 7665, 7281, 7646, 7622, 8107, 7518, 8141, 7504, 7826, 7634, 7869, 7142, 8038, 7419, 7578, 7467, 7703, 7742, 7417, 7826, 7493, 7645, 8220, 7734, 7643, 8107, 7448, 7599, 8145, 7704, 8101, 7576, 7827, 7316, 7569, 7649, 7923, 8046, 7973, 7673, 7436, 7739, 7727, 8075, 7618, 7630, 6848, 7671, 7786, 7080, 7783, 7442, 7507, 7709, 7857, 7904, 7584, 7139, 7312, 7980, 7392, 8002, 7800, 7180, 7758, 7584, 7987, 7346, 7632, 7056, 7948, 8065, 7465, 7565, 7687, 7674, 7606, 7597, 7834, 7721, 7999, 7742, 7723, 8000, 7592, 7771, 8056, 7484, 7294, 7857, 7744, 7623, 7456, 8452, 7978, 7611, 7859, 7781, 7729, 7791, 7372, 7262, 7272, 7273, 7840, 7426, 7846, 7434, 7605, 8282, 7664, 7825, 7730, 7732, 8115, 7733, 8142, 7858, 7637, 7927, 7713, 7399, 8101, 7844, 7053, 7583, 7904, 7148, 7880, 8119, 7625, 8294, 7947, 7775, 7696, 7750, 6976, 7119, 7967, 7729, 7738, 8070, 7826, 7641, 7693, 7555, 7601, 7823, 7908, 7620, 8034, 7252, 7443, 7852, 8001, 7587, 7768, 7264, 7613, 7218, 7588, 7297, 7752, 7457, 7201, 7881, 7188, 7447, 8357, 7553, 7941, 7673, 7528, 7248, 7478, 7592, 7985, 7550, 7725, 8077, 7920, 7142, 7951, 7368, 7777, 8283, 8064, 7392, 7529, 7751, 7331, 7616, 7459, 7747, 7960, 7424, 7924, 7659, 7637, 7839, 7667, 7655, 7622, 7573, 7423, 7419, 7444, 7874, 7594, 7900, 8040, 7345, 7790, 7523, 7326, 7501, 7835, 7486, 7555, 7892, 7475, 7841, 8093, 7624, 7503, 7832, 7646, 7506, 7531, 7250, 7242, 7017, 7983, 7744, 7248, 7603, 7421, 7460, 7796, 7753, 7535, 7477, 7333, 7062, 7656, 7571, 7945, 7561, 7325, 7990, 8130, 7625, 7725, 7405, 7738, 7682, 7365, 7850, 7708, 7318, 7714, 7458, 8120, 7747, 8091, 7399, 7588, 7903, 7133, 7238, 8025, 7712, 7766, 7496, 7452, 7575, 7656, 7893, 7153, 7190, 7516, 7232, 7548, 7710, 7482, 7557, 7644, 7427, 7345, 7865, 7656, 7392, 7626, 7971, 7513, 8469, 7509, 7530, 7595, 7359, 8156, 7138, 7670, 7437, 7331, 7771, 7500, 7493, 7716, 7552, 7759, 7750, 8093, 8021, 7752, 7286, 7807, 7534, 7713, 7339, 7767, 7182, 7513, 7260, 7918, 8002, 8011, 7520, 7745, 7703, 7509, 7546, 7841, 8025, 7582, 7175, 7540, 7749, 7461, 7230, 7743, 8087, 7596, 7783, 7754, 7201, 7782, 7685, 7483, 7286, 7748, 7797, 8117, 7771, 7521, 7851, 7637, 7394, 7317, 7593, 7972, 7653, 8166, 7556, 7734, 7450, 7220, 7854, 7940, 8117, 7423, 7584, 8171, 7224, 7608, 7588, 7541, 7624, 7269, 7861, 7186, 8163, 7809, 7641, 7219, 7803, 8156, 7947, 7691, 7566, 7828, 7796, 7728, 7670, 7749, 7461, 7711, 8170, 7469, 7363, 7681, 7934, 7798, 7327, 7653, 7375, 7180, 7500, 7854, 7959, 7602, 7483, 8053, 7651, 7703, 7699, 7851, 8088, 7345, 7171, 7818, 7880, 7806, 7709, 7476, 7719, 8170, 7535, 7753, 8183, 7249, 7806, 7735, 7650, 7743, 7687, 7693, 7721, 7335, 7946, 7295, 7817, 7558, 7394, 7340, 7863, 7408, 7759, 7263, 7316, 7101, 7968, 7227, 7483, 7346, 7499, 7555, 7810, 7710, 7589, 7632, 7401, 7982, 7447, 7738, 7828, 7726, 7100, 7490, 7955, 7801, 7789, 7349, 7240, 7642, 7831, 7451, 8072, 7655, 8047, 7717, 7772, 7496, 7737, 7630, 7826, 7251, 7416, 7699, 7968, 7334, 7951, 7526, 7629, 7721, 7195, 7197, 7632, 7372, 7729, 7364, 7371, 7442, 8011, 7499, 7996, 7396, 7921, 7492, 7496, 7973, 7800, 7976, 7321, 7479, 7938, 7588, 7523, 7631, 7541, 7800, 7916, 8138, 8065, 8093, 7478, 7748, 7654, 7697, 7629, 7781, 7867, 7086, 7909, 7287, 7575, 7234, 7675, 8597, 7590, 7690, 7526, 7358, 7950, 7450, 7433, 7705, 7601, 6963, 7583, 7774, 7880, 7911, 7815, 7877, 7378, 7379, 7755, 7906, 7355, 7911, 6978, 7584, 7580, 7854, 8228, 7259, 7882, 8042, 7681, 7699, 7828, 7214, 7630, 7544, 7488, 8092, 7926, 7196, 8095, 7697, 8404, 7285, 7574, 7587, 7509, 7642, 7793, 7969, 7325, 7431, 7029, 7790, 7766, 7361, 7629, 8123, 7333, 7638, 7475, 7464, 7104, 7848, 7725, 7770, 8120, 7948, 7561, 7807, 7562, 7538, 7533, 7558, 7769, 7648, 7914, 8023, 7922, 7600, 8622, 7884, 7413, 7886, 7349, 7504, 7883, 7689, 7631, 7786, 7704, 8587, 7613, 7901, 7300, 7553, 7749, 7409, 8019, 7927, 7165, 8330, 7631, 7235, 7443, 7996, 7812, 7653, 7334, 7725, 7732, 7841, 7171, 7927, 8173, 8131, 7090, 7667, 8293, 7813, 7501, 7603, 7550, 7827, 7564, 7380, 7452, 7599, 7873, 7758, 7617, 7745, 8178, 7924, 7536, 7773, 7814, 7512, 7337, 7296, 7655, 7925, 8248, 7681, 7817, 7985, 7943, 7701, 7683, 8265, 7687, 7500, 7334, 7409, 7654, 7585, 7531, 7493, 7521, 8053, 7940, 7642, 7644, 8076, 7512, 7109, 7383, 7967, 7885, 7758, 7295, 7935, 7874, 7566, 7294, 8102, 7722, 7991, 7639, 7594, 8188, 7234, 7207, 7656, 7634, 7601, 7677, 7402, 7432, 7696, 7454, 7891, 8302, 7268, 7580, 7813, 7577, 8159, 7603, 7570, 7733, 7331, 7460, 7830, 7786, 7254, 8077, 7656, 7393, 7557, 7750, 7408, 7795, 7467, 7845, 7776, 7139, 7761, 7493, 7340, 7559, 7371, 7522, 7732, 7320, 7533, 7593, 7566, 7773, 7765, 7347, 8105, 7588, 7677, 8409, 8349, 7348, 7524, 7507, 8026, 8405, 7759, 7749, 7714, 7259, 7950, 7833, 7283, 7846, 7788, 7785, 7412, 8221, 7692, 7743, 7900, 8063, 7568, 7856, 7551, 7655, 7419, 7802, 7906, 7752, 7068, 7374, 7641, 7453, 7902, 7538, 7725, 7516, 7446, 7508, 7636, 7985, 8167, 7418, 7256, 7627, 7860, 7926, 7198, 7800, 7929, 7872, 7760, 7364, 6937, 7560, 7547, 7492, 7712, 7577, 8172, 7340, 7773, 7517, 7671, 7956, 7644, 7666, 7637, 7264, 7694, 7374, 7588, 7060, 7418, 7524, 7384, 7630, 7691, 7285, 7546, 8652, 7685, 7967, 7846, 7132, 7404, 7669, 7321, 7889, 7888, 7794, 7558, 7365, 7077, 7606, 7513, 7591, 8038, 7759, 7464, 7580, 7918, 7634, 7652, 7777, 7689, 7761, 7617, 7171, 7698, 7495, 7597, 8155, 8065, 7479, 7132, 7592, 7498, 7248, 7683, 8080, 7560, 7247, 7409, 7722, 7650, 7528, 7807, 7940, 7813, 7444, 7849, 7824, 7545, 7906, 7637, 7425, 7238, 7346, 7892, 7609, 7906, 7550, 7353, 7426, 8027, 7723, 8355, 7421, 7679, 7429, 7304, 7664, 7875, 6747, 7294, 7720, 7692, 7974, 7634, 7277, 7734, 7653, 7520, 7591, 8016, 7340, 7927, 7555, 7459, 7902, 7547, 7608, 7947, 7837, 7685, 7468, 7907, 7691, 7752, 7373, 7822, 8219, 7730, 7927, 8289, 7862, 8052, 7590, 7303, 7270, 8004, 7388, 7715, 7336, 8028, 7807, 7909, 7928, 7625, 7465, 7983, 7374, 7812, 8105, 7652, 7623, 7937, 7553, 7858, 7479, 7979, 7598, 7739, 7627, 7925, 7604, 7484, 7453, 7883, 7449, 7697, 8013, 8123, 8236, 7442, 8163, 7552, 7713, 7321, 7786, 7734, 8081, 7401, 7437, 8364, 7398, 7434, 8207, 8069, 7485, 8102, 7724, 8248, 7803, 8369, 7622, 7375, 7911, 7547, 8064, 7414, 7230, 7814, 7780, 7968, 7124, 7569, 7993, 7545, 7710, 7802, 7461, 7814, 7553, 7241, 7769, 7336, 7650, 7227, 7617, 7588, 8194, 7641, 7530, 7038, 6974, 8028, 7455, 7731, 7317, 8125, 7879, 7865, 8280, 7850, 7105, 7922, 7457, 7437, 7781, 7778, 7540, 7631, 7637, 7852, 8001, 7637, 7340, 7717, 7782, 7461, 8173, 7358, 7739, 7802, 7457, 7505, 7840, 7497, 7152, 7488, 7840, 7836, 7506, 6978, 7339, 7641, 8034, 7798, 7363, 7511, 7996, 8471, 7905, 7542, 7328, 7947, 7745, 8072, 7527, 6965, 7243, 7512, 7347, 7416, 7530, 7476, 7346, 7755, 7975, 7820, 7832, 7300, 7552, 8374, 8286, 7489, 7960, 7972, 7515, 7613, 7640, 7316, 7492, 7310, 7732, 7729, 7326, 7906, 7365, 7533, 7857, 7718, 7139, 7622, 8152, 6962, 7606, 7683, 6947, 7719, 7731, 7547, 7616, 7616, 7281, 7586, 7800, 7985, 7523, 7258, 7386, 7677, 7683, 6986, 7296, 7745, 7691, 7429, 7925, 7300, 7915, 8216, 7726, 7676, 7399, 7449, 8348, 7553, 7223, 7651, 7896, 7591, 7319, 8068, 7828, 7537, 7310, 7759, 7784, 7700, 7994, 7223, 7588, 7325, 7538, 7857, 7591, 7111, 8336, 6737, 7899, 7480, 8010, 7736, 7747, 7573, 7648, 7616, 8126, 7886, 7746, 7321, 7745, 7777, 7926, 7984, 7640, 7526, 7521, 7911, 7706, 7882, 7468, 7921, 8298, 7837, 7705, 7171, 7779, 7735, 7707, 8098, 7887, 7640, 7352, 7517, 8312, 8076, 7786, 7450, 7893, 7406, 7648, 6815, 7225, 7607, 7844, 7877, 7273, 7396, 7145, 7951, 8152, 7950, 7496, 7358, 7813, 7395, 7477, 7501, 7627, 7572, 7482, 7119, 7302, 7502, 7120, 7842, 7765, 7677, 7665, 6785, 8349, 7635, 7636, 7426, 7476, 7179, 7515, 7919, 8164, 7702, 7303, 7864, 7530, 7870, 8011, 8001, 7936, 7497, 8142, 7089, 7486, 7575, 7818, 7451, 7596, 7358, 7485, 7815, 7342, 7721, 7218, 7625, 7336, 7665, 7770, 7681, 7773, 7275, 7456, 7054, 7348, 7544, 7623, 7744, 7346, 7743, 7573, 7476, 7230, 7582, 7559, 7141, 7068, 7846, 7147, 7364, 7962, 7462, 7611, 8052, 7833, 7757, 7367, 7524, 7170, 7563, 7410, 7938, 7830, 7385, 7687, 7698, 7773, 7544, 7784, 7403, 7209, 7713, 7681, 8078, 7737, 7559, 7387, 7226, 7492, 7288, 8035, 7670, 8093, 7702, 7628, 7368, 7683, 7411, 7589, 7220, 7755, 7998, 7302, 7374, 7582, 7654, 8095, 7336, 8412, 7544, 7441, 7785, 8085, 7395, 7944, 7725, 7626, 7367, 7418, 7732, 7349, 7833, 7703, 6814, 7758, 7514, 7577, 7936, 7788, 7380, 7680, 7844, 7487, 7528, 7435, 8170, 7955, 7877, 7667, 7323, 8468, 8269, 7789, 7517, 7708, 7839, 7543, 7244, 7394, 8060, 7598, 7754, 7799, 7962, 7055, 7825, 7524, 8186, 7827, 7298, 8060, 7893, 7366, 7710, 7855, 7792]
    extra_future_stats_info_loc = extra_future_stats_info.find("*") + 1
    total_amount_of_simss = extra_future_stats_info[:extra_future_stats_info_loc-1]
    extra_future_stats_info = extra_future_stats_info[extra_future_stats_info_loc:]
    extra_future_stats_info = ast.literal_eval(extra_future_stats_info)
    extra_all_dps_results = extra_future_stats_info
    #extra_all_dps_results = []
    #for i in extra_future_stats_info:
        #i = round(i)
        #extra_all_dps_results.append(i)
    extra_all_dps_results_min = int(min(extra_all_dps_results))
    extra_all_dps_results_max = int(max(extra_all_dps_results))
    counts1, bins1 = np.histogram(extra_all_dps_results, bins=range(extra_all_dps_results_min, extra_all_dps_results_max, 50))
    bins1 = 0.5 * (bins1[:-1] + bins1[1:])
    fig_250_title = str("DPS Breakdown for All ") + str(total_amount_of_simss) + str(" Simulations")
    fig250 = px.bar(x=bins1, y=counts1, labels={'x':'DPS', 'y':'Occurrence'}, title=fig_250_title, template="plotly_dark", color=counts1, color_continuous_scale="sunset")
    fig250.update_layout(coloraxis_showscale=False)
    
    data_251 = pd.DataFrame(dict(DPSValue=extra_all_dps_results))
    fig251  = px.box(data_251, x="DPSValue", template="plotly_dark")
    fig251.update_layout(xaxis=dict(
                          title=None,
                          showgrid=False, ),
                            yaxis=dict(
                            title=None,
                            showgrid=False,))
    #fig251.update_traces(orientation='h') 
    #fig250 = px.histogram(x=bins1, y=counts1, labels={'x':'DPS', 'y':'Occurrence'}, title=fig_250_title, template="plotly_dark", marginal="box")
    #extra_stats_split_list = extra_sim_stats_info.replace("*^*",", ")
    #extra_stats_split_list = extra_stats_split_list.split(", ")


    # extra_stats_split_list = extra_sim_stats_info.split("*^*")
    # current_gear_split_list = gear_currently_worn.split("*&*")



    e_stats_hit = extra_stats_split_list[0]
    e_stats_hit_perc = extra_stats_split_list[1] + "%"
    e_stats_crit = extra_stats_split_list[2] + "%"
    e_stats_crit_rating = extra_stats_split_list[3]
    e_stats_strength = extra_stats_split_list[4]
    e_stats_stamina = extra_stats_split_list[5]
    e_stats_hp = extra_stats_split_list[6]
    e_stats_armor = extra_stats_split_list[7]
    e_stats_agi = extra_stats_split_list[8]
    e_stats_ap = extra_stats_split_list[9]
    e_stats_armor_pen = extra_stats_split_list[10]
    e_stats_armor_pen_perc = extra_stats_split_list[11] + "%"
    e_stats_expertise = extra_stats_split_list[12]
    e_stats_expertise_rating = extra_stats_split_list[13]
    e_stats_expertise_dodge_parry_reduc = str(float(e_stats_expertise) * .25) + "%"
    e_stats_haste = extra_stats_split_list[14] + "%"
    e_stats_haste_rating = extra_stats_split_list[15]
    c_g_head = current_gear_split_list[0]
    c_g_neck = current_gear_split_list[1]
    c_g_shoulders = current_gear_split_list[2]
    c_g_back = current_gear_split_list[3]
    c_g_chest = current_gear_split_list[4]
    c_g_wrist = current_gear_split_list[5]
    c_g_gloves = current_gear_split_list[6]
    c_g_waist = current_gear_split_list[7]
    c_g_legs = current_gear_split_list[8]
    c_g_boots = current_gear_split_list[9]
    c_g_ring1 = current_gear_split_list[10]
    c_g_ring2 = current_gear_split_list[11]
    c_g_trinket1 = current_gear_split_list[12]
    c_g_trinket2 = current_gear_split_list[13]
    c_g_sigil = current_gear_split_list[14]
    c_g_mh = current_gear_split_list[15]
    c_g_oh = current_gear_split_list[16]
    c_g_2h = extra_stats_split_list[16]
    c_g_2h = ast.literal_eval(c_g_2h)



    #Extra future stuff
    future_extra_sim_stats_info = dash_all_data["content_extra_future_stats_area"] #database 1 (version 2)
    future_extra_sim_stats_info = future_extra_sim_stats_info.to_string(index = False) #database 1 (version 2)


    # dash_all_data = dash_all_data.to_string(index = False)
    # dash_data_split = dash_all_data.split("*&*")
    # t_damage = float(dash_data_split[1])
    # fight_length = float(dash_data_split[2])
    # rotation = dash_data_split[3]
    # rotation = ast.literal_eval(rotation)
    # rotation_time = dash_data_split[4]
    # rotation_time = ast.literal_eval(rotation_time)
    # rotation_damage = dash_data_split[5]
    # rotation_damage = ast.literal_eval(rotation_damage)
    # rotation_status = dash_data_split[6]
    # rotation_status = ast.literal_eval(rotation_status)
    # rune_0_tracker = dash_data_split[7]
    # rune_0_tracker = ast.literal_eval(rune_0_tracker)
    # rune_1_tracker = dash_data_split[8]
    # rune_1_tracker = ast.literal_eval(rune_1_tracker)
    # rune_2_tracker = dash_data_split[9]
    # rune_2_tracker = ast.literal_eval(rune_2_tracker)
    # rune_3_tracker = dash_data_split[10]
    # rune_3_tracker = ast.literal_eval(rune_3_tracker)
    # rune_4_tracker = dash_data_split[11]
    # rune_4_tracker = ast.literal_eval(rune_4_tracker)
    # rune_5_tracker = dash_data_split[12]
    # rune_5_tracker = ast.literal_eval(rune_5_tracker)
    # rune_6_tracker = dash_data_split[13]
    # rune_6_tracker = ast.literal_eval(rune_6_tracker)
    # rune_7_tracker = dash_data_split[14]
    # rune_7_tracker = ast.literal_eval(rune_7_tracker)
    # rune_8_tracker = dash_data_split[15]
    # rune_8_tracker = ast.literal_eval(rune_8_tracker)
    # rune_9_tracker = dash_data_split[16]
    # rune_9_tracker = ast.literal_eval(rune_9_tracker)
    # rune_10_tracker = dash_data_split[17]
    # rune_10_tracker = ast.literal_eval(rune_10_tracker)
    # rune_11_tracker = dash_data_split[18]
    # rune_11_tracker = ast.literal_eval(rune_11_tracker)
    # rune_time_tracker = dash_data_split[19]
    # rune_time_tracker = ast.literal_eval(rune_time_tracker)
    # runic_power_tracker = dash_data_split[20]
    # runic_power_tracker = ast.literal_eval(runic_power_tracker)
    all_data = pd.DataFrame()
    all_data2 = pd.DataFrame()
    ability_order = rotation
    timeline_order = rotation_time
    damage_order = rotation_damage
    status_order = rotation_status
    timeline_order_data = []
    timeline_order_data_end = []
    for i in timeline_order:
        if i < 1:
            i = .000001
        i = round(i, 6)
        iz = i + 0.5
        if type(i) == int or i.is_integer() == True:
            i += .000001
        if type(iz) == int or iz.is_integer() == True:
            iz += .000001
        i = timedelta(seconds=i)
        iz = timedelta(seconds=iz)
        total = "1970-01-01 " + str(i)
        total_end = "1970-01-01 " + str(iz)
        finished_converted_time = datetime.strptime(total, '%Y-%m-%d %H:%M:%S.%f')
        finished_converted_time_end = datetime.strptime(total_end, '%Y-%m-%d %H:%M:%S.%f')
        timeline_order_data.append(finished_converted_time)
        timeline_order_data_end.append(finished_converted_time_end)
    x = 0
    for i in ability_order:
        if damage_order[x] == 0:
            damage_scale = 0
        elif damage_order[x] < 150:
            damage_scale = "Under 150"
        elif damage_order[x] < 300:
            damage_scale = "Under 300"
        elif damage_order[x] < 500:
            damage_scale = "Under 500"
        elif damage_order[x] < 750:
            damage_scale = "Under 750"
        elif damage_order[x] < 1000:
            damage_scale = "Under 1000"
        elif damage_order[x] < 2000:
            damage_scale = "Under 2000"
        elif damage_order[x] >= 2000:
            damage_scale = "Over 2000"
        data = pd.DataFrame(dict(Ability=i, index=[0],Start=timeline_order_data[x], Finish=timeline_order_data_end[x], Damage=damage_order[x], Status=status_order[x]))
        all_data = pd.concat([all_data, data])
        data2 = pd.DataFrame(dict(Ability=i, index=[0],Start=timeline_order_data[x], Finish=timeline_order_data_end[x], Damage=damage_order[x], Status=status_order[x], DamageScale=damage_scale))
        all_data2 = pd.concat([all_data2, data2])
        x += 1
    unique_ability_df_table = []
    unique_miss_count_df_table = []
    unique_dodge_count_df_table = []
    unique_parry_count_df_table = []
    unique_glance_count_df_table = []
    unique_block_count_df_table = []
    unique_crit_count_df_table = []
    unique_hit_count_df_table = []
    unique_dot_count_df_table = []
    unique_active_count_df_table = []
    unique_proc_count_df_table = []
    unique_damage_per_cast_df_table = []
    unique_damage_df_table = []
    for i in np.unique(np.array(ability_order)):
        search_data = all_data.loc[all_data['Ability'] == i]
        miss_search = search_data.loc[search_data['Status'] == "Miss"]
        dodge_search = search_data.loc[search_data['Status'] == "Dodge"]
        parry_search = search_data.loc[search_data['Status'] == "Parry"]
        glance_search = search_data.loc[search_data['Status'] == "Glance"]
        block_search = search_data.loc[search_data['Status'] == "Block"]
        crit_search = search_data.loc[search_data['Status'] == "Crit"]
        hit_search = search_data.loc[search_data['Status'] == "Hit"]
        dot_search = search_data.loc[search_data['Status'] == "DOT"]
        active_search = search_data.loc[search_data['Status'] == "Active"]
        proc_search = search_data.loc[search_data['Status'] == "Proc"]
        if miss_search.empty:
            unique_miss_count_df_table.append(0)
        else:
            unique_miss_count_df_table.append(len(miss_search.index))

        if dodge_search.empty:
            unique_dodge_count_df_table.append(0)
        else:
            unique_dodge_count_df_table.append(len(dodge_search.index))
        if parry_search.empty:
            unique_parry_count_df_table.append(0)
        else:
            unique_parry_count_df_table.append(len(parry_search.index))
        if glance_search.empty:
            unique_glance_count_df_table.append(0)
        else:
            unique_glance_count_df_table.append(len(glance_search.index))
        if block_search.empty:
            unique_block_count_df_table.append(0)
        else:
            unique_block_count_df_table.append(len(block_search.index))
        if crit_search.empty:
            unique_crit_count_df_table.append(0)
        else:
            unique_crit_count_df_table.append(len(crit_search.index))
        if hit_search.empty:
            unique_hit_count_df_table.append(0)
        else:
            unique_hit_count_df_table.append(len(hit_search.index))
        if dot_search.empty:
            unique_dot_count_df_table.append(0)
        else:
            unique_dot_count_df_table.append(len(dot_search.index))
        if active_search.empty:
            unique_active_count_df_table.append(0)
        else:
            unique_active_count_df_table.append(len(active_search.index))
        if proc_search.empty:
            unique_proc_count_df_table.append(0)
        else:
            unique_proc_count_df_table.append(len(proc_search.index))
        unique_damage_per_cast_df_table.append(round((sum(search_data['Damage'])) / len(search_data['Damage']), 4))
        unique_damage_df_table.append(round(sum(search_data['Damage']), 4))
        unique_ability_df_table.append(i)
    status_table_data = pd.DataFrame(dict(Ability=unique_ability_df_table, Miss=unique_miss_count_df_table, Dodge=unique_dodge_count_df_table, Parry=unique_parry_count_df_table, Glance=unique_glance_count_df_table, Block=unique_block_count_df_table, Crit=unique_crit_count_df_table, Hit=unique_hit_count_df_table, DOT=unique_dot_count_df_table, Active=unique_active_count_df_table, Proc=unique_proc_count_df_table, Avg_Damage=unique_damage_per_cast_df_table, All_Damage=unique_damage_df_table))


    statuss_sum_list = ["Miss", "Dodge", "Parry", "Glance", "Block", "Crit", "Hit", "DOT", "Active", "Proc"]
    status_table_data['Sum'] = status_table_data[statuss_sum_list].sum(axis=1)
    status_table_data['MissP'] = status_table_data["Miss"]/status_table_data["Sum"]
    status_table_data['DodgeP'] = status_table_data["Dodge"]/status_table_data["Sum"]
    status_table_data['ParryP'] = status_table_data["Parry"]/status_table_data["Sum"]
    status_table_data['GlanceP'] = status_table_data["Glance"]/status_table_data["Sum"]
    status_table_data['BlockP'] = status_table_data["Block"]/status_table_data["Sum"]
    status_table_data['CritP'] = status_table_data["Crit"]/status_table_data["Sum"]
    status_table_data['HitP'] = status_table_data["Hit"]/status_table_data["Sum"]
    status_table_data['DOTP'] = status_table_data["DOT"]/status_table_data["Sum"]
    status_table_data['ActiveP'] = status_table_data["Active"]/status_table_data["Sum"]
    status_table_data['ProcP'] = status_table_data["Proc"]/status_table_data["Sum"]
    status_table_data['MissP'] = status_table_data['MissP'].apply(lambda x: x * 100)
    status_table_data['DodgeP'] = status_table_data['DodgeP'].apply(lambda x: x * 100)
    status_table_data['ParryP'] = status_table_data['ParryP'].apply(lambda x: x * 100)
    status_table_data['GlanceP'] = status_table_data['GlanceP'].apply(lambda x: x * 100)
    status_table_data['BlockP'] = status_table_data['BlockP'].apply(lambda x: x * 100)
    status_table_data['CritP'] = status_table_data['CritP'].apply(lambda x: x * 100)
    status_table_data['HitP'] = status_table_data['HitP'].apply(lambda x: x * 100)
    status_table_data['DOTP'] = status_table_data['DOTP'].apply(lambda x: x * 100)
    status_table_data['ActiveP'] = status_table_data['ActiveP'].apply(lambda x: x * 100)
    status_table_data['ProcP'] = status_table_data['ProcP'].apply(lambda x: x * 100)
    status_table_data = status_table_data.round({'MissP': 2, 'DodgeP': 2, 'ParryP': 2, 'GlanceP': 2, 'BlockP': 2, 'CritP': 2, 'HitP': 2, 'DOTP': 2, 'ActiveP': 2, 'ProcP': 2})
    status_table_data['MissP'] = status_table_data['MissP'].astype(str) + '%'
    status_table_data['DodgeP'] = status_table_data['DodgeP'].astype(str) + '%'
    status_table_data['ParryP'] = status_table_data['ParryP'].astype(str) + '%'
    status_table_data['GlanceP'] = status_table_data['GlanceP'].astype(str) + '%'
    status_table_data['BlockP'] = status_table_data['BlockP'].astype(str) + '%'
    status_table_data['CritP'] = status_table_data['CritP'].astype(str) + '%'
    status_table_data['HitP'] = status_table_data['HitP'].astype(str) + '%'
    status_table_data['DOTP'] = status_table_data['DOTP'].astype(str) + '%'
    status_table_data['ActiveP'] = status_table_data['ActiveP'].astype(str) + '%'
    status_table_data['ProcP'] = status_table_data['ProcP'].astype(str) + '%'
    status_table_data['DPSPA'] = status_table_data["All_Damage"].apply(lambda x: x / fight_length)
    status_table_data = status_table_data.round({'DPSPA': 3})

    dps_timeline_breaks = int(fight_length / 3)
    time_each_break = fight_length / dps_timeline_breaks
    time_breaks = []
    timeline_dps_list = []
    for times in range(0, dps_timeline_breaks):
        times += 1
        timeline_current_time = times * time_each_break
        time_breaks.append(times * time_each_break)
        timeline_dps_num = []
        for timeline_time_position, timeline_time in enumerate(timeline_order):
            if timeline_time < timeline_current_time:
                timeline_dps_num.append(timeline_time_position)
        timeline_damage_list = []
        for timeline_damage in timeline_dps_num:
            timeline_damage_list.append(damage_order[timeline_damage])
        timeline_damage = sum(timeline_damage_list)
        timeline_dps = timeline_damage / timeline_current_time
        timeline_dps_list.append(timeline_dps)
    dps_table_data = pd.DataFrame(dict(DPS=timeline_dps_list, Time=time_breaks))

    stats_columns_names = ["Hit", "Hit Percentage", "Crit", "Crit Rating", "Strength", "Stamina", "Health", "Armor", "Agility", "Attack Power", "Armor Penetration", "Armor Penetration Percentage", "Expertise", "Expertise Rating", "Dodge & Parry Reduction", "Haste", "Haste Rating"]
    stats_columns_stats = [e_stats_hit, e_stats_hit_perc, e_stats_crit, e_stats_crit_rating, e_stats_strength, e_stats_stamina, e_stats_hp, e_stats_armor, e_stats_agi, e_stats_ap, e_stats_armor_pen, e_stats_armor_pen_perc, e_stats_expertise, e_stats_expertise_rating, e_stats_expertise_dodge_parry_reduc, e_stats_haste, e_stats_haste_rating]
    stats_table_data = pd.DataFrame(dict(Names=stats_columns_names, Data=stats_columns_stats))
    if c_g_2h == False:
        gear_columns_names = ["Head", "Neck", "Shoulders", "Back", "Chest", "Wrist", "Gloves", "Waist", "Legs", "Boots", "Ring1", "Ring2", "Trinket1", "Trinket2", "Sigil", "Main hand", "Off hand"]
        gear_columns_values = [c_g_head, c_g_neck, c_g_shoulders, c_g_back, c_g_chest, c_g_wrist, c_g_gloves, c_g_waist, c_g_legs, c_g_boots, c_g_ring1, c_g_ring2, c_g_trinket1, c_g_trinket2, c_g_sigil, c_g_mh, c_g_oh]
        gear_table_data = pd.DataFrame(dict(Names=gear_columns_names, Data=gear_columns_values))
    else:
        gear_columns_names = ["Head", "Neck", "Shoulders", "Back", "Chest", "Wrist", "Gloves", "Waist", "Legs", "Boots", "Ring1", "Ring2", "Trinket1", "Trinket2", "Sigil", "Main hand"]
        gear_columns_values = [c_g_head, c_g_neck, c_g_shoulders, c_g_back, c_g_chest, c_g_wrist, c_g_gloves, c_g_waist, c_g_legs, c_g_boots, c_g_ring1, c_g_ring2, c_g_trinket1, c_g_trinket2, c_g_sigil, c_g_mh]
        gear_table_data = pd.DataFrame(dict(Names=gear_columns_names, Data=gear_columns_values))



    colors = {'Main hand': '#45515E',
              'Off hand': '#576778',
              'Icy Touch': '#ACFDFC',
              'Obliterate': '#6AAEF7',
              'OH - Obliterate': '#55BDE0',
              'Frost Strike': '#2087f5',
              'OH - Frost Strike': '#12AADE',
              'Howling Blast': '#60FCFA',
              'Frost Fever': '#9AE3E2',
              'Blood Plague': '#E67F63',
              'Blood Strike': '#F2463D',
              'OH - Blood Strike': '#E6443A',
              'Blood Boil': '#FF3320',
              'Pestilence': '#D7F507',
              'Plague Strike': '#36C219',
              'OH - Plague Strike': '#2EA816',
              'Unbreakable Armor': '#F5A720',
              'Horn of Winter': '#CDD1C9',
              'Empowered Rune Weapon': '#7C9FC4',
              'Blood Tap': '#F54638',
              'Bloody Vengeance': '#DB7F8E',
              'Dancing Rune Weapon': '#FF3864',
              'Heart Strike': '#BC4B51',
              'Bone Shield': '#79B473',
              'Wandering Plague': '#98E02B',
              'Crypt Fever': '#8CB369',
              'Desolation': '#EFF7F6',
              'Scourge Strike': '#5C0029',
              'Blood-Caked Blades': '#91AEC1',
              'Necrosis': '#EAF2EF',
              'Death Coil': '#E2F89C',
              'Unholy Blight': '#0A8754',
              'Death and Decay': '#912F56',
              'Death Strike': '#A0A4B8',
              'Sudden Doom': '#D5E1A3',
              }
    colors_status = {'Hit': '#39CCCC',
              'Crit': '#FFDC00',
              'DOT': '#01FF70',
              'Proc': '#723BFF',
              'Active': '#381D7F',
              'Miss': '#FF4136',
              'Dodge': '#85144b',
              'Parry': '#FF283E',
              'Glance': '#80201B',
              'Block': '#40100D',
              }
    fig = px.timeline(all_data,x_start="Start", x_end="Finish", y="Ability", color="Ability",opacity=1, color_discrete_map=colors, hover_data=["Status", "Damage"], template="plotly_dark")
    fig.update_layout(xaxis=dict(
                          title='Timeline',
                          linecolor = "#BCCCDC",
                          showgrid=False,
                          tickformat = '%H:%M:%S',
                                      ),
                            yaxis=dict(
                            title=None,
                            linecolor="#BCCCDC",
                            showgrid=False,
                            ))
    t_dps = fight_length
    #t_dps = round(max(timeline_order),0)
    total_damage = round(sum(damage_order), 3)
    total_dps = round((t_damage / t_dps), 3)
    #t_damage = "Damage Status Map.                  Total Damage Done - " + str(t_damage) + "                  DPS - " + str(t_dps)
    total_damage = "Total Damage Done - " + str(total_damage) + "                  DPS - " + str(total_dps) + "                  Fight Length - " + str(fight_length) + "                  Number of Targets - " + str(number_of_targets_in_fight)
    fig.update_layout(
        hoverlabel=dict(
            font_size=12,
            font_family="Rockwell",
        )
    )
    all_data_no_zero = all_data.copy()
    all_data_no_zero = all_data_no_zero[all_data_no_zero.Damage != 0]
    fig2 = px.pie(all_data_no_zero, values='Damage', names='Ability', title='Damage by attack',color="Ability",color_discrete_map=colors, template="plotly_dark")
    fig3 = px.treemap(all_data, path=[px.Constant("All Damage"),'Ability', 'Status'], values='Damage',title=total_damage ,color="Ability",color_discrete_map=colors, template="plotly_dark")
    fig4 = px.pie(all_data, names='Status', title='Status Percentage',color="Status",color_discrete_map=colors_status, template="plotly_dark")
    fig5 = px.parallel_categories(all_data2, dimensions=['Ability', 'Status', 'DamageScale'],labels={'Ability':'Ability Name', 'Status':'Damage Status', 'DamageScale':'Damage Sclae'},color="Damage", color_continuous_scale=px.colors.sequential.Plotly3,range_color=(0,2000), template="plotly_dark")
    fig601 = px.line(dps_table_data, x='Time', y="DPS", template="plotly_dark")
    fig602 = px.scatter(dps_table_data,x='Time', y='DPS',color='DPS',template="plotly_dark")
    fig6 = go.Figure(data=fig601.data + fig602.data)
    rune_time_loop_num = 0
    for rune_time in rune_time_tracker:
        rune_0_tracker[rune_time_loop_num] -= rune_time
        if rune_0_tracker[rune_time_loop_num] < 0:
            rune_0_tracker[rune_time_loop_num] = 0
        rune_1_tracker[rune_time_loop_num] -= rune_time
        if rune_1_tracker[rune_time_loop_num] < 0:
            rune_1_tracker[rune_time_loop_num] = 0
        rune_2_tracker[rune_time_loop_num] -= rune_time
        if rune_2_tracker[rune_time_loop_num] < 0:
            rune_2_tracker[rune_time_loop_num] = 0
        rune_3_tracker[rune_time_loop_num] -= rune_time
        if rune_3_tracker[rune_time_loop_num] < 0:
            rune_3_tracker[rune_time_loop_num] = 0
        rune_4_tracker[rune_time_loop_num] -= rune_time
        if rune_4_tracker[rune_time_loop_num] < 0:
            rune_4_tracker[rune_time_loop_num] = 0
        rune_5_tracker[rune_time_loop_num] -= rune_time
        if rune_5_tracker[rune_time_loop_num] < 0:
            rune_5_tracker[rune_time_loop_num] = 0
        rune_6_tracker[rune_time_loop_num] -= rune_time
        if rune_6_tracker[rune_time_loop_num] < 0:
            rune_6_tracker[rune_time_loop_num] = 0
        rune_7_tracker[rune_time_loop_num] -= rune_time
        if rune_7_tracker[rune_time_loop_num] < 0:
            rune_7_tracker[rune_time_loop_num] = 0
        rune_8_tracker[rune_time_loop_num] -= rune_time
        if rune_8_tracker[rune_time_loop_num] < 0:
            rune_8_tracker[rune_time_loop_num] = 0
        rune_9_tracker[rune_time_loop_num] -= rune_time
        if rune_9_tracker[rune_time_loop_num] < 0:
            rune_9_tracker[rune_time_loop_num] = 0
        rune_10_tracker[rune_time_loop_num] -= rune_time
        if rune_10_tracker[rune_time_loop_num] < 0:
            rune_10_tracker[rune_time_loop_num] = 0
        rune_11_tracker[rune_time_loop_num] -= rune_time
        if rune_11_tracker[rune_time_loop_num] < 0:
            rune_11_tracker[rune_time_loop_num] = 0
        rune_time_loop_num += 1

    rune_table_data = pd.DataFrame(dict(Rune0=rune_0_tracker,
    Rune1=rune_1_tracker,
    Rune2=rune_2_tracker,
    Rune3=rune_3_tracker,
    Rune4=rune_4_tracker,
    Rune5=rune_5_tracker,
    Rune6=rune_6_tracker,
    Rune7=rune_7_tracker,
    Rune8=rune_8_tracker,
    Rune9=rune_9_tracker,
    Rune10=rune_10_tracker,
    Rune11=rune_11_tracker,
    RuneTime=rune_time_tracker))
    runic_power_data = pd.DataFrame(dict(Runicpower=runic_power_tracker, Time=rune_time_tracker))
    fig7 = go.Figure()
    # fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["RuneTime"], mode="lines", name="Time", line_color='#ffffff'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune0"], mode="lines", name="Blood1", line_color='#FF4136'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune1"], mode="lines", name="Blood2", line_color='#FF4136'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune2"], mode="lines", name="Frost1", line_color='#39CCCC'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune3"], mode="lines", name="Frost2", line_color='#39CCCC'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune4"], mode="lines", name="Unholy1", line_color='#2ECC40'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune5"], mode="lines", name="Unholy2", line_color='#2ECC40'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune6"], mode="lines", name="Death_Blood1", line_color='#80201B'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune7"], mode="lines", name="Death_Blood2", line_color='#80201B'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune8"], mode="lines", name="Death_Frost1", line_color='#154D4D'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune9"], mode="lines", name="Death_Frost2", line_color='#154D4D'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune10"], mode="lines", name="Death_Unholy1", line_color='#124D18'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune11"], mode="lines", name="Death_Unholy2", line_color='#124D18'))
    fig7.update_layout(yaxis_range=[0, 10])
    # fig7.update_layout(yaxis_range=[0,int(fight_length+1)])
    fig7.update_layout(title="Rune Usage Cooldowns", template="plotly_dark")
    fig7.update_traces(mode="lines", hovertemplate=None)
    fig7.update_layout(hovermode="x")
    fig7.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False)
              )
    fig8 = px.line(runic_power_data, x="Time", y="Runicpower", title='Runic Power Usage', template="plotly_dark")
    fig8.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False)
              )
    fig2.update_layout(
        hoverlabel=dict(
            font_size=12,
            font_family="Rockwell",
        )
    )
    fig3.update_layout(
        hoverlabel=dict(
            font_size=12,
            font_family="Rockwell",
        )
    )
    fig4.update_layout(
        hoverlabel=dict(
            font_size=12,
            font_family="Rockwell",
        )
    )
    fig3.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    fig6.update_layout(title="Damage Over Time", template="plotly_dark")
    fig6.update_traces(line_color='#ffffff', line_width=1)
    fig6.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False)
              )



    return html.Div(children=[
        html.Div([
            html.H1(children='Last Simulation', style={'color': '#ffffff'}),
            dcc.Graph(
                id='graph1',
                figure=fig
            ),
        ]),
        html.Div([
            dcc.Graph(
                id='graph3',
                figure=fig3
            ),
        ]),
        html.Div([
            dcc.Graph(
                id='graph250',
                figure=fig250
            ),
        ]),
         html.Div([
            dcc.Graph(
                id='graph251',
                figure=fig251
            ),
        ]),
        html.Div(children=[
            dcc.Graph(id="graph2",figure=fig2, style={'display': 'inline-block'}),
            dcc.Graph(id="graph4",figure=fig4, style={'display': 'inline-block'})
        ]),
        html.Div([
            dash_table.DataTable(id='table',
                #columns=[{"name": i, "id": i} for i in status_table_data.columns],
                columns=[{"name": "Ability", "id":"Ability"},{"name": "Miss", "id":"Miss"},
                      {"name": "Dodge", "id":"Dodge"},{"name": "Parry", "id":"Parry"},
                      {"name": "Glance", "id":"Glance"},{"name": "Block", "id":"Block"},
                      {"name": "Crit", "id":"Crit"},{"name": "Hit", "id":"Hit"},
                      {"name": "DOT", "id":"DOT"},{"name": "Active", "id":"Active"},
                      {"name": "Proc", "id":"Proc"},{"name": "Average Damage", "id":"Avg_Damage"},
                      {"name": "Total Damage", "id":"All_Damage"},
                      {"name": "Average DPS", "id":"DPSPA"},
                      


                    #  {"name": "Sum - DELETE", "id":"Sum"},{"name": "MissPercentage - DELETE", "id":"MissP"},
                         ],
                data=status_table_data.to_dict('records'),
                tooltip_data=[{
                    'Miss': {'value': '{}'.format(str(row['MissP']) + " Miss Rate"), 'type': 'markdown'},
                    'Dodge': {'value': '{}'.format(str(row['DodgeP']) + " Dodge Rate"), 'type': 'markdown'},
                    'Parry': {'value': '{}'.format(str(row['ParryP']) + " Parry Rate"), 'type': 'markdown'},
                    'Glance': {'value': '{}'.format(str(row['GlanceP']) + " Glance Rate"), 'type': 'markdown'},
                    'Block': {'value': '{}'.format(str(row['BlockP']) + " Block Rate"), 'type': 'markdown'},
                    'Crit': {'value': '{}'.format(str(row['CritP']) + " Crit Rate"), 'type': 'markdown'},
                    'Hit': {'value': '{}'.format(str(row['HitP']) + " Hit Rate"), 'type': 'markdown'},
                    'DOT': {'value': '{}'.format(str(row['DOTP']) + " DOT Rate"), 'type': 'markdown'},
                    'Active': {'value': '{}'.format(str(row['ActiveP']) + " Active Rate"), 'type': 'markdown'},
                    'Proc': {'value': '{}'.format(str(row['ProcP']) + " Proc Rate"), 'type': 'markdown'},
                    'Avg_Damage': {'value': '{}'.format(str(row['Ability'])), 'type': 'markdown'},
                    'All_Damage': {'value': '{}'.format(str(row['Ability'])), 'type': 'markdown'},
                    'DPSPA': {'value': '{}'.format(str(row['Ability'])), 'type': 'markdown'},
                 } for row in status_table_data.to_dict('records')],
                css=[{
                    'selector': '.dash-table-tooltip',
                    'rule': 'background-color: grey !important; font-family: monospace; color: white !important; textAlign: center'
                }],
                tooltip_delay=0,
                tooltip_duration=None,
                style_cell={'textAlign': 'center'},
                style_data={'color': 'white','backgroundColor': 'black'},
                style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': '#4D4B4B',
            },
            {
            "if": {"state": "selected"},
            # "backgroundColor": "#94E66C",
            "backgroundColor": "inherit !important",
            "border": "inherit !important",
            # 'fontWeight': 'bold'
            },
            {
                'if': {
                    'filter_query': '{Miss} > 0',
                    'column_id': 'Miss'
                },
                'backgroundColor': '#FF4136',
                'color': 'white'
            },
            {
                'if': {
                    'column_id': 'Dodge',
                    'filter_query': '{Dodge} > 0'
                },
                'backgroundColor': '#85144b',
            },
            {
                'if': {
                    'column_id': 'Parry',
                    'filter_query': '{Parry} > 0'
                },
                'backgroundColor': '#FF283E',
            },
            {
                'if': {
                    'column_id': 'Glance',
                    'filter_query': '{Glance} > 0'
                },
                'backgroundColor': '#80201B',
            },
            {
                'if': {
                    'column_id': 'Block',
                    'filter_query': '{Block} > 0'
                },
                'backgroundColor': '#40100D',
            },
            {
                'if': {
                    'column_id': 'Crit',
                    'filter_query': '{Crit} > 0'
                },
                'backgroundColor': '#FFDC00',
                'color': 'black'
            },
            {
                'if': {
                    'column_id': 'Hit',
                    'filter_query': '{Hit} > 0'
                },
                'backgroundColor': '#39CCCC',
                'color': 'black'
            },
            {
                'if': {
                    'column_id': 'DOT',
                    'filter_query': '{DOT} > 0'
                },
                'backgroundColor': '#01FF70',
                'color': 'black'
            },
            {
                'if': {
                    'column_id': 'Active',
                    'filter_query': '{Active} > 0'
                },
                'backgroundColor': '#381D7F',
            },
            {
                'if': {
                    'column_id': 'Proc',
                    'filter_query': '{Proc} > 0'
                },
                'backgroundColor': '#723BFF',
            }
        ],
                style_header={
        'backgroundColor': 'rgb(210, 210, 210)',
        'color': 'black',
        'fontWeight': 'bold'
    },
            )
        ]),
        html.Div([

            dcc.Graph(
                id='graph6',
                figure=fig6
            ),
        ]),
        html.Div([

            dcc.Graph(
                id='graph5',
                figure=fig5
            ),
        ]),
        html.Div([

            dcc.Graph(
                id='graph7',
                figure=fig7
            ),
        ]),
        html.Div([

            dcc.Graph(
                id='graph8',
                figure=fig8
            ),
        ]),
        html.Div(children=[
    html.Div(children=[
    html.Div([
            dash_table.DataTable(id='table2',
                columns=[{"name": "N", "id":"Names"},{"name": "D", "id":"Data"},
                          ],
                data=stats_table_data.to_dict('records'),
                style_cell={'textAlign': 'center'},
                style_data={'color': 'white','backgroundColor': 'black'},
                style_header = {'display': 'none'},
                style_data_conditional=[
                    {
            'if': {'column_id': 'Data'},
            "fontWeight": "bold",
            'textAlign': 'right'

        },
                    {
            'if': {'column_id': 'Names'},
            "fontWeight": "italic",
            'textAlign': 'right'

        },
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': '#4D4B4B',
            },]
        )
        ],style={'display': 'inline-block', 'float': 'left', 'padding-left': '250px'}),
    html.Div([
            dash_table.DataTable(id='table3',
                #columns=[{"name": "N", "id":"Names"},{"name": "D", "id":"Data"},
                #          ],
                columns=[{"name": "D", "id":"Data"},{"name": "N", "id":"Names"},
                          ],
                data=gear_table_data.to_dict('records'),
                style_cell={'textAlign': 'center'},
                style_data={'color': 'white','backgroundColor': 'black'},
                style_header = {'display': 'none'},
                style_data_conditional=[
                    {
            'if': {'column_id': 'Data'},
            "fontWeight": "bold",
            'textAlign': 'left'

        },
                    {
            'if': {'column_id': 'Names'},
            "fontWeight": "italic",
            'textAlign': 'left'

        },
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': '#4D4B4B',
            },]
        )
        ],style={'display': 'inline-block', 'float': 'right', 'padding-right': '250px'}),
    ])
        ]),
        html.Div(
        [   html.H1(
            html.I("Buff'd Stats & Gear", style={'color': '#ffffff'}), style={'textAlign': 'center'}),
            html.Br(),
        ]),
        html.Div(
        [   html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
            html.H1(
            html.I("", style={'color': '#ffffff'}), style={'textAlign': 'center'}),
            html.Br(),
        ])
    ])

serverll.layout = html.Div(children=[
all_lastlaugh_stuff()
])