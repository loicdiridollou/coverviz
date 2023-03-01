import plotly.express as px
import pandas as pd
df = px.data.gapminder().query("year == 2007")

link_ref = '<a href="http://google.com" style="cursor: pointer" target="_blank" rel="noopener noreferrer">{}</a>'  # pylint: disable=E501
df['country'] = df['country'].apply(lambda item: link_ref.format(item, "{}"))

fig = px.treemap(df,
                 path=['continent', 'country'],
                 values='pop',
                 color='lifeExp',
                 hover_data=['iso_alpha'])

fig.show()

px.treemap(
    df,
    names="name",
    path=['module_1', 'module_2', 'module_3', 'module_4', 'module_5', 'module_6'],
    values="size",
    color="cov",
    color_continuous_scale="RdYlGn",
    range_color=[0, 1],
).write_html('codecov.html')


def process(res):
    tot = []
    for v in res:
        if v[0][-3:] != '.py':
            continue
        if v[1][1] == 0:
            continue

        dic = {'name': v[0][1:]}
        for i in range(1, len(v[0].split('/'))):
            dic[f'module_{i}'] = v[0].split('/')[i]
        dic['size'] = v[1][1]
        dic['cov'] = v[1][0]/(v[1][1] or 1)
        tot.append(dic)
    return pd.DataFrame(tot)
