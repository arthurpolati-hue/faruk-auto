"""Construit les pages à partir de src/app.html et src/demo.json.

- faruk-auto.html : version publiée comme Artifact Claude (sans balises html/head/body)
- index.html      : page complète pour GitHub Pages
"""
import json
from pathlib import Path

root = Path(__file__).parent
demo = json.loads((root / "src/demo.json").read_text(encoding="utf-8"))
body = (root / "src/app.html").read_text(encoding="utf-8").replace("__DEMO__", json.dumps(demo, ensure_ascii=False))
firebase = (root / "src/firebase.html").read_text(encoding="utf-8")

(root / "faruk-auto.html").write_text(body, encoding="utf-8")
(root / "index.html").write_text(
    '<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    '<meta name="color-scheme" content="light dark">\n'
    '<style>html,body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
    '</head>\n<body>\n' + firebase + '\n' + body + '\n</body>\n</html>\n',
    encoding="utf-8",
)
print("faruk-auto.html et index.html générés")
