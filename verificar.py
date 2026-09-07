#!/usr/bin/env python3
"""Verificação editorial e técnica do site da Futura. Falha (exit 1) se alguma regra for violada.
Regras: sem travessão; sem primeira pessoa; sem juízo de valor ou frases de efeito conhecidas;
siglas em português (OMI, não IMO); HTML aninhado; JS válido; toda ficha com Pergunta, Método e Resultado."""
import re, sys, pathlib, subprocess
from html.parser import HTMLParser

ARQ = ['index.html', 'publicacoes.html', 'midia.html']
PROIBIDAS = [
    r'—',                                   # travessão
    r'\b(nós|nossa|nosso|nossas|nossos)\b', # primeira pessoa
    r'\b(levamos|organizamos|assinamos|medimos|construímos|fizemos|comparamos|apresentamos)\b',
    r'\bIMO\b',                             # sigla em inglês
    r'cobrável', r'quem só vai reagir', r'inédit', r'nunca "não existe"',
    r'futuros? melhor', r'futuros? pior', r'sem virar desastre', r'onde as mortes acontecem',
    r'primeiro produto', r'dezoito projetos|dezessete projetos|vinte cidades|quarenta títulos|vinte e nove entradas',
]
erros = []

class P(HTMLParser):
    T = ('ul','li','div','section','article','main','header','footer','nav','p','span','a','h1','h2','h3','button','dl','dt','dd','dialog')
    def __init__(s): super().__init__(); s.st=[]; s.err=[]
    def handle_starttag(s,t,a):
        if t in s.T: s.st.append(t)
    def handle_endtag(s,t):
        if t in s.T:
            if s.st and s.st[-1]==t: s.st.pop()
            else: s.err.append((t,s.getpos()))

for f in ARQ:
    txt = pathlib.Path(f).read_text()
    corpo = re.sub(r'<script>.*?</script>|<style>.*?</style>', '', txt, flags=re.S)
    visivel = re.sub(r'<[^>]+>', ' ', corpo)
    for pat in PROIBIDAS:
        for m in re.finditer(pat, visivel):
            ctx = re.sub(r'\s+',' ', visivel[max(0,m.start()-40):m.end()+40])
            erros.append(f'{f}: "{m.group(0)}" em …{ctx}…')
    q = P(); q.feed(txt)
    if q.err or q.st: erros.append(f'{f}: HTML mal aninhado {q.err[:2]} {q.st[:2]}')
    if f == 'index.html':
        for card in re.findall(r'<article class="projeto.*?</article>', txt, re.S):
            nome = re.search(r'projeto-nome">(.*?)</h3>', card, re.S).group(1)
            for rot in ('Pergunta','Método','Resultado'):
                if f'<dt>{rot}</dt>' not in card: erros.append(f'index.html: ficha de "{nome}" sem {rot}')
            if 'class="teaser' not in card: erros.append(f'index.html: "{nome}" sem frase de abertura')
        js = re.search(r'<script>(.*?)</script>', txt, re.S).group(1)
        r = subprocess.run(['node','-e','new Function(require("fs").readFileSync(0,"utf8"))'], input=js, text=True, capture_output=True)
        if r.returncode: erros.append('index.html: JS inválido: '+r.stderr.strip()[:120])

if erros:
    print('VERIFICAÇÃO FALHOU'); [print(' -', e) for e in erros]; sys.exit(1)
print('verificação ok:', ', '.join(ARQ))
