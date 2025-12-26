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
    "Rebel Penguin Federation": "#ffffff",
    "Winged Hussars": "#ff3333",
    "Help Force": "#3366ff",
    "Smart Penguins": "#ff6666",
    "Warlords of Kosmos": "#888888",
    "Freeland" : "#666666"
}

with open('map.js', 'r') as file:
    content = file.read()

# CSS INJETADO DIRETAMENTE (Cool Boxes Garantidas)
html_content = """
<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@600&display=swap" rel="stylesheet">
<style>
    body {
        background: transparent;
        font-family: 'Rajdhani', sans-serif;
        margin: 0;
        padding: 10px;
        overflow-x: hidden;
    }
    .army-card {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: rgba(20, 30, 50, 0.85); /* Fundo escuro */
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-left-width: 5px; /* Borda grossa colorida */
        margin-bottom: 8px;
        padding: 12px 15px;
        border-radius: 4px;
        backdrop-filter: blur(4px);
        transition: transform 0.2s;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .army-card:hover {
        transform: translateX(5px);
        background: rgba(40, 50, 80, 0.95);
    }
    .army-name {
        color: #e0e6ed;
        font-weight: 700;
        font-size: 1rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .army-count {
        background: rgba(255,255,255,0.1);
        color: #fff;
        padding: 2px 8px;
        border-radius: 10px;
        font-size: 0.85rem;
        font-weight: bold;
    }
</style>
</head>
<body>
"""

for term, color in search_terms.items():
    count = content.lower().count(term.lower()) - 1
    if count >= 1:
        # Usa o CSS injetado acima
        html_content += f'''
        <div class="army-card" style="border-left-color: {color};">
            <span class="army-name">{term}</span>
            <span class="army-count">{count}</span>
        </div>
        '''

html_content += "</body></html>"

with open("army_code.html", 'w') as file:
    file.write(html_content)
print("army_code.html fixed with embedded CSS.")
