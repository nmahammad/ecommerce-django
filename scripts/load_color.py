from product.models import Color
import csv


def run():
    with open('scripts/colors.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        for row in reader:
            print(row)

            color = Color(name=row[2], code=row[4] )           
            color.save()