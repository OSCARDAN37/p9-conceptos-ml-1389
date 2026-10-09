# Oscar Flores NC = 1389
import  pandas as pd

# 1. Crear un dataset de ejemplo simular a un CSV
# 22.
datos22 = {
    'distancia_km': [5.1, 2.9, 4.0, 1.4, 6.3],
    'trafico_nivel': [3, 2, 1, 3, 2],
    'edad_repartidor': [40, 27, 33, 22, 45],
    'tiempo_entrega_min': [48, 24, 28, 14, 58]
}

df = pd.DataFrame(datos22)

# 2. Separar Variables de Entrada (X) y Variable Objetivo (y)
X = df[['distancia_km', 'trafico_nivel', 'edad_repartidor']] # Features / Entradas
y = df['tiempo_entrega_min']                                  # Target / Salida

# 3. Mostrar estructura
print("--- DATOS DE ENTRADA  ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO ---")
print(y.head(2))
print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
print("Programa realizado por Oscar Flores NC = 1389")