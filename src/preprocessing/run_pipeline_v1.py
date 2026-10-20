"""
Pipeline V1 unifié : Ingestion -> Normalisation -> Analyse -> VAD -> Découpage
Traite l'ensemble des vidéos du corpus pilote (VID001 et VID002).
"""
import os
import sys
import glob
from pathlib import Path
import numpy as np
import soundfile as sf
import pandas as pd

# Ajoute la racine du projet au chemin Python
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.features.audio_features import compute_audio_stats, plot_waveform_and_energy
from src.preprocessing.segmentation import segment_audio_file

os.makedirs("docs/figures", exist_ok=True)
os.makedirs("data/processed/segments", exist_ok=True)

wav_files = sorted(glob.glob("data/processed/*.wav"))

print("="*65)
print("🚀 CLÔTURE PHASES 0 & 1 : TRAITEMENT DE TOUTES LES VIDÉOS PILOTES")
print("="*65)

summary = []

for wav_path in wav_files:
    filename = os.path.basename(wav_path)
    vid_id = "VID001" if "VID001" in filename else "VID002"
    out_dir = f"data/processed/segments/{vid_id}"
    out_csv = f"data/processed/segments_{vid_id}.csv"
    
    # 1. Analyse physique globale du signal
    data, sr = sf.read(wav_path)
    stats = compute_audio_stats(data, sr)
    
    # 2. Génération de la figure d'énergie
    fig_path = f"docs/figures/waveform_{vid_id}.png"
    plot_waveform_and_energy(wav_path, output_img=fig_path, duration_max=35.0)
    
    # 3. Segmentation VAD robuste (top-db ajusté selon le domaine)
    top_db = 26.0 if vid_id == "VID001" else 15.0
    min_silence = 300.0 if vid_id == "VID001" else 200.0 # Seuil plus strict pour l'église bruyante
    df_seg = segment_audio_file(
        wav_path, 
        out_dir, 
        top_db=top_db, 
        min_speech_ms=500.0, 
        min_silence_ms=min_silence
    )
    df_seg.to_csv(out_csv, index=False)
    
    summary.append({
        "video": vid_id,
        "duree_totale_s": stats["duration_sec"],
        "rms_global": round(stats["rms"], 4),
        "zcr_moyen": round(stats["zcr"], 4),
        "nb_segments": len(df_seg),
        "duree_moy_seg_s": round(df_seg["duration_sec"].mean(), 2)
    })
    print(f"✅ {vid_id} traité : {len(df_seg)} segments extraits dans {out_dir}")

df_summary = pd.DataFrame(summary)
df_summary.to_csv("data/annotations/synthese_phase1.csv", index=False)
print("\n📊 SYNTHÈSE DES DEUX CAS D'USAGE :")
print(df_summary.to_string(index=False))