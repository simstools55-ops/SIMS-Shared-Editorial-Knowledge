#!/usr/bin/env python3
from pathlib import Path
import argparse, shutil, json, hashlib
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("source",type=Path); ap.add_argument("target",choices=["writer","article-creator"]); ap.add_argument("destination",type=Path); a=ap.parse_args()
 if a.destination.exists(): shutil.rmtree(a.destination)
 a.destination.mkdir(parents=True)
 for name in ["knowledge","validation","docs"]: shutil.copytree(a.source/name,a.destination/name)
 shutil.copytree(a.source/"mappings"/a.target,a.destination/"mappings"/a.target)
 for name in ["README.md","LICENSE","VERSION","CHANGELOG.md"]: shutil.copy2(a.source/name,a.destination/name)
 ver=(a.source/"VERSION").read_text(encoding="utf-8").strip()
 scope={"target_product":a.target,"source_version":ver,"integrated_version":ver,"included_mapping":a.target,"excluded_mapping":"article-creator" if a.target=="writer" else "writer"}
 (a.destination/"SNAPSHOT_SCOPE.json").write_text(json.dumps(scope,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 files={str(p.relative_to(a.destination)).replace("\\","/"):sha(p) for p in sorted(a.destination.rglob("*")) if p.is_file() and p.name!="SNAPSHOT_MANIFEST.json"}
 manifest={"source_repository":"SIMS-Shared-Editorial-Knowledge","source_version":ver,"integrated_version":ver,"target_product":a.target,"files":files}
 (a.destination/"SNAPSHOT_MANIFEST.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
if __name__=="__main__": main()
