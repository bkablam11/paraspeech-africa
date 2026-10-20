import os
import subprocess
import pandas as pd
import soundfile as sf
import imageio_ffmpeg

# Obtenir le chemin absolu vers le binaire FFmpeg autonome
FFMPEG_BIN = imageio_ffmpeg.get_ffmpeg_exe()
print(f"🔧 Utilisation du binaire FFmpeg : {FFMPEG_BIN}")

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
ANNOTATIONS_DIR = "data/annotations"

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)
os.makedirs(ANNOTATIONS_DIR, exist_ok=True)

PILOT_VIDEOS = [
    {
        "id": "VID001",
        "url": "https://www.youtube.com/watch?v=nlD2t9IHQa0",
        "lang_pair": "FR_FON",
        "domain": "LEARN",
        "year": "2021",
        "filename": "FR_FON_LEARN_2021_VID001"
    },
    {
        "id": "VID002",
        "url": "https://www.youtube.com/watch?v=B9UGheA6thk",
        "lang_pair": "FR_FON",
        "domain": "RELIGION",
        "year": "2020",
        "filename": "FR_FON_RELIGION_2020_VID002"
    }
]

metadata_records = []

for vid in PILOT_VIDEOS:
    raw_audio_path = os.path.join(RAW_DIR, f"{vid['filename']}.m4a")
    processed_wav_path = os.path.join(PROCESSED_DIR, f"{vid['filename']}.wav")
    
    # Si le fichier brut n'existe pas encore, le télécharger
    if not os.path.exists(raw_audio_path):
        print(f"\n📥 1. Téléchargement : {vid['filename']}...")
        cmd_dl = [
            "yt-dlp",
            "-f", "ba",
            "-o", raw_audio_path,
            vid["url"]
        ]
        subprocess.run(cmd_dl, check=True)
    else:
        print(f"\n Audio brut déjà téléchargé : {raw_audio_path}")
    
    print(f"🔄 2. Conversion FFmpeg vers 16 kHz Mono PCM : {processed_wav_path}...")
    cmd_ffmpeg = [
        FFMPEG_BIN, "-y",
        "-i", raw_audio_path,
        "-ar", "16000",
        "-ac", "1",
        "-c:a", "pcm_s16le",
        processed_wav_path
    ]
    subprocess.run(cmd_ffmpeg, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    # 3. Mesures physiques élémentaires (Phase 0)
    info = sf.info(processed_wav_path)
    metadata_records.append({
        "video_id": vid["id"],
        "filename": f"{vid['filename']}.wav",
        "url": vid["url"],
        "lang_pair": vid["lang_pair"],
        "domain": vid["domain"],
        "duration_seconds": round(info.duration, 2),
        "sample_rate": info.samplerate,
        "channels": info.channels,
        "format": info.format
    })

csv_path = os.path.join(ANNOTATIONS_DIR, "metadata_raw.csv")
df_meta = pd.DataFrame(metadata_records)
df_meta.to_csv(csv_path, index=False)

print("\n Ingestion & Conversion terminées avec succès !")
print(df_meta[["video_id", "filename", "duration_seconds", "sample_rate", "channels"]])