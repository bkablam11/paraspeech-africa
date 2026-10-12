# COMPTE RENDU DE RÉUNION
**Projet ParaSpeech Africa – PIIA Cohorte 2 (AMA)**

**Date :** Mardi 6 octobre 2026  
**Heure :** 20h00 – 21h00 (Durée : 1 heure)  
**Lieu :** Visioconférence (Google Meet / Enregistrement Tactiq AI)  
**Objet :** Cadrage technique, organisation du flux collaboratif et lancement de la Phase 0  

---

### 1. PARTICIPANTS

**Étaient présents :**
* **Edjabrou Ulrich Blanchard KABLAM**, Coordinateur / Lead technique (Rédacteur)
* **Richnel EGUE**, Ingénieur Machine Learning / Membre de l’équipe

**Absents excusés (membres de l’équipe projet) :**
* **Ghilth GBAGUIDI**
* **Wilfried BONOU**

---

### 2. ORDRE DU JOUR

1. **Rappel du cadre et du calendrier du projet fil rouge (ParaSpeech Africa)**
2. **Analyse d’un échantillon vidéo pilote (cas pratique Cotonou : Français – Fongbe)**
3. **Validation du couple de langues de travail**
4. **Architecture de travail collaboratif (GitHub, Local, Google Colab & Drive)**
5. **Méthodologie Git et convention d'équipe**
6. **Plan d'action immédiat et rituels d'équipe**

---

### 3. DÉROULEMENT ET SYNTHÈSE DES ÉCHANGES

#### 1. Rappel du cadre et du calendrier du projet
* **Edjabrou U.B.K.** rappelle la structure du projet ParaSpeech Africa au sein du PIIA :
  * **Octobre 2026 :** Phase 0 (Kick-off, fondations mathématiques, mise en place de l'environnement) puis Phase 1 (Pipeline de données, traitement du signal, segmentation).
  * **Novembre 2026 :** Phase 2 (Machine Learning supervisé, classification des paires candidates).
* L’objectif fondamental d'octobre est de mettre en place le dépôt, l'arborescence minimale et les fondations mathématiques du signal avant d'attaquer la modélisation complexe.

#### 2. Analyse de la vidéo pilote et problématique d'alignement
* L'équipe a visionné et analysé un extrait vidéo d'une prédication bilingue enregistrée à Cotonou (Bénin).
* **Constats techniques relevés par Richnel E. et Edjabrou U.B.K. :**
  * L’interprétation n’est pas du « mot-à-mot » strict : l’interprète résume parfois ou adapte le propos face à des phrases sources trop longues du locuteur principal.
  * Il existe des risques de chevauchement vocal lorsque l'orateur reprend la parole avant la fin de la traduction.
  * *Conclusion technique :* Le système devra être capable de détecter la fin réelle des tours de parole pour proposer des segments appariés cohérents, malgré la variabilité du débit d'élocution.

#### 3. Choix du binôme linguistique
* **Décision retenue : Français $\longleftrightarrow$ Fongbe (Fon).**
* **Justification :** 
  * Présence de Richnel E. (locuteur/familier du contexte béninois).
  * Alignement avec les initiatives nationales béninoises citées dans le cadrage PIIA (*JaimeMaLangue*, SNIAM 2023-2027).
  * Disponibilité de ressources audiovisuelles publiques accessibles (cultes, discours, conférences) permettant de constituer le corpus sans blocage d'acquisition.

#### 4. Architecture de travail et environnement technique
* Adoption d'une architecture hybride validée par l'équipe :
  * **GitHub :** Référentiel unique du code source, des modules (`src/`), des notebooks de recherche et des tests.
  * **Environnement Local :** Développement modulaire, écriture des scripts et tests rapides.
  * **Google Colab (CUDA GPU) :** Dédié aux calculs intensifs (extraction audio lourde, traitement spectrogrammes, futures inférences ML/DL).
  * **Google Drive :** Espace de stockage des gros fichiers médias bruts et traités (`.mp4`, `.wav`), ces derniers étant strictement exclus de Git via le `.gitignore`.

#### 5. Protocole Git et règles de collaboration
* Pour garantir la traçabilité et éviter tout conflit ou écrasement de code :
  * **Interdiction de committer directement sur la branche principale (`main`).**
  * Création systématique de branches thématiques de travail (`feature/nom-tache` ou `dev-prenom`).
  * Relecture, validation collective et intégration par *Pull Requests (PR)* et *Merge*.

---

### 4. DÉCISIONS ET ACTIONS À ENTREPRENDRE

| Action | Responsable(s) | Échéance |
| :--- | :--- | :--- |
| **Création du repository GitHub** `paraspeech-africa`, configuration du `.gitignore` et invitation des collaborateurs (Richnel, Ghilth, Wilfried). | Edjabrou U.B.K. | Immédiat |
| **Initialisation de l'arborescence standard** (`data/`, `src/`, `notebooks/`, `tests/`, `README.md`). | Edjabrou U.B.K. | 07/10/2026 |
| **Recherche et collecte de 2 à 3 vidéos pilotes** d’interprétation consécutive Français–Fongbe de bonne qualité acoustique. | Richnel E. & l'équipe | 10/10/2026 |
| **Partage du présent compte-rendu** dans le canal de discussion du groupe. | Edjabrou U.B.K. | 06/10/2026 |
| **Clonage du repo en local et test d'accès Colab** par chaque membre de l'équipe. | Tous les membres | 11/10/2026 |

---

### 5. CONCLUSION ET PROCHAINE RÉUNION

La réunion s’est déroulée dans un climat de travail constructif et pragmatique. Les bases de la Phase 0 sont posées.

* **Rythme arrêté :** Point de synchronisation hebdomadaire fixé **chaque mardi à 19h30 (GMT)**.
* **Prochaine réunion :** **Mardi 13 octobre 2026 à 19h30**.  
  * *Ordre du jour prévu :* Revue de l'arborescence Git, validation des vidéos pilotes collectées, extraction du premier signal $16\text{ kHz}$ et visualisation des premières métriques mathématiques ($E_{\text{RMS}}$, distribution d'amplitude).

---

*Fait à Abidjan / Cotonou, le 6 octobre 2026*  
**Le Coordinateur du Projet / Rédacteur :**  
*Edjabrou Ulrich Blanchard KABLAM*