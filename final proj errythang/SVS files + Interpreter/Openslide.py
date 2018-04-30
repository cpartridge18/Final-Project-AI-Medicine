import openslide
import csv
import sys


File_names = ["TCGA-38.svs", "TCGA-44.svs", 'TCGA-52.svs', 'TCGA-26.txt']

for x in File_names:
	a=openslide.OpenSlide(x)
	a.get_thumbnail(a.dimensions).show()
	#show first slide



txt_file = r"annotations.txt"
csv_file = r"TCGAannotations.csv"

in_txt = open(txt_file, "r")
out_csv = csv.writer(open(csv_file, 'wb'))

file_string = in_txt.read()

file_list = file_string.split('\n')

for row in file_list:       
    out_csv.writerow(row)

print (TCGAannotations.csv)
