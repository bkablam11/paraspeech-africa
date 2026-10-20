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

### OPTION 1 : Le Message Global (Tout-en-un pour le groupe)
*À copier-coller directement pour donner le cap à Richnel, Ghilth et Wilfried :*

---

📢 **Point d’avancement & Feuille de route — ParaSpeech Africa (Phase 0)**

Salut l'équipe ! 

Suite à notre séance de cadrage du 06/10, la structure de notre projet fil rouge est désormais officiellement initialisée conformément au cahier des charges de l'AMA.

Voici les informations clés et les actions attendues de chacun pour cette semaine :

---

### 1️⃣ Dépôt GitHub & Accès
* **Lien du dépôt :** `https://github.com/bkablam11/paraspeech-africa`
* 👉 **Action obligatoire :** Vérifiez vos boîtes mail (invitation GitHub) et **acceptez l'invitation** pour avoir vos droits d'accès en écriture.

---

### 2️⃣ Protocole Git & Environnement de travail
Pour éviter les conflits et garantir la note d'évaluation Git (10%), **interdiction formelle de committer directement sur `main`**.

💻 **En local (sur votre machine) :**
```bash
# 1. Cloner le projet
git clone https://github.com/bkablam11/paraspeech-africa.git
cd paraspeech-africa

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Créer votre propre branche de travail
git checkout -b dev-[votre-prenom]
```

☁️ **Dans Google Colab (calcul GPU) :**
Dans la première cellule de votre notebook :
```python
# 1. Cloner le projet dans Colab
!git clone https://github.com/bkablam11/paraspeech-africa.git
%cd paraspeech-africa

# 2. Installer les packages du projet
!pip install -r requirements.txt -q
```
*(⚠️ Rappel : ne committez aucun fichier audio lourd `.mp4` ou `.wav` sur Git, le `.gitignore` est déjà configuré).*

---

### 3️⃣ Collecte des Données Pilotes (Français ⟷ Fongbe)
**Responsables :** Richnel & l'ensemble de l'équipe.  
**Objectif :** Trouver et partager **2 à 3 vidéos YouTube de référence**.

**Critères de sélection obligatoires :**
1. **Durée :** Courte (entre **5 et 15 minutes**).
2. **Structure de parole :** Interprétation **consécutive stricte** (l'orateur parle en français pendant 5 à 15 secondes, s'arrête, puis l'interprète traduit en fongbe). Pas de traduction simultanée où les deux voix se chevauchent.
3. **Qualité acoustique :** Voix claires et intelligibles, idéalement **sans musique d'ambiance permanente** ni applaudissements continus.

🔍 *Mots-clés suggérés sur YouTube :*
* `"culte traduction fon cotonou"`
* `"prédication français fon"`
* `"discours bilingue fon bénin"`
* `"église apostolique cotonou français fon"`

---

### 4️⃣ Prochaine Réunion Hebdomadaire
🗓 **Mardi 13 octobre à 19h30 (GMT)**
* **Ordre du jour :**
  1. Validation des vidéos pilotes collectées.
  2. Extraction et conversion en audio normalisé $16\text{ kHz}$ mono.
  3. Visualisation du signal et premières mesures mathématiques ($E_{\text{RMS}}$, distribution d'amplitude, Zero Crossing Rate).

Merci à tous pour votre implication, on avance avec méthode ! 🚀



# COMPTE RENDU D'ÉTAPE : CLÔTURE DES PHASES 0 \& 1
**Projet :** ParaSpeech Africa – PIIA Cohorte 2 (Machine Learning)  
**Institution :** Académie des Mathématiques Appliquées (AMA), Cotonou, Bénin  
**Équipe :** Edjabrou Ulrich Blanchard KABLAM (Lead), Richnel EGUE, Ghilth GBAGUIDI, Wilfried BONOU  
🗓 **Mardi 13 et 20 octobre à 20h-21h (GMT)**

---

## 1. Cadre Stratégique \& Décisions Initiales (Phase 0)

1. **Binôme linguistique validé :** **Français $\longleftrightarrow$ Fongbe (Fon)**.
   * *Justification :* Langue nationale béninoise prioritaire inscrite dans la stratégie nationale d'IA (SNIAM 2023–2027) et le projet public *JaimeMaLangue*, forte présence de locuteurs au sein de l'équipe et disponibilité de captations avec interprétation consécutive.
2. **Architecture collaborative d'ingénierie :**
   * **GitHub (`paraspeech-africa`) :** Source unique de vérité pour le code source (`src/`), les tests et la documentation.
   * **Environnement local (VS Code / macOS) :** Écriture modulaire, prétraitement et validation immédiate.
   * **Google Colab (Nvidia CUDA) :** Réservé pour les phases ultérieures de calcul lourd (embeddings, inférence ML/DL).
   * **Gestion des données :** Règle stricte via `.gitignore` excluant les fichiers médias volumineux (`.mp4`, `.wav`) du dépôt distant pour ne pas saturer Git.

---

## 2. Infrastructure \& Résolution des Verrous Système

Plusieurs blocages d'infrastructure logicielle ont été diagnostiqués et résolus avec rigueur :

* **Incompatibilité Python 3.14 sur Mac Intel (x86_64) :**  
  * *Problème :* L'installation de `librosa` échouait car `llvmlite 0.50.0` n'avait pas de binaires précompilés pour Python 3.14 sur architecture Intel, réclamant un compilateur `cmake` absent.
  * *Solution :* Création d'un environnement virtuel isolé sous **Python 3.11 stable** via l'outil `uv`, garantissant des packages précompilés et une installation instantanée sans dépendance de compilation.
* **Intégration d'un moteur FFmpeg autonome :**  
  * *Problème :* L'installation système de FFmpeg via Homebrew a été bloquée en configuration *Tier 3*.
  * *Solution :* Intégration du package `imageio-ffmpeg` encapsulant un binaire statique portable directement pilotable en Python sans dépendance externe au système d'exploitation.

---

## 3. Constitution du Corpus Pilote \& Normalisation Acoustique

Deux vidéos aux caractéristiques acoustiques volontairement contrastées ont été acquises et converties selon la norme de laboratoire vocal (**16 000 Hz, mono, PCM 16-bit**) :

1. **`VID001` — Cas Studio / Apprentissage (`FR_FON_LEARN_2021_VID001.wav`) :**
   * *Durée :* 486,61 s (~8 min 06 s).
   * *Profil :* Signal étalon (*Gold Baseline*) à fort rapport signal/bruit ($\text{SNR}$), absence de réverbération, phrases courtes alternées avec sous-titres visuels.
2. **`VID002` — Cas Réel de Terrain / Culte Godomey (`FR_FON_RELIGION_2020_VID002.wav`) :**
   * *Durée :* 99,37 s (~1 min 40 s).
   * *Profil :* Prédication en direct dans un temple avec sonorisation de salle, écho, bruits d'ambiance et réactions de l'assemblée.

Les métadonnées initiales de ces flux ont été automatisées dans `data/annotations/metadata_raw.csv`.

---

## 4. Analyse Mathématique \& Métrologie du Signal (Phase 1)

Le calcul des descripteurs physiques fondamentaux du signal via `src/features/audio_features.py` a mis en lumière les propriétés suivantes :

$$\bar{x} = \frac{1}{N}\sum x_i, \quad \operatorname{Var}(X) = \frac{1}{N}\sum (x_i - \bar{x})^2, \quad \operatorname{RMS} = \sqrt{\frac{1}{N}\sum x_i^2}$$

### Tableau comparatif des deux environnements :

| Grandeur physique | Studio (`VID001`) | Terrain Église (`VID002`) | Constat scientifique |
| :--- | :---: | :---: | :--- |
| **Moyenne $\bar{x}$ (Offset DC)** | $\approx -8{,}34 \times 10^{-8}$ | $\approx -1{,}20 \times 10^{-7}$ | Centrage parfait autour de zéro (absence de composante continue parasite). |
| **Énergie RMS globale** | **$0{,}0529$** | **$0{,}1069$** | Puissance sonore **deux fois plus élevée** dans l'église (gain micro et sono de salle). |
| **ZCR moyen (Passage par zéro)** | **$0{,}0838$** | **$0{,}1221$** | **+45 % de passages par zéro** dans l'église : signature physique directe de la réverbération et du bruit de fond. |

---

## 5. Détection d'Activité Vocale (VAD) \& Segmentation

L'étape de découpage automatique a fait l'objet d'une analyse d'erreurs et d'une amélioration algorithmique majeure :

1. **Échec de l'approche naïve par percentile (25 %) :**  
   * Produisait des segments parasites sur de simples bruits de fond respiratoires ($\text{RMS} = 0{,}0018$).
   * Générait une sous-segmentation critique avec un segment artificiel de $44{,}06\text{ s}$ sur `VID001`.
2. **Implémentation d'un seuillage dynamique en décibels relatifs (Top-dB) :**  
   * Algorithme évaluant l'énergie court-terme sur fenêtres de $25\text{ ms}$ avec pas de $10\text{ ms}$, seuillant à $\gamma_{\text{dB}}$ sous le pic RMS ($26\,\text{dB}$ en studio, $15\,\text{dB}$ en église).
   * **Résultat sur `VID001` :** **127 segments vocaux unitaires nets** extraits ($\approx 1{,}12\text{ s}$ par réplique, $\text{RMS} \ge 0{,}07$, élimination totale des silences).
   * **Résultat sur `VID002` :** **5 segments de discours complets** extraits ($\approx 18\text{ s}$ par tour de parole, correspondant exactement au temps d'expression naturelle du prédicateur et de l'interprète).
3. **Sérialisation :** Tous les segments ont été exportés sous forme de fichiers audio `.wav` autonomes dans `data/processed/segments/VID001/` et `VID002/`.

---

## 6. Intégration Stratégique du Corpus `ffr-v1` (Bonaventure Dossou)

Le corpus textuel de référence `ffr-v1` (117 000 phrases parallèles Français–Fongbe) a été forké et cadré pour servir :
1. De **calibration empirique du ratio de durée** $D(S_i, T_j)$ pour notre baseline mathématique ($\mu_r \approx 1{,}1$, $\sigma_r \approx 0{,}3$).
2. De **vérité terrain linguistique** pour la gestion stricte de l'orthographe tonale et des caractères spéciaux du Fongbe ($\varepsilon, \rho,$ \text{\reflectbox{r}}).
3. De dictionnaire de validation pour la future interface d'annotation humaine **ParaSpeech Studio**.

---

## 7. Livrables Scientifiques Produits

À ce stade du projet, l'ensemble des supports documentaires formels sont prêts :
* **Code source versionné :** Scripts modulaires `download_audio.py`, `segmentation.py`, `audio_features.py` et pipeline d'orchestration `run_pipeline_v1.py`.
* **Rapport scientifique en LaTeX (`docs/latex/rapport_phase0_phase1.tex`) :** Document de 4 pages à deux colonnes rédigé selon le template officiel de l'AMA.
* **Support de soutenance Beamer (`docs/latex/presentation_phase0_phase1.tex`) :** Présentation de 8 diapositives au format 16:9 avec charte graphique AMA, calibrée pour un pitch oral de 5 minutes.

---

## 8. Bilan \& Prochaine Étape : Phase 2 (Novembre 2026)

| Phase | Statut | Commentaire |
| :--- | :---: | :--- |
| **Phase 0 (Lancement \& Données pilotes)** | **100 % Validée** | Environnement, ingestion, métadonnées, convention de nommage opérationnels. |
| **Phase 1 (Signal \& Segmentation V1)** | **100 % Validée** | Statistiques calculées, VAD adaptatif validé, 127 + 5 segments découpés. |
| **Phase 2 (Machine Learning supervisé)** | **À démarrer** | Formulation des paires candidates $(S_i, T_j)$ et baseline explicable. |

### Feuille de route immédiate pour la Phase 2 :
1. **Génération des paires candidates $(S_i, T_j)$** par fenêtre glissante causale ($t_{\text{start}}(T_j) > t_{\text{end}}(S_i)$).
2. **Implémentation de la baseline mathématique explicable :**
   $$\operatorname{Score}(S_i, T_j) = w_1 T(i, j) + w_2 D(i, j) + w_3 P(i, j) + w_4 A(i, j)$$
3. **Entraînement des classificateurs supervisés sous Scikit-learn** (Régression logistique, SVM, Random Forest).