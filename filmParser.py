import json

with open ('films.json') as f:
    file = json.load(f)

hf = open('films.html', 'w', encoding='utf-8');
html_template = '''<html>
<head>
<title>Каталог фильмов</title>
</head>
<body>
<h1>Фильмы</h1>
'''
for item in file:
    title = item["Title"]
    description = item["Plot"]
    year = item["Year"]
    runtime = item["Runtime"]
    genre = item["Genre"]
    language = item["Language"]
    img = item["Poster"]
    
    html_template += f"<h2>{title}</h2>"
    html_template += f"<p>{description}</p>"
    html_template += f"<p>{year}</p>"
    html_template += f"<p>{runtime}</p>"
    html_template += f"<p>{genre}</p>"
    html_template += f"<p>{language}</p>"
    html_template += f"<img src='{img}'>"
html_template += """
</body>
</html>
"""
hf.write(html_template);
hf.close();