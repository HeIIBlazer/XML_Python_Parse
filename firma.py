base = """<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>Page Title</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <link rel='stylesheet' type='text/css' media='screen' href='main.css'>
    <script src='main.js'></script>
</head>
<body>"""

import xml.etree.ElementTree as ET
tree = ET.parse("firma.xml") # or ET.parse("path_to_xml_file")
firma_name = tree.find("Firma")
name = "<h1>"+str(firma_name.attrib["name"])+"</h1>"
with open("firma.html", "w", encoding="utf-8") as date:
    for i in tree.findall("Firma/offer"):  # or tree.findall('globalVariables/globalVariable/name')
        unit = """<div>
            <h2>Tour of """
        for j in i:
            if j.tag == "country":
                unit += j.text+"""</h2>
                <h3>Tour information</h3>
                <p>"""
            elif j.tag != "programe":
                unit += j.text+"""</p>
                <p>"""
            if j.tag == "programe":
                for q in j:
                    unit += q.text+"""</p>
                        <p>"""
                    if q.tag == "hotels":
                        for w in q:
                            unit += w.text
                        unit += "</p>"
        unit += "</div>"
        base += unit
    base += """</body>
    </html>"""
    date.write(base)

                    

        

