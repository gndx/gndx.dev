---
title: 'Aprenda a criar vídeos com Inteligência Artificial usando o Claude Code'
description: 'Como transformo uma única frase em um reel de 60 segundos com Claude Code, uma skill, ElevenLabs, Whisper, HyperFrames e FFmpeg. Inclui a skill completa para personalizar e um prompt para adaptá-la ao seu canal.'
pubDate: '2026-11-14T21:00:00.000Z'
heroImage: '/blog/141126-asi-hago-mis-reels-con-ia/portada-pt.webp'
categories:
  - 'ia'
  - 'ferramentas'
authors:
  - 'gndx'
tags:
  - 'claude code'
  - 'skills'
  - 'hyperframes'
  - 'elevenlabs'
  - 'whisper'
  - 'ffmpeg'
  - 'reels'
---

Você já viu centenas de vídeos como os meus, mas ninguém explica como eles são feitos. No reel eu contei em um minuto; aqui está a versão completa: qual ferramenta faz o quê, em que ordem, os erros que me custaram caro e **a skill inteira para você copiar**, junto com um prompt que a entende e ajuda você a adaptá-la ao seu canal.

A ideia de fundo é simples: **eu não edito vídeos, eu escrevo regras**. Dou uma frase ao Claude Code, ele lê as minhas regras e faz o trabalho pesado. Eu escolho a história, reviso e corrijo. E cada correção vira uma regra nova.

![Como faço meus reels com IA](/blog/141126-asi-hago-mis-reels-con-ia/portada-pt.webp)

## O que você precisa

| Ferramenta | Para quê | Notas |
|---|---|---|
| **Claude Code** | O agente que faz todo o trabalho | Roda no seu terminal, dentro da pasta do projeto |
| **Uma skill** (`SKILL.md`) | Suas regras: canal, estilo, voz, passos | Fica em `~/.claude/skills/<nome>/SKILL.md` |
| **HyperFrames** | Transforma HTML em vídeo | Código aberto (HeyGen). Precisa de Node.js 22+, FFmpeg e Chrome. Use com `npx hyperframes` |
| **ElevenLabs** | Texto → voz | Uma voz pronta ou a sua voz clonada. A chave, só em uma variável de ambiente |
| **Whisper** | Voz → texto, para conferir | O modelo `small`, local (eu uso o faster-whisper) |
| **FFmpeg** | Junta, mede e ajusta o áudio | Loudness, picos e quadros pretos |
| **Three.js** | O mundo 3D (opcional) | Já vem dentro do projeto |

Também uso música licenciada (Epidemic Sound) e um template de projeto que fui montando reel a reel. Se você não tem template, tudo bem: no primeiro vídeo o Claude Code cria com você.

## Passo 1 · Tudo começa com uma frase

![Passo 1: a frase no Claude Code](/blog/141126-asi-hago-mis-reels-con-ia/paso-1-prompt-pt.webp)

Abro o Claude Code na pasta dos meus vídeos e escrevo o nome da skill seguido do tema, com as minhas palavras (eu escrevo em espanhol):

```text
/video-tech crea un video explicando cómo usamos esta tool, las herramientas, la estructura, la skill… en pasos, amigable y listo
```

`/video-tech` carrega a skill; o resto é o pedido. Não precisa de um prompt perfeito: as regras já estão na skill. Essa é a graça.

<aside class="promo-mentor not-prose" aria-label="Mentoria com Oscar Barajas">
<p class="promo-mentor__eyebrow">Mentoria · @gndx</p>
<p class="promo-mentor__title">Compre a pasta com todos os meus aprendizados</p>
<div class="promo-mentor__options">
<p class="promo-mentor__option"><span class="promo-mentor__price">$1,99 USD</span><span class="promo-mentor__detail">Só a pasta</span></p>
<p class="promo-mentor__option promo-mentor__option--featured"><span class="promo-mentor__price">$20 USD</span><span class="promo-mentor__detail">A pasta + mentoria e acompanhamento do seu projeto</span></p>
</div>
<a class="promo-mentor__cta" href="https://mentor.gndx.dev/" target="_blank" rel="noopener">Ir para mentor.gndx.dev <span aria-hidden="true">→</span></a>
</aside>

## Passo 2 · A skill: um arquivo com todas as suas regras

![Passo 2: a skill](/blog/141126-asi-hago-mis-reels-con-ia/paso-2-skill-pt.webp)

Uma skill é um arquivo Markdown com um cabeçalho (nome e descrição) e as suas instruções. O Claude Code lê antes de começar, então **se você muda a skill, mudam todos os seus vídeos**. A minha tem seis blocos:

- **O canal**: a conta, os temas, o tom e a frase final.
- **Estilo**: cores, fontes, o que é desenhado e o que é "de verdade", e a zona segura do Instagram.
- **Dados**: só fontes primárias, com data; superlativos são checados em várias fontes.
- **Voz**: qual voz, em que velocidade e como escrever as palavras que ela lê errado.
- **Passo a passo**: 13 passos, da história ao render.
- **Antes de entregar**: a checklist que sempre é revisada.

No fim do artigo você tem uma versão completa, pronta para copiar e personalizar.

## Passo 3 · Um template e três histórias

![Passo 3: template e três histórias](/blog/141126-asi-hago-mis-reels-con-ia/paso-3-plantilla-pt.webp)

O Claude Code pesquisa o tema e monta o projeto a partir do meu template com um único comando:

```bash
sh plantillas/nuevo.sh tech mi-reel
```

O template traz tudo o que se repete em cada reel: o script da voz, o gerador de legendas e capítulos, o mundo 3D, fontes, música e efeitos. Ele também cria uma **maquete**: estima os tempos da voz a partir do texto, então o reel inteiro roda sem gastar um único caractere do ElevenLabs.

Depois ele propõe **três histórias diferentes**, cada uma com seu roteiro segundo a segundo e os dados já checados. Eu escolho uma com um clique. Todas seguem a mesma estrutura, a que melhor funcionou para mim:

1. **Gancho** nos 3 primeiros segundos: uma pergunta surpreendente sobre o que você está vendo.
2. **Promessa** curta: "te conto em um minuto".
3. **Capítulos** de 4 a 6 segundos que viram: "mas…", "até que…".
4. **Um dado** com número.
5. **Fecho** que volta ao gancho.
6. **Chamada** para seguir.

## Passo 4 · A voz, em uma única tomada

![Passo 4: voz e verificação](/blog/141126-asi-hago-mis-reels-con-ia/paso-4-voz-pt.webp)

O Claude Code escreve o roteiro (umas 150 palavras para 60 segundos) e o **ElevenLabs** dá a voz. A onda da imagem é a de verdade: o volume da voz deste reel, frase por frase.

Aqui aprendi a lição mais cara: no começo eu gerava a voz **frase por frase** e deixava espaços entre elas para as animações "respirarem". Soava cortado. Agora o roteiro inteiro vai **em uma única chamada** e depois é cortado nos silêncios, só para saber quando cada palavra começa. A voz flui e as legendas continuam palavra por palavra.

Depois o **Whisper** escuta cada frase e compara com o roteiro. Se uma palavra sai errada, ela é escrita como soa: para a voz em espanhol dizer "FFmpeg" direito, o roteiro diz "efe efe eme peg" (na tela aparece a forma correta).

> 🔐 A chave do ElevenLabs vai só na variável `ELEVENLABS_API_KEY`. Nunca em um arquivo do projeto, nunca no chat.

## Passo 5 · O vídeo é uma página web

![Passo 5: o vídeo é uma página web](/blog/141126-asi-hago-mis-reels-con-ia/paso-5-web-pt.webp)

Este é o truque que mais surpreende: cada reel é **uma página web**. O HyperFrames pega um `index.html` com camadas (o mundo 3D em um `<canvas>` com Three.js, as legendas, os capítulos, os cartões, o áudio) e uma linha do tempo do GSAP **pausada**. Cada quadro é um instante exato dessa linha do tempo, então o resultado é o mesmo em cada render.

Antes de renderizar eu confiro duas coisas:

```bash
npx hyperframes check        # erros, contraste, textos que somem rápido demais
npx hyperframes preview      # a pré-visualização no navegador
```

Também coloco a **zona segura do Instagram** em cima de capturas de vários segundos: o cabeçalho cobre a parte de cima, os botões a direita e o texto do post a parte de baixo. Tudo o que importa vai em x 100–980 e y 222–1660 (e à esquerda de x 900 abaixo de y 1280). Essas medidas saíram de um reel publicado, não de um guia.

## Passo 6 · 1.800 fotos que viram um MP4

![Passo 6: render e FFmpeg](/blog/141126-asi-hago-mis-reels-con-ia/paso-6-render-pt.webp)

O HyperFrames congela a página e fotografa **1.800 vezes** (60 segundos a 30 fps). O **FFmpeg** junta as fotos com o áudio em um MP4, e depois eu uso para medir:

```bash
npx hyperframes render -q delivery -o renders/mi-reel.mp4
ffmpeg -i renders/mi-reel.mp4 -filter_complex ebur128=peak=true -f null -   # loudness e pico real
ffmpeg -i renders/mi-reel.mp4 -vf blackdetect=d=0.05 -an -f null -          # quadros pretos
```

Minhas metas: **entre −13 e −14 LUFS**, pico real **abaixo de −2 dBTP**, nenhum quadro preto e o Whisper entendendo todas as frases na mixagem final. O reel deste guia saiu com −13,9 LUFS e −2,8 dBTP, sem masterizar.

## Passo 7 · Cada erro vira uma regra

![Passo 7: as correções](/blog/141126-asi-hago-mis-reels-con-ia/paso-7-correcciones-pt.webp)

Esta é a parte que faz o sistema melhorar. No `CLAUDE.md` do projeto há uma seção **"Correções"**: cada vez que eu corrijo algo, o Claude Code anota com a data e a regra do jeito que eu falei, **antes de continuar**. Se vale para sempre, ele também muda a skill ou o template.

Já são 17. Algumas:

- O primeiro vídeo saiu na horizontal e sem voz → **vertical 9:16 e com narração**.
- O logo ficava embaixo do cabeçalho do Instagram → **zona segura medida**.
- "Começo fraco" → **o gancho é uma pergunta surpreendente**, com algo grande na tela nessa palavra.
- A voz soava cortada → **uma única tomada**.

O próximo vídeo não repete o erro. Por isso cada reel me custa menos que o anterior.

## A skill completa (copie e deixe do seu jeito)

![Sua vez: a skill e o prompt](/blog/141126-asi-hago-mis-reels-con-ia/tu-skill-pt.webp)

Esta é uma versão genérica da minha skill. Troque tudo o que está entre `{{chaves}}` e salve em `~/.claude/skills/video-seu-canal/SKILL.md`. Depois, no Claude Code, escreva `/video-seu-canal` e o tema.

````markdown
---
name: video-{{seu-canal}}
description: Faz um reel vertical (9:16, 60 s, com voz) para {{@sua-conta}} sobre {{seus temas}}, com HyperFrames, voz do ElevenLabs e verificação com Whisper. Use quando eu pedir um reel ou escrever /video-{{seu-canal}}.
---

# Reel · {{@sua-conta}}

Tudo fica em `{{caminho/do/seu/projeto}}`. Antes de mexer em qualquer coisa, leia o `CLAUDE.md` do projeto (principalmente "Correções") e carregue a skill `/hyperframes`.

## O canal
- Conta: {{@sua-conta}} · Plataforma: {{Instagram Reels / TikTok / YouTube Shorts}}.
- Temas: {{3 a 6 temas}}. Público: {{com quem você fala}}.
- Tom: {{de você para você, frases curtas, próximo…}}. Nunca: {{o que você não quer ver}}.
- Fecho (voz e cartão final): "{{Me siga para mais…}}" e só {{@sua-conta}}.

## Estilo
- Formato: 1080 × 1920, 30 fps, 60 s.
- Cores: fundo {{#hex}}, destaque {{#hex}} (só para o que importa), texto {{#hex}}. Vermelho, só para erros.
- Fontes: {{fonte dos títulos}} e {{fonte das etiquetas}}.
- Zona segura de {{sua plataforma}}: todo o texto em x 100–980, y 222–1660 (e x ≤ 900 abaixo de y 1280). Meça em uma captura de um vídeo publicado na sua conta e confira antes de renderizar.
- Logos e produtos reais, da fonte: nunca redesenhados.

## Dados
- Só fontes primárias (documentação oficial, comunicados, papers). Anote a data em que conferiu.
- Superlativos ("o primeiro", "o mais…"): cheque em várias fontes ou suavize na narração.
- O código que aparecer na tela tem que funcionar: teste antes.

## Voz
- ElevenLabs, voz {{nome ou ID}} ({{pronta / clonada}}), modelo eleven_multilingual_v2, velocidade {{1.1}}.
- A chave vai só na variável ELEVENLABS_API_KEY: nunca em um arquivo nem impressa.
- Uma única tomada: o roteiro inteiro em uma chamada (com tempos por palavra) e depois cortado por frases nos silêncios. Frase por frase soa cortado.
- Números por extenso no texto lido; na tela, em algarismos.
- O que a voz lê errado é escrito como soa ({{ex.: "efe efe eme peg" para FFmpeg}}); na tela vai a forma correta.
- Confira cada frase com o Whisper (modelo small, idioma {{pt}}) e de novo na mixagem final.

## Passo a passo
1. História. Gancho nos 3 primeiros segundos: uma pergunta surpreendente sobre o que se vê, com algo grande na tela na palavra-chave. Promessa curta. Capítulos de 4 a 6 s que viram ("mas…", "até que…"). Um dado com número. Fecho que volta ao gancho. Chamada final. Proponha 3 histórias diferentes, com roteiro segundo a segundo e os dados já checados, e me deixe escolher.
2. Dados, com fonte e data, no SPEC.md.
3. Projeto em videos/<nome>/ (cada versão na sua pasta: -v2, -v3…). Se houver template, copie; se não, npx hyperframes init.
4. Roteiro: umas 150 palavras, contado com conectores, não como lista. A última frase é a chamada final.
5. Voz em uma tomada e Whisper. Confira a duração: a voz termina antes do segundo 57.
6. Camadas a partir dos tempos da voz: legendas palavra por palavra (embaixo, a palavra-chave em uma pílula colorida), capítulos, notas, números que caem dígito por dígito e selos para conquistas e erros.
7. Mundo 3D (opcional, Three.js): o protagonista, de verdade; algo novo na tela a cada ~0,2 s.
8. Som: música licenciada que abaixa sob a voz; um efeito para cada ação visível, mais baixo se cair em cima da voz.
9. Revisão: npx hyperframes check com 0 erros e capturas com a zona segura por cima.
10. Pré-visualização aberta no navegador antes de renderizar.
11. Render com -q delivery e medidas: 1800 quadros, −13 a −14 LUFS, pico real ≤ −2 dBTP, sem quadros pretos, Whisper na mixagem.
12. REVIEW.md: o que foi medido, o que não foi e a parte mais fraca.
13. Correções: cada vez que eu corrigir algo, adicione com data em "Correções" do CLAUDE.md antes de continuar e, se valer para sempre, mude aqui também.

## Antes de entregar, confira
- [ ] 0 erros no check e todo o texto dentro da zona segura.
- [ ] A voz termina antes do segundo 57 e o cartão final mostra a chamada.
- [ ] Dados com fonte e data; superlativos checados.
- [ ] A chave não está em nenhum arquivo.
- [ ] Peça para ouvir com fones de ouvido.
````

<aside class="promo-mentor not-prose" aria-label="Mentoria com Oscar Barajas">
<p class="promo-mentor__eyebrow">Mentoria · @gndx</p>
<p class="promo-mentor__title">Compre a pasta com todos os meus aprendizados</p>
<div class="promo-mentor__options">
<p class="promo-mentor__option"><span class="promo-mentor__price">$1,99 USD</span><span class="promo-mentor__detail">Só a pasta</span></p>
<p class="promo-mentor__option promo-mentor__option--featured"><span class="promo-mentor__price">$20 USD</span><span class="promo-mentor__detail">A pasta + mentoria e acompanhamento do seu projeto</span></p>
</div>
<a class="promo-mentor__cta" href="https://mentor.gndx.dev/" target="_blank" rel="noopener">Ir para mentor.gndx.dev <span aria-hidden="true">→</span></a>
</aside>

## O prompt para adaptar a você

Cole isto no Claude Code (ou no seu chat de IA favorito) seguido da sua skill. Ele vai entrevistar você, reescrever a skill para o seu canal e melhorá-la toda vez que você disser o que não gostou em um vídeo:

```text
Você é especialista em skills do Claude Code e em vídeo curto para redes sociais.
Abaixo está o meu SKILL.md. Quero adaptá-lo ao meu canal e melhorá-lo.

1. Leia tudo e me resuma em 5 linhas o que ela faz, quais ferramentas supõe (Claude Code, HyperFrames, ElevenLabs, Whisper, FFmpeg) e quais partes são exemplos (tudo o que está entre {{chaves}}).
2. Me entreviste com uma pergunta por vez (no máximo 12): plataforma e formato, minha conta e meu público, temas, tom e como eu falo, cores e fontes da minha marca, voz (pronta ou clonada, velocidade), frase final, de onde tiro os dados, o que nunca quero ver, o que tenho instalado e onde fica o meu projeto.
3. Com as minhas respostas, reescreva a skill completa: mesma estrutura (cabeçalho, O canal, Estilo, Dados, Voz, Passo a passo, Antes de entregar), sem nenhuma {{chave}} e sem o que não se aplica a mim. Escreva a descrição do cabeçalho para o Claude Code saber quando usá-la.
4. Me diga 3 riscos ou lacunas que você vê (por exemplo: a zona segura da minha plataforma, direitos da música, dados sem fonte, a chave da API) e como a skill os cobre.
5. A partir de agora, toda vez que eu disser o que não gostei em um vídeo, proponha a mudança exata na skill (antes → depois) e adicione a uma seção "Correções" com a data.

Não invente nada sobre mim: se não souber, pergunte.

--- MEU SKILL.md ---
(cole a sua skill aqui)
```

## Para terminar

O que mais me surpreendeu não foi a IA fazendo vídeos: foi que **o sistema aprende com as minhas correções**. Uma frase, uma skill e um registro de erros. O resto é repetir, corrigir e anotar.

Se você fizer a sua versão, me mostre: estou como **@gndx** no Instagram e no YouTube. E se quiser ver o reel que explica este guia em 60 segundos, ele está no meu perfil.
