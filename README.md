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
la métrica CM es peor en cuanto a resultados, esto se debe a que compara uno a uno los resultados con las querys verdaderas. 
<img src="https://github.com/EnzoRg/text_mining/blob/main/imagen/table_results.png" alt="Table" width="250"/>

# Conclusiones
Al analizar los resultados en la Figura se observa como los modelos tienden a disminuir su eficiencia en las querys generadas a medida que la complejidad de las preguntas aumenta, en especial en los niveles Challenging. Aunque para este último caso, GPT-4o mini tiene una amplia ventaja. En general ambos modelos presentan resultados similares debido a que son versiones de los productos que compiten directamente. En conclusión, esta
 batalla la podría haber ganado Gemini 1.5 Flash, si el usuario utiliza un instrucción y pregunta clara. Cuando menos contexto tiene, GPT-4o mini es superior. Estos hallazgos resaltan la importancia de ajustar el número de ejemplos proporcionados y considerar estrategias que mejoren la precisión de las consultas generadas, especialmente en escenarios con preguntas de mayor dificultad.
![image](https://github.com/EnzoRg/text_mining/blob/main/imagen/ex_total_1x4.png)

## Referencias
- [Can LLM Already Serve as a Database Interface? A Big Bench for Large-Scale Database Grounded Text-to-SQLs](https://neurips.cc/) - Li et al., 2024  
- [Spider: A Large-Scale Human-Labeled Dataset for Complex and Cross-Domain Semantic Parsing and Text-to-SQL Task](https://arxiv.org/abs/1809.08887) - Yu et al., 2018  
- [Seq2SQL: Generating Structured Queries from Natural Language using Reinforcement Learning](https://arxiv.org/abs/1709.00103) - Zhong et al., 2017  
- [Understanding the Effects of Noise in Text-to-SQL: An Examination of the BIRD-Bench Benchmark](https://arxiv.org/abs/2402.12243) - Wretblad et al., 2024  
- [Semantic Evaluation for Text-to-SQL with Distilled Test Suite](https://www.aclweb.org/anthology/2020.emnlp-main.582/) - Zhong et al., 2020  
- [How to Prompt LLMs for Text-to-SQL: A Study in Zero-shot, Single-domain, and Cross-domain Settings](https://arxiv.org/abs/2305.11853) - Chang & Fosler-Lussier, 2023  
- [Synthesizing Text-to-SQL Data from Weak and Strong LLMs](https://doi.org/10.48550/arXiv.2408.03256) - Yang et al., 2024  
- [Benchmarking the Text-to-SQL Capability of Large Language Models: A Comprehensive Evaluation](https://doi.org/10.48550/arXiv.2403.02951) - Zhang et al., 2024  
- [CHASE-SQL: Multi-Path Reasoning and Preference Optimized Candidate Selection in Text-to-SQL](https://arxiv.org/abs/2410.01943) - Pourreza et al., 2024  
- [Divide and Prompt: Chain of Thought Prompting for Text-to-SQL](https://arxiv.org/abs/2304.11556) - Liu & Tan, 2023  
- [Evaluating the Text-to-SQL Capabilities of Large Language Models](https://arxiv.org/abs/2204.00498) - Rajkumar et al., 2022  
- [Dr.Spider: A Diagnostic Evaluation Benchmark towards Text-to-SQL Robustness](https://arxiv.org/abs/2301.08881) - Chang et al., 2023  
- [A Comprehensive Evaluation of ChatGPT's Zero-shot Text-to-SQL Capability](https://arxiv.org/abs/2303.13547) - Liu et al., 2023  
- [Large Language Model Enhanced Text-to-SQL Generation: A Survey](https://arxiv.org/abs/2410.06011) - Zhu et al., 2024  
- [Evaluating LLMs for Text-to-SQL Generation With Complex SQL Workload](https://arxiv.org/abs/2407.19517) - Ma et al., 2024  

