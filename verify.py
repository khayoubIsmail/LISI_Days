import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# We need to extract the cards only under Doctorants
# The Doctorants section starts with <h2 class="section-title">Doctorants</h2>
# The grid is <div class="speakers-grid">
match = re.search(r'<h2 class="section-title">Doctorants</h2>.*?<div class="speakers-grid">(.*?)</div>\s*</section>', text, re.DOTALL)

if match:
    grid_html = match.group(1)
    # Count speaker cards
    cards = re.findall(r'<div class="speaker-card">', grid_html)
    names = re.findall(r'<p class="speaker-name">([^<]+)</p>', grid_html)
    
    print(f'Found {len(cards)} cards in Doctorants section.')
    print(f'Found {len(names)} names.')
    
    # Print out the names sequentially to see if all 45 exist
    for idx, name in enumerate(names, 1):
        print(f"{idx}. {name.strip()}")
else:
    # Try alternate bound
    match = re.search(r'<h2 class="section-title">Doctorants</h2>(.*?)<!-- Section Programme -->', text, re.DOTALL)
    if match:
        grid_html = match.group(1)
        cards = re.findall(r'<div class="speaker-card">', grid_html)
        names = re.findall(r'<p class="speaker-name">([^<]+)</p>', grid_html)
        print(f'Found {len(cards)} cards in Doctorants section.')
        print(f'Found {len(names)} names.')
        for idx, name in enumerate(names, 1):
            print(f"{idx}. {name.strip()}")
    else:
        print("Could not find section.")
