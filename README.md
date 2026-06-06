# Speech Anonymization & Depression Biomarkers

## 📖 Project Description 

This project investigates the impact of speech anonymization algorithms on the preservation of depression-related acoustic biomarkers.

Specifically, it examines whether acoustic features known to be associated with depression can still be detected after applying state-of-the-art voice anonymization techniques.

## 📊 Dataset

This project uses the **DAIC-WOZ dataset** (Gratch et al., 2014), a sub-corpus of the Distress Analysis Interview Corpus (DAIC) containing 189 semi-structured clinical interviews.

Participants are labelled as depressed or non-depressed based on their score on the Patient Health Questionnaire (**PHQ-8**), using a threshold of **PHQ-8 ≥ 10**.

Three anonymized versions of the dataset were generated using the **B3, B4, and B5 baseline systems** from the VoicePrivacy 2024 Challenge (Tomashenko et al., 2024), each offering a different level of privacy protection.

## 🎵 Acoustic Features

Acoustic features were extracted using the **eGeMAPS feature set** (Eyben et al., 2015), consisting of 88 functional parameters covering:

* Frequency-related features (F0, jitter, formants)
* Energy and amplitude-related features (loudness, shimmer, HNR)
* Spectral features (Alpha Ratio, Hammarberg Index, MFCCs)
* Temporal features (speech rate, pause patterns)
* Equivalent sound level

Feature extraction was performed using **openSMILE** (Eyben et al., 2010).

## 📂 Repository Structure

```text
speech-anonymization-biomarkers-depression/
│
├── README.md
├── carbon_footprint_tracker.py
└── features_extraction/
    ├── extract_egemaps_features.py
    └── add_id_speaker_egemaps.py
```

### 👩‍💻 Description of the scripts

* `extract_egemaps_features.py`: eGeMAPS feature extraction.
* `add_id_speaker_egemaps.py`: Add Speaker ID for the .csv eGeMAPS feature extraction file.
* `carbon_footprint_tracker.py`: Carbon footprint estimation using CodeCarbon.

## 🌱 Carbon Footprint

The carbon footprint of each computational step was estimated using **CodeCarbon** (Courty et al., 2023).

## 📚 References

* Gratch et al. (2014). *The Distress Analysis Interview Corpus*. LREC.
* Eyben et al. (2015). *The Geneva Minimalistic Acoustic Parameter Set*. IEEE Transactions on Affective Computing.
* Eyben et al. (2010). *openSMILE*. ACM Multimedia.
* Tomashenko et al. (2024). *VoicePrivacy 2024 Challenge*. Interspeech.
* Lottick et al. (2019). Energy usage reports: Environmental awareness as part of algorithmic accountability. NeurIPS.

## 👥 Authors

Master's students in Natural Language Processing (NLP) at the IDMC (Institut des Sciences du Digital, Managment & Cognition).
