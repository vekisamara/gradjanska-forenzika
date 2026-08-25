#!/usr/bin/env python3
"""GFO Historical Anomaly Engine v0.1: separate historical/peer deviation signals only."""
from __future__ import annotations
import argparse,csv,hashlib,json,math
from collections import defaultdict
from datetime import datetime,timezone
from pathlib import Path

VERSION="0.1.0"

def read(p):
    with Path(p).open(newline="",encoding="utf-8") as f:return list(csv.DictReader(f))
def write(p,rows):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    if not rows:p.write_text("",encoding="utf-8");return
    keys=[]
    for r in rows:
        for k in r:
            if k not in keys:keys.append(k)
    with p.open("w",newline="",encoding="utf-8") as f:w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(rows)
def n(v):
    try:
        x=float(v);return x if math.isfinite(x) else None
    except:return None
def yes(v):return str(v).strip().lower() in {"1","true","yes","y"}
def z(x,m,s):return None if x is None or m is None or s in (None,0) else (x-m)/s
def rr(x):return None if x is None else round(x,6)
def sha(p):
    h=hashlib.sha256()
    with Path(p).open("rb") as f:
        for c in iter(lambda:f.read(1048576),b""):h.update(c)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser();ap.add_argument("current_csv");ap.add_argument("mapping_csv");ap.add_argument("baseline_csv");ap.add_argument("peer_csv");ap.add_argument("--current-election-id",required=True);ap.add_argument("--output",default="./historical-anomaly-output");ap.add_argument("--min-mapping-confidence",type=float,default=.95);a=ap.parse_args()
    out=Path(a.output);out.mkdir(parents=True,exist_ok=True);flags=[]
    maps={}
    for r in read(a.mapping_csv):
        if not yes(r.get("usable_for_baseline")) or (n(r.get("mapping_confidence")) or 0)<a.min_mapping_confidence:continue
        k=(r.get("historical_election_id",""),r.get("historical_polling_station_code",""));c=r.get("canonical_polling_station_code","")
        if k in maps and maps[k]!=c:flags.append({"record_id":"|".join(k),"rule_code":"GFO-HA-V001","severity":"error","message":"Conflicting usable mapping"})
        elif all(k) and c:maps[k]=c
    groups=defaultdict(list)
    for r in read(a.current_csv):
        if r.get("election_id")==a.current_election_id:groups[r.get("polling_station_code","")].append(r)
    current={}
    for ps,g in groups.items():
        code=maps.get((a.current_election_id,ps))
        if not code:continue
        vals={}
        for f in ("registered_voters","total_votes","valid_votes","invalid_votes"):
            s={x for r in g if (x:=n(r.get(f))) is not None}
            if len(s)>1:flags.append({"record_id":code,"rule_code":"GFO-HA-V002","severity":"error","message":f"Inconsistent {f}"})
            vals[f]=next(iter(s),None)
        reg,total,valid,invalid=[vals[x] for x in ("registered_voters","total_votes","valid_votes","invalid_votes")]
        if reg is not None and total is not None and total>reg:flags.append({"record_id":code,"rule_code":"GFO-HA-V003","severity":"error","message":"total_votes exceeds registered_voters"})
        if None not in (total,valid,invalid) and valid+invalid!=total:flags.append({"record_id":code,"rule_code":"GFO-HA-V004","severity":"error","message":"valid+invalid != total"})
        current[code]={"municipality_code":g[0].get("municipality_code",""),"registered_voters":reg,"turnout":total/reg if reg not in (None,0) and total is not None else None,"invalid_rate":invalid/total if total not in (None,0) and invalid is not None else None}
    base={r.get("canonical_polling_station_code"):r for r in read(a.baseline_csv)};peers={r.get("target_polling_station_code"):r for r in read(a.peer_csv)};signals=[]
    for code,o in sorted(current.items()):
        b=base.get(code);p=peers.get(code)
        if not b:flags.append({"record_id":code,"rule_code":"GFO-HA-V005","severity":"warning","message":"No historical baseline"});continue
        t=o["turnout"];ir=o["invalid_rate"];reg=o["registered_voters"];bt=n(b.get("turnout_mean"));bts=n(b.get("turnout_std"));bi=n(b.get("invalid_rate_mean"));bis=n(b.get("invalid_rate_std"));br=n(b.get("registered_voters_mean"));pt=n(p.get("turnout_mean")) if p else None;pts=n(p.get("turnout_std")) if p else None;pi=n(p.get("invalid_rate_mean")) if p else None;pis=n(p.get("invalid_rate_std")) if p else None;ptz=z(t,pt,pts);piz=z(ir,pi,pis)
        signals.append({"canonical_polling_station_code":code,"municipality_code":o["municipality_code"],"current_election_id":a.current_election_id,"registered_voters":rr(reg),"turnout":rr(t),"invalid_rate":rr(ir),"historical_election_count":b.get("historical_election_count",""),"historical_turnout_mean":rr(bt),"historical_turnout_std":rr(bts),"historical_turnout_delta":rr(None if t is None or bt is None else t-bt),"historical_turnout_z":rr(z(t,bt,bts)),"historical_invalid_rate_mean":rr(bi),"historical_invalid_rate_std":rr(bis),"historical_invalid_rate_delta":rr(None if ir is None or bi is None else ir-bi),"historical_invalid_rate_z":rr(z(ir,bi,bis)),"historical_registered_voters_mean":rr(br),"registered_voter_change_pct":rr(None if reg is None or br in (None,0) else 100*(reg-br)/br),"peer_available":str(p is not None).lower(),"peer_count":p.get("peer_count","") if p else "","peer_turnout_mean":rr(pt),"peer_turnout_std":rr(pts),"peer_turnout_delta":rr(None if t is None or pt is None else t-pt),"peer_turnout_z":rr(ptz),"peer_invalid_rate_mean":rr(pi),"peer_invalid_rate_std":rr(pis),"peer_invalid_rate_delta":rr(None if ir is None or pi is None else ir-pi),"peer_invalid_rate_z":rr(piz),"turnout_invalid_interaction":rr(None if ptz is None or piz is None else ptz*piz)})
    write(out/"historical_anomaly_signals.csv",signals);write(out/"validation_flags.csv",flags)
    manifest={"module":"historical_anomaly_engine_v0_1.py","module_version":VERSION,"processed_at":datetime.now(timezone.utc).isoformat(),"current_election_id":a.current_election_id,"current_input_sha256":sha(a.current_csv),"mapping_input_sha256":sha(a.mapping_csv),"historical_baseline_sha256":sha(a.baseline_csv),"peer_group_features_sha256":sha(a.peer_csv),"current_mapped_station_count":len(current),"signal_row_count":len(signals),"validation_flag_count":len(flags),"composite_score_produced":False,"political_variables_used":False}
    (out/"historical_anomaly_manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding="utf-8")
    print(f"Current mapped stations: {len(current)}\nSignal rows: {len(signals)}\nValidation flags: {len(flags)}\nOutput: {out.resolve()}")
if __name__=="__main__":main()
