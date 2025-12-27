import json
import os

# --- CONFIGURAÇÃO ---
DATA_DIR = 'data'
OUTPUT_MAP_JS = 'map.js'
OUTPUT_ARMY_HTML = 'army_code.html'
OUTPUT_WEALTH_HTML = 'wealth_code.html'

def load_json(filename):
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        print(f"⚠️ Aviso: {filename} não encontrado em {DATA_DIR}")
        return [] if filename == 'servers.json' else {}
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

# 1. CARREGAR DADOS
servers = load_json('servers.json')
armies = load_json('armies.json')

print(f"📖 Lidos {len(servers)} servidores e {len(armies)} exércitos.")

# ==========================================
# PARTE A: GERAR MAP.JS
# ==========================================
print("⚙️ A gerar map.js...")

# Mapa de cores simples para injeção no JS
army_colors = {name: data['color'] for name, data in armies.items()}

# A lógica JavaScript que será escrita no ficheiro
# Nota: Mantemos a estrutura do teu map.js original mas injetamos os dados limpos
js_content = f"""
// GERADO AUTOMATICAMENTE POR generate_site.py
// NÃO EDITAR DIRETAMENTE - EDITE data/servers.json

var mapData = {json.dumps(servers, indent=2)};

Highcharts.mapChart('container', {{
    chart: {{
      height: 'fill',
      weight: 'auto',
      backgroundColor: 'transparent',
      type: 'line',
      map: 'cpa',
    }},
    title: {{ text: '' }},
    mapNavigation: {{ enabled: true }},
    legend: {{ enabled: false }},
    plotOptions: {{
      map: {{
        allAreas: false,
        joinBy: ['id', 'controller'],
        keys: ['id', 'controller'],
      }},
    }},
    series: [{{
      name: 'cpa',
      tooltip: {{
        headerFormat: '',
        pointFormat: '<b>Server:</b> {{point.name}}<br><b>Controller:</b> {{point.controller}}<br><b>Type:</b> {{point.type}}<br><b>Continent:</b> {{point.continent}}'
      }},
      dataLabels: {{
        enabled: true,
        formatter: function() {{
          if (this.point.type === "CAPITAL") {{
            return '<span style="color: #ffff00; text-shadow: 0 0 3px #000; font-weight:bold">' + this.point.name + '</span>';
          }} else {{
            return this.point.name;
          }}
        }}
      }},
      keys: ['id', 'controller'],
      type: "map",
      joinBy: "id",
      mapData: mapData,
      data: mapData.map(s => ({{ id: s.id, controller: s.controller }}))
    }}]
}}, function(chart) {{
    // APLICAR CORES DINAMICAMENTE
    const armyColors = {json.dumps(army_colors)};
    
    chart.series[0].points.forEach(function(point) {{
        if (point.controller && armyColors[point.controller]) {{
            point.graphic.css({{ fill: armyColors[point.controller] }});
        }} else {{
            point.graphic.css({{ fill: '#4a5568' }}); // Cor cinza padrão se sem dono
        }}
    }});
}});
"""

with open(OUTPUT_MAP_JS, 'w', encoding='utf-8') as f:
    f.write(js_content)

# ==========================================
# PARTE B: GERAR LISTAS (HTML)
# ==========================================
def generate_html_list(items, filename, title_col="name", val_col="value"):
    print(f"⚙️ A gerar {filename}...")
    html = """
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@600&display=swap" rel="stylesheet">
<style>
    /* CUSTOM SCROLLBAR */
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: rgba(0, 0, 0, 0.2); border-radius: 4px; }
    ::-webkit-scrollbar-thumb { background: #1c3d5e; border-radius: 4px; border: 1px solid rgba(0, 243, 255, 0.1); }
    html { scrollbar-width: thin; scrollbar-color: #1c3d5e rgba(0, 0, 0, 0.2); }

    body { background: transparent; font-family: 'Rajdhani', sans-serif; margin: 0; padding: 5px; overflow-x: hidden; }
    .card {
        display: flex; justify-content: space-between; align-items: center;
        background: rgba(20, 30, 50, 0.85); border: 1px solid rgba(255,255,255,0.1);
        border-left-width: 5px; margin-bottom: 8px; padding: 10px 15px;
        border-radius: 4px; color: #e0e6ed; cursor: pointer; transition: 0.2s;
        backdrop-filter: blur(4px);
    }
    .card:hover { transform: translateX(5px); background: rgba(40, 50, 80, 0.95); border-color: rgba(0, 243, 255, 0.3); }
    .name { font-weight: 700; text-transform: uppercase; font-size: 1rem; }
    .count { background: rgba(255,255,255,0.1); padding: 2px 8px; border-radius: 10px; font-weight: bold; font-size: 0.85rem; }
</style>
</head>
<body>
"""
    
    for item in items:
        html += f"""
    <div class="card" style="border-left-color: {item['color']};">
        <span class="name">{item[title_col]}</span>
        <span class="count">{item[val_col]}</span>
    </div>"""

    # Script de Hover universal
    html += """
<script>
    const cards = document.querySelectorAll('.card');
    cards.forEach(c => {
        c.addEventListener('mouseenter', () => {
            const name = c.querySelector('.name').innerText;
            window.parent.postMessage({type: 'hoverArmy', army: name}, '*');
        });
        c.addEventListener('mouseleave', () => window.parent.postMessage({type: 'resetMap'}, '*'));
    });
</script>
</body>
</html>
"""
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

# 1. LISTA DE FORÇAS ATIVAS (Calculado automaticamente do mapa)
land_counts = {}
for s in servers:
    owner = s.get('controller')
    if owner and owner in armies:
        land_counts[owner] = land_counts.get(owner, 0) + 1

sorted_forces = sorted(
    [{'name': k, 'value': v, 'color': armies[k]['color']} for k, v in land_counts.items()],
    key=lambda x: x['value'], reverse=True
)
generate_html_list(sorted_forces, OUTPUT_ARMY_HTML)

# 2. LISTA DE RIQUEZA (Valor manual do JSON)
sorted_wealth = sorted(
    [{'name': k, 'value': f"${v.get('wealth', 0)}", 'color': v['color'], 'raw_wealth': v.get('wealth', 0)} 
     for k, v in armies.items() if v.get('wealth', 0) > 0],
    key=lambda x: x['raw_wealth'], reverse=True
)
generate_html_list(sorted_wealth, OUTPUT_WEALTH_HTML)

print("✅ SUCESSO! map.js, army_code.html e wealth_code.html foram atualizados.")