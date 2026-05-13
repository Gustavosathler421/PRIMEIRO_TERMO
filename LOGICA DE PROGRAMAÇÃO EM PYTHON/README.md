# PRIMEIRO_TERMO
Material para o 1°Termo - LOPAL - SOP - ARI - LER

##LOPAL
Lógica de programação em Python

##SOP
Sistemas operacionais

##ARI
arquitetura IoT
# Aula: Engenharia de Requisitos - Engenharia e Técnicas de Elicitação

## 📌 Conteúdo da Aula
Este documento serve como guia de apoio para o entendimento do processo de descoberta, documentação e validação das necessidades de um sistema de software junto aos stakeholders.

---

## 🛠️ 1. Requisitos Funcionais vs. Não-Funcionais

### 🔹 Requisitos Funcionais (RF)
* Definição: Descrevem o que o sistema **deve fazer** (comportamentos, ações e recursos).
* **Exemplo 1:** O sistema deve permitir que o administrador exclua cadastros de usuários.
* **Exemplo 2:** O sistema deve enviar um e-mail de confirmação após a compra.

### 🔹 Requisitos Não-Funcionais (RNF)
* Definição: Descrevem as **restrições, qualidades e propriedades** sob as quais o sistema deve operar (desempenho, segurança, usabilidade).
* **Exemplo 1:** O sistema deve carregar qualquer página em menos de 1.5 segundos.
* **Exemplo 2:** Os dados de pagamento devem seguir o padrão de criptografia PCI-DSS.

---

## 📊 2. Modelagem através de Diagramas
Os diagramas traduzem os requisitos em modelos visuais antes do início do desenvolvimento do código.

* **Diagrama de Casos de Uso (UML):** Representa os atores do sistema (usuários, outros sistemas) e suas interações com as funcionalidades do software.
* **Diagrama de Classes:** Mapeia a estrutura estática do sistema, mostrando os objetos e como eles se relacionam.
* **Diagrama de Fluxo de Dados (DFD):** Demonstra como as informações se movem através do sistema, desde a entrada até o armazenamento.

---

## 🗂️ 3. Técnicas de Levantamento de Requisitos

### 🗣️ A. Entrevistas
* **O que é:** Conversa direta e direcionada entre o analista e os stakeholders.
* **Formatos:** Estruturada (perguntas fixas) ou não-estruturada (discussão aberta).
* **Vantagem:** Excelente para entender em profundidade o modelo de negócio atual e as principais dores do cliente.

### 🧠 B. Brainstorming
* **O que é:** Reunião dinâmica em grupo para geração em massa de novas ideias sem julgamentos prévios.
* **Processo:** Foco em quantidade de ideias na primeira fase, seguido por filtragem e categorização dos requisitos.
* **Vantagem:** Estimula a criatividade e ajuda a descobrir requisitos inovadores que um único usuário não pensaria sozinho.

### 📱 C. Prototipagem
* **O que é:** Construção de modelos rápidos e interativos das telas do software (baixa, média ou alta fidelidade).
* **Objetivo:** Dar uma visão tangível do produto final antes que a equipe escreva o código real.
* **Vantagem:** Reduz ruídos de comunicação, permitindo que o cliente valide se o fluxo desenhado atende às suas reais necessidades.

---

## 📑 4. Relatórios Técnicos (Especificação de Requisitos)
Os dados coletados nas técnicas acima devem ser consolidados em documentos formais conhecidos como **Especificação de Requisitos de Software (ERS)**.

* **Objetivo do Relatório:** Servir como um contrato técnico entre o cliente e a equipe de desenvolvimento.
* **Estrutura Básica:**
  1. Escopo e Objetivos do Sistema.
  2. Descrição Geral dos Atores.
  3. Matriz de Rastreabilidade (vinculando RFs a RNFs).
  4. Critérios de Aceitação (condições para validar que o requisito foi entregue com sucesso).
