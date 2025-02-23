# Batalla de Gigantes: Comparando LLMs para la traducción de lenguaje natural a SQL


## Resumen
Los grandes modelos de lenguaje (LLMs) son cada vez más eficientes en tareas que requieren conocimiento previo, como la interacción con bases de datos para almacenar, organizar y compartir información. El enfoque Text-to-SQL permite convertir instrucciones en lenguaje natural, proporcionadas por un usuario, en querys SQL funcionales, por lo que evaluar su rendimiento es clave. Este proyecto compara el rendimiento de Gemini 1.5 Flash y GPT-4o mini, utilizando una base de datos diseñada para la evaluación y cuatro métricas para medir la efectividad. Los resultados muestran un desempeño similar, con una ligera ventaja para Gemini 1.5 Flash, aunque GPT-4o mini sobresale en querys complejas con poco contexto.

## Hipótesis
Los modelos de lenguaje pre entrenados, como Gemini o GPT, lograrán un mejor rendimiento en tareas de traducción de lenguaje natural a SQL en entornos de few-shot learning, comparados con escenarios de zero-shot. Además, se espera que el modelo Gemma, supere a los anteriores modelos en cuanto a consultas SQL complejas.

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

# Resultados 
La Tabla muestra los resultados de la smétricas  evaluadas, separadas en Zero-shot y Few-shot. Se observa una clara mejora al darle más ejemplos al modelo para generar la query (Few-shot). Debido a que la métrica VES parte de los resultados de EX, pero multiplicado por una constante que representa el tiempo de ejecución, presenta un valor mayor indicando que las querys generadas son eficientemente peor al ejecutarse comparadas con las querys verdades. La métrica que mejor resultados presento fue VA. Esta métrica no es de gran ayuda para el objetivo de este proyecto pero si para verificar que los modelos tienen la capacidad de generar querys que se puede ejecutar sin errores. Por ultimo
la métrica CM es peor en cuanto a resultados, esto se debe a que compara uno a uno los resultados con las querys verdaderas. La figura 2 muestra los resultados agrupados
según la dificultad de la pregunta. Se observa una como la métrica EX disminuye a medida que la pregunta se vuelve más compleja.

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

## Referencias
- [BIRD-SQL: A BIg Bench for Large-Scale Database Grounded Text-to-SQLs](https://bird-bench.github.io/)
- [C3: Zero-shot Text-to-SQL with ChatGPT](https://paperswithcode.com/paper/c3-zero-shot-text-to-sql-with-chatgpt)
- [A comprehensive evaluation of ChatGPT's zero-shot Text-to-SQL capability](https://paperswithcode.com/paper/a-comprehensive-evaluation-of-chatgpt-s-zero)
- [ChatGPT for SQL: How to Write SQL Queries with OpenAI](https://popsql.com/blog/chatgpt-for-sql)
- [Natural Language to SQL using ChatGPT](https://medium.com/@soumyansh/natural-language-to-sql-using-chatgpt-cb330d055180)
