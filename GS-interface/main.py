'''
Experiment with css grid layout with dash using python3 
'''
'''
    TODO 
    - Add all the main tabs
    - Identify the sub-tabs to be shown
    - Implement all the sub-tabs
    - Add documentation
    - Refresh button
    - Time selection
    - Link-up to the main server
    - the parmeters might not be sorted in time. Check This!
'''

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go

import time
import datetime


#custom display modules


from gsclasses import Eps
from gsclasses import Obc
from gsclasses import Ax100
from gsclasses import Adcs 


#import Eps
#from DisplayEPS import *

from contextTabs import *
from contextInfoGen import eps_context_info
from contextFigGen import gen_context_fig



app = dash.Dash(__name__)

eps = Eps.EPS()
obc = Obc.OBC()
ax100 = Ax100.AX100()
adcs = Adcs.ADCS()


'''
#reloads data from the main Mongodb
eps.reload()
obc.reload()
ax100.reload()
adcs.reload()
'''


#loads random test data
eps.test_load()
obc.test_load()
ax100.test_load()
adcs.test_load()

def table_elem (field,val,unit=''):
    return html.Tr([
        html.Td([
            str(field)
        ]),
        html.Td([
            str(val) +' '+ str(unit)
        ])
    ])



#TODO the parmeters might not be sorted in time. Check This!
def gen_main_info(eps,obc,ax100,adcs):
    #return "main info"
    return html.Div( children=[ 
        html.H3("power_input"),
        html.Table([
            table_elem ("CH1(11.7V):", eps.params["Cin_0"].Vals[-1], "mA"),
            table_elem ("CH2(11.7V):", eps.params["Cin_1"].Vals[-1], "mA"),
            table_elem ("CH3(3.3V):",  eps.params["Cin_2"].Vals[-1], "mA"),
            
        ]),
        html.H3("power_output"),
        html.Table([
            table_elem ("OBC(3.3V):", eps.params["C_obc"].Vals[-1], "mA"),
            table_elem ("AX100(3.3V):", eps.params["C_radio"].Vals[-1], "mA"),
            table_elem ("V_payload(5V):", eps.params["C_payload"].Vals[-1], "mA"),
           
            table_elem ("Battery mode:", eps.params["battmode"].Vals[-1], "mA"),
        ]),
        html.Hr(),
        html.Table([
            table_elem ("Battery mode:", eps.params["battmode"].Vals[-1]),
            table_elem ("Battery voltage:", eps.params["vbatt"].Vals[-1]/1000, "V"),
            table_elem ("EPS ground watchdog:", eps.params["wdt_GND"].Vals[-1]),
            table_elem ("EPS Boot count:", eps.params["boot_cnt"].Vals[-1]),
        ]),
        html.Hr(),
        html.Table([
            table_elem ("OBC temp A:", obc.params["temp_a"].Vals[-1]),
            table_elem ("OBC Boot count:", obc.params["boot_count"].Vals[-1]/1000, "V"),
        ])
    ])


app.layout = html.Div([
    html.H1("SpooQy-1 Ground Station"),
    html.P("Hit refresh to reload"),
    
    html.Div(
        className="grid-container",
        children=[
            html.Div(
                className="mainheader",
                children=[
                    dcc.Tabs(id="main-tabs", value='main-eps', children=[
        
                        dcc.Tab(label='EPS', value='main-eps'),
                        dcc.Tab(label='OBC', value='main-obc'),
                        dcc.Tab(label='AX100', value='main-ax100'),
                        dcc.Tab(label='ADCS', value='main-adcs'),
    
                    ]),
                ]
                
            ),
            html.Div(
                className="info",
                children= gen_main_info(eps,obc,ax100,adcs) #"info"
            ),
            html.Div(
                className="subheader",
                id="context-sub-tabs",
                children=[
                    dcc.Tabs(id="context-tabs",),
                ]
            ),
            html.Div(
                className="contextinfo",
                id="tab-context-info"
            ),
            html.Div(
                className="figure",
                id="tab-context-plot"

            )

        ]
    ),


])





@app.callback(Output('context-tabs', 'value'),
              [Input("main-tabs", 'value')])
def select_default_context_tab(main_tab):
    if main_tab == "main-eps": return 'eps-vbatt'
    elif main_tab == "main-obc": return 'obc-temp_a'
    elif main_tab == "main-ax100": return 'ax-val1'

@app.callback(Output('context-tabs', 'children'),
              [Input("main-tabs", 'value')])
def render_context_tabs(main_tab):
    return genContextTabs(main_tab)



@app.callback(Output('tab-context-info', 'children'),
              [Input("context-tabs", 'value'),Input("main-tabs", 'value')])
def render_context_info(tab,main_tab):
    #return eps_context_info(eps,tab,main_tabs)
    return main_tab
    

@app.callback(Output('tab-context-plot', 'children'),
              [Input("context-tabs", 'value'),Input("main-tabs", 'value')])
def render_context_plot(tab,main_tab):
    if main_tab == 'main-eps': return gen_context_fig(eps, tab[4:])
    elif main_tab == 'main-obc':return gen_context_fig(obc,tab[4:])
    elif main_tab == 'main-ax100': return gen_context_fig(ax100,tab[4:])
    elif main_tab == 'main-adcs': return gen_context_fig(adcs,tab[4:])
            



if __name__ == '__main__':
    app.run_server(debug=True)
