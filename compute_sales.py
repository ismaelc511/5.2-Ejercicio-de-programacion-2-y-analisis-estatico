"""
Módulo para calcular el costo total de las ventas
"""
import json
import time


def compute_sales(price_catalogue_file: str, sales_record_file: str) -> float:
    """
    Calcula el costo total de las ventas
    """

    with open(price_catalogue_file, 'r', encoding='utf-8') as f:
        price_catalogue = json.load(f)

    with open(sales_record_file, 'r', encoding='utf-8') as f:
        sales_records = json.load(f)

    total_cost = 0.0

    for sale in sales_records:
        for product_sale in price_catalogue:
            if product_sale['title'] == sale['Product']:
                total_cost += product_sale['price'] * sale['Quantity']

    return total_cost


def main():
    """
    Función principal que solicita archivos de entrada y muestra resultados.
    """
    start_time = time.time()
    price_catalogue_file = input("Enter the price catalogue file: ")
    sales_record_file = input("Enter the sales record file: ")

    try:
        result = compute_sales(price_catalogue_file, sales_record_file)
        print(f"Total Cost: ${result:.2f}")
    except FileNotFoundError as e:
        print(f"File not found error: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time Elapsed: {elapsed_time:.6f} seconds")


if __name__ == "__main__":
    main()
