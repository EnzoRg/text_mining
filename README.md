# Batalla de Gigantes: Comparando LLMs para la Traducción de Lenguaje Natural a SQL

**Autor:** Enzo Manolucos  

<p align="center">
  <img src="/figures/banner.png" alt="Banner" width="500"/>
</p>

## Abstract

Los grandes modelos de lenguaje (LLMs) son cada vez más eficientes en tareas que requieren conocimiento previo, como la interacción con bases de datos. El enfoque **Text-to-SQL** permite convertir instrucciones en lenguaje natural en consultas SQL funcionales. En este proyecto se compara el rendimiento de **Gemini 1.5 Flash** y **GPT-4o Mini**, utilizando el dataset **BIRD** y cuatro métricas de evaluación.

> Los resultados muestran un rendimiento similar, con una ligera ventaja para Gemini 1.5 Flash. Sin embargo, GPT-4o Mini sobresale en consultas complejas con poco contexto.

## 1. Introducción

Text-to-SQL busca generar automáticamente consultas SQL a partir de instrucciones en lenguaje natural. Los LLMs permiten que incluso usuarios sin conocimientos técnicos interactúen con bases de datos de forma efectiva. La calidad de los *prompts* y los datasets de entrenamiento son clave para mejorar estos modelos.

<p align="center">
  <img src="/figures/user_text_to_sql.png" alt="Ejemplo de Text-to-SQL" width="500"/>
</p>

_Un modelo toma un esquema y una pregunta como entrada, y genera una consulta SQL como salida._

[Infome completo](/docs/Informe.pdf)

## 2. Trabajos Previos

### 2.1 Datasets

- **WikiSQL**: operaciones simples `SELECT` y `WHERE`.
- **SPIDER**: consultas complejas y esquemas variados.
- **BIRD**: incorpora conocimiento externo y eficiencia en ejecución.

> ⚠️ *SPIDER 2.0 no estaba disponible al momento de comenzar el proyecto.*

### 2.2 Métodos

- Diferencia actual de precisión:  
  - LLMs: 74.12%  
  - Expertos humanos: 92.96%

- Métodos explorados:
  - Finetuning de modelos con ejemplos Text-to-SQL.
  - Enfoques como **divide and conquer**, razonamiento por planes de ejecución y ejemplos sintéticos.
  - **Divide-and-Prompt** con *Chain of Thought*.


## 3. Experimento

### 3.1 Dataset

Se utilizó el dataset **BIRD**, específicamente la base de datos **Superhero**, con 129 preguntas relacionadas al mundo de los cómics, divididas en las siguientes dificultades:

- 63% Simple
- 26% Moderate
- 12% Challenging

> Esta base contiene solo un 15% de ruido, la menor en BIRD.

### 3.2 Métricas

- **Execution Accuracy (EX):** consultas con resultados idénticos.
- **Valid Efficiency Score (VES):** eficiencia de consultas válidas.
- **Component Matching (CM):** coincidencia exacta entre keywords.
- **Valid SQL (VA):** proporción de consultas sin errores de ejecución.

### 3.3 Modelos Comparados

<p align="center">
  <img src="/figures/models.png" alt="Modelos" width="500"/>
</p>

[Comparación de modelos - LLM Stats](https://llm-stats.com/models/compare/gpt-4o-mini-2024-07-18-vs-gemini-1.5-flash)

**Los modelos utilizados no son de código abierto, lo cual limita la reproducibilidad del experimento.** Sin embargo, fueron elegidos por su disponibilidad y popularidad.

### 3.4 Prompts

- **Zero-Shot**: incluye la tarea y la pregunta, con una variante que incluye conocimiento externo.

- **Few-Shot**: incluye la tarea, la pregunta y ejemplos, con una variante que incluye conocimiento externo.

## 4. Resultados

<p align="center">
  <img src="/figures/table_results.png" alt="Resultados" width="500"/>
</p>

- Ambos modelos obtuvieron una alta tasa de **validación sintáctica (VA)**, por encima del 90%.
- Gemini tuvo mejor desempeño general, particularmente en **VES** y **CM**.
- GPT-4o Mini mostró mejor **razonamiento contextual** en consultas difíciles.

> *GPT-4o Mini fue capaz de inferir relaciones indirectas mejor que Gemini en ciertas consultas complejas, aunque esto no se refleje completamente en las métricas.*

## 5. Conclusiones

- **Gemini 1.5 Flash** tuvo un rendimiento ligeramente superior en las métricas.
- **GPT-4o Mini** demostró mejor razonamiento en ejemplos complejos sin contexto adicional.
- Ambos modelos son aptos para tareas Text-to-SQL, aunque sus fortalezas difieren:
  - Gemini: precisión estructural.
  - GPT-4o: inferencia contextual.
- Se observa como la métrica EX disminuye a medida que la pregunta se vuelve más compleja.

<p align="center">
  <img src="/figures/ex_total_1x4.png" alt="Grafico de resultados" width="1000"/>
</p>

*La elección del modelo puede depender del tipo de consultas esperadas y de la disponibilidad de recursos computacionales.*

## 6. Limitaciones
El análisis se realizó exclusivamente sobre una base de datos del dominio de superhéroes utilizando el dataset BIRD, lo que restringe la generalización de los resultados a otros dominios.

Debido a limitaciones de cómputo, solo se evaluaron dos modelos y se utilizaron dos tipos de prompts. Explorar más modelos o técnicas de prompting podría haber brindado una visión más completa.

Además, al trabajar con modelos propietarios, no se garantiza la reproducibilidad futura de los resultados, ya que estos modelos pueden cambiar con el tiempo. Los resultados reportados corresponden al estado de los modelos en noviembre de 2024.

## 7. Trabajo Futuro
Para mejorar este enfoque, se propone:

- Optimizar los prompts con técnicas de few-shot más avanzadas.
- Evaluar modelos más recientes o especializados en generación de SQL.
- Incorporar métricas que también midan eficiencia computacional.
- Ampliar la base de datos para mejorar la generalización.
- Automatizar el pipeline de evaluación para facilitar su aplicación en nuevos contextos.
- Implementar los modelos en un sistema real para evaluar su impacto práctico.

## Referencias

- [Can LLM Already Serve as a Database Interface? A Big Bench for Large-Scale Database Grounded Text-to-SQLs](https://neurips.cc/)
- [Spider: A Large-Scale Human-Labeled Dataset for Complex and Cross-Domain Semantic Parsing and Text-to-SQL Task](https://arxiv.org/abs/1809.08887) 
- [Seq2SQL: Generating Structured Queries from Natural Language using Reinforcement Learning](https://arxiv.org/abs/1709.00103)
- [Understanding the Effects of Noise in Text-to-SQL: An Examination of the BIRD-Bench Benchmark](https://arxiv.org/abs/2402.12243)
- [Semantic Evaluation for Text-to-SQL with Distilled Test Suite](https://www.aclweb.org/anthology/2020.emnlp-main.582/)
- [How to Prompt LLMs for Text-to-SQL: A Study in Zero-shot, Single-domain, and Cross-domain Settings](https://arxiv.org/abs/2305.11853) 
- [Synthesizing Text-to-SQL Data from Weak and Strong LLMs](https://doi.org/10.48550/arXiv.2408.03256)
- [Benchmarking the Text-to-SQL Capability of Large Language Models: A Comprehensive Evaluation](https://doi.org/10.48550/arXiv.2403.02951) 
- [CHASE-SQL: Multi-Path Reasoning and Preference Optimized Candidate Selection in Text-to-SQL](https://arxiv.org/abs/2410.01943) 
- [Divide and Prompt: Chain of Thought Prompting for Text-to-SQL](https://arxiv.org/abs/2304.11556) 
- [Evaluating the Text-to-SQL Capabilities of Large Language Models](https://arxiv.org/abs/2204.00498)
- [Dr.Spider: A Diagnostic Evaluation Benchmark towards Text-to-SQL Robustness](https://arxiv.org/abs/2301.08881)  
- [A Comprehensive Evaluation of ChatGPT's Zero-shot Text-to-SQL Capability](https://arxiv.org/abs/2303.13547)
- [Large Language Model Enhanced Text-to-SQL Generation: A Survey](https://arxiv.org/abs/2410.06011) 
- [Evaluating LLMs for Text-to-SQL Generation With Complex SQL Workload](https://arxiv.org/abs/2407.19517)  
