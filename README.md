# 🦉 GrammatikLint

**GrammatikLint** é um corretor gramatical inteligente e acessível, desenvolvido especificamente para apoiar a alfabetização e o letramento de crianças e jovens no Brasil. O projeto combina tecnologia de ponta em Processamento de Linguagem Natural (NLP) com uma interface lúdica e inclusiva para transformar o aprendizado da língua portuguesa em uma experiência interativa.
<img width="1879" height="909" alt="image" src="https://github.com/user-attachments/assets/faa0a5af-cb18-424d-bb5e-19f5ac288e56" />
<img width="1338" height="897" alt="image" src="https://github.com/user-attachments/assets/d8daa052-7a0f-44e2-873b-122cec1d60ed" />

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

## 🚀 Melhorias Funcionais

As melhorias funcionais focam em enriquecer a experiência do usuário e expandir o impacto pedagógico do GrammatikLint.

| Categoria | Sugestão de Melhoria | Descrição Detalhada | Impacto Pedagógico |
| :--- | :--- | :--- | :--- |
| **Feedback Pedagógico** | **Explicações Detalhadas dos Erros** | Além de sugerir a correção, a ferramenta poderia explicar *por que* a frase está incorreta, utilizando exemplos e regras gramaticais simplificadas. Isso transformaria a correção em uma oportunidade de aprendizado ativo. | Aprofunda a compreensão das regras gramaticais, promovendo o aprendizado autônomo e a retenção do conhecimento. |
| **Personalização** | **Dicionário e Regras Personalizáveis** | Permitir que professores ou administradores adicionem palavras (nomes próprios, termos regionais) ou criem/ajustem regras gramaticais específicas para as necessidades de suas turmas ou regiões. | Adapta a ferramenta a diferentes contextos educacionais e culturais, tornando-a mais relevante e precisa para cada usuário. |
| **Acompanhamento** | **Relatórios de Progresso do Aluno** | Desenvolver uma interface para visualizar o histórico de análises de um aluno, identificando padrões de erros, evolução do score de qualidade e áreas que necessitam de mais atenção. | Permite que professores e pais acompanhem o desenvolvimento do aluno, personalizem o ensino e intervenham proativamente. |
| **Engajamento** | **Gamificação Avançada** | Expandir o sistema de "score de qualidade" com elementos de gamificação, como conquistas, níveis, desafios e recompensas virtuais, para motivar o uso contínuo e o aprimoramento. | Aumenta o engajamento e a motivação dos alunos, tornando o aprendizado mais divertido e menos intimidante. |
| **Inclusão** | **Acessibilidade Visual Aprimorada** | Além do suporte a Libras, implementar opções para pessoas com baixa visão (aumento de contraste, fontes de alta legibilidade) e dislexia (fontes específicas, espaçamento ajustável). | Garante que a ferramenta seja verdadeiramente inclusiva para um espectro ainda maior de necessidades educacionais especiais. |
| **Integração** | **Integração com LMS** | Possibilitar a integração do GrammatikLint com plataformas de gestão de aprendizagem (LMS) populares, permitindo o compartilhamento de resultados e atividades. | Facilita a adoção em ambientes escolares já estabelecidos e otimiza o fluxo de trabalho de professores. |

## ⚙️ Melhorias Técnicas

As melhorias técnicas visam otimizar a arquitetura, a performance e a manutenibilidade do sistema, garantindo sua escalabilidade e confiabilidade.

| Categoria | Sugestão de Melhoria | Descrição Detalhada | Benefício |
| :--- | :--- | :--- | :--- |
| **Arquitetura** | **Refatoração do Backend** | Separar claramente as responsabilidades entre os módulos. O `nlp.py` e `rules.py` devem ser bibliotecas de funções puras, enquanto `main.py` deve ser o ponto de entrada da API, orquestrando as chamadas. | Melhora a modularidade, testabilidade e manutenibilidade do código, facilitando futuras expansões. |
| **Testes** | **Implementação de Testes Automatizados** | Desenvolver testes unitários para as funções de análise (`nlp.py`, `rules.py`) e testes de integração para as rotas da API (`main.py`). | Garante a correção do código, previne regressões e facilita a introdução de novas funcionalidades com confiança. |
| **Implantação** | **Dockerização Completa** | Finalizar e otimizar o `docker-compose.yml` para incluir o backend (FastAPI) e, opcionalmente, servir o frontend estático. Isso padroniza o ambiente de execução. | Simplifica a implantação em diferentes ambientes (escolas, servidores), garantindo consistência e reduzindo problemas de configuração. |
| **Performance** | **Otimização do Processamento de Texto** | Para textos muito longos, explorar técnicas como processamento em lote, cache de resultados ou a utilização de modelos spaCy mais leves, se aplicável, para manter a responsividade. | Garante uma experiência de usuário fluida, mesmo com grandes volumes de texto, essencial para uso em sala de aula. |
| **Configuração** | **Gerenciamento de Configurações** | Utilizar variáveis de ambiente ou um arquivo de configuração (`.env`, `config.ini`) para parâmetros como o caminho do banco de dados ou configurações do spaCy. | Facilita a configuração e adaptação do sistema para diferentes ambientes sem alterar o código-fonte. |
| **Logging** | **Sistema de Logging Robusto** | Implementar um sistema de logging adequado para registrar eventos, erros e informações de depuração, auxiliando na identificação e resolução de problemas. | Melhora a capacidade de monitoramento e depuração do sistema em produção. |



Desenvolvido com ❤️ para a educação brasileira.
