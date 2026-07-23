#!/usr/bin/env python3
from pathlib import Path
import argparse, shutil, json

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("source", type=Path)
    ap.add_argument("target", choices=["writer","article-creator"])
    ap.add_argument("destination", type=Path)
    a=ap.parse_args()
    if a.destination.exists(): shutil.rmtree(a.destination)
    a.destination.mkdir(parents=True)
    for name in ["knowledge","validation","docs"]:
        shutil.copytree(a.source/name,a.destination/name)
    shutil.copytree(a.source/"mappings"/a.target,a.destination/"mappings"/a.target)
    for name in ["README.md","LICENSE","VERSION","CHANGELOG.md"]:
        shutil.copy2(a.source/name,a.destination/name)
    (a.destination/"SNAPSHOT_SCOPE.json").write_text(json.dumps({"target_product":a.target,"included_mapping":a.target,"excluded_mapping":"article-creator" if a.target=="writer" else "writer"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
if __name__=="__main__": main()
