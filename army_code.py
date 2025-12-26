# Define the sentences to search for and their corresponding colors
search_terms = {
    "Club Penguin Armies": "#87d1ff",
    "CPA Battleground": "#ff4d4d",  # Ajustei para um vermelho mais brilhante (legivel)
    "Club Penguin Army Judges": "#ff3366", # Ajuste para neon
    "Water Vikings": "#3366ff",     # Azul mais claro para aparecer no fundo escuro
    "Army of Club Penguin": "#00cc00", # Verde mais brilhante
    "Elite Guardians of Club Penguin": "#a0a0a0", # Cinza claro
    "Special Weapons and Tactics": "#00ff00",
    "Silver Empire": "#ffffff",
    "People's Imperial Confederation": "#6666ff",
    "Dark Pirates": "#ff3333",
    "Templars": "#ffdd33", # Amarelo mais brilhante
    "Rebel Penguin Federation": "#ffffff", # MUDANÇA CRÍTICA: RPF de Preto para Branco na lista (ou usa cinza #444 se quiseres escuro, mas branco é melhor)
    "Winged Hussars": "#ff3333",
    "Help Force": "#3333ff",
    "Smart Penguins": "#ff5555",
    "Warlords of Kosmos": "#cccccc", # Mudado de preto para cinza claro
    "Freeland" : "#888888"
}

# Open the file in read mode
with open('map.js', 'r') as file:
    content = file.read()

# Initialize HTML with enhanced CSS for Dark Mode
html_content = """
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@600&display=swap" rel="stylesheet">
<style>
    body {
        background: transparent;
        color: #e0e6ed; /* Texto base claro */
        font-family: 'Rajdhani', sans-serif;
        margin: 0;
        padding: 5px;
        /* Scrollbar fina para ficar bonito */
        scrollbar-width: thin;
        scrollbar-color: #00f3ff transparent;
    }
    
    .army-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 8px 12px;
        margin-bottom: 6px;
        background: rgba(25, 30, 50, 0.6); /* Fundo semi-transparente em cada item */
        border-left: 4px solid #fff; /* A cor vai aqui via inline style */
        border-radius: 0 4px 4px 0; /* Cantos arredondados na direita */
        transition: all 0.2s ease;
    }

    .army-row:hover {
        background: rgba(40, 50, 80, 0.8);
        transform: translateX(2px);
    }

    .army-name {
        font-size: 0.95rem;
        font-weight: 600;
        letter-spacing: 0.5px;
        text-shadow: 0 1px 2px rgba(0,0,0,0.5); /* Sombra para leitura perfeita */
    }

    .count-badge {
        background: rgba(0,0,0,0.4);
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 0.8rem;
        color: #aaa;
        border: 1px solid rgba(255,255,255,0.05);
    }
</style>
</head>
<body>
"""

# Iterate and Generate
for term, color in search_terms.items():
    # Count occurrences
    count = content.lower().count(term.lower()) - 1

    if count >= 1:
        # AQUI ESTÁ O TRUQUE:
        # 1. border-left-color: usa a cor do exército para identificação.
        # 2. color: usa a cor do exército para o NOME também (mas usei versões mais claras no dicionário acima).
        #    Se preferir texto sempre branco, mude style="color: {color}" para style="color: #fff".
        html_content += f'''
        <div class="army-row" style="border-left-color: {color};">
            <span class="army-name" style="color: {color};">{term}</span>
            <span class="count-badge">{count}</span>
        </div>
        '''

html_content += "</body></html>"

with open("army_code.html", 'w') as file:
    file.write(html_content)
print("army_code.html updated successfully with Dark Mode styles.")
