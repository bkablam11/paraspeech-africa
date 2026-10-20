"""
Module de segmentation audio robuste (VAD par seuillage d'énergie adaptatif).
Phase 1 - ParaSpeech Africa.
"""
import os
import numpy as np
import soundfile as sf
import pandas as pd


def segment_audio_file(
    wav_path: str,
    output_dir: str,
    top_db: float = 28.0,
    min_speech_ms: float = 600.0,
    min_silence_ms: float = 250.0,
    frame_ms: float = 25.0,
    hop_ms: float = 10.0
):
    """
    Découpe un fichier audio en segments de parole réels et exporte les fichiers .wav individuels.
    - top_db : seuil sous le pic d'énergie (en dB). 28-30 dB filtre parfaitement le souffle et les clics.
    """
    signal, sr = sf.read(wav_path)
    os.makedirs(output_dir, exist_ok=True)
    
    frame_len = int((frame_ms / 1000.0) * sr)
    hop_len = int((hop_ms / 1000.0) * sr)
    
    num_frames = 1 + int((len(signal) - frame_len) / hop_len)
    frames = np.lib.stride_tricks.as_strided(
        signal,
        shape=(num_frames, frame_len),
        strides=(signal.strides[0] * hop_len, signal.strides[0])
    )
    
    # 1. Énergie RMS par trame
    rms = np.sqrt(np.mean(frames**2, axis=1) + 1e-12)
    
    # 2. Seuil en dB relatif à l'énergie maximale
    peak_rms = np.max(rms)
    threshold_rms = peak_rms * (10 ** (-top_db / 20.0))
    
    is_speech = rms > threshold_rms
    min_speech_frames = int(min_speech_ms / hop_ms)
    min_silence_frames = int(min_silence_ms / hop_ms)
    
    segments = []
    in_speech = False
    start_frame = 0
    silence_counter = 0
    
    for i, active in enumerate(is_speech):
        if active:
            if not in_speech:
                in_speech = True
                start_frame = i
            silence_counter = 0
        else:
            if in_speech:
                silence_counter += 1
                if silence_counter >= min_silence_frames:
                    end_frame = i - silence_counter
                    if (end_frame - start_frame) >= min_speech_frames:
                        t_start = round(start_frame * (hop_ms / 1000.0), 3)
                        t_end = round(end_frame * (hop_ms / 1000.0), 3)
                        duration = round(t_end - t_start, 3)
                        
                        idx = len(segments) + 1
                        seg_name = f"seg_{idx:04d}.wav"
                        seg_filepath = os.path.join(output_dir, seg_name)
                        
                        seg_audio = signal[int(t_start * sr):int(t_end * sr)]
                        sf.write(seg_filepath, seg_audio, sr)
                        
                        seg_rms = float(np.sqrt(np.mean(seg_audio**2)))
                        seg_zcr = float(np.sum(np.abs(np.diff(np.sign(seg_audio)))) / (2 * len(seg_audio)))
                        
                        segments.append({
                            "segment_id": idx,
                            "audio_file": seg_name,
                            "t_start": t_start,
                            "t_end": t_end,
                            "duration_sec": duration,
                            "rms": round(seg_rms, 4),
                            "zcr": round(seg_zcr, 4)
                        })
                    in_speech = False
                    silence_counter = 0
                    
    return pd.DataFrame(segments)


if __name__ == "__main__":
    wav_file = "data/processed/FR_FON_LEARN_2021_VID001.wav"
    out_dir = "data/processed/segments/VID001"
    output_csv = "data/processed/segments_VID001.csv"
    
    print(f"✂️ Découpage propre et extraction des fichiers audio : {wav_file}...")
    df = segment_audio_file(wav_file, out_dir, top_db=26.0, min_speech_ms=500.0, min_silence_ms=350.0)
    
    df.to_csv(output_csv, index=False)
    print(f" {len(df)} vrais segments vocaux extraits dans : {out_dir}")
    print(df.head(10))