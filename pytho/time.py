from datetime import datetime
from dateutil import tz
import PySimpleGUI as sg
#import necesary modules

real_start = datetime(2021, 1, 1, 0, 0, 0, 0, tz.UTC)
ulina_start = datetime(2045, 1, 1, 0, 0, 0, 0, tz.UTC)
#variables for the beginning of ulina's 3 month time, both in real ulina time
time_format = "%c"
times = []
def format_time(time, ulina):
    if ulina != True:
        time = datetime.now(tz=tz.tzlocal())
        string = datetime.strftime(time, time_format) + ' ' + datetime.now(tz=tz.tzlocal()).tzname()
    else:
        string = datetime.strftime(time, time_format) + ' Ulina Central Time'

    return string
#variable and function for formatting time

def convert(time):
    if time != "":
        real_current = datetime(month= int(time[0] + time[1]), day= int(time[3] + time[4]), year= int('20' + time[6] + time[7]), tzinfo=tz.UTC)
        real_time_passed = (real_current - real_start)
        ulina_time_passed = (real_time_passed * 4)
        ulina_current = ulina_start + ulina_time_passed
        string = datetime.strftime(ulina_current, '%x')
        return string

def find_time():
    real_current = datetime.now(tz=tz.UTC)
    real_time_passed = (real_current - real_start)
    ulina_time_passed = (real_time_passed * 4)
    ulina_current = ulina_start + ulina_time_passed
    times = [format_time(ulina_current, True), format_time(real_current, False)]
    return times

layout = [
    [sg.Text('Real Time:', background_color='#284272'), sg.Text(find_time()[1], size=(40,1), key='-REAL-', background_color='#21365e')],
    [sg.Text('Ulina Time:', background_color='#284272'), sg.Text(find_time()[0], size=(40,1), key='-ULINA-', background_color='#21365e')],
    [sg.Text(' '*30, background_color='#284272')],
    [sg.In(key='-REALCAL-', enable_events=True, visible=False), sg.CalendarButton('Real Time Date:', format='%x', default_date_m_d_y=(datetime.now().month, datetime.now().day, datetime.now().year)), sg.Text('Enter Date', key='-REALDATE-', background_color='#21365e')],
    [sg.Button('Convert to Ulina Time:', key= 'Convert'), sg.Text((''), key='-REALCONVERT-', size=(7,1), background_color='#21365e')],
    [sg.Text(' '*30, background_color='#284272')],
    [sg.Button('Exit')],
    ]

sg.theme('DarkBlue 13')
window = sg.Window('Ulina Time', layout, finalize=True, size=(450,200), auto_size_buttons=True, auto_size_text=True, background_color='#284272', )

while True:
    event, values = window.read(timeout=10)
    
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    
    window['-ULINA-'].update(find_time()[0])
    window['-REAL-'].update(find_time()[1])
    
    if event == '-REALCAL-':
        window['-REALDATE-'].update(values['-REALCAL-'])
    if event == 'Convert':
        window['-REALCONVERT-'].update(convert(values['-REALCAL-']))

