from pathlib import Path
import pandas as pd

def find_repo_root():
    starts=[Path.cwd(), Path(__file__).resolve().parent]
    candidates=[]
    for start in starts:
        candidates.extend([start, *start.parents])
    for p in candidates:
        if (p/'requirements.txt').exists() and (p/'data/Figure5').is_dir(): return p
    raise RuntimeError('Repository root not found.')
ROOT=find_repo_root()
p=ROOT/'data/Figure5/Figure5C_StudyCoding_DERIVED_37.csv'
df=pd.read_csv(p)
assert len(df)==37
criteria=['Functional_EV_experiment','In_vivo_evidence','Direct_EV_linked_immune_inflammatory_effect','Specific_cargo_evidence','Functionally_supported_cargo','EV_context_causal_cargo']
assert len(criteria)==6
for c in criteria: assert set(df[c].dropna().astype(str).str.strip()) <= {'Yes','No'}
chron=df[df.Aging_framework.eq('Chronological-aging only')]
sen=df[df.Aging_framework.eq('Senescence only')]
mixed=df[df.Aging_framework.str.startswith('Mixed',na=False)]
assert (len(chron),len(sen),len(mixed))==(9,26,2)
counts=lambda d:[int(d[c].eq('Yes').sum()) for c in criteria]
chron_counts=counts(chron); sen_counts=counts(sen)
assert chron_counts==[9,9,8,6,3,2], chron_counts
assert sen_counts==[22,16,11,24,18,12], sen_counts
print('Figure 5C validation: PASS')
print('Criteria:', len(criteria))
print('Chronological-aging only:', chron_counts, '/ 9')
print('Senescence only:', sen_counts, '/ 26')
print('Causal cargo: chronological 2/9; senescence 12/26')
