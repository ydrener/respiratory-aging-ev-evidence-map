# Respiratory aging–extracellular vesicle evidence map: public reproducibility package

This is the **SLIM public GitHub package** supporting figure-level reproducibility for the Ageing Research Reviews manuscript. It is derived from the validated master reproducibility archive, but intentionally excludes raw bibliographic exports, abstract text, the ASReview project database, SPECTER2 raw inputs/embeddings, journal Supplementary material, and internal QC/provenance archives.

## Scope

The repository reproduces and validates the manuscript-locked analysis outputs from public derived tables only:

- final included studies: **37**
- full-text outcomes: **37 included / 13 excluded / 1 report not retrieved**
- Figure 3: **14,366 / 12,913 / 1,453 / 767 / 52 / 12,146**
- residual audit: **Top 50 = 50; additional relevant = 0**
- Figure 5C: **6 criteria**
- causal cargo: **senescence-only 12/26; chronological-aging-only 2/9**

This SLIM repository is designed to reproduce the **locked counts and figure-level derived outputs**, not to redistribute database-derived bibliographic text or rerun SPECTER2/ASReview from proprietary/raw source records.

## Repository structure

```text
respiratory-aging-ev-evidence-map/
├── README.md
├── VALIDATION_REPORT.md
├── REPOSITORY_SHA256.tsv
├── requirements.txt
├── requirements-optional.txt
├── code/
│   ├── Figure1/
│   ├── Figure2/
│   ├── Figure3/
│   └── Figure5/
└── data/
    ├── Figure1/
    ├── Figure2/
    ├── Figure3/
    └── Figure5/
```

## Installation

```bash
python -m pip install -r requirements.txt
```

`requirements-optional.txt` contains only optional interactive tooling and is not required for validation.

## Execution

Run notebooks from anywhere inside the cloned repository; they resolve the repository root automatically and use repository-relative inputs only.

```bash
jupyter nbconvert --to notebook --execute code/Figure1/Figure1_CorpusConstruction_FrozenMapping_CLEAN.ipynb --output /tmp/F1_1.ipynb
jupyter nbconvert --to notebook --execute code/Figure1/Figure1_Deduplication_Rules_Reconstructed_REFERENCE.ipynb --output /tmp/F1_2.ipynb
jupyter nbconvert --to notebook --execute code/Figure1/Figure1_Selection_Reproducible_FINAL.ipynb --output /tmp/F1_3.ipynb
jupyter nbconvert --to notebook --execute code/Figure1/Figure1_TitleOnly_AbstractRecovery_RECONSTRUCTED_CLEAN.ipynb --output /tmp/F1_4.ipynb
jupyter nbconvert --to notebook --execute code/Figure1/Figure1_TitleOnly_SafetyLane_CLEAN.ipynb --output /tmp/F1_5.ipynb
jupyter nbconvert --to notebook --execute code/Figure2/Figure2_ASReview_Reproducible_CLEAN.ipynb --output /tmp/F2.ipynb
jupyter nbconvert --to notebook --execute code/Figure3/Figure3_SPECTER2_Reproducible_CLEAN.ipynb --output /tmp/F3.ipynb
python code/Figure5/Figure5C_EvidenceProfiles_FINAL.py
```

## Public-data design

Only derived analysis variables needed for reproducibility are included. Bibliographic titles, abstracts, DOI/PMID fields, author/journal fields, raw source database exports, `.asreview` files, SPECTER2 input/embedding archives, and journal Supplementary Tables/Appendices are deliberately excluded.

See `VALIDATION_REPORT.md` for the actual execution results used to validate this release.
