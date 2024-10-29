# %% [markdown]
# ## Notebook de desarrollo API juegps olimpicos
# ---
# -importando librerias

# %%
import pandas as pd
import numpy as np
from fastapi import FastAPI

# %% [markdown]
# -Instanciando fastapi

# %%
app=FastAPI()

# %% [markdown]
# -Cargar Datasets

# %%
df=pd.read_parquet('Data/Dataset.parquet')

# %% [markdown]
# -Funciones

# %%
@app.get('/')
def index():
    return{"API":"Online"}

# %% [markdown]
# Funcion Medals

# %%
@app.get("/medals")
def medals():
    medal= df['Medal'].value_counts()
    dic = {}
    for i in range(len(medal)):
        dic[medal.index[i]] = int(medal.values[i])
    return dic

# %%
medals()

# %% [markdown]
# Funcion Medals_country(pais)

# %%
@app.get("/medal_country/{Pais}")
def medal_country(Pais:str):
    filtro = df[df['Team']==Pais]
    medallas = filtro['Medal'].value_counts()
    dic={}
    if filtro.empty:
        return{'Error':f"El pais {Pais} no existe o esta mal escrito"}
    for i in range(len(medallas)):
        dic[medallas.index[i]]=int(medallas.values[i])
    return dic

# %%
medal_country('México')

# %% [markdown]
# Funcion Medals_year(año)

# %%
@app.get("/medal_year/{year}")
def medal_year(year:int):
    filtro = df[df['Year']==year]
    medallas = filtro['Medal'].value_counts()
    dic={}
    if filtro.empty:
        return{'Error':f'No hubo juegos olimpicos en el año {year}'}
    for i in range(len(medallas)):
        dic[medallas.index[i]]=int(medallas.values[i])
    return dic

# %%
medal_year(2001)

# %% [markdown]
# funcion athletes(nombres)

# %%
@app.get("/Atletas/{nombre}")
def Atletas(nombre: str):
    filtro = df[df["Name"] == nombre]
    dic={}
    if filtro.empty:
        return{'Error':'Revise los datos ingresados'}
    dic['Name']=nombre
    dic['Sexo']=filtro['Sex'].values[0]
    dic['Edad']=list(filtro['Age'].value_counts().index)
    dic['Pais']=list(filtro['Team'].value_counts().index)
    dic['Juegos']=list(filtro['Games'].value_counts().index)
    dic['Evento']=list(filtro['Event'].value_counts().index)
    Medallas={}
    for i in range(len(filtro['Medal'].value_counts())):
        Medallas[filtro['Medal'].value_counts().index[i]]=int(filtro['Medal'].value_counts().values[i])
        dic['Medallas']=Medallas
        return dic


# %%
Atletas("Heikki Ilmari Savolainen")


