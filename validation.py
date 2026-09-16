import os, csv, pandas as pd
from datetime import datetime as dt

def file_existence(file_path):
    file_exists = os.path.exists(file_path)
    if not file_exists:
        print(f"\n{file_path} doesnot exists")
        return False
    return True

def add_csv_header(file_path, fields):
    file_exists = file_existence(file_path)
    with open (file_path, mode= "w" , newline= "") as file:
        header = csv.DictWriter(file, fieldnames= fields)
        if not file_exists:
            header.writeheader()
            print(f"Header Successfully Written in file: {file}\n")
        else:
            print(f"{file} already exists!!!\n")

csv_path = r"tictactoe_data.csv"
header = ["SN","Player 1", "Player 2", "Conqueror", "Date"]
exist = add_csv_header(csv_path, header)
exist