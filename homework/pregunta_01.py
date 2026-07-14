# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


def pregunta_01():
        """
        El archivo `files//shipping-data.csv` contiene información sobre los envios
        de productos de una empresa. Cree un dashboard estático en HTML que
        permita visualizar los siguientes campos:

        * `Warehouse_block`

        * `Mode_of_Shipment`

        * `Customer_rating`

        * `Weight_in_gms`

        El dashboard generado debe ser similar a este:

        https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

        Para ello, siga las instrucciones dadas en el siguiente video:

        https://youtu.be/AgbWALiAGVo

        Tenga en cuenta los siguientes cambios respecto al video:

        * El archivo de datos se encuentra en la carpeta `data`.

        * Todos los archivos debe ser creados en la carpeta `docs`.

        * Su código debe crear la carpeta `docs` si no existe.

        """

        import os
        import pandas as pd
        import matplotlib.pyplot as plt

        # Rutas
        data_path = os.path.join("files", "input", "shipping-data.csv")
        out_dir = "docs"

        # Crear carpeta docs si no existe
        os.makedirs(out_dir, exist_ok=True)

        # Leer datos
        df = pd.read_csv(data_path)

        # 1) Envios por Warehouse_block
        counts_warehouse = df["Warehouse_block"].value_counts()
        plt.figure(figsize=(6, 4))
        counts_warehouse.plot(kind="bar", color="#4C72B0")
        plt.title("Shipments per Warehouse block")
        plt.xlabel("Warehouse_block")
        plt.ylabel("Number of shipments")
        plt.tight_layout()
        plt.savefig(os.path.join(out_dir, "shipping_per_warehouse.png"))
        plt.close()

        # 2) Mode of Shipment
        counts_mode = df["Mode_of_Shipment"].value_counts()
        plt.figure(figsize=(6, 4))
        counts_mode.plot(kind="bar", color="#55A868")
        plt.title("Mode of Shipment")
        plt.xlabel("Mode_of_Shipment")
        plt.ylabel("Number of shipments")
        plt.tight_layout()
        plt.savefig(os.path.join(out_dir, "mode_of_shipment.png"))
        plt.close()

        # 3) Average Customer Rating per Warehouse_block
        avg_rating = df.groupby("Warehouse_block")["Customer_rating"].mean()
        plt.figure(figsize=(6, 4))
        avg_rating.plot(kind="bar", color="#C44E52")
        plt.title("Average Customer Rating by Warehouse block")
        plt.xlabel("Warehouse_block")
        plt.ylabel("Average Customer Rating")
        plt.ylim(0, 5)
        plt.tight_layout()
        plt.savefig(os.path.join(out_dir, "average_customer_rating.png"))
        plt.close()

        # 4) Weight distribution
        plt.figure(figsize=(6, 4))
        df["Weight_in_gms"].plot(kind="hist", bins=30, color="#8172B2")
        plt.title("Weight Distribution (gms)")
        plt.xlabel("Weight_in_gms")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.savefig(os.path.join(out_dir, "weight_distribution.png"))
        plt.close()

        # Crear un index.html simple que muestre las imágenes
        html = """
        <!doctype html>
        <html lang="es">
        <head>
            <meta charset="utf-8">
            <title>Shipping Dashboard</title>
            <style>body{font-family:Arial,Helvetica,sans-serif;} .grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;} img{width:100%;height:auto;border:1px solid #ddd;padding:4px;background:#fff}</style>
        </head>
        <body>
            <h1>Shipping Dashboard</h1>
            <div class="grid">
                <div><h3>Shipments per Warehouse</h3><img src="shipping_per_warehouse.png" alt="shipping_per_warehouse"></div>
                <div><h3>Mode of Shipment</h3><img src="mode_of_shipment.png" alt="mode_of_shipment"></div>
                <div><h3>Average Customer Rating</h3><img src="average_customer_rating.png" alt="average_customer_rating"></div>
                <div><h3>Weight Distribution</h3><img src="weight_distribution.png" alt="weight_distribution"></div>
            </div>
        </body>
        </html>
        """

        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as fh:
                fh.write(html)

        return None