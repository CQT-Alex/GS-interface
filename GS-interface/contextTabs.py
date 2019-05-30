#from gsclasses import Eps
#from gsclasses import Param
#import Eps
#import Param

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go

import time
import datetime

def genContextTabs(main_tab):
    if main_tab == "main-eps": 
        return [
            dcc.Tab(label='vbatt', value='eps-vbatt'),
            dcc.Tab(label='temp_0', value='eps-temp_0'),
            dcc.Tab(label='temp_1', value='eps-temp_1'),
            dcc.Tab(label='temp_2', value='eps-temp_2'),
            dcc.Tab(label='temp_3', value='eps-temp_3'),
            dcc.Tab(label='temp_4', value='eps-temp_4'),
            dcc.Tab(label='temp_5', value='eps-temp_5'), #C_payload
        
            #Solar power input
            dcc.Tab(label='Vin_0', value='eps-Vin_0'),#Vin_0
            dcc.Tab(label='Vin_1', value='eps-Vin_1'),#Vin_1
            dcc.Tab(label='Vin_2', value='eps-Vin_2'),#Vin_2
            dcc.Tab(label='Cin_0', value='eps-Cin_0'),#Cin_0
            dcc.Tab(label='Cin_1', value='eps-Cin_1'),#Cin_1
            dcc.Tab(label='Cin_2', value='eps-Cin_2'),#Cin_2

            # Power output 

            dcc.Tab(label='V_obc', value='eps-V_obc'),#V_obc
            dcc.Tab(label='V_radio', value='eps-V_radio'),#V_radio
            dcc.Tab(label='V_payload', value='eps-V_payload'),#V_payload
            dcc.Tab(label='c-obc', value='eps-C_obc'),
            dcc.Tab(label='c-radio', value='eps-C_radio'), #temp_0
            dcc.Tab(label='C_payload', value='eps-C_payload'),
            dcc.Tab(label='battmode', value='eps-battmode'), #V_battmode 

            # Watchdog Timer and boot causes
            dcc.Tab(label='wdt_i2c', value='eps-wdt_i2c'),#wdt_i2c
            dcc.Tab(label='wdt_GND', value='eps-wdt_GND'),#wdt_GND
            dcc.Tab(label='boot_cnt', value='eps-boot_cnt'),#boot_cnt
            dcc.Tab(label='cntWdtI2c', value='eps-cntWdtI2c'),#cntWdtI2c
            dcc.Tab(label='cntwdtGND', value='eps-cntwdtGND'),#cntwdt
            dcc.Tab(label='cntWdtCsp_0', value='eps-cntWdtCsp_0'),#cntWdtCsp_0
            dcc.Tab(label='cntWdtCsp_1', value='eps-cntWdtCsp_1'),#cntWdtCsp_1
            dcc.Tab(label='bootCause', value='eps-bootCause'),#bootCause
 
            

        ]
    elif main_tab == "main-obc":
        return [
            dcc.Tab(label='temp_a', value='obc-temp_a'),
            dcc.Tab(label='oval2', value='obc-oval2'),
        ]
    elif main_tab == "main-ax100":
        return [
            dcc.Tab(label='ax1', value='ax1-val1'),
            dcc.Tab(label='ax2', value='ax1-val2'),
        ]
    elif main_tab == "main-ADCS":
        return [
            dcc.Tab(label='val1', value='adc-val1'),
            dcc.Tab(label='val1', value='adc-val1'),
        ]
