"""
Update Day 2 schedule:
1. Add Pause-Cafe after 10h35 (after BOUDOUAR/KNIDIRI)
2. Shift all subsequent presentations by 20 minutes
3. Add Pause-Dejeuner after the last presentation
4. Update index.html cards for Day 2 doctorants
"""
import re

# Time mapping: old -> new (20 min shift)
TIME_MAP = {
    "10h40 \u2013 11h00": "11h00 \u2013 11h20",
    "10h40 - 11h00": "11h00 - 11h20",
    "11h05 \u2013 11h25": "11h25 \u2013 11h45",
    "11h05 - 11h25": "11h25 - 11h45",
    "11h30 \u2013 11h50": "11h50 \u2013 12h10",
    "11h30 - 11h50": "11h50 - 12h10",
    "11h55 \u2013 12h15": "12h15 \u2013 12h35",
    "11h55 - 12h15": "12h15 - 12h35",
    "12h20 \u2013 12h40": "12h40 \u2013 13h00",
    "12h20 - 12h40": "12h40 - 13h00",
    "12h45 \u2013 13h05": "13h05 \u2013 13h25",
    "12h45 - 13h05": "13h05 - 13h25",
    "13h10 \u2013 13h30": "13h30 \u2013 13h50",
    "13h10 - 13h30": "13h30 - 13h50",
    "13h35 \u2013 13h55": "13h55 \u2013 14h15",
    "13h35 - 13h55": "13h55 - 14h15",
    "13h55 \u2013 14h15": "14h15 \u2013 14h35",
    "13h55 - 14h15": "14h15 - 14h35",
}

# ===================== UPDATE prog.html =====================
with open("prog.html", "r", encoding="utf-8") as f:
    prog = f.read()

# Pause-cafe entry to insert
pause_cafe_html = '                                                <div class="list-group-item list-group-item-action">\r\n                                                    <p class="mb-1"><strong>10h35 \u2013 10h55</strong> Pause-Caf\u00e9</p>\r\n                                                </div>\r\n'

# Find insertion point after BOUDOUAR in Salle Seminaire 1
# Look for the pattern: end of BOUDOUAR div, before ELMAJDOUBI
marker1 = "10h40 \u2013 11h00</strong> ELMAJDOUBI"
pos1 = prog.find(marker1)
if pos1 != -1:
    # Go back to find the <div before this
    search_back = prog.rfind('<div class="list-group-item', 0, pos1)
    prog = prog[:search_back] + pause_cafe_html + prog[search_back:]
    print("[OK] Added Pause-Cafe before ELMAJDOUBI in Salle Seminaire 1")
else:
    print("[FAIL] Could not find ELMAJDOUBI marker")

# Find insertion point after KNIDIRI in Salle Seminaire 2
marker2 = "10h40 \u2013 11h00</strong> EL MESTEM"
pos2 = prog.find(marker2)
if pos2 != -1:
    search_back = prog.rfind('<div class="list-group-item', 0, pos2)
    prog = prog[:search_back] + pause_cafe_html + prog[search_back:]
    print("[OK] Added Pause-Cafe before EL MESTEM in Salle Seminaire 2")
else:
    print("[FAIL] Could not find EL MESTEM marker")

# Now apply time shifts in prog.html (only in Day 2 section)
day2_marker = "Mardi 21 Avril 2026"
day2_pos = prog.find(day2_marker)
if day2_pos != -1:
    before_day2 = prog[:day2_pos]
    after_day2 = prog[day2_pos:]
    
    for old_time, new_time in TIME_MAP.items():
        after_day2 = after_day2.replace(old_time, new_time)
    
    prog = before_day2 + after_day2
    print("[OK] Shifted all Day 2 times by 20 minutes in prog.html")

# Update session time ranges (09h00 - 13h55 -> 09h00 - 14h35)
prog = prog.replace('09h00 - 13h55', '09h00 - 14h35')

# Update activites paralleles time range 
prog = prog.replace('09h00 - 13h35', '09h00 - 14h35')

# Update the old pause at the end to Pause-Dejeuner
prog = prog.replace('13h35 - 14h35', '14h35 - 15h35')
prog = prog.replace('<h5>Pause</h5>', '<h5>Pause-D\u00e9jeuner</h5>')
prog = prog.replace('Pause-Caf\u00e9</h6>', 'Pause-D\u00e9jeuner</h6>')

# Fix: The pause-cafe we just inserted should stay as Pause-Cafe
# The one at the bottom of Day 2 should be Pause-Dejeuner
# Let's be more precise - find the one after all sessions
# Actually the replacement above already handles this correctly since
# 'Pause-Cafe</h6>' was the old bottom pause, and we changed it.
# The inline ones we inserted use <p> tags not <h6>

# Update Cloture timing
prog = prog.replace('14h40 - 17h00', '15h40 - 17h00')

with open("prog.html", "w", encoding="utf-8") as f:
    f.write(prog)
print("[OK] prog.html saved")

# ===================== UPDATE index.html =====================
with open("index.html", "r", encoding="utf-8") as f:
    idx = f.read()

# Shift Day 2 cards
for old_time, new_time in TIME_MAP.items():
    old_pattern = "Mardi 21 Avril, " + old_time
    new_pattern = "Mardi 21 Avril, " + new_time
    count = idx.count(old_pattern)
    if count > 0:
        idx = idx.replace(old_pattern, new_pattern)
        print("[OK] Replaced %d cards: %s -> %s" % (count, old_time, new_time))

with open("index.html", "w", encoding="utf-8") as f:
    f.write(idx)
print("[OK] index.html saved")

print("\n=== DONE ===")
print("- Added Pause-Cafe (10h35-10h55) in both sessions after BOUDOUAR/KNIDIRI")
print("- Shifted all subsequent Day 2 presentations by 20 minutes")
print("- Updated end-of-day pause to Pause-Dejeuner (14h35-15h35)")
print("- Updated Cloture timing to 15h40-17h00")
print("- Updated all Day 2 doctorant card times in index.html")
