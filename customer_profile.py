import plotly.express as px
import pandas as pd
import os
pd.options.plotting.backend = "plotly"
pd.set_option("display.max_rows", None,"display.max_columns", None)

CWD = os.getcwd()

def reader(path):

    x = pd.read_csv(path,delimiter=';')# x axis profile

    graph = pd.read_csv(path,delimiter=';')

    graph['actual profile']=graph['actual profile'].str.replace(r'\w+\$\s+', '').str.replace('.', '')\
                   .str.replace(',', '.').astype(float,errors='ignore')

    return x, graph

def figure(x,graph,n1,n2,first_name,save_path):
    '''n1,n2 is the window range
    first_name is df columns names, find it in advance'''

    fig=px.line(x=x['Datum'][n1:n2], y=graph[first_name][n1:n2])

    fig['data'][0]['name'] = first_name

    title = {'text': title_name,
             'y': 0.95,
             'x': 0.5,
             'xanchor': 'center',
             'yanchor': 'top'}
    fig.update_layout(
        xaxis_title="Time, days",
        yaxis_title="Energy, kWh",
        title=title,
        legend_title="Legend",
        legend=dict(
            x=0.85,
            y=0.7,
            traceorder="reversed",
            title_font_family="Times New Roman",
            font=dict(
                family="Courier",
                size=12,
                color="black"
            ),
            bgcolor="LightSteelBlue",
            bordercolor="Black",
            borderwidth=1
        )
    )
    fig.show()
    fig.write_html(save_path)

if __name__ == '__main__':

    n1=0
    n2=24*365*4 #*4 bcoz it is 15mins
    profile_name= "Profile"

    path = CWD+f'/{profile_name}.csv'
    save_path = CWD+f'/{profile_name}.html'
    first_name='actual profile'
    title_name = f"{profile_name} energy consumption profile"

    x,graph = reader(path)
    figure(x, graph, n1, n2, first_name, save_path)




