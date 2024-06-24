import pandas as pd
import plotly.express as px

df_A = pd.read_excel("turma-A.xlsx")

notas_A = df_A[["Nota 1", "Nota 2", "Nota 3", "Nota 4"]]
#print(df_A.groupby("Nome")[["Nota 1", "Nota 2", "Nota 3", "Nota 4"]].sum())

df_A['Total Notas'] = df_A[['Nota 1', 'Nota 2', 'Nota 3', 'Nota 4']].sum(axis=1)
total_soma_notas = df_A.groupby('Nome')['Total Notas'].sum().reset_index()
#print(total_soma_notas)

df_A['Media de Notas'] = df_A[['Nota 1', 'Nota 2', 'Nota 3', 'Nota 4']].mean(axis=1)
media = df_A.groupby('Nome')['Media de Notas'].sum().reset_index().round(2)
#print(media)
#print(df_A)

menor_numero_faltas = df_A["Faltas"].min()
alunos_menor_numero_faltas = df_A[df_A['Faltas'] == menor_numero_faltas]['Nome']

maior_numero_faltas = df_A["Faltas"].max()
alunos_maior_numero_faltas = df_A[df_A['Faltas'] == maior_numero_faltas]['Nome']

def determinar_resultado(media):
    return 'aprovado' if media >= 6 else 'reprovado'
df_A['Resultado Final'] = df_A['Media de Notas'].apply(determinar_resultado)
#print(df_A[["Nome", "Media de Notas", "Resultado Final"]])
#print(df_A["Resultado Final"].describe())


print(f"""
{df_A.info()}
----------------------------
Dados da planilha 

----------------------------
Linhas e colunas

{df_A.shape}

-----------------------------
Dados das notas da turma A

{notas_A.describe()}

------------------------------
Alunos com maior taxa de faltas

{", ".join(alunos_maior_numero_faltas)}
faltas: {maior_numero_faltas}

Alunos com menor taxa de faltas

{", ".join(alunos_menor_numero_faltas)}
faltas: {menor_numero_faltas}

-------------------------------
Tabela com os dados tratados da turma A 

{df_A}
""")


