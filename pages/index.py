import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smaller size screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

introduction = dbc.Row(
    [
        dcc.Markdown(
            """
            
            ### Introduction

            This blog post intents to explore crime data in Chicago and showcase the implementation of a predictive model for arrests in Chicago. This could help the public institutions in 3 main ways:
            
            1.	Better create public policy for correctional agencies

            2.	Help focus the countermeasures on negatively impacted crime categories according to the prediction

            3.	Guide the resource allocation by crime categories

            """
        ),

    ],
)
problem = dbc.Row(
    [
        dcc.Markdown(
            """
            
            ### Understanding Crime in Chicago


            Chicago, the nation’s third-biggest city, accounted for 22% of the nationwide increase with 749 murders (see right chart below) in 2016,
             more than the number of murders in the largest city, New York (334), and the second-largest, Los Angeles (294) for the same year, combined. 
             The estimated number of homicides in Chicago increased by 52% in 2016. 

             The number of homicides rose by 8.6% in the United States[1](https://ucr.fbi.gov/crime-in-the-u.s/2016/crime-in-the-u.s.-2016/topic-pages/murder), making Chicago an outlier, 
             and an interesting case to analyze. The vast majority of these killings happened in five mostly black and 
             Latino neighborhoods on the south and west side where only 9% of the 2.7m city lives[2](https://www.economist.com/democracy-in-america/2017/09/26/chicago-accounted-for-22-of-a-nationwide-increase-in-murders-last-year)
            

            
            [Documentation and NoteBook here](https://github.com/johanaluna/Chicago)
            """
        ),

    ],
)
graphs = dbc.Row([
    dbc.Col(
        html.Img(src='/assets/crimes_evo.png',style={'width':'100%','height':'100%'}
        )),
     dbc.Col(
        html.Img(src='/assets/homis_evo.png',style={'width':'100%','height':'100%'}
        ))
    ],
)

empty_rows= dbc.Row([
    dbc.Col(
        html.Div(' ',style={'text-align': 'center','font-size':16,'font-weight':'bold','height':'36px'})
    )
])
column_list=[introduction, empty_rows,problem,graphs]

layout = dbc.Col(column_list)