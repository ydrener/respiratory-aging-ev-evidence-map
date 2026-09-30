# Respiratory aging–extracellular vesicle evidence map: reproducibility repository

This repository provides the code and derived data supporting the manuscript:

**“Cellular Senescence and Chronological Aging in Respiratory Extracellular Vesicle Biology: Mapping the Mechanistic Gap”**

prepared for submission to *Ageing Research Reviews*.

The repository supports reproducibility of the manuscript-level counts and figure-level analytical outputs using public derived data. Raw bibliographic exports, abstract text, the ASReview project database, SPECTER2 raw inputs/embeddings, journal Supplementary material, and internal QC/provenance archives are intentionally excluded.

## Scope

The repository reproduces and validates the manuscript-locked analysis outputs:

- final included studies: **37**
- full-text outcomes: **37 included / 13 excluded / 1 report not retrieved**
- Figure 3: **14,366 / 12,913 / 1,453 / 767 / 52 / 12,146**
- residual audit: **Top 50 = 50; additional relevant = 0**
- Figure 5C: **6 criteria**
- causal cargo: **senescence-only 12/26; chronological-aging-only 2/9**

The repository is designed to reproduce the locked counts and figure-level derived outputs. It does not rerun database retrieval, ASReview active learning, abstract-recovery APIs, SPECTER2 encoding, or embedding generation from the original bibliographic records.

## Repository structure

```text
respiratory-aging-ev-evidence-map/
├── README.md
├── VALIDATION_REPORT.md
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

Figure-level reproducibility
Figure 1 — Study identification and selection
The Figure 1 notebooks validate the quantitative study-selection trail, including:
- database and deduplication counts
- 14,366-record deduplicated corpus
- title+abstract and title-only lanes
- title-only abstract-recovery and safety checks
- full-text outcomes
- duplicate-report consolidation
Figure 2 — ASReview screening dynamics
The Figure 2 notebook reconstructs the derived screening trajectory and validates:
- 765 human screening decisions
- 50 Relevant and 715 Not relevant decisions
- 2 positive seeds
- 767 total labeled records
- 52 records advanced as candidates
- terminal screening run after the final Relevant record
Figure 3 — Semantic mapping and residual audit
The Figure 3 notebook validates the derived data underlying:
- the 14,366-record semantic map
- six-cluster solution
- 52 candidate records
- 12,146-record residual pool
- Top-50 residual audit
- zero additional Relevant records
The public repository uses frozen derived variables rather than redistributing the original SPECTER2 embeddings or bibliographic source text.
Figure 5C — Evidence-profile comparison
The Figure 5C script reproduces the six evidence criteria comparing:
- chronological-aging-only studies (n = 9)
- senescence-only studies (n = 26)
Mixed studies are not included in this between-group comparison.

Installation
python -m pip install -r requirements.txt

requirements-optional.txt contains optional dependencies and is not required for the mandatory validation workflow.

Execution
The notebooks resolve the repository root automatically and use repository-relative inputs.
jupyter nbconvert --to notebook --execute code/Figure1/Figure1_CorpusConstruction_FrozenMapping_CLEAN.ipynb --output /tmp/F1_1.ipynb
jupyter nbconvert --to notebook --execute code/Figure1/Figure1_Deduplication_Rules_Reconstructed_REFERENCE.ipynb --output /tmp/F1_2.ipynb
jupyter nbconvert --to notebook --execute code/Figure1/Figure1_Selection_Reproducible_FINAL.ipynb --output /tmp/F1_3.ipynb
jupyter nbconvert --to notebook --execute code/Figure1/Figure1_TitleOnly_AbstractRecovery_RECONSTRUCTED_CLEAN.ipynb --output /tmp/F1_4.ipynb
jupyter nbconvert --to notebook --execute code/Figure1/Figure1_TitleOnly_SafetyLane_CLEAN.ipynb --output /tmp/F1_5.ipynb
jupyter nbconvert --to notebook --execute code/Figure2/Figure2_ASReview_Reproducible_CLEAN.ipynb --output /tmp/F2.ipynb
jupyter nbconvert --to notebook --execute code/Figure3/Figure3_SPECTER2_Reproducible_CLEAN.ipynb --output /tmp/F3.ipynb
python code/Figure5/Figure5C_EvidenceProfiles_FINAL.py

Public-data design
Only derived analysis variables needed for reproducibility are included.
The repository deliberately excludes bibliographic titles, abstracts, DOI/PMID fields, author and journal fields, raw source-database exports, .asreview project files, SPECTER2 raw inputs/embedding archives, and journal Supplementary Tables/Appendices.
See VALIDATION_REPORT.md for the execution results used to validate the public release.

Manuscript
Title: Cellular Senescence and Chronological Aging in Respiratory Extracellular Vesicle Biology: Mapping the Mechanistic Gap
Journal: Ageing Research Reviews
Status: Manuscript in preparation / submission
The repository citation and publication DOI will be updated after publication.
