# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

import plotly.graph_objs as go

from helper import *
from data import Data

from datetime import datetime, date
from sklearn.manifold import MDS
import dash_table as dt

import pandas as pd
import base64
import io

PLOTLY_LOGO = "./assets/logo.png"

GLOBAL_MARGIN = {'l': 60, 'b': 60, 't': 10, 'r': 10}
GLOBAL_MARGIN_BOTTOMLARGE = {'l': 60, 'b': 100, 't': 10, 'r': 10}
GLOBAL_MARKER_SIZE = 7
GLOBAL_TEMPLATE = "plotly_white"
AGGREGATION = "Insgesamt"


external_stylesheets = [dbc.themes.CERULEAN]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


server = app.server

dataset_names = ["raw.csv", "raw_c.csv"]

loaded_datasets = {}
#data = Data()


app.layout = html.Div([



    dbc.Navbar(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("PPR Hausaufgaben Cheatingtool", className="ml-2")),
                    ],
                    align="center",
                    # no_gutters=True,
                ),
                href="https://www.ni.tu-berlin.de/menue/members/postgraduate_students_and_doctoral_candidates/goerttler_thomas/",
            ),
        ],
        color="primary",
        dark=True,
        id = "navbar",
    ),


    # content will be rendered in this element
    html.Div([

        dbc.Row(
                [

                    dbc.Col(html.Div([
                        dbc.FormGroup(
                            [
                                dbc.Label("Datei", html_for="example-email"),
                                dbc.FormText("Lade Datei", color="secondary"),
                                dcc.Upload(
                                    id="upload-data",
                                    children=html.Div(
                                        ["Drag file (i.e. '...-Antworten.csv)"]
                                    ),
                                    style={
                                        "width": "100%",
                                        "height": "60px",
                                        "lineHeight": "60px",
                                        "borderWidth": "1px",
                                        "borderStyle": "dashed",
                                        "borderRadius": "5px",
                                        "textAlign": "center",
                                        "margin": "10px",
                                    },
                                    multiple=False,
                                ),
                                dbc.FormText("Wähle aus", color="secondary"),
                                dcc.Dropdown(
                                    id='data_picker',
                                    options=[{'label': i, 'value': i} for i in dataset_names],
                                    clearable=False
                                ),
                            ]
                        ),
                        dbc.FormGroup(
                            [
                                dbc.Label("Aufgabe", html_for="example-email"),
                                dbc.FormText("Aufgabenauswahl", color="secondary"),
                                dcc.Dropdown(
                                    id='exercise_picker',
                                    clearable=False,
                                    multi=False,
                                ),
                                dbc.FormText("Aufgaben, die zur Summe dazuzählen sollen", color="secondary"),
                                dcc.Dropdown(
                                    id='exercise_picker_sum',
                                    clearable=True,
                                    multi=True,
                                ),
                            ]
                        ),
                        dbc.FormGroup(
                        [
                                dbc.Label("Auswahl", html_for="example-email"),
                                dcc.Checklist(
                                    id = "options_picker",
                                    options=[
                                        {'label': 'Leere Abgaben verstecken', 'value': 'empty'},
                                        {'label': 'Vorlageähnlich verstecken', 'value': 'template'},
                                        {'label': 'Mit Musterlösung', 'value': 'solution'}
                                    ],
                                    value=['empty', 'template'],
                                    labelStyle = dict(display='block')
                                )
                            ]
                        ),
                        dbc.FormGroup(
                            [
                                dbc.Label("Studierendenvergleich", html_for="example-email"),
                                dbc.FormText("Student:in 1", color="secondary"),
                                dcc.Dropdown(
                                    id='student_1_picker',
                                    #options=[{'label': i, 'value': i} for i in data.names],
                                    #value=data.names[0],
                                    clearable=False,
                                    multi=False,
                                ),
                                dbc.FormText("Student:in 2", color="secondary"),
                                dcc.Dropdown(
                                    id='student_2_picker',
                                    #options=[{'label': i, 'value': i} for i in data.names],
                                    #value=data.names[0],
                                    clearable=False,
                                    multi=False,
                                ),
                            ]
                        ),


                    ],
                    className="h-100"),md=3, className="sidebar"),
                    dbc.Col(html.Div([

                        dbc.Row([
                            dbc.Col(html.H5('Ähnlichkeitswerte der Studierenden'), md=12, className="title_container")
                        ]),
                        dbc.Row([
                            dbc.Col(dt.DataTable(id='top10', columns=[{"name": i, "id": i} for i in ["Student:in 1", "Student:in 2", 'Ähnlichkeit']], page_size=10))
                        ]),
                        dbc.Row([
                            dbc.Col(html.H5('Ähnlichkeiten'), md=6, className="title_container"),
                            dbc.Col(html.H5('Graphisch'), md=6, className="title_container"),
                        ]),
                        dbc.Row([
                                dbc.Col(dcc.Graph(id='similarity'), md=6, className="graph_container"),
                                dbc.Col(dcc.Graph(id='mds'), md=6, className="graph_container"),
                        ]),
                        dbc.Row([
                            dbc.Col(html.H5('Dirketer Vergleich von 2 Student:innen'), md=12, className="title_container")
                        ]),
                        dbc.Row([
                            dbc.Col(html.H5('Ausgabe Student:in 1'), md=4, className="title_container"),
                            dbc.Col(html.H5('Ausgabe Student:in 2'), md=4, className="title_container"),
                            dbc.Col(html.H5('Ähnlichkeiten'), md=4, className="title_container"),
                        ]),
                        dbc.Row([
                               dbc.Col(html.Div(id='answer_1'), md=4, className="graph_container"),
                               dbc.Col(html.Div(id='answer_2'), md=4, className="graph_container"),
                               dbc.Col(dcc.Graph(id='student_comparision'), md=4, className="graph_container"),
                        ]),
                    ],
                    className="h-100"),md=9, className="content")
                ], className="h-100"
        ),


    ],
        id='page-content',
        className="h-100"
    )

], className="h-100")




@app.callback(
    [
        Output('data_picker', 'options'),
        Output('data_picker', 'value'),
    ],
    [
        Input('upload-data', 'filename'),
        Input("upload-data", "contents"),
    ])
def update_dropdown(uploaded_filename, uploaded_file_content):

    if uploaded_file_content != None:

        content_type, content_string = uploaded_file_content.split(',')
        decoded = base64.b64decode(content_string)

        try:
            if 'csv' in uploaded_filename:
                data = Data(io.StringIO(decoded.decode('utf-8')))

            loaded_datasets[uploaded_filename] = data

        except Exception as e:
            print(e)

        print("Update data")

    else:
        return [], None

    if uploaded_filename == None:
        return [], None
    return [{'label': i, 'value': i} for i in loaded_datasets.keys()], uploaded_filename


@app.callback(
    [
        Output('exercise_picker', 'options'),
        Output('exercise_picker', 'value'),
        Output('exercise_picker_sum', 'options'),
        Output('exercise_picker_sum', 'value'),

        Output('student_1_picker', 'options'),
        Output('student_1_picker', 'value'),
        Output('student_2_picker', 'options'),
        Output('student_2_picker', 'value'),
    ],
    [
        Input('data_picker', 'value'),
    ])
def update_dropdown(data_picker):

    print("Data Picker was updated.")

    if data_picker != None:
        print(f"Change dataset to {data_picker}")
        data = loaded_datasets[data_picker]
    else:
        print("return pass")
        return [], None, [], None, [], None, [], None

    return  [{'label': i, 'value': i} for i in data.col_names + [AGGREGATION]], AGGREGATION, [{'label': i, 'value': i} for i in data.col_names], data.col_names, [{'label': i, 'value': i} for i in data.names], data.names[0], [{'label': i, 'value': i} for i in data.names], data.names[1]




@app.callback(
    [
        Output('answer_1', 'children'),
        Output('answer_2', 'children'),
        Output('student_comparision', 'figure'),
    ],
    [
        Input('student_1_picker', 'value'),
        Input('student_2_picker', 'value'),
        Input('exercise_picker', 'value'),
        Input('data_picker', 'value'),
    ],)
def update_output(student1, student2, exercise_picker, data_picker):

    print("Update student comparision")

    if data_picker == None or exercise_picker == None:
        return "", "", {}

    data = loaded_datasets[data_picker]


    sims = [data.similarities[key].at[student1, student2] for key in data.similarities.keys()]
    print(data.similarities.keys(), sims)

    figure={
            'data': [
                {'x': list(data.similarities.keys()), 'y':sims, 'type': 'bar'},
            ],
            'layout': {
                'yaxis': {'range': [0.0, 1.0],}
            }
        }
    if exercise_picker == AGGREGATION:
        return "", "", figure

    answer1 = answer2 = ""
    if student1 != None:
        answer1 = data.submissions.at[student1, exercise_picker]
    if student2 != None:
        answer2 = data.submissions.at[student2, exercise_picker]


    return answer1, answer2, figure

@app.callback(
    [
        Output('similarity', 'figure'),
        Output('mds', 'figure'),
        Output('top10', 'data'),
    ],
    [
        Input('data_picker', 'value'),
        Input('exercise_picker', 'value'),
        Input('exercise_picker_sum', 'value'),
        Input('options_picker', 'value'),
        Input('student_1_picker', 'value'),
        Input('student_2_picker', 'value'),
    ],)
def update_figure(data_picker, exercise_picker, exercise_picker_sum, options_picker, student1, student2):

    print("Update similarities")
    print(data_picker, exercise_picker)

    if exercise_picker == None or data_picker == None:
        return {}, {}, []

    data = loaded_datasets[data_picker]

    if exercise_picker == AGGREGATION:


        if exercise_picker_sum == None:
            return {}, {}, []

        keys = exercise_picker_sum
        r = data.similarities[keys[0]] - data.similarities[keys[0]]
        for key in keys:
            r += data.similarities[key]
        r = r/len(keys)
    else:
        r = data.similarities[exercise_picker]


    try:
        print(r["Vorlage, Die"].sort_values())
    except:
        print("No template defined")

    if options_picker != [] and exercise_picker != AGGREGATION:

        indeces = data.names

        if "empty" in options_picker:

            indeces_empty = data.get_not_empty_indices(exercise_picker)
            indeces = list(set(indeces).intersection(set(indeces_empty)))

        if "template" in options_picker:
            try:
                indeces_non_teample = data.get_non_similar_to_template(exercise_picker)
                indeces = list(set(indeces).intersection(set(indeces_non_teample)))
            except:
                print("No template defined")


        r = r.loc[indeces, :]
        r = r[indeces]

        if r.empty:
            return {}, {}, []


    rdm_fig = px.imshow(r, height=300, color_continuous_scale=px.colors.sequential.Viridis)
    rdm_fig.update_layout(margin=GLOBAL_MARGIN)
    rdm_fig.update_xaxes(showticklabels=False)
    rdm_fig.update_yaxes(showticklabels=False)

    start = 0

    embedding = MDS(n_components=2)
    X_transformed = embedding.fit_transform(r)

    X_transformed = np.round(X_transformed, 2)


    df = pd.DataFrame(X_transformed,columns=['x','y'], index = r.index)

    df['text'] = df.index
    df['same'] = df.groupby(['x','y'])['text'].transform(lambda x: '<br>'.join(x))
    counted_X = df.groupby(['x','y','same']).count().reset_index()

    counted_X = counted_X.rename(columns={'text': 'size'})
    counted_X = counted_X.rename(columns={'same': 'text'})

    counted_X['color'] = 1
    counted_X['color'][counted_X['text'].str.contains(student1)] = 0
    counted_X['color'][counted_X['text'].str.contains(student2)] = 0
    counted_X['size'] = 5 + 3 * np.log(counted_X['size'])


    unq, count = np.unique(X_transformed, axis=0, return_counts=True)
    X_transformed = X_transformed + np.random.normal(0, 0.001, size = X_transformed.shape)




    mds_fig = go.Figure()
    mds_fig.add_trace(go.Scatter(x=counted_X['x'], y=counted_X['y'], mode='markers', text = counted_X['text'],
        marker = {"color": counted_X['color'], "size": counted_X['size'], "line": {"width": 2, "color": 'Black'} } ))#,
                                 # marker={"size": GLOBAL_MARKER_SIZE, "color": colors, "colorscale": 'Magma',
                                 #         "reversescale": True, "showscale": True,
                                 #         "line": {"width": 1, "color": 'black'}},
                                 # line={"width": 1, "color": 'black'}, name=f"{model}", text=text))

                                 #"color": 'rgba(135, 206, 250, 0.5)',


    mds_fig.update_layout(height=300, margin=GLOBAL_MARGIN, showlegend=False,
                          xaxis={"title": "MDS dim 12", "scaleanchor": "y", "scaleratio": 1},
                          yaxis={"title": "MDS dim 2"}, template=GLOBAL_TEMPLATE)


    upper = r.where(np.triu(np.ones(r.shape), 1).astype(np.bool))
    upper = upper.stack().reset_index()
    upper.columns = ['Student:in 1','Student:in 2','Ähnlichkeit']



    upper = upper.sort_values(by='Ähnlichkeit', ascending=False)

    return rdm_fig, mds_fig, upper.to_dict('records')





if __name__ == '__main__':
    app.run_server(debug=True)