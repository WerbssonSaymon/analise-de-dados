import pandas as pd
import plotly.express as px

df_B = pd.read_excel("turma-B.xlsx")

notas_B = df_B[["Nota 1", "Nota 2", "Nota 3", "Nota 4"]]
#print(df_B.groupby("Nome")[["Nota 1", "Nota 2", "Nota 3", "Nota 4"]].sum())

df_B['Total Notas'] = df_B[['Nota 1', 'Nota 2', 'Nota 3', 'Nota 4']].sum(axis=1)
total_soma_notas = df_B.groupby('Nome')['Total Notas'].sum().reset_index()
#print(total_soma_notas)

df_B['Media de Notas'] = df_B[['Nota 1', 'Nota 2', 'Nota 3', 'Nota 4']].mean(axis=1)
media = df_B.groupby('Nome')['Media de Notas'].sum().reset_index().round(2)
#print(media)
#print(df_B)

menor_numero_faltas = df_B["Faltas"].min()
alunos_menor_numero_faltas = df_B[df_B['Faltas'] == menor_numero_faltas]['Nome']

maior_numero_faltas = df_B["Faltas"].max()
alunos_maior_numero_faltas = df_B[df_B['Faltas'] == maior_numero_faltas]['Nome']

def determinar_resultado(media):
    return 'aprovado' if media >= 6 else 'reprovado'
df_B['Resultado Final'] = df_B['Media de Notas'].apply(determinar_resultado)
#print(df_B[["Nome", "Media de Notas", "Resultado Final"]])
#print(df_B["Resultado Final"].describe())


print(f"""
{df_B.info()}
----------------------------
Dados da planilha 

----------------------------
Linhas e colunas

{df_B.shape}

-----------------------------
Dados das notas da turma A

{notas_B.describe()}

------------------------------
Alunos com maior taxa de faltas

{", ".join(alunos_maior_numero_faltas)}
faltas: {maior_numero_faltas}

Alunos com menor taxa de faltas

{", ".join(alunos_menor_numero_faltas)}
faltas: {menor_numero_faltas}

-------------------------------
Tabela com os dados tratados da turma A 

{df_B}
""")


