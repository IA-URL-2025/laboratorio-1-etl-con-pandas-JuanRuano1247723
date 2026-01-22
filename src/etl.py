from pathlib import Path
import pandas as pd

def run_etl():
    """
    Implementa el proceso ETL.
    No cambies el nombre de esta función.
    """
    # TODO: implementar
    base_dir = Path(__file__).resolve().parent.parent
    input_file = base_dir / "data" / "citas_clinica.csv"
    output_file = base_dir / "data" / "output.csv"


    df = pd.read_csv(input_file)
    print(df)
    df["paciente"] = df["paciente"].str.title()
    df["especialidad"] = df["especialidad"].str.upper()
    df["fecha_cita"] = pd.to_datetime(df["fecha_cita"], errors="coerce")
    df = df[df["fecha_cita"].notna()]
    df = df[df["estado"] == "CONFIRMADA"]
    df = df[df["costo"] > 0]
    df["telefono"] = df["telefono"].fillna("NO REGISTRA")

    df.to_csv(output_file, index=False)

    pass


if __name__ == "__main__":
    run_etl()
