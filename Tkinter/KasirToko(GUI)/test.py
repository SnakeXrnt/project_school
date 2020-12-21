from json import *
from datetime import  datetime
from reportlab.pdfgen import canvas
from pandas import *

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

now = datetime.now()

q = str(now) +  ' LIST HARGA DAN STOCK BARANG.pdf'

styles = getSampleStyleSheet()
report = SimpleDocTemplate('report/LIST HARGA DAN STOCK BARANG.pdf')
report_title = Paragraph("LIST HARGA DAN STOCK BARANG", styles["h1"])
report.title = (str(now))
report.build([report_title])

fruit = {

}

f = open('login_info.json','r')

fruit = load(f)

table_data = []
for k, v in fruit.items():
    table_data.append([k, v])

print(table_data)
report_table = Table(data=table_data)
report.build([report_title, report_table])
from reportlab.lib import colors

table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
report.build([report_title, report_table])
