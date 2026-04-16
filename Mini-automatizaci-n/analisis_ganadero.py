import sys

from pathlib import Path

import pandas as pd

CSV_POR_DEFECTO = "datos_ganaderos_realistas_analisis_59172.csv"

COLUMNAS_OBLIGATORIAS = [
    "fecha_control",
    "animal_id",
    "finca_id",
    "departamento",
    "municipio",
    "raza",
    "edad_meses",
    "peso_kg",
    "estado_salud",
    "produccion_leche_l_dia",
    "costo_alimentacion_cop_dia",
    "alerta_principal",
]

def obtener_ruta_csv():

    if len(sys.argv) > 1:

        return Path(sys.argv[1])

    return Path(__file__).with_name(CSV_POR_DEFECTO)


def cargar_datos(ruta_csv):


    if not ruta_csv.exists():
  
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_csv}")

    df = pd.read_csv(ruta_csv)

    faltantes = [col for col in COLUMNAS_OBLIGATORIAS if col not in df.columns]

    if faltantes:

        raise ValueError("Faltan columnas obligatorias: " + ", ".join(faltantes))

    df["fecha_control"] = pd.to_datetime(df["fecha_control"], errors="coerce")

    df["edad_meses"] = pd.to_numeric(df["edad_meses"], errors="coerce")

    df["peso_kg"] = pd.to_numeric(df["peso_kg"], errors="coerce")

    df["produccion_leche_l_dia"] = pd.to_numeric(
        df["produccion_leche_l_dia"], errors="coerce"
    )

    df["costo_alimentacion_cop_dia"] = pd.to_numeric(
        df["costo_alimentacion_cop_dia"], errors="coerce"
    )

    return df

def detectar_alertas(df):

    return {
        "peso_bajo_menor_200kg": int((df["peso_kg"] < 200).sum()),

        "animales_en_observacion": int((df["estado_salud"] == "En observación").sum()),

        "alertas_distintas_de_sin_novedad": int(
            df["alerta_principal"]
            .fillna("Sin dato")
            .astype(str)
            .str.strip()
            .ne("Sin novedad")
            .sum()
        ),

        "registros_sin_peso": int(df["peso_kg"].isna().sum()),
    }

def guardar_salidas(df, carpeta_base):

    carpeta_salidas = carpeta_base / "salidas"


    carpeta_salidas.mkdir(exist_ok=True)

    resumen_numerico = df[
        ["edad_meses", "peso_kg", "produccion_leche_l_dia", "costo_alimentacion_cop_dia"]
    ].describe().round(2)

    resumen_numerico.to_csv(
        carpeta_salidas / "resumen_numerico.csv",
        encoding="utf-8-sig"
    )

    alertas = detectar_alertas(df)

    pd.DataFrame(
        [{"alerta": clave, "cantidad": valor} for clave, valor in alertas.items()]
    ).to_csv(
        carpeta_salidas / "resumen_alertas.csv",
        index=False,
        encoding="utf-8-sig"
    )

    reporte = f"""
REPORTE DE ANALISIS GANADERO
==================================================

Total de registros: {len(df):,}
Total de animales únicos: {df["animal_id"].nunique():,}
Total de fincas: {df["finca_id"].nunique():,}
Departamentos: {df["departamento"].nunique():,}
Municipios: {df["municipio"].nunique():,}

Rango de fechas:
- Desde: {df["fecha_control"].min().date()}
- Hasta: {df["fecha_control"].max().date()}

Indicadores principales:
- Peso promedio: {df["peso_kg"].mean():.2f} kg
- Peso máximo: {df["peso_kg"].max():.2f} kg
- Peso mínimo: {df["peso_kg"].min():.2f} kg
- Producción promedio de leche: {df["produccion_leche_l_dia"].mean():.2f} L/día
- Costo promedio de alimentación: {df["costo_alimentacion_cop_dia"].mean():.2f} COP/día

Alertas:
- Peso bajo menor a 200 kg: {alertas["peso_bajo_menor_200kg"]}
- Animales en observación: {alertas["animales_en_observacion"]}
- Alertas distintas de 'Sin novedad': {alertas["alertas_distintas_de_sin_novedad"]}
- Registros sin peso: {alertas["registros_sin_peso"]}
""".strip()


    (carpeta_salidas / "reporte_analisis_ganadero.txt").write_text(
        reporte,
        encoding="utf-8"
    )

def main():

    ruta_csv = obtener_ruta_csv()

    print(f"[INFO] Archivo de entrada: {ruta_csv}")

    df = cargar_datos(ruta_csv)

    print(f"[INFO] Registros cargados: {len(df):,}")

    guardar_salidas(df, ruta_csv.parent)

    print("[OK] Análisis finalizado correctamente.")

    print(f"[OK] Revisa la carpeta: {ruta_csv.parent / 'salidas'}")

if __name__ == "__main__":

    try:
        main()

    except Exception as e:

        print(f"[ERROR] {e}")