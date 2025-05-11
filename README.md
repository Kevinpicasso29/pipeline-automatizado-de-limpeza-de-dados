# 🧹 Pipeline Automatizado de Limpeza de Dados

Este projeto é um pipeline automatizado para limpeza de dados utilizando **Python** e **pandas**. Ele é útil para qualquer pessoa que esteja trabalhando com dados reais, que geralmente vêm com valores ausentes, formatos inconsistentes e outliers. Automatizar esse processo economiza tempo e melhora a qualidade da análise de dados ou dos modelos de machine learning.

---

## 📌 Objetivo

Criar um script **modular e reutilizável** que:

- Carregue dados a partir de um arquivo CSV
- Trate valores ausentes
- Formate colunas com problemas de digitação ou tipo
- Detecte e trate outliers (valores extremos)
- Registre todas as etapas realizadas em um log

---

## 🚀 Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)

---

## ⚙️ Funcionalidades

### 1. Carregamento de Dados
- Lê arquivos `.csv` com pandas.
- Exibe mensagens claras em caso de erro (ex: caminho errado ou arquivo inválido).

### 2. Tratamento de Valores Ausentes
- Detecta colunas com valores nulos.
- Permite preencher usando:
  - Média (`mean`)
  - Mediana (`median`)
  - Moda (`mode`)

### 3. Formatação de Dados
- Converte colunas chamadas `data` para o tipo `datetime`.
- Remove espaços em branco extras em colunas de texto.

### 4. Detecção e Tratamento de Outliers
- Utiliza o método **IQR (Interquartile Range)** para identificar valores extremos.
- Substitui valores muito altos ou baixos por limites aceitáveis (limite inferior/superior).

### 5. Log das Ações
- Registra todas as etapas realizadas no arquivo `cleaning_log.txt`.

---

## 🧪 Exemplo de Dados de Entrada (`data.csv`)

```csv
id,nome,idade,data,quantidade
1,João,25,2023-01-01,10
2,Maria,,2023-01-02,-5
3,José,30,2023-01-03,20
4,Ana,,,
5,Pedro,22,2023-01-05,15


