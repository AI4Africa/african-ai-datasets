# 🌍 Awesome African AI Datasets

A **curated, community-maintained** list of **free and open datasets** for Artificial Intelligence and Machine Learning projects **focused on Africa**.  

Datasets are tagged by **domain**, have Kaggle-style metadata, and are verified to be truly free for research or commercial use (license permitting).  

✅ **Always check individual dataset licenses before use.**  

---

## 📂 Table of Contents
- [Natural Language Processing (NLP)](#-natural-language-processing-nlp)
- [Speech / Voice](#-speech--voice)
- [Computer Vision & Wildlife](#-computer-vision--wildlife)
- [Geospatial & Agriculture](#-geospatial--agriculture)
- [Climate & Weather](#-climate--weather)
- [Contribution Guide](#-contribution-guide)

---

## 🗣 Natural Language Processing (NLP)

### MasakhaNER
![Domain](https://img.shields.io/badge/Domain-NLP-blue) ![License](https://img.shields.io/badge/License-Mixed-lightgrey) ![Year](https://img.shields.io/badge/Year-2021-orange)
- **Description**: Named Entity Recognition datasets for multiple African languages.
- **Languages**: Yoruba, Hausa, Igbo, Swahili, Amharic, Wolof, Kinyarwanda, and more.
- **Size**: ~20K annotated sentences.
- **Samples**: Named entities tagged in context.
- **Tasks**: NER model training, evaluation, transfer learning.
- **Source**: Masakhane Project.
- **Link**: [https://github.com/masakhane-io/masakhaner](https://github.com/masakhane-io/masakhaner)
- **License**: Mixed permissive licenses (check per language).
- **Last Updated**: 2021-05
- **Best For**: Low-resource NLP research, multilingual NER.

---

### MasakhaPOS
![Domain](https://img.shields.io/badge/Domain-NLP-blue) ![License](https://img.shields.io/badge/License-CC%20BY--SA%204.0-green) ![Year](https://img.shields.io/badge/Year-2020-orange)
- **Description**: POS-tagged datasets for African languages.
- **Languages**: Yoruba, Hausa, Igbo, Swahili, Wolof, etc.
- **Size**: ~10K sentences across languages.
- **Samples**: Tokenized and tagged sentences.
- **Tasks**: POS tagging model development.
- **Source**: Masakhane Project.
- **Link**: [https://github.com/masakhane-io/masakhapos](https://github.com/masakhane-io/masakhapos)
- **License**: CC BY-SA 4.0.
- **Last Updated**: 2020-11
- **Best For**: Linguistic modeling & POS benchmarking.

---

## 🎙 Speech / Voice

### Mozilla Common Voice — African Languages
![Domain](https://img.shields.io/badge/Domain-Speech-red) ![License](https://img.shields.io/badge/License-CC0-green) ![Year](https://img.shields.io/badge/Year-2024-orange)
- **Description**: Crowdsourced speech recordings in African languages.
- **Languages**: Swahili, Chichewa, Amharic, Luganda, Kinyarwanda, and more.
- **Size**: Varies (up to 100+ hours per language).
- **Samples**: Audio clips + transcriptions.
- **Tasks**: ASR, TTS, keyword spotting.
- **Source**: Mozilla Foundation.
- **Link**: [https://commonvoice.mozilla.org/en/datasets](https://commonvoice.mozilla.org/en/datasets)
- **License**: CC0 (Public Domain).
- **Last Updated**: 2024-06
- **Best For**: Speech recognition & synthesis in low-resource languages.

---

### OpenSLR African Language Speech Corpora
![Domain](https://img.shields.io/badge/Domain-Speech-red) ![License](https://img.shields.io/badge/License-Varies-lightgrey) ![Year](https://img.shields.io/badge/Year-2023-orange)
- **Description**: Speech corpora for Yoruba, Igbo, Hausa, and others.
- **Languages**: Multiple African languages.
- **Size**: Ranges from 5–50 hours per dataset.
- **Samples**: Audio recordings + transcripts.
- **Tasks**: ASR model training.
- **Source**: OpenSLR.org.
- **Link**: [http://openslr.org](http://openslr.org)
- **License**: Mostly research use (check individual set).
- **Last Updated**: 2023-12
- **Best For**: End-to-end speech recognition.

---

## 📸 Computer Vision & Wildlife

### Snapshot Serengeti (LILA)
![Domain](https://img.shields.io/badge/Domain-Computer%20Vision-purple) ![License](https://img.shields.io/badge/License-Open-green) ![Year](https://img.shields.io/badge/Year-2019-orange)
- **Description**: Camera trap images of wildlife in Serengeti National Park, Tanzania.
- **Geography**: Serengeti, Tanzania.
- **Size**: ~3.2 million images.
- **Samples**: Labeled species, time, and location.
- **Tasks**: Object detection, species recognition.
- **Source**: LILA Science.
- **Link**: [http://lila.science/datasets/snapshot-serengeti](http://lila.science/datasets/snapshot-serengeti)
- **License**: Open for research use.
- **Last Updated**: 2019-08
- **Best For**: Wildlife monitoring, ecological research.

---

## 🛰 Geospatial & Agriculture

### Radiant Earth MLHub — African Crop / Land Cover Datasets
![Domain](https://img.shields.io/badge/Domain-Geospatial-green) ![License](https://img.shields.io/badge/License-CC%20BY%204.0-green) ![Year](https://img.shields.io/badge/Year-2024-orange)
- **Description**: Satellite imagery datasets for African agriculture and land cover mapping.
- **Geography**: Multiple African countries.
- **Size**: Varies (GBs of imagery).
- **Samples**: Multispectral and labeled crop types.
- **Tasks**: Land cover classification, yield prediction.
- **Source**: Radiant Earth Foundation.
- **Link**: [https://mlhub.earth](https://mlhub.earth)
- **License**: CC BY 4.0 or similar.
- **Last Updated**: 2024-03
- **Best For**: Agriculture & environmental monitoring.

---

## 🌦 Climate & Weather

### CHIRPS — Climate Hazards Group InfraRed Precipitation with Station Data
![Domain](https://img.shields.io/badge/Domain-Climate-blueviolet) ![License](https://img.shields.io/badge/License-Free-green) ![Year](https://img.shields.io/badge/Year-2023-orange)
- **Description**: High-resolution precipitation dataset.
- **Geography**: Global, with detailed African coverage.
- **Size**: 0.05° resolution daily data from 1981–present.
- **Samples**: Gridded precipitation values.
- **Tasks**: Drought monitoring, climate modeling.
- **Source**: UC Santa Barbara CHC.
- **Link**: [https://www.chc.ucsb.edu/data/chirps](https://www.chc.ucsb.edu/data/chirps)
- **License**: Free for research & non-commercial use.
- **Last Updated**: 2023-12
- **Best For**: Climate research, hydrology.

---

## 🤝 Contribution Guide

We welcome **pull requests** to add, update, or improve dataset entries.

**Steps:**
1. **Fork** this repository.
2. Add your dataset entry in the correct section using the template below.

### Dataset Entry Template
```markdown
### Dataset Name
![Domain](https://img.shields.io/badge/Domain-DOMAINCOLOR) ![License](https://img.shields.io/badge/License-LICENSETYPE-green) ![Year](https://img.shields.io/badge/Year-YYYY-orange)
- **Description**: Short description of the dataset.
- **Languages / Geography**: List languages or regions covered.
- **Size**: Approximate size in MB/GB or number of samples.
- **Samples**: Brief description of sample type.
- **Tasks**: List AI/ML tasks supported.
- **Source**: Organization or project name.
- **Link**: [Dataset link](https://example.com)
- **License**: License type.
- **Last Updated**: YYYY-MM.
- **Best For**: Suggested research/application areas.
