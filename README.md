# Discord Image Classification Bot 🤖

Este projeto é um bot para Discord capaz de analisar imagens usando um modelo de inteligência artificial treinado no Teachable Machine.

## 🚀 O que o bot faz

O bot recebe uma imagem enviada em um canal do Discord e utiliza um modelo de inteligência artificial para identificar se a imagem mostra:

* 🐱 Gato real
* 🤖 Gato gerado por IA

Depois da análise, o bot envia o resultado no próprio canal do Discord junto com a porcentagem de confiança da classificação.

## 🧠 Como funciona

O projeto utiliza um modelo treinado no Teachable Machine.

O processo funciona assim:

1. O usuário envia uma imagem no Discord.
2. O comando `$check` é utilizado.
3. O bot salva a imagem.
4. O modelo de inteligência artificial analisa a imagem.
5. O bot identifica a classe com maior probabilidade.
6. O resultado é enviado para o Discord.

## 📁 Arquivos principais

* `main.py` — código principal do bot do Discord.
* `model.py` — código responsável por carregar o modelo e analisar as imagens.
* `keras_model.h5` — modelo de inteligência artificial treinado.
* `labels.txt` — nomes das classes utilizadas pelo modelo.

## 💻 Tecnologias utilizadas

* Python
* Discord.py
* TensorFlow
* Keras
* NumPy
* Pillow
* Teachable Machine

## 📸 Exemplo

O usuário pode enviar uma imagem de um gato e utilizar:

`$check`

O bot então responde com algo parecido com:

`Gato real - 99.98%`

## 📌 Objetivo

O objetivo deste projeto é aprender como utilizar inteligência artificial para classificação de imagens e integrá-la a um bot do Discord.

## 👨‍💻 Autor

Yago Davi
