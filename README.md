# Batalla de Gigantes: Comparando modelos de lenguaje para la traducción de lenguaje natural a SQL


## Resumen
El objetivo de este proyecto es analizar diferentes modelos de lenguaje de gran tamaño (LLM) como GPT, LLaMA y Gemma, para generar consultas (querys) SQL a partir de indicaciones en lenguaje natural. Se utilizará el dataset BIRD, que contiene tanto consultas SQL simples como complejas con su respectiva descripciones en lenguaje natural, permitiendo evaluar el rendimiento de los modelos en escenarios variados. Las evaluaciones se llevarán a cabo en tres etapas, aplicando estrategias de zero-shot, one-shot y few-shot learning. Las métricas principales serán la Execution Accuracy (EX) y el Valid Efficiency Score (VES), que medirán la precisión y la eficiencia en la generación de consultas SQL. Este análisis comparativo permitirá identificar las fortalezas y limitaciones de cada enfoque, con el objetivo de mejorar la interacción entre usuarios no técnicos y bases de datos.

## Hipótesis
Los modelos de lenguaje pre entrenados, como GPT y LLaMA, lograrán un mejor rendimiento en tareas de traducción de lenguaje natural a SQL en entornos de few-shot learning, comparados con escenarios de zero-shot. Además, se espera que el modelo Gemma, supere a los anteriores modelos en cuanto a consultas SQL complejas.

## Objetivos 
- Comparar el rendimiento de modelos de lenguaje 
- Evaluar el impacto de los diferentes prompts para mejorar resultados 
- Explorar la capacidad de los modelos para manejar consultas de diferentes niveles de complejidad
- Identificar y analizar los principales errores en la generación de querys 
- Optimizar los prompts utilizados en cada modelo para obtener los mejores resultados

## Técnicas relevantes
- Transformers 
- Prompt engineering
- Métricas de evalución
- Análisis de error
- Correlación 

## Planificación 
- Modelos evaluados: se seleccionarán los siguientes modelos para la generación de querys: 
  - GPT
  - LLaMA
  - Gemma
- Dataset: se utilizará el dataset mini-dev BIRD 
- Estrategias de prompts:  
  - Zero-shot: Se le pide al modelo que genere respuestas sin ejemplos previos
  - One-shot: Se le proporciona un ejemplo previo para mejorar la generación
  - Few-shot: Se le proporcionan varios ejemplos previos, incluyendo cabeceras de tablas
- Métricas de evaluación: 
  - Execution Accuracy (EX): Mide si la consulta generada devuelve los resultados correctos al ser ejecutada en la base de datos.
  - Valid Efficiency Score (VES): Mide la eficiencia en la generación de consultas válidas dentro de un tiempo razonable.
- Análisis de errores: se clasificarán los errores en las respuestas generada


## Referencias
- [BIRD-SQL: A BIg Bench for Large-Scale Database Grounded Text-to-SQLs](https://bird-bench.github.io/)
- [C3: Zero-shot Text-to-SQL with ChatGPT](https://paperswithcode.com/paper/c3-zero-shot-text-to-sql-with-chatgpt)
- [A comprehensive evaluation of ChatGPT's zero-shot Text-to-SQL capability](https://paperswithcode.com/paper/a-comprehensive-evaluation-of-chatgpt-s-zero)
- [ChatGPT for SQL: How to Write SQL Queries with OpenAI](https://popsql.com/blog/chatgpt-for-sql)
- [Natural Language to SQL using ChatGPT](https://medium.com/@soumyansh/natural-language-to-sql-using-chatgpt-cb330d055180)
