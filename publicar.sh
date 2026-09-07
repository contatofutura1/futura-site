#!/usr/bin/env bash
# Publica o site: verifica as regras editoriais e técnicas, sincroniza e envia ao repositório.
set -e
cd "$(dirname "$0")"
python3 verificar.py
git add -A
git commit -q -m "${1:-Atualização do site}" || true
git push -q "https://x-access-token:${GITHUB_TOKEN}@github.com/contatofutura1/futura-site.git" main
git fetch -q origin && git merge-base --is-ancestor HEAD origin/main && echo "publicado: $(git log --oneline | head -1)"
