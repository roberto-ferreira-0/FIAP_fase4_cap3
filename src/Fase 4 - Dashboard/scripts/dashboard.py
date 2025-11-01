import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# === 1. Carrega os dados ===
try:
    df = pd.read_csv("dados_esp32.csv", parse_dates=["data"])
except FileNotFoundError:
    st.error("Arquivo 'dados_esp32.csv' não encontrado. Verifique se o arquivo está na mesma pasta do script.")
    st.stop()

# === 1.1 Remove possíveis duplicatas para o modelo, mantendo o mais recente ===
df_model = df.drop_duplicates(subset=["data"], keep='last').copy()

# === 2. Título ===
st.title("🌾 Dashboard FarmTech - ESP32 Monitoramento")

# === 3. Exibe últimos dados ===
st.subheader("📋 Últimos dados recebidos")
st.dataframe(df.tail(10))

# === 4. Gráfico da temperatura ===
st.subheader("🌡️ Temperatura ao longo do tempo")
fig1, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df["data"], df["temperatura"], color='red', marker='o')
ax1.set_xlabel("Data")
ax1.set_ylabel("Temperatura (°C)")
ax1.tick_params(axis='x', rotation=45)
st.pyplot(fig1)

# === 5. Gráfico da umidade ===
st.subheader("💧 Umidade ao longo do tempo")
fig2, ax2 = plt.subplots(figsize=(10, 4))
ax2.plot(df["data"], df["umidade"], color='blue', marker='o')
ax2.set_xlabel("Data")
ax2.set_ylabel("Umidade (%)")
ax2.tick_params(axis='x', rotation=45)
st.pyplot(fig2)

# === 6. Modelo preditivo ===
st.subheader("🔮 Previsão de Umidade com base na Temperatura")

# Verifica se há dados suficientes
if len(df_model) < 5:
    st.warning("Poucos dados para treinamento do modelo. Adicione mais registros.")
    st.stop()

X = df_model[["temperatura"]]
y = df_model["umidade"]

# Divide dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Treina modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Avaliação do modelo
y_pred = modelo.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
st.write(f"📉 Erro médio quadrático (MSE): {mse:.2f}")

# === 7. Simulação interativa ===
st.subheader("📈 Simulação: prever umidade com nova temperatura")
temp_input = st.slider(
    "Temperatura atual (°C)",
    float(df["temperatura"].min()),
    float(df["temperatura"].max()),
    float(df["temperatura"].mean()),
)
entrada = pd.DataFrame([[temp_input]], columns=["temperatura"])
pred = modelo.predict(entrada)[0]
st.success(f"🔍 Previsão de Umidade: {pred:.2f} %")
