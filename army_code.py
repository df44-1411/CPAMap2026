# Define the sentences to search for and their corresponding colors
search_terms = {
    "Club Penguin Armies": "#87d1ff",
    "CPA Battleground": "#dd2100",
    "Club Penguin Army Judges": "#ca2244",
    "Water Vikings": "#000080",
    "Army of Club Penguin": "#008000",
    "Elite Guardians of Club Penguin": "grey",
    "Special Weapons and Tactics": "#00ff00",
    "Silver Empire": "white",
    "People's Imperial Confederation": "#333399",
    "Dark Pirates": "#800000",
    "Templars": "#ffcc00",
    "Rebel Penguin Federation": "#000000",
    "Winged Hussars": "#ff0000",
    "Help Force": "#0000ff",
    "Smart Penguins": "red",
    "Warlords of Kosmos": "black",
    "Freeland" : "grey"
}

# Open the file in read mode
with open('map.js', 'r') as file:
    # Read the content of the file
    content = file.read()

# Initialize the HTML content with Custom CSS for the Dashboard
html_content = """
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@600&display=swap" rel="stylesheet">
<style>
    body {
        background: transparent;
        color: #e0e6ed;
        font-family: 'Rajdhani', sans-serif;
        margin: 0;
        padding: 10px;
    }
    /* Estilo do Cartão de Exército */
    .army-card {
        margin: 6px 0;
        padding: 10px 15px;
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 4px;
        border-left: 4px solid #fff; /* Cor padrão, substituída inline */
        display: flex;
        justify-content: space-between;
        align-items: center;
        transition: all 0.2s ease;
        cursor: default;
    }
    .army-card:hover {
        background: rgba(255, 255, 255, 0.08);
        transform: translateX(3px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .army-name {
        font-weight: bold;
        text-transform: uppercase;
        font-size: 0.9rem;
        letter-spacing: 0.5px;
    }
    .territory-count {
        background: rgba(255,255,255,0.1);
        padding: 2px 8px;
        border-radius: 10px;
        font-size: 0.8rem;
        color: #fff;
    }
</style>
</head>
<body>
"""

# Iterate over the search terms
for term, color in search_terms.items():
    # Count the occurrences of the term in the content
    count = content.lower().count(term.lower()) - 1

    # If the term appears more than once
    if count >= 1:
        # Add a line to the HTML content using the new classes
        # Usamos 'color' tanto para o texto quanto para a borda esquerda
        html_content += f'''
        <div class="army-card" style="border-left-color: {color};">
            <span class="army-name" style="color: {color};">{term}</span>
            <span class="territory-count">{count}</span>
        </div>
        '''

# Close the HTML tags
html_content += "</body></html>"

# Write the HTML content to "army_code.html"
with open("army_code.html", 'w') as file:
    file.write(html_content)
