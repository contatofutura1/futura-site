#!/usr/bin/env bash
# Baixa as imagens listadas em imagens.txt para img/. Roda no Netlify a cada publicação.
set -e
mkdir -p img
while read -r nome url; do
  [[ -z "$nome" || "$nome" == \#* ]] && continue
  if [[ ! -f "img/$nome" ]]; then
    echo "baixando $nome"
    curl -fsSL --retry 3 -o "img/$nome" "$url"
  fi
done < imagens.txt
ls -la img
