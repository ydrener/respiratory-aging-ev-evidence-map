# VALIDATION REPORT — SLIM public GitHub package

## Release basis

- Source master: `ARR_EV_Aging_Reproducibility_GitHub_VALIDATED.zip`
- Source master SHA-256: `c66fc7f0d8942c6a48221f09d63e53100c883756b1cd555cf64ab3230472a483`
- The source master was not modified; the SLIM package was built in a separate working directory.

## Mandatory execution status

| File / check | Status | Actual executed result |
|---|---|---|
| `code/Figure1/Figure1_CorpusConstruction_FrozenMapping_CLEAN.ipynb` | PASS | 27,768 raw; 14,366 deduplicated; 13,402 duplicates removed; 12,913 title+abstract; 1,453 title-only |
| `code/Figure1/Figure1_Deduplication_Rules_Reconstructed_REFERENCE.ipynb` | PASS | 14,366 deduplicated groups; reconstructed dedup-support audit completed |
| `code/Figure1/Figure1_Selection_Reproducible_FINAL.ipynb` | PASS | full-text 51 unique candidates = 37 included / 13 excluded / 1 not retrieved |
| `code/Figure1/Figure1_TitleOnly_AbstractRecovery_RECONSTRUCTED_CLEAN.ipynb` | PASS | 1,453 title-only; 192 frozen recovered-abstract statuses validated |
| `code/Figure1/Figure1_TitleOnly_SafetyLane_CLEAN.ipynb` | PASS | 178 Article/Letter audited, all not relevant; 19 high-signal reviewed; 0 additionally advanced |
| `code/Figure2/Figure2_ASReview_Reproducible_CLEAN.ipynb` | PASS | 765 human-screened = 50 relevant + 715 not relevant; 2 positive seeds; 767 total labeled; 52 candidates; last relevant at 408; terminal run 357 |
| `code/Figure3/Figure3_SPECTER2_Reproducible_CLEAN.ipynb` | PASS | 14,366 corpus; 12,913 title+abstract; 1,453 title-only; 767 ASReview-labeled; 52 candidates; 12,146 residual; Top50=50; additional relevant=0; 6 clusters |
| `code/Figure5/Figure5C_EvidenceProfiles_FINAL.py` | PASS | 6 criteria; chronological counts [9,9,8,6,3,2]/9; senescence counts [22,16,11,24,18,12]/26; causal cargo 2/9 and 12/26 |
| external locked-count validator against SLIM data | PASS | all manuscript locked values matched exactly |
| mandatory requirements (`pip install --no-index -r requirements.txt`) | PASS | all required packages satisfied in validation environment |
| repository-relative input/path scan | PASS | no `google.colab`, `files.upload()`, `files.download()`, `/content/`, `/mnt/data/`, or Windows absolute-path dependency in packaged code |
| public-data field scan | PASS | no title, abstract, DOI, PMID, author, journal, keyword, raw source-ID, primary-source, or adjudication-note columns in packaged CSV data |


## Release-level correction during validation

A release-ZIP recheck initially exposed one path-resolution bug in `Figure5C_EvidenceProfiles_FINAL.py`: running the script by absolute path from outside the repository did not resolve the repository root. The script was corrected to search from both the current working directory and its own `__file__` location, and the mandatory validation sequence was restarted after this correction.

## Locked values confirmed

- final included studies = **37**
- full-text outcomes = **37 included / 13 excluded / 1 not retrieved**
- Figure 3 = **14,366 / 12,913 / 1,453 / 767 / 52 / 12,146**
- residual Top50 = **50**
- additional relevant = **0**
- Figure 5C = **6 criteria**
- senescence-only causal cargo = **12/26**
- chronological-aging-only causal cargo = **2/9**

## Public-SLIM exclusions

The following master-package content was intentionally excluded from the public SLIM repository:

- `large_immutable_inputs/` in full: raw broad master, raw-to-master map, SPECTER2 input, SPECTER2 output/embedding archive, and `.asreview` project.
- `search/` in full: exact search-strategy archive is manuscript/Supplementary Appendix material rather than executable SLIM data.
- `provenance/` and `qc/` in full: internal manifests, archived checksums, QC/status files, and prior validator were not reused.
- journal/source-data style duplicates and intermediate summary CSVs from `data/Figure1`, `data/Figure2`, and `data/Figure3`.
- bibliographic text fields (titles, abstracts, DOI/PMID, authors, journals, source identifiers) were removed when constructing public derived tables.
- study names were removed from Figure 5C public coding; only anonymous study number, framework, and six evidence variables remain.

## Interpretation of reproducibility scope

The SLIM repository validates the manuscript-locked counts and regenerates figure-level analytical summaries from derived public data. It intentionally does **not** claim to rerun database retrieval, ASReview learning, abstract-recovery APIs, SPECTER2 encoding, or embedding generation from raw bibliographic records because those source objects are excluded from public distribution by design.
