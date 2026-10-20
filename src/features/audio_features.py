"""
Module d'extraction des caractéristiques physiques et statistiques du signal audio.
Conforme au programme PIIA - Cohorte 2 (AMA) - Phase 1.
"""
import os
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt


def compute_audio_stats(signal: np.ndarray, sr: int):
    """
    Calcule les indicateurs mathématiques fondamentaux sur l'ensemble du signal :
    - Moyenne temporelle (x_bar)
    - Variance du signal (Var(X))
    - Valeur efficace globale (RMS)
    - Taux de passage par zéro moyen (Zero Crossing Rate - ZCR)
    """
    mean_val = float(np.mean(signal))
    var_val = float(np.var(signal))
    rms_val = float(np.sqrt(np.mean(signal**2)))
    
    # Zero Crossing Rate : proportion de changements de signe par échantillon
    zero_crossings = np.sum(np.abs(np.diff(np.sign(signal)))) / (2 * len(signal))
    
    duration = len(signal) / sr
    
    return {
        "duration_sec": round(duration, 3),
        "mean": mean_val,
        "variance": var_val,
        "rms": rms_val,
        "zcr": float(zero_crossings)
    }


def compute_frame_energy(signal: np.ndarray, sr: int, frame_ms: float = 25.0, hop_ms: float = 10.0):
    """
    Calcule l'énergie RMS par fenêtre glissante (Short-Time Energy).
    - frame_length : 25 ms (fenêtre d'analyse standard de la parole)
    - hop_length : 10 ms (pas d'avancement)
    """
    frame_len = int((frame_ms / 1000.0) * sr)
    hop_len = int((hop_ms / 1000.0) * sr)
    
    # Découpage vectorisé en trames
    num_frames = 1 + int((len(signal) - frame_len) / hop_len)
    frames = np.lib.stride_tricks.as_strided(
        signal,
        shape=(num_frames, frame_len),
        strides=(signal.strides[0] * hop_len, signal.strides[0])
    )
    
    # Calcul de la RMS par trame
    rms_frames = np.sqrt(np.mean(frames**2, axis=1))
    times = np.arange(num_frames) * (hop_ms / 1000.0)
    
    return times, rms_frames


def plot_waveform_and_energy(wav_path: str, output_img: str = None, duration_max: float = 30.0):
    """
    Trace la forme d'onde et l'enveloppe d'énergie RMS sur les 'duration_max' premières secondes
    pour visualiser les alternances orateur <-> interprète et les silences.
    """
    data, sr = sf.read(wav_path)
    
    # Si le fichier dépasse duration_max, on tronque pour la visualisation
    max_samples = int(duration_max * sr)
    segment = data[:max_samples]
    t_wave = np.linspace(0, len(segment) / sr, len(segment))
    
    times_rms, rms_frames = compute_frame_energy(segment, sr)
    
    # Seuil empirique de silence (15% de l'énergie moyenne de la parole)
    silence_threshold = np.mean(rms_frames) * 0.25
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 7), sharex=True)
    
    # 1. Waveform (Amplitude brute)
    ax1.plot(t_wave, segment, color="#2b5c8f", lw=0.6, alpha=0.8)
    ax1.set_title(f"Forme d'onde (Waveform) - {os.path.basename(wav_path)} (0 - {duration_max}s)", fontsize=12, fontweight='bold')
    ax1.set_ylabel("Amplitude")
    ax1.grid(True, linestyle="--", alpha=0.5)
    
    # 2. Énergie RMS court-terme
    ax2.plot(times_rms, rms_frames, color="#c93b2b", lw=1.5, label="RMS (fenêtre 25ms)")
    ax2.axhline(silence_threshold, color="#2ca02c", linestyle=":", lw=2, label=f"Seuil de silence ({silence_threshold:.4f})")
    ax2.set_title("Énergie Court-Terme (RMS) & Détection des Silences", fontsize=12, fontweight='bold')
    ax2.set_xlabel("Temps (secondes)", fontsize=11)
    ax2.set_ylabel("Énergie RMS")
    ax2.legend(loc="upper right")
    ax2.grid(True, linestyle="--", alpha=0.5)
    
    plt.tight_layout()
    
    if output_img:
        plt.savefig(output_img, dpi=150)
        print(f"📊 Graphique sauvegardé sous : {output_img}")
    else:
        plt.show()


if __name__ == "__main__":
    wav_file = "data/processed/FR_FON_LEARN_2021_VID001.wav"
    
    if os.path.exists(wav_file):
        data, sr = sf.read(wav_file)
        stats = compute_audio_stats(data, sr)
        print("\n📈 Grandeurs statistiques fondamentales du signal :")
        for k, v in stats.items():
            print(f"  • {k:15s}: {v}")
        
        # Générer et afficher la figure
        os.makedirs("docs/figures", exist_ok=True)
        plot_waveform_and_energy(
            wav_file,
            output_img="docs/figures/waveform_energy_VID001.png",
            duration_max=35.0
        )
    else:
        print(f"Fichier introuvable : {wav_file}")