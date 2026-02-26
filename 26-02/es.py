import pandas as pd
import numpy as np

np.random.seed(42)  
dati = {
    'temperature': np.random.uniform(15, 30, 30)
}
df = pd.DataFrame(dati)


temp_max = df['temperature'].max()
temp_min = df['temperature'].min()
temp_media = df['temperature'].mean()
temp_mediana = df['temperature'].median()


print("--- Statistiche Temperature Mensili ---")
print(f"Temperatura Massima: {temp_max:.2f} °C")
print(f"Temperatura Minima:  {temp_min:.2f} °C")
print(f"Temperatura Media:   {temp_media:.2f} °C")
print(f"Mediana:             {temp_mediana:.2f} °C")



import matplotlib.pyplot as plt

df['temperature'].plot(kind='line', marker='o', color='orange')
plt.title('Andamento Temperature del Mese')
plt.xlabel('Giorno')
plt.ylabel('Gradi Celsius (°C)')
plt.grid(True)
plt.show()






plt.figure(figsize=(10, 5))
plt.hist(df['temperature'], bins=8, color='skyblue', edgecolor='black')

plt.axvline(temp_media, color='red', linestyle='dashed', linewidth=2, label=f'Media: {temp_media:.2f}°C')

plt.title('Distribuzione delle Temperature')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Frequenza (Giorni)')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.show()