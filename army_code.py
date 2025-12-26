# Mapeamento de Cores (Adicionei cores neon/claras para ficarem bem no tema escuro)
search_terms = {
    "Club Penguin Armies": "#87d1ff",
    "CPA Battleground": "#ff4d4d",
    "Club Penguin Army Judges": "#ff3366",
    "Water Vikings": "#3399ff",
    "Army of Club Penguin": "#00cc00",
    "Elite Guardians of Club Penguin": "#b0b0b0",
    "Special Weapons and Tactics": "#00ff00",
    "Silver Empire": "#ffffff",
    "People's Imperial Confederation": "#9966ff",
    "Dark Pirates": "#ff3333",
    "Templars": "#ffcc00",
    "Rebel Penguin Federation": "#ffffff", # Branco na borda
    "Winged Hussars": "#ff3333",
    "Help Force": "#3366ff",
    "Smart Penguins": "#ff6666",
    "Warlords of Kosmos": "#888888",
    "Freeland" : "#666666"
}

with open('map.js', 'r') as file:
    content = file.read()

# HTML Template que linka o CSS externo
html_content = """
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="army_code.css">
</head>
<body>
"""

for term, color in search_terms.items():
    count = content.lower().count(term.lower()) - 1
    if count >= 1:
        # Gera a DIV com a classe .army-card e a cor na borda
        html_content += f'''
        <div class="army-card" style="border-left-color: {color};">
            <span class="army-name">{term}</span>
            <span class="army-count">{count}</span>
        </div>
        '''

html_content += "</body></html>"

with open("army_code.html", 'w') as file:
    file.write(html_content)
print("Updated army_code.html linked to army_code.css")
