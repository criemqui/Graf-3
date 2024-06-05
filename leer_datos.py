import pandas as pd
import plotly.graph_objects as go

# Crear un DataFrame con los datos proporcionados
data = {
    'd': list(range(1, 21)),
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 
                'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 
                'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 
                'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'],
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 
                 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

df = pd.DataFrame(data)

# Crear un boxplot con barras de error de diferente color usando Plotly Graph Objects
fig = go.Figure()

# Definir los colores para cada materia
colors = {
    'Matemáticas': 'rgb(31, 119, 180)',
    'Historia': 'rgb(214, 39, 40)',
    'Ciencias': 'rgb(0, 255, 255)',
    'Lenguaje': 'rgb(148, 0, 211)'
}

# Agregar los boxplots por cada materia
for materia in df['materia'].unique():
    fig.add_trace(go.Box(
        y=df[df['materia'] == materia]['nota'],
        name=materia,
        boxmean=True,
        marker_color=colors[materia]
    ))

# Ajustar los ejes y agregar el título
fig.update_layout(
    title='Gráfico de cajas',
    yaxis_title='Nota',
    template='plotly_white'
)

# Mostrar el gráfico
fig.show()
