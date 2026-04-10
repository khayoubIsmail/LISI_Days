import textwrap
from bs4 import BeautifulSoup

def sort_doctorants():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    section = soup.find(lambda t: t.name == 'h2' and 'Doctorants' in t.get_text())
    
    if not section:
        print("Doctorants section not found.")
        return

    grid = section.find_next_sibling('div', class_='speakers-grid')
    if not grid:
        print("speakers-grid not found.")
        return

    # Extract all speaker cards
    cards = grid.find_all('div', class_='speaker-card', recursive=False)
    
    # Extract comments if they are associated with cards or just discard them and re-add general markers.
    # Actually, we can just sort the cards directly.
    
    def get_sort_key(card):
        # find the details
        details_div = card.find('div', class_='speaker-details')
        if not details_div:
            return (99, "99h99")
        
        spans = details_div.find_all('span')
        if len(spans) < 2:
            return (99, "99h99")
            
        time_text = spans[1].get_text(strip=True) # e.g. "Lundi 20 Avril, 14h00 – 14h20"
        
        # Parse day
        day_val = 99
        if 'lundi' in time_text.lower():
            day_val = 0
        elif 'mardi' in time_text.lower():
            day_val = 1
            
        # Parse time
        import re
        time_match = re.search(r'(\d{2})h(\d{2})', time_text)
        if time_match:
            time_val = f"{time_match.group(1)}:{time_match.group(2)}"
        else:
            time_val = "99:99"
            
        return (day_val, time_val)

    # Sort the cards
    cards.sort(key=get_sort_key)
    
    # Remove all existing contents inside the grid
    grid.clear()
    
    # Re-append the sorted cards with nice formatting
    for i, card in enumerate(cards):
        # Create a newline before each comment and card
        grid.append("\n          <!-- Doctorant {} -->\n          ".format(i+1))
        grid.append(card)
        
    grid.append("\n        ")

    # Save to file
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Done sorting doctorant cards.")

if __name__ == '__main__':
    sort_doctorants()
