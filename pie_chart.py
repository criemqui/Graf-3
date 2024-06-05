import pandas as pd
import plotly.express as px

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

# Reemplazar 'Sí' por 'Aprobados' y 'No' por 'No Aprobados'
df['aprobado'] = df['aprobado'].replace({'Sí': 'Aprobados', 'No': 'No Aprobados'})

# Contar la cantidad de aprobados y no aprobados
aprobado_counts = df['aprobado'].value_counts()

# Crear el pie chart con Plotly
fig = px.pie(aprobado_counts, values=aprobado_counts, names=aprobado_counts.index, 
             title='Gráfico de tortas',
             labels={'index': 'Estado', 'value': 'Cantidad'},
             template='plotly_white')

# Mostrar el gráfico
fig.show()
