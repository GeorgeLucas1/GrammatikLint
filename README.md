# 🦉 GrammatikLint

**GrammatikLint** é um corretor gramatical inteligente e acessível, desenvolvido especificamente para apoiar a alfabetização e o letramento de crianças e jovens no Brasil. O projeto combina tecnologia de ponta em Processamento de Linguagem Natural (NLP) com uma interface lúdica e inclusiva para transformar o aprendizado da língua portuguesa em uma experiência interativa.

---

## 🌟 Propósito Social

O Brasil ainda enfrenta grandes desafios na educação, com cerca de **9,1 milhões de pessoas** que não sabem ler ou escrever (IBGE 2024). O analfabetismo atinge de forma desproporcional a região Nordeste (11,1%) e populações pretas e pardas.

O **GrammatikLint** nasceu para ser mais do que uma ferramenta técnica; ele é uma proposta de **política pública federal**. Sua missão é:
- **Combater o analfabetismo funcional** através de feedback imediato e pedagógico.
- **Democratizar o acesso**, funcionando localmente sem dependência de APIs pagas ou internet constante.
- **Promover a inclusão**, contando com suporte nativo a **Libras** para alunos surdos.

---

## 🚀 Funcionalidades

- **Análise Inteligente:** Identifica erros de concordância nominal e verbal, ortografia, pontuação e repetições.
- **Entrada por Voz:** Permite que o estudante fale a frase, facilitando o uso para quem ainda está desenvolvendo a escrita.
- **Score de Qualidade:** Atribui uma nota ao texto, incentivando a melhoria contínua de forma gamificada.
- **Privacidade e Offline:** Processamento local via Python e spaCy, garantindo que os dados não saiam da escola.
- **Acessibilidade:** Integração com o widget **VLibras** para garantir que todos possam aprender.

---

## 🛠️ Tecnologia

O coração do projeto utiliza tecnologias de padrão industrial adaptadas para o contexto educacional:

| Componente | Tecnologia | Descrição |
| :--- | :--- | :--- |
| **Motor de NLP** | [spaCy](https://spacy.io/) | Biblioteca de código aberto para processamento de linguagem humana. |
| **Backend** | [FastAPI](https://fastapi.tiangolo.com/) | API de alta performance em Python para gerenciar as análises. |
| **Banco de Dados** | SQLite | Armazenamento local de histórico e análises para acompanhamento pedagógico. |
| **Front-end** | HTML5, CSS3, JS | Interface temática de "sala de aula" (quadro negro e caderno). |
| **Voz** | Web Speech API | Captura de áudio diretamente no navegador. |

---

## 📦 Como Executar

### Pré-requisitos
- Python 3.10+
- Modelo de português do spaCy (`pt_core_news_sm`)

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/GeorgeLucas1/GrammatikLint.git
   cd GrammatikLint
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   python -m spacy download pt_core_news_sm
   ```

3. Inicie o servidor backend:
   ```bash
   python main.py
   ```
   *(Nota: O servidor rodará em `http://localhost:8000`)*

4. Abra a interface:
   Basta abrir o arquivo `front-end/site.html` no seu navegador preferido.

---

## 🦉 Visão de Futuro

O GrammatikLint aspira tornar-se uma ferramenta padrão em escolas públicas de todo o país, servindo como um "professor assistente" digital que nunca se cansa, nunca julga e está sempre pronto para ensinar com clareza e paciência.

---
Desenvolvido com ❤️ para a educação brasileira.
