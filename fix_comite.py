import re
import subprocess

# 1. Get the old students
result = subprocess.run(['git', 'show', 'HEAD:index.html'], capture_output=True, text=True, encoding='utf-8')
old_content = result.stdout
match = re.search(r'(<!-- Étudiants -->.*?)</div>\s*</section>', old_content, re.DOTALL)
students_html = ""
if match:
    students_html = match.group(1).split('<!-- Étudiants -->')[1]

# Wrap students in a comite-section
students = f"""
        <!-- Étudiants -->
        <div class="comite-section">
          <h3 class="comite-title">Étudiants</h3>
          <div class="comite-grid">
{students_html}
"""

# 2. Add Evaluators HTML
evaluators = """
        <!-- Comité d'évaluation : Master/poster -->
        <div class="comite-section">
          <h3 class="comite-title">Comité d'évaluation : Master/poster</h3>
          <div class="comite-grid">
            <div class="comite-card">
              <div class="comite-image-circle">
                <img src="assets/images/comite/homme.png" alt="Pr. Ikdid Abdelouafi">
              </div>
              <div class="comite-info">
                <h4 class="comite-name" style="color: #ff6b6b;">Pr. Ikdid Abdelouafi</h4>
                <p class="comite-role" style="color: #1a5f7a;">Enseignant à la FSSM</p>
              </div>
            </div>
            
            <div class="comite-card">
              <div class="comite-image-circle">
                <img src="assets/images/comite/afoudi.jpg" alt="Pr. Afoudi Yassine">
              </div>
              <div class="comite-info">
                <h4 class="comite-name" style="color: #ff6b6b;">Pr. Afoudi Yassine</h4>
                <p class="comite-role" style="color: #1a5f7a;">Enseignant à la FSSM</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Comité d'évaluation des présentations (PhD) -->
        <div class="comite-section">
          <h3 class="comite-title">Comité d'évaluation des présentations (PhD)</h3>
          <div class="comite-grid">
            
            <div class="comite-card">
              <div class="comite-image-circle">
                <img src="assets/images/comite/homme.png" alt="Pr. Elouarak">
              </div>
              <div class="comite-info">
                <h4 class="comite-name" style="color: #ff6b6b;">Pr. Elouarak</h4>
                <p class="comite-role" style="color: #1a5f7a;">Enseignant à la FSSM</p>
              </div>
            </div>
            
            <div class="comite-card">
              <div class="comite-image-circle">
                <img src="assets/images/speaker/chadi.jpg" alt="Pr. Chadi">
              </div>
              <div class="comite-info">
                <h4 class="comite-name" style="color: #ff6b6b;">Pr. Chadi</h4>
                <p class="comite-role" style="color: #1a5f7a;">Enseignant à la FSSM</p>
              </div>
            </div>
            
            <div class="comite-card">
              <div class="comite-image-circle">
                <img src="assets/images/comite/homme.png" alt="Pr. Aznague">
              </div>
              <div class="comite-info">
                <h4 class="comite-name" style="color: #ff6b6b;">Pr. Aznague</h4>
                <p class="comite-role" style="color: #1a5f7a;">Enseignant à la FSSM</p>
              </div>
            </div>
            
            <div class="comite-card">
              <div class="comite-image-circle">
                <img src="assets/images/comite/homme.png" alt="Pr. Fahd">
              </div>
              <div class="comite-info">
                <h4 class="comite-name" style="color: #ff6b6b;">Pr. Fahd</h4>
                <p class="comite-role" style="color: #1a5f7a;">Enseignant à la FSSM</p>
              </div>
            </div>
            
            <div class="comite-card">
              <div class="comite-image-circle">
                <img src="assets/images/comite/femme.png" alt="Pr. Latifa">
              </div>
              <div class="comite-info">
                <h4 class="comite-name" style="color: #ff6b6b;">Pr. Latifa</h4>
                <p class="comite-role" style="color: #1a5f7a;">Enseignante à la FSSM</p>
              </div>
            </div>
            
            <div class="comite-card">
              <div class="comite-image-circle">
                <img src="assets/images/comite/maria.jpeg" alt="Pr. Maria">
              </div>
              <div class="comite-info">
                <h4 class="comite-name" style="color: #ff6b6b;">Pr. Maria</h4>
                <p class="comite-role" style="color: #1a5f7a;">Enseignante à la FSSM</p>
              </div>
            </div>
            
            <div class="comite-card">
              <div class="comite-image-circle">
                <img src="assets/images/comite/homme.png" alt="Pr. Hadni">
              </div>
              <div class="comite-info">
                <h4 class="comite-name" style="color: #ff6b6b;">Pr. Hadni</h4>
                <p class="comite-role" style="color: #1a5f7a;">Enseignant à la FSSM</p>
              </div>
            </div>
            
            <div class="comite-card">
              <div class="comite-image-circle">
                <img src="assets/images/comite/homme.png" alt="Pr. Elbachari">
              </div>
              <div class="comite-info">
                <h4 class="comite-name" style="color: #ff6b6b;">Pr. Elbachari</h4>
                <p class="comite-role" style="color: #1a5f7a;">Enseignant à la FSSM</p>
              </div>
            </div>
            
            <div class="comite-card">
              <div class="comite-image-circle">
                <img src="assets/images/comite/homme.png" alt="Pr. Elkiram">
              </div>
              <div class="comite-info">
                <h4 class="comite-name" style="color: #ff6b6b;">Pr. Elkiram</h4>
                <p class="comite-role" style="color: #1a5f7a;">Enseignant à la FSSM</p>
              </div>
            </div>
            
            <div class="comite-card">
              <div class="comite-image-circle">
                <img src="assets/images/comite/homme.png" alt="Pr. Abdelouahed">
              </div>
              <div class="comite-info">
                <h4 class="comite-name" style="color: #ff6b6b;">Pr. Abdelouahed</h4>
                <p class="comite-role" style="color: #1a5f7a;">Enseignant à la FSSM</p>
              </div>
            </div>
            
            <div class="comite-card">
              <div class="comite-image-circle">
                <img src="assets/images/comite/femme.png" alt="Pr. Hasna">
              </div>
              <div class="comite-info">
                <h4 class="comite-name" style="color: #ff6b6b;">Pr. Hasna</h4>
                <p class="comite-role" style="color: #1a5f7a;">Enseignante à la FSSM</p>
              </div>
            </div>
            
            <div class="comite-card">
              <div class="comite-image-circle">
                <img src="assets/images/comite/homme.png" alt="Pr. Ilyas">
              </div>
              <div class="comite-info">
                <h4 class="comite-name" style="color: #ff6b6b;">Pr. Ilyas</h4>
                <p class="comite-role" style="color: #1a5f7a;">Enseignant à la FSSM</p>
              </div>
            </div>
            
            <div class="comite-card">
              <div class="comite-image-circle">
                <img src="assets/images/comite/homme.png" alt="Pr. Mustapha">
              </div>
              <div class="comite-info">
                <h4 class="comite-name" style="color: #ff6b6b;">Pr. Mustapha</h4>
                <p class="comite-role" style="color: #1a5f7a;">Enseignant à la FSSM</p>
              </div>
            </div>
            
          </div>
        </div>
"""

with open('d:/other-Projects/LISI_Days/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace using regex to be safe about whitespaces
replacement = evaluators + "\n" + students + "\n      </div>\n    </section>\n\n    <section class=\"contact\" id=\"contact\">"

content = re.sub(r'      </div>\n    </section>\s*<section class="contact" id="contact">', replacement, content)

with open('d:/other-Projects/LISI_Days/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Done fixing")
