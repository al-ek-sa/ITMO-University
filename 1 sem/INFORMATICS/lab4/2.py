# Author = Lishik Aleksandra Yuryevna
# Group = P3106
# Date = 07.11.2025
# Option 503302%132=118
# Task 1.2

import hcl2
import pickle
import configparser

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    hcl = read_file("doc.hcl")
    datahcl = hcl2.loads(hcl)
    print(datahcl)
    databinary = pickle.dumps(datahcl)
    print(databinary)
    dataini = configparser.ConfigParser()
    for schedule in datahcl.get('schedule', []):
        for name, data in schedule.items():
            dataini['schedule'] = {'name': name}
            for nameweek, dataweek in data.items():
                for day in dataweek:
                    for nameday, periods in day.items():
                        for period in periods:
                            for nameperiod, dataperiod in period.items():
                                section = f"{nameweek}.{nameday}.{nameperiod}"
                                section = section.replace("_", " ")
                                dataini[section] = dataperiod
    with open("doc2.ini", "w", encoding="utf-8") as f:
        dataini.write(f)
    with open("doc2.ini", "r", encoding="utf-8") as f:
        ini = f.read()
        print(ini)
if __name__ == "__main__":
    main()