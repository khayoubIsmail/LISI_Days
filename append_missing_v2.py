import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# simple extraction of speaker-name
existing_names = re.findall(r'<p class="speaker-name">([^<]+)</p>', content)
existing_names = [n.strip() for n in existing_names]
existing_names.append('Mohamed LAFHAM') # handle the edge case manually

prompt_list = """
14h00 – 14h20 EL FAQAR Abdessabour Chakir — Deep Learning in Material Design for Efficient Batteries
14h25 – 14h45 M'RHAR Kaoutar — Deep learning and language models for anticancer drug design
14h50 – 15h10 AIT MOHAMED Firdaous — Large Models Acceleration Techniques
15h15 – 15h35 KHAYOUB Ismail — LLM-Based Agents
15h40 – 16h00 Hafsa MATICH — AI-Based Structural Health Monitoring for Civil Infrastructure Diagnosis and Safety
16h05 – 16h25 ARSALANE Moad — Artificial intelligence and agriculture
16h30 – 16h50 MEKIANI Leila — LLM pour la conception de nouveaux médicaments : de la description de la maladie à la molécule
16h55 – 17h15 AIT HAMMOU Najia — Application of Artificial Intelligence and Robotics in Agriculture: Integration of sensors and assembly of programmable electronic cards
17h20 – 17h40 FADILI Aymane — Audio intelligence for local languages
17h45 – 18h05 FARAH Raja — Identifying Influential Nodes in Complex Networks Using Machine Learning

14h00 – 14h20 MESSAOUDI Salma — PINN-Based Digital Twin for Autonomous Vehicles with Sensor Integration and Web Platform
14h25 – 14h45 RAFIQ Imane — Système d'intelligence artificielle pour la surveillance, la prédiction et l'aide à la décision utilisant l'analyse du Big Data et l'Internet des objets : application dans le domaine medical
14h50 – 15h10 MORAKIB Marouan — Développement d'un modèle hybride Deep Learning – RL pour le diagnostic médical et la personnalisation des traitements
15h15 – 15h35 TARGUOAUI Mouad — Apprentissage automatique par renforcement hybridé appliqué à la classification et l'optimisation intelligente des flux énergétiques
15h40 – 16h00 RHESDAOUI Meryem — Communication V2X
16h05 – 16h25 OUHMIDOU Hajar — Deep learning and machine learning to avoid congestion in vehicle networks
16h30 – 16h50 OUBELOUAH Oumaima — AegisFlow
16h55 – 17h15 EL HABIB Oumaima — Overview of intelligent systems for deepfake detection in social media content
17h20 – 17h40 MALAINE Mariem — Intégration des modèles d'IA et d'otolithes DEB pour une meilleure estimation de l'âge et de la croissance des poissons
17h45 – 18h05 ELMANSOURI Abdelhalim — Sentiment analysis within the Moroccan parliamentary context, specifically focusing on questions directed by deputies to the government

09h00 – 09h20 CHATAOUI Nouhayla — Reinforcement Learning for Stock Market Returns Forecasting using Multi-Objective Optimization
09h25 – 09h45 LHASNAOUI Chaima — Enabling Federated Learning On the Edge for Enhanced Privacy in Medical Imaging
09h50 – 10h10 AIT BAALI Fatiha — Federated Fine-Tuning of Large Language Models for Domain-Specific Applications: Balancing Personalization and Privacy
10h15 – 10h35 BOUDOUAR Youssef — Deep multimodal learning and continuous learning for fault prognosis and real-time supervision and monitoring of nuclear
10h40 – 11h00 ELMAJDOUBI Mousaab — Market World Models: Learning Causal Representations for Modeling and Simulating Economic and Financial Dynamics
11h05 – 11h25 ATTIOUI Sanae — Les antennes fractales
11h30 – 11h50 OUASSINE Younes — Identification des coraux dans les collections d'images numériques à l'aide de modèles hybrides d'apprentissage en profondeur/ontologie/symbolique
11h55 – 12h15 AITIBOUREK Lahcen — TinyML-based for agricultural IoT devices
12h20 – 12h40 AL MOUATAMID Youssef — Traitement automatisé de l'information juridique pour la protection de l'environnement marin
12h45 – 13h05 EL KHARRACHI Khayya — Étude et proposition de modèles neuronales pour la reconnaissance et la classification des documents et images
13h10 – 13h30 CHAFIA Ibtissam — Modeling Spatio-Temporal and Social Dynamics of Marine Animals with Artificial Intelligence
13h35 – 13h55 CHETOUI Ismail — Graph Neural Networks for Educational Applications
13h55 – 14h15 Hanane Moufid — Using IA for Cyberattack Detection and Prevention

09h00 – 09h20 BABA Naima — SIGIRO: An information system for intelligent water resource management “a prospective dashboard for water resources”: the case of the MARRAKECH-SAFI region
09h25 – 09h45 JABIR Somaya — Apports des méthodes de reconnaissance automatique du langage pour la recherche de données pour la modélisation bioénergétique du type Dynamic Energy Budget
09h50 – 10h10 LECHHAB Hind — Vers une approche d'analyse spatio-temporelle des comportements de conduite à grande échelle basé sur l'IA
10h15 – 10h35 KNIDIRI Dounia — Smart-biochar
10h40 – 11h00 EL MESTEM Oumayma — Diagnostic de la fatigue et inattention
11h05 – 11h25 KASSIMI M'bark — Avancement de l'article de revue
11h30 – 11h50 LAZGHAM Loubna — L'intégration du blockchain et de l'IA dans le renforcement de la cybersecurity dans les smarts cities
11h55 – 12h15 AIT EZOUINE Elhoussine — Traitement et indexation des vidéos à l'aide de l'IA
12h20 – 12h40 ALHYANE Rachid — Combinaison de modèles d'apprentissage profond pour la classification multiclasse d'images médicales
12h45 – 13h05 Mohamed LAFHAM — Intelligent Tutoring System in Education 4.0
13h10 – 13h30 AOMARI Nisrine — État d'avancement thèse
13h35 – 13h55 LACHIHAB Oussama — Adaptive Multi-Modal Transformer Fusion for Multi-person Tracking Under Variable Scene Density
"""

missing_docs = []
lines = prompt_list.strip().split('\n')
for line in lines:
    if line.strip() == '':
        continue
    parts = line.split('—')
    if len(parts) >= 2:
        name_time = parts[0].strip()
        match_time = re.match(r'([\dohO]+[ \-–]+[\dohO]+)(.*)', name_time)
        if match_time:
            time_part = match_time.group(1).strip()
            name_only = match_time.group(2).strip()
        else:
            time_part = ""
            name_only = name_time
            
        title_only = parts[1].strip()
        
        # Check against existing names dynamically
        name_words = set(name_only.lower().split())
        match = False
        for ex in existing_names:
            if name_only.lower() in ex.lower() or ex.lower() in name_only.lower():
                match = True
                break
        
        if not match:
            missing_docs.append({'name': name_only, 'title': title_only, 'time': time_part})

females = [
    "Hafsa MATICH", "RHESDAOUI Meryem", "ATTIOUI Sanae", 
    "EL KHARRACHI Khayya", "CHAFIA Ibtissam", "Hanane Moufid", 
    "EL MESTEM Oumayma", "AOMARI Nisrine"
]

new_cards = ""
count = 35 # approx starting ID
for m in missing_docs:
    img = "femme.png" if m['name'] in females else "homme.png"
    new_cards += f'''
          <!-- Doctorant {count} -->
          <div class="speaker-card">
            <div class="speaker-image-circle">
              <img src="assets/images/comite/{img}" alt="{m['name']}">
            </div>
            <div class="speaker-info">
              <h3 class="speaker-talk-title">{m['title']}</h3>
              <p class="speaker-name">{m['name']}</p>
              <div class="speaker-details">
                <span><i class="fas fa-map-marker-alt"></i> Salles de Séminaire</span>
                <span><i class="fas fa-calendar-alt"></i> {m['time']}</span>
              </div>
            </div>
          </div>
'''
    count += 1

# Find EXACT insertion point for Doctorants grid closing div
target = '        </div>\n      </div>\n    </section>\n\n    <!-- Section Compétitions et Activités -->'
if target in content:
    content = content.replace(target, new_cards + target)
else:
    print("WARNING: Could not find exact insertion target. Look closely.")
    print("Attempting alternate insertion mechanism.")
    # Alternate:
    pattern = r'(\s*</div>\s*</div>\s*</section>\s*<!-- Section Compétitions et Activités -->)'
    match = re.search(pattern, content)
    if match:
        content = content[:match.start()] + new_cards + content[match.start():]
    else:
        print("Failed both mechanisms.")

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Appended {len(missing_docs)} missing docs successfully inside Doctorants grid.")
