from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Загружаем набор данных gapminder
df = px.data.gapminder()

# Получаем уникальные названия стран, отсортированные по алфавиту
countries = df['country'].drop_duplicates().sort_values()

# Инициализация Dash-приложения
app = Dash(__name__)
server = app.server 

# Layout приложения
app.layout = html.Div([
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": country, "value": country} for country in countries],
        value="Canada"  # начальное значение по заданию
    ),
    dcc.Graph(id="gdp-growth")
])

# Callback для обновления графика при выборе страны
@app.callback(
    Output("gdp-growth", "figure"),
    Input("country-dropdown", "value")
)
def update_graph(selected_country):
    # Фильтруем по выбранной стране
    filtered_df = df[df["country"] == selected_country]
    # Строим график
    fig = px.line(
        filtered_df,
        x="year",
        y="gdpPercap",
        title=f"GDP Per Capita Over Time for {selected_country}"
    )
    return fig

# Запуск приложения
if __name__ == "__main__": 
    app.run(debug=True)