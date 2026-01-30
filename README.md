

# Face Blurring Tool

Un outil Python simple et efficace pour flouter automatiquement les visages dans des images, vidéos ou en temps réel via webcam, utilisant MediaPipe pour la détection faciale.

## 📋 Fonctionnalités

- **Mode Image** : Floute les visages dans une image statique
- **Mode Vidéo** : Traite une vidéo complète et floute tous les visages détectés
- **Mode Webcam** : Floute les visages en temps réel depuis votre webcam

## 🛠️ Prérequis

- Python 3.7+
- OpenCV
- MediaPipe

## 📦 Installation

1. Clonez ou téléchargez ce repository

2. Installez les dépendances requises :
```bash
pip install opencv-python mediapipe
```

## 🚀 Utilisation

### Mode Webcam (par défaut)
```bash
python face_blur.py --mode webcam
```

Appuyez sur `ESC` pour quitter.

### Mode Image
```bash
python face_blur.py --mode image --filePath chemin/vers/image.jpg
```

L'image traitée sera sauvegardée dans `./output/output.png`

### Mode Vidéo
```bash
python face_blur.py --mode video --filePath chemin/vers/video.mp4
```

La vidéo traitée sera sauvegardée dans `./output/output.mp4`

## ⚙️ Arguments

| Argument | Type | Défaut | Description |
|----------|------|--------|-------------|
| `--mode` | str | `webcam` | Mode d'exécution : `webcam`, `image`, ou `video` |
| `--filePath` | str | `None` | Chemin vers le fichier image ou vidéo (requis pour modes image/vidéo) |

## 📁 Structure du projet
```
.
├── face_blur.py          # Script principal
├── README.md             # Documentation
└── output/               # Dossier de sortie (créé automatiquement)
    ├── output.png        # Image traitée
    └── output.mp4        # Vidéo traitée
```

## 🔧 Paramètres de détection

Le script utilise MediaPipe Face Detection avec les paramètres suivants :
- **model_selection** : 0 (modèle optimisé pour courte distance, < 2 mètres)
- **min_detection_confidence** : 0.5 (seuil de confiance minimum pour la détection)

Vous pouvez ajuster ces paramètres dans le code selon vos besoins.

## 📝 Exemples
```bash
# Flouter les visages dans une photo de groupe
python face_blur.py --mode image --filePath photos/groupe.jpg

# Flouter les visages dans une vidéo de surveillance
python face_blur.py --mode video --filePath videos/surveillance.mp4

# Utilisation en temps réel
python face_blur.py --mode webcam
```

## 🔄 Comment ça marche

1. **Détection des visages** : MediaPipe détecte les visages dans l'image/frame
2. **Extraction des coordonnées** : Les bounding boxes des visages sont récupérées
3. **Application du flou** : Un flou gaussien (30x30) est appliqué sur chaque visage détecté
4. **Sauvegarde** : Le résultat est affiché (webcam) ou sauvegardé (image/vidéo)

## ⚙️ Personnalisation

### Modifier l'intensité du flou

Dans la fonction `process_img()`, changez les valeurs `(30, 30)` :
```python
img[y1:y1 + h, x1:x1 + w, :] = cv2.blur(img[y1:y1 + h, x1:x1 + w, :], (50, 50))
```

### Changer le modèle de détection
```python
# model_selection=0 : courte distance (< 2m)
# model_selection=1 : longue distance (> 2m)
with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
```

### Ajuster la confiance de détection
```python
# Valeur entre 0.0 et 1.0
# Plus élevé = moins de faux positifs, mais peut manquer des visages
min_detection_confidence=0.7
```

## ⚠️ Notes importantes

- Le flou par défaut est de 30x30 pixels
- Les vidéos en sortie utilisent le codec MP4V avec 25 FPS
- Le dossier `output/` est créé automatiquement
- Les fichiers de sortie écrasent les fichiers précédents

## 🐛 Résolution de problèmes

### "Cannot open webcam"
- Vérifiez que votre webcam est connectée
- Essayez de changer `cv2.VideoCapture(0)` en `cv2.VideoCapture(1)`

### "Failed to read video"
- Vérifiez que le chemin du fichier est correct
- Assurez-vous que le format vidéo est supporté (mp4, avi, mov, etc.)

### Performances lentes
- Réduisez la résolution de la vidéo/webcam
- Utilisez `model_selection=0` pour de meilleures performances

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer de nouvelles fonctionnalités
- Améliorer la documentation

## 📄 Licence

Ce projet est libre d'utilisation pour des fins éducatives et personnelles.

## 🙏 Remerciements

- [MediaPipe](https://google.github.io/mediapipe/) pour la détection faciale
- [OpenCV](https://opencv.org/) pour le traitement d'image

---

**Note de confidentialité** : Cet outil est conçu pour protéger la vie privée en floutant les visages. Assurez-vous d'avoir les permissions nécessaires avant de traiter des images/vidéos de personnes.
