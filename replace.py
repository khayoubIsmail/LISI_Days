import re
import os

images_dir = "assets/images/speaker"
html_path = "index.html"

images = os.listdir(images_dir)

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

def find_image(name, images):
    name_parts = [p for p in re.findall(r'\w+', name.lower()) if len(p) > 2 and p not in ["ait", "el", "ben", "pr", "dr"]]
    
    # Check exact matches of parts first
    for img in images:
        img_name_lower = os.path.splitext(img)[0].lower()
        for part in name_parts:
            # Match word boundaries to avoid 'hasna' matching 'lhasnaoui'
            if re.search(r'\b' + re.escape(part) + r'\b', img_name_lower.replace('_', ' ')):
                return img
    
    # Check substring inclusion
    for img in images:
        img_name_lower = os.path.splitext(img)[0].lower()
        for part in name_parts:
            if len(part) > 3 and part in img_name_lower:
                return img
                
    return None

pattern1 = r'(<img src="([^"]+)" alt="([^"]+)">)'

def replace_all(match):
    full_string = match.group(0)
    img_tag_src = match.group(2)
    alt_text = match.group(3)
    
    # ONLY map if we are currently using generic placeholders
    if "homme.png" in img_tag_src or "femme.png" in img_tag_src:
        matched_img = find_image(alt_text, images)
        if matched_img:
            return re.sub(r'src="[^"]+"', f'src="{images_dir}/{matched_img}"', full_string)
            
    return full_string

new_content = re.sub(pattern1, replace_all, html_content)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Done replacing.")
