import camelot

tables = camelot.read_pdf('data/input/foo.pdf', pages='1')

print(tables)

tables.export('data/output/foo.csv', f='csv', compress=True)
tables[0].to_csv('data/output/foo.csv')