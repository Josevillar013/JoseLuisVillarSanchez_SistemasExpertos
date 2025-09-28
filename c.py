from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Puntos clave (año, precio BTC en USD, comentario)
data_usd = [
    (2010, 0.08, "Primeros años"),
    (2011, 5.00, "Primeras subidas"),
    (2013, 1000.0, "Pico 2013"),
    (2015, 300.0, "Fondo entre ciclos"),
    (2017, 19000.0, "Pico burbuja 2017"),
    (2018, 3500.0, "Corrección 2018"),
    (2020, 10000.0, "Inicio rally 2020"),
    (2021, 69000.0, "Máximo 2021"),
    (2022, 17000.0, "Caída 2022"),
    (2024, 110000.0, "Post-halving 2024"),
    (2025, 115000.0, "2025 — referencia"),
]

# Tipos de cambio USD -> MXN aproximados por año
fx = {
    2010: 12.8, 2011: 12.3, 2013: 12.9, 2015: 15.8,
    2017: 18.9, 2018: 19.2, 2020: 21.0, 2021: 20.5,
    2022: 20.0, 2024: 19.5, 2025: 18.4
}

# Construir DataFrame con conversión a MXN
rows = []
for year, price_usd, note in data_usd:
    fx_rate = fx.get(year, 19.0)
    price_mxn = price_usd * fx_rate
    rows.append({
        "Year": datetime(year, 1, 1),
        "BTC_USD": price_usd,
        "FX_USD_MXN": fx_rate,
        "BTC_MXN": price_mxn,
        "Note": note
    })

df = pd.DataFrame(rows)

# Mostrar tabla en consola
print(df)

# Guardar CSV
df.to_csv("btc_mxn_estimated_keypoints.csv", index=False)

# Graficar
plt.figure(figsize=(10,5))
plt.plot(df["Year"], df["BTC_MXN"], marker='o')
plt.yscale('log')  # escala log para ver bien los saltos
plt.title("Evolución estimada del precio de Bitcoin en MXN (puntos clave)")
plt.xlabel("Año")
plt.ylabel("Precio por 1 BTC (MXN, escala log)")
for i, r in df.iterrows():
    plt.annotate(
        f"{r['Year'].year}: {int(r['BTC_MXN']):,}",
        (r["Year"], r["BTC_MXN"]),
        textcoords="offset points",
        xytext=(0,8),
        ha='center',
        fontsize=8
    )
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.tight_layout()
plt.savefig("btc_mxn_estimated_keypoints.png", dpi=150)
plt.show()
