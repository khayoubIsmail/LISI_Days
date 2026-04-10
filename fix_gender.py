import re
html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

females = [
    "Hafsa MATICH", "RHESDAOUI Meryem", "ATTIOUI Sanae", 
    "EL KHARRACHI Khayya", "CHAFIA Ibtissam", "Hanane Moufid", 
    "EL MESTEM Oumayma", "AOMARI Nisrine"
]

for name in females:
    pattern = rf'<img src="assets/images/comite/homme\.png" alt="{name}">'
    replace = f'<img src="assets/images/comite/femme.png" alt="{name}">'
    content = re.sub(pattern, replace, content)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)
