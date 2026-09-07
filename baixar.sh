#!/usr/bin/env bash
# Baixa as imagens listadas em imagens.txt para img/. Roda no Netlify a cada publicação.
# Uma imagem que falhe não impede a publicação: o site trata a ausência.
mkdir -p img
ok=0; falha=0
while read -r nome url; do
  [[ -z "$nome" || "$nome" == \#* ]] && continue
  if [[ -f "img/$nome" ]]; then ok=$((ok+1)); continue; fi
  if curl -fsSL --retry 2 --max-time 40 -A "Mozilla/5.0 (site futuraevidencelab.com.br)" -o "img/$nome" "$url"; then
    echo "baixado $nome"; ok=$((ok+1))
  else
    echo "AVISO: falhou $nome ($url)"; rm -f "img/$nome"; falha=$((falha+1))
  fi
done < imagens.txt
echo "imagens: $ok ok, $falha com falha"
ls -la img
exit 0
