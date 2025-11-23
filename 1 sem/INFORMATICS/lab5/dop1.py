import polars as pl

df = pl.read_excel('lab5.xlsx')

result_data = []
for i in range(1, 13): 
    row = df.row(i)
    binary = "".join(str(row[j]) for j in range(6, 25))
    row4 = "".join(str(row[j]) for j in range(4, 5))
    result_data.append([
        row[0], 
        row[1],  
        row[2],           
        row4,  
        binary
    ])
result_data1 = []
for n in range(1, 3): 
    row = df.row(n)
    result_data1.append([
        "",
        row[1],  
        row[2], 
        "",
        "",
    ])  

def table(data1, data2, file=None):
    size = [15, 17, 15, 15, 20]

    name = ["Переменная Х", "Формула подсчета", "Значение", "Переменная B", "Значение"]
    type = ["str", "str", "i64", "str", "str"]
    borders = {
        'upper section': "┌" + "┬".join("─" * w for w in size) + "┐",
        'middle separator': "├" + "┴".join("─" * w for w in size) + "┤",
        'middle separator1': "├" + "┬".join("─" * w for w in size) + "┤",
        'lower section': "└" + "┴".join("─" * w for w in size) + "┘"
    }    
    rows = [
        borders['upper section'],
        "│" + "│".join(f"{h:^{w}}" for h,w in zip(name, size)) + "│",
        "│" + "│".join(f"{t:^{w}}" for t,w in zip(type, size)) + "│",
        borders['middle separator']
    ] + [
        "│" + " ".join(f"{str(cell):^{w}}" for cell,w in zip(row, size)) + "│" 
        for row in data2
    ] + [borders['middle separator1']
    ] + [     
        "│" + "│".join(f"{str(cell):^{w}}" for cell,w in zip(row, size)) + "│" 
        for row in data1
    ] + [borders['lower section']]
    table_end = "\n".join(rows)
    print(table_end) if file is None else file.write(table_end + "\n")
table(result_data, result_data1)
with open('dop1.txt', 'w', encoding='utf-8') as f:
    table(result_data, result_data1, file=f)