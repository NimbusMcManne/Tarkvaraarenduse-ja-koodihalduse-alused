#!/bin/bash
# generate_data.sh
# Autor: Gregory Kuusmik
# Kuupäev: 2026-09-16
# Kirjeldus: Käivitab genereate_data.py faili, mis genereerib 200 suvalist andmepunkti. Seda tehakse N=10 korda.
# Kasutamine: ./generate_data.sh
data_path="../data"
file_path="generate_data.py"
for i in {1..10}; do
    echo "Jooksutan $i korda"
    touch "$data_path/data$i.txt"
    python "$file_path" > "$data_path/data$i.txt"
done