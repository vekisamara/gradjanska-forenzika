#!/usr/bin/env python3
"""GFO Election Analytics — Repeat Election Calibration Engine v0.1.

Compares original and repeat observations for an explicit official polling-station set.
Produces descriptive deltas only. No fraud inference, no anomaly verdict, no LLM use.
"""
from __future__ import annotations
import argparse,csv,json,hashlib
from pathlib import Path
from datetime import datetime, timezone

VERSION='0.1.0'

def read_csv(p):
    with Path(p).open(newline='',encoding='utf-8') as f: return list(csv.DictReader(f))
def num(v):
    try:return float(v) if v not in (None,'') else None
    except:return None
def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for c in iter(lambda:f.read(1<<20),b''):h.update(c)
    return h.hexdigest()
def write_csv(p,rows):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    fields=[]
    for r in rows:
        for k in r:
            if k not in fields:fields.append(k)
    with p.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('official_repeat_list')
    ap.add_argument('original_station_results')
    ap.add_argument('repeat_station_results')
    ap.add_argument('--output',default='./repeat-calibration-v0.1')
    a=ap.parse_args(); out=Path(a.output);out.mkdir(parents=True,exist_ok=True)
    ref=read_csv(a.official_repeat_list); orig=read_csv(a.original_station_results); rep=read_csv(a.repeat_station_results)
    codes=[r['polling_station_code'] for r in ref]
    oi={r['polling_station_code']:r for r in orig}; ri={r['polling_station_code']:r for r in rep}
    flags=[]; rows=[]
    for code in codes:
        o=oi.get(code); r=ri.get(code)
        if not o: flags.append({'record_id':code,'rule_code':'GFO-RC-V001','severity':'error','message':'Missing original observation'})
        if not r: flags.append({'record_id':code,'rule_code':'GFO-RC-V002','severity':'error','message':'Missing repeat observation'})
        if not o or not r: continue
        def d(field):
            x,y=num(o.get(field)),num(r.get(field)); return None if x is None or y is None else y-x
        rego,regr=num(o.get('registered_voters')),num(r.get('registered_voters'))
        if rego is not None and regr is not None and rego!=regr:
            flags.append({'record_id':code,'rule_code':'GFO-RC-V003','severity':'warning','message':f'Registered voters changed {rego} -> {regr}'})
        to=num(o.get('turnout_percentage')); tr=num(r.get('turnout_percentage'))
        io=num(o.get('invalid_votes')); ir=num(r.get('invalid_votes'))
        vo=num(o.get('valid_votes')); vr=num(r.get('valid_votes'))
        tvo=num(o.get('total_votes')); tvr=num(r.get('total_votes'))
        invro=(io/tvo) if io is not None and tvo not in (None,0) else None
        invrr=(ir/tvr) if ir is not None and tvr not in (None,0) else None
        rows.append({
            'polling_station_code':code,
            'municipality_code':r.get('municipality_code') or o.get('municipality_code',''),
            'registered_voters_original':rego,'registered_voters_repeat':regr,'registered_voters_delta':d('registered_voters'),
            'total_votes_original':tvo,'total_votes_repeat':tvr,'total_votes_delta':d('total_votes'),
            'valid_votes_original':vo,'valid_votes_repeat':vr,'valid_votes_delta':d('valid_votes'),
            'invalid_votes_original':io,'invalid_votes_repeat':ir,'invalid_votes_delta':d('invalid_votes'),
            'turnout_pct_original':to,'turnout_pct_repeat':tr,'turnout_pct_delta':None if to is None or tr is None else tr-to,
            'invalid_rate_original':invro,'invalid_rate_repeat':invrr,'invalid_rate_delta':None if invro is None or invrr is None else invrr-invro,
        })
    write_csv(out/'repeat_calibration_deltas.csv',rows);write_csv(out/'validation_flags.csv',flags)
    manifest={'module':'repeat_calibration_engine_v0_1.py','module_version':VERSION,'processed_at':datetime.now(timezone.utc).isoformat(),
      'official_repeat_list_sha256':sha(a.official_repeat_list),'original_input_sha256':sha(a.original_station_results),'repeat_input_sha256':sha(a.repeat_station_results),
      'official_station_count':len(codes),'comparable_station_count':len(rows),'validation_flag_count':len(flags),'error_flag_count':sum(x['severity']=='error' for x in flags)}
    (out/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f"Official repeat stations: {len(codes)}\nComparable stations: {len(rows)}\nValidation flags: {len(flags)}\nErrors: {manifest['error_flag_count']}\nOutput: {out.resolve()}")
if __name__=='__main__':main()
