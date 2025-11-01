#dashboard_main.py

import math as mt
import os
import csv
import sys
import shutil
import streamlit as st
import serial
import yaml
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import tensorflow as tf
import torch
import cv2
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.schema import FetchedValue
from google.colab import drive
from IPython.display import Image, display
from PIL import Image
#from models.models import SensorMPX
#from models.models import Base, SensorMPX, UnidadeMedida, AreaCapturada
from datetime import datetime


#Entrada Central

try:
    from config import database
    # Adicione aqui outros módulos de configuração, como o de credenciais AWS
except ImportError:
    st.error("Erro: Não foi possível importar os módulos de configuração. Verifique a pasta 'config'.")
    sys.exit()

#Função principal da Dashboard
def main():
    st.set_page_config(
        page_title="Sistema de Gestão Agronegócio - Fase 7",
        layout="wide"
    )

    st.title("🚜 Consolidação - Sistema de Gestão Agronegócio")

    # Verifica a conexão com o banco de dados logo no início
    if database.check_connection():
        st.sidebar.success("✅ Conexão DB (Fase 2) OK!")
    else:
        st.sidebar.error("❌ Erro de Conexão com o Banco de Dados (Fase 2)!")

#Abas de navegação entre os modulos
tab_home, tab_f1, tab_f3, tab_f6, tab_alerta = st.tabs([
    "🏠 Visão Geral", 
    "📈 Insumos e Met. (F1)", 
    "💧 IoT e Irrigação (F3)", 
    "👁️ Visão Comp. (F6)",
    "☁️ Serviço de Alerta AWS (F7)"
])

with tab_home:
    st.header("Status Geral do Sistema")
    st.write("Bem-vindo ao sistema consolidado. Utilize as abas acima para acessar as funcionalidades.")
    # Exibe um resumo dos dados do DB (Fase 2)

with tab_f1:
    st.header("Análise de Insumos e Dados Meteorológicos (Fase 1)")
    # Implementação no Passo 3.1
    
with tab_f3:
    st.header("Controle de Sensores e Irrigação (Fase 3)")
    # Implementação no Passo 3.2

with tab_f6:
    st.header("Monitoramento Visual (Visão Computacional - Fase 6)")
    # Implementação no Passo 3.3

with tab_alerta:
    st.header("Configuração e Teste de Alerta AWS/SNS")
    # Implementação no Passo 3.4