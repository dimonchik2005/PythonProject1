from src.file_readers import (
    read_transactions_from_csv,
    read_transactions_from_excel,
)

csv_data = read_transactions_from_csv("data/transactions.csv")
excel_data = read_transactions_from_excel("data/transactions_excel.xlsx")

print(csv_data[:2])
print(excel_data[:2])
