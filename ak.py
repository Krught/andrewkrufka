
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
    #rotation = dash_all_data["content_dps_results_rotation"] #database 1 (version 2)
    # rotation = rotation.to_list() #database 1 (version 2)
    # rotation = str(rotation)
    # rotation = rotation[2:-2]
    # rotation = rotation.replace("\\", "")
    # rotation = ast.literal_eval(rotation)

    rotation_time = data_time
    #rotation_time = dash_all_data["content_dps_results_rotation_time"] #database 1 (version 2)
    # rotation_time = rotation_time.to_list() #database 1 (version 2)
    # rotation_time = str(rotation_time)
    # rotation_time = rotation_time[2:-2]
    # rotation_time = ast.literal_eval(rotation_time)

    rotation_damage = data_dam
    #rotation_damage = dash_all_data["content_dps_results_rotation_damage"] #database 1 (version 2)
    # rotation_damage = rotation_damage.to_list() #database 1 (version 2)
    # rotation_damage = str(rotation_damage)
    # rotation_damage = rotation_damage[2:-2]
    # rotation_damage = ast.literal_eval(rotation_damage)

    rotation_status = data_sta
    #rotation_status = dash_all_data["content_dps_results_rotation_status"] #database 1 (version 2)
    # rotation_status = rotation_status.to_list() #database 1 (version 2)
    # rotation_status = str(rotation_status)
    # rotation_status = rotation_status[2:-2]
    # rotation_status = ast.literal_eval(rotation_status)



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

    # dps_timeline_breaks = int(fight_length / 3)
    # time_each_break = fight_length / dps_timeline_breaks
    # time_breaks = []
    # timeline_dps_list = []
    # for times in range(0, dps_timeline_breaks):
    #     times += 1
    #     timeline_current_time = times * time_each_break
    #     time_breaks.append(times * time_each_break)
    #     timeline_dps_num = []
    #     for timeline_time_position, timeline_time in enumerate(timeline_order):
    #         if timeline_time < timeline_current_time:
    #             timeline_dps_num.append(timeline_time_position)
    #     timeline_damage_list = []
    #     for timeline_damage in timeline_dps_num:
    #         timeline_damage_list.append(damage_order[timeline_damage])
    #     timeline_damage = sum(timeline_damage_list)
    #     timeline_dps = timeline_damage / timeline_current_time
    #     timeline_dps_list.append(timeline_dps)
    # dps_table_data = pd.DataFrame(dict(DPS=timeline_dps_list, Time=time_breaks))



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
    # t_dps = fight_length
    # total_damage = round(sum(damage_order), 3)
    # total_dps = round((t_damage / t_dps), 3)
    # total_damage = "Total Damage Done - " + str(total_damage) + "                  DPS - " + str(total_dps) + "                  Fight Length - " + str(fight_length) + "                  Number of Targets - " + str(number_of_targets_in_fight)
    fig.update_layout(
        hoverlabel=dict(
            font_size=12,
            font_family="Rockwell",
        )
    )
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
        html.Div([
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
    ])



server.layout = html.Div(children=[
all_dash_stuff()
])
