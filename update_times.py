import re
from bs4 import BeautifulSoup

with open('prog.html', 'r', encoding='utf-8') as f:
    prog_content = f.read()

soup = BeautifulSoup(prog_content, 'html.parser')

# Find all rows in the table
current_day = "TBD"
current_room = "Salles de Séminaire"

doctorant_map = [] # list of dictionaries: {name, time, room, day}

for tr in soup.find_all('tr'):
    # Check if this row is a date row
    h4 = tr.find('h4')
    if h4:
        # e.g., Lundi 20 Avril 2026
        # Let's extract just the day and date e.g. "Lundi 20 Avril"
        full_date = h4.get_text(strip=True)
        # trim year if present
        current_day = re.sub(r' \d{4}$', '', full_date)
        continue
    
    h5 = tr.find('h5')
    if h5:
        h5_text = h5.get_text(strip=True)
        if "Session" in h5_text and ":" in h5_text:
            # e.g. Session 1 : Salle Séminaire 1
            current_room = h5_text.split(':')[1].strip()
            
    # Now check list items for presentations
    for item in tr.find_all('div', class_='list-group-item'):
        p = item.find('p')
        if not p: continue
        
        strong = p.find('strong')
        if not strong: continue
        
        # Format usually: <strong>14h00 – 14h20</strong> EL FAQAR Abdessabour Chakir — Deep Learning...
        time_text = strong.get_text(strip=True)
        
        full_text = p.get_text(strip=True)
        # Clean up non-breaking spaces
        full_text = full_text.replace('\xa0', ' ')
        
        if '—' in full_text and time_text in full_text:
            after_time = full_text.split('—')[0].replace(time_text, '').strip()
            # after_time should be the name
            name = after_time
            if name:
                doctorant_map.append({
                    'name': name,
                    'time': time_text,
                    'room': current_room,
                    'day': current_day
                })

print(f"Extracted {len(doctorant_map)} records from prog.html")

# Now load index.html and update the doctorant cards
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

soup_idx = BeautifulSoup(index_content, 'html.parser')
doc_section = soup_idx.find(lambda t: t.name == 'h2' and 'Doctorants' in t.get_text())

if doc_section:
    grid = doc_section.find_next_sibling('div', class_='speakers-grid')
    if grid:
        cards = grid.find_all('div', class_='speaker-card')
        for card in cards:
            name_tag = card.find('p', class_='speaker-name')
            if not name_tag: continue
            name_in_card = name_tag.get_text(strip=True)
            
            # Find match in map
            match = None
            name_words = set(name_in_card.lower().split())
            for d in doctorant_map:
                d_words = set(d['name'].lower().split())
                # checking subset or significant intersection
                if all(w in d['name'].lower() for w in name_words) or all(w in name_in_card.lower() for w in d_words):
                    match = d
                    break
                    
            if match:
                # Update details
                details_div = card.find('div', class_='speaker-details')
                if details_div:
                    spans = details_div.find_all('span')
                    if len(spans) >= 2:
                        # spans[0] is room
                        spans[0].clear()
                        spans[0].append(soup_idx.new_tag('i', attrs={'class': 'fas fa-map-marker-alt'}))
                        spans[0].append(" " + match['room'])
                        
                        # spans[1] is time
                        spans[1].clear()
                        spans[1].append(soup_idx.new_tag('i', attrs={'class': 'fas fa-calendar-alt'}))
                        spans[1].append(" " + match['day'] + ", " + match['time'])
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup_idx))
    print("Done updating index.html")
else:
    print("Could not find Doctorants section in index.html")
