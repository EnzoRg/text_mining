# Evaluación comparativa y desarrollo experimental de modelos de lenguaje para la transformación de lenguaje natural a consultas SQL

## Resumen
El objetivo de este proyecto es analizar diferentes modelos de lenguaje de gran tamaño (LLM) como GPT, LLaMA y Gemini, para generar consultas (querys) SQL a partir de indicaciones en lenguaje natural. Se utilizará el dataset Spider, que contiene diversas consultas SQL emparejadas con descripciones en lenguaje natural, permitiendo evaluar el rendimiento de los modelos en escenarios variados y complejos. Las evaluaciones se llevarán a cabo en tres etapas, aplicando estrategias de zero-shot, one-shot y few-shot learning. Las métricas principales serán la Execution Accuracy (EX) y el Valid Efficiency Score (VES), que medirán la precisión y la eficiencia en la generación de consultas SQL. Este análisis comparativo permitirá identificar las fortalezas y limitaciones de cada enfoque, con el objetivo de mejorar la interacción entre usuarios no técnicos y bases de datos.

## Hipótesis
Los modelos de lenguaje pre entrenados, como GPT y LLaMA, lograrán un mejor rendimiento en tareas de traducción de lenguaje natural a SQL en entornos de few-shot learning, comparados con escenarios de zero-shot. Además, se espera que el modelo Gemini, supere a los anteriores modelos en cuanto a consultas SQL complejas.

## Objetivos 
- Comparar el rendimiento de modelos de lenguaje 
- Evaluar el impacto de los diferentes prompts 
- Explorar la capacidad de los modelos para manejar consultas de diferentes niveles de complejidad
- Identificar y analizar los principales errores en la generación de querys 
- Optimizar los prompts utilizados en cada modelo para obtener los mejores resultados

## Técnicas relevantes

## Planificación 

## Referencias
