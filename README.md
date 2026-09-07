# Futura — site institucional

futuraevidencelab.com.br. Páginas estáticas, sem build de código: o Netlify publica a raiz do repositório a cada envio ao ramo `main`, depois de rodar `baixar.sh` (imagens externas listadas em `imagens.txt`).

## Arquivos
- `index.html` — capa, Projetos (Ação, Imaginação, Conhecimento), Onde (mapa-múndi), Quem, Contato
- `publicacoes.html` — periódicos, capítulos de livro, artigos na imprensa, relatórios, anais
- `midia.html` — entrevistas, matérias e comunicados
- `404.html`, `favicon.svg`, `apple-touch-icon.png`, `icone-192.png`, `icone-512.png`, `site.webmanifest`, `compartilhar.png` (cartão de redes), `retrato.jpg`
- `img/` — mapas em contorno (SVG gerados por código) e fotos baixadas na publicação
- `robots.txt`, `sitemap.xml`, `_redirects` (www e http para o endereço principal), `_headers` e `netlify.toml`

## Regras editoriais (verificadas automaticamente por `verificar.py`)
- Sem travessão em nenhuma página.
- Sem primeira pessoa; o sujeito das frases é o projeto, o estudo, a conferência.
- Sem juízo de valor, frases de efeito, máximas de abertura ou contagens ("dezoito projetos").
- Siglas em português e por extenso na primeira aparição (OMI, não IMO; Organização Mundial da Saúde).
- Cada projeto: título que diz o que aconteceu; linha "ano, organização (Futura)" quando feito pela Futura; uma frase curta; ficha com Pergunta, Método e Resultado.

## Desenho
- Playfair (display, opsz 1200, wdth 87.5, wght 300) e Jost (texto). Preto, branco, terracota como cor ativa.
- Capa: wordmark, "Imaginar não basta.", predicado. Sem sumário, sem Posição.
- Projetos em três grupos por relevância; em cada grupo, a primeira é reportagem (largura inteira, mapa ou foto em cinco colunas) e as demais são notas em três colunas, sem imagem.
- Mapas: contorno em fio fino, território em fio preto, arco do logotipo em terracota (`minimal.mjs`, estilo A). A malha de pontos só no mapa-múndi de Onde.
- Créditos de foto ao passar o mouse (sempre visíveis em toque).

## Publicar
```
python3 verificar.py            # falha se alguma regra for violada
GITHUB_TOKEN=... ./publicar.sh "mensagem"
```
Publicar em lote, não a cada ajuste: cada publicação consome crédito do plano do Netlify. Conferir o site público depois.

## Pendente (só a titular)
DKIM "Start authentication" no Google Admin; registro DMARC no Registro.br; Search Console (reverificação e envio do sitemap); domínio parecido monitorelninobrasi.com.br.
