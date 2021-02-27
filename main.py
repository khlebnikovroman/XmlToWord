import xml.etree.ElementTree as ET
import docx
from random import randint

print('Введите имя файла')
fileName = input()
tree = ET.parse(fileName)
root = tree.getroot()
functions = []
# Поиск тегов <Заключение> на любом уровне
for member in root.iter('member'):
    params = []
    name = member.get("name")
    try:
        summary = member.find("summary").text
    except:
        summary = None

    try:
        for par in member.findall('param'):
            params.append(par.text)
    except:
        params = None

    try:
        returns = member.find("returns").text
    except:
        returns = None

    functions.append({"name": name, 'summary': summary, "params": params, "returns": returns})

print(functions)
doc = docx.Document()

table = doc.add_table(rows=len(functions) + 1, cols=4)
table
table.rows[0].cells[0].text = "Название функции"
table.rows[0].cells[1].text = "Описание"
table.rows[0].cells[2].text = "Параметры"
table.rows[0].cells[3].text = "Возращает"
for i in range(len(functions)):
    try:
        table.rows[i + 1].cells[0].text = functions[i]["name"].strip()
    except:
        pass

    try:
        table.rows[i + 1].cells[1].text = functions[i]["summary"].strip()
    except:
        pass

    try:
        for j in range(len(functions[i]["params"])):
            table.rows[i + 1].cells[2].text = functions[i]["params"][j].strip()
    except:
        pass

    try:
        table.rows[i + 1].cells[3].text = functions[i]["returns"].strip()
    except:
        pass

doc.save(str(randint(129381,439852783745))+'.docx')