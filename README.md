# Batalla de Gigantes: Comparando LLMs para la traducción de lenguaje natural a SQL

**Enzo Nicolás Manolucos**

<p align="center">
  <img src="/imagen/banner.png" alt="Banner" width="500"/>
</p>

## Abstract 
Los grandes modelos de lenguaje (LLMs) son cada vez más eficientes en tareas que requieren conocimiento previo, como la interacción con bases de datos para almacenar, organizar y compartir información. El enfoque Text-to-SQL permite convertir instrucciones en lenguaje natural, proporcionadas por un usuario, en *querys* SQL funcionales, por lo que evaluar su rendimiento es clave. Este proyecto compara el rendimiento de Gemini 1.5 Flash y GPT-4o mini, utilizando una base de datos diseñada para la evaluación y cuatro métricas para medir la efectividad. Los resultados muestran un desempeño similar, con una ligera ventaja para Gemini 1.5 Flash, aunque GPT-4o mini sobresale en *querys* complejas con poco contexto.

## Introducción 
Text-to-SQL es un tipo de tarea en el procesamiento de lenguaje natural (NLP) cuyo objetivo es generar automáticamente querys SQL a partir de texto en lenguaje natural. Esta tarea implica convertir instrucción de texto de entrada a una representación estructurada y luego utilizar esta representación para generar una query SQL semánticamasnte correcta que pueda ejecutarse en una base datos.


A través del uso de grandes modelos de lenguaje (LLMs), un usuario sin conocimientos o con los conocimientos mínimos de los datos puede acceder a bases de datos e interactuar con ellas mediante Text-to-SQL. Los LLMs han emergido como grandes
herramientas, demostrando un gran potencial para comprender preguntas complejas y poder traducirlas de forma precisa.


Además, el uso óptimo de los prompts juega un papel crucial al momento de darle indicaciones a los LLMs para generación querys SQL. Para madurar estos modelos, se desarrollaron a lo largo de los años diversos datasets y métricas exclusivamente
diseñadas para este tipo de tareas.



<p align="center">
  <img src="/imagen/user_text_to_sql.png" alt="Ejemplo de Text-to-SQL" width="500"/>
</p>

Figura 1: Ejemplo de una tarea Text-to-SQL. Un usuario brinda el esquema el cual describe la base de datos y una pregunta relacionada al mismo. El modelo toma el
esquema y la pregunta como la entrada, y genera una *query* SQL como salida.

## Trabajos Previos

### Datasets

Existen diversos datasets para evaluar esta tarea. WikiSQL (Zhong et al., 2017) es un dataset que contempla operaciones simples del tipo SELECT y WHERE sin incluir *querys* anidades ni operaciones del tipo JOIN. Más tarde se desarrollo SPIDER (Yu
et al., 2018) para ser una aproximación más certera a escenarios del mundo real, donde los modelos deben crear *querys* complejas y entender el esquema de la
base de datos.


Recientemente[^1] se creó BIRD (Li et al., 2024) para cerrar la brecha entre investigación académica y aplicaciones de la industria. Este dataset intro-
duce preguntas que requieren conocimiento externo y optimización en la ejecución de las *querys*.

[^1]: SPIDER 2.0 no había sido lanzado al momento de iniciar este proyecto.

### Métodos 

Existe una diferencia significativa en la precisión entre LLMs (74.12 %) y una persona experta en el dominio (92.96 %)[^2]. Debido a que aun existe una diferencia grande entre ambos, se da la necesidad de continuar con el desarrollo de los LLMs destinados a esta tarea para poder equiparar los resultados.


Se exploraron diversos enfoques para crear modelos capaces de realizar tareas Text-to-SQL. Una forma de hacerlo es mediante el finetune sobre LLMs
en ejemplos del tipo Text-to-SQL. Este proceso implica utilizar un modelo preentrenado, la preparación de los datos, el ajuste de parámetros y la evaluación.
El objetivo es generar resultados precisos y que se adapten a este tipo de tareas.


Los autores (Pourreza et al., 2024) proponen generar respuestas utilizando estrategias como el enfoque divide y vencerás, razonamiento basado en planes de ejecución y ejemplos sintéticos personalizados. Luego un agente selecciona la mejor query basado en comparaciones.


Los autores (Liu and Tan, 2023) proponen un nuevo paradigma llamado Divide-and-Prompt, basado en la técnica Chain of Thought (CoT), que guía al modelo mediante un proceso de razonamiento paso a paso. Este enfoque combina la división de tareas complejas en subtareas manejables con la aplicación del razonamiento CoT para resolver cada una de ellas.

[^2]: BIRD-Bench Leaderboard ingresado el 11-11-2024.

## Experimento 

### Dataset 
El dataset de BIRD es usado en este proyecto ya que esta orientado a escenarios más reales y del mundo real de las bases de datos, contempla diferentes campos de dominio y presenta tres niveles de complejidad: Simple, Moderate y Challenging.


Contiene 12.721 preguntas con sus respectivas querys SQL y 95 bases de datos, con un tamaño total de 33.4 GB. Debido a su tamaño y alcance significativos, el experimento se llevó a cabo utilizando únicamente una base de datos.


Superhero incluye querys relacionadas al mundo de los comics con un total de 129 preguntas con su query, divididas en 63% Simple, 26% Moderate y 12% Challenging. Si bien trabajos previos (Wretbladet al., 2024) demostraron la existencia de ruido en
todo de BIRD, esta base de datos presenta el menor nivel de ruido, con un 15%. En el apéndice A se describe con más detalle la base de datos.

### Métricas
Para evaluar el desempeño de los modelos, se decidió utilizar las siguientes métricas:
- **Execution Accuracy (EX)** mide la proporción de querys en los que los resultados ejecutados entre las querys predichas y las verdades son idénticos, en relación total de querys SQL.
- **Valid Efficiency Score (VES)** mide la eficiencia de las querys generadas válidas por los modelos. Esto se refiere a las querys generadas cuyos resultados coinciden con las querys verdaderas. La eficiencia, en este caso, se refiere al tiempo de ejecución.
- **Component Matching (CM)** mide la coincidencia exacta promedio entre los keywords de las querys generadas y las querys verdaderas (Yu et al., 2018).
- **Valid SQL (VA)** mide la proporción de querys generadas que pueden ejecutarse sin errores, indistintamente del resultado (Zhong et al.,2020).

Las dos primeras métricas son las utilizadas en el dataset seleccionado (Li et al., 2024). CM servirá para analizar las querys generadas por palabras y VA para demostrar que los modelos pueden generar querys sin errores.

### Modelos 

Los modelos utilizados son Gemini 1.5 Flash y GPT-4o mini, a través de sus APIs. La decisión de utilizar estos modelos radica en su facil acceso y su popularidad entre los usuarios, donde nace el titulo de este proyecto al comparar estos dos grandes modelos para este tipo de tareas. La Tabla 1 muestra la comparación[^3] de los modelos utilizados.

<p align="center">
  <img src="/imagen/models.png" alt="Modelos" width="500"/>
</p>

Tabla 1: Comparación entre los modelos Gemini 1.5 Flash y GPT-4o Mini utilizados en este proyecto.

Además estos modelos, y sus variantes, son los que mejor resultados presentan en el leaderbord[^4] de BIRD.

[^3]: Datos obtenidos de LLM Stats. 
[^4]: BIRD-Bench Leaderboard ingresado el 11-11-2024.

# Resultados 
La Tabla muestra los resultados de la smétricas  evaluadas, separadas en Zero-shot y Few-shot. Se observa una clara mejora al darle más ejemplos al modelo para generar la query (Few-shot). Debido a que la métrica VES parte de los resultados de EX, pero multiplicado por una constante que representa el tiempo de ejecución, presenta un valor mayor indicando que las querys generadas son eficientemente peor al ejecutarse comparadas con las querys verdades. La métrica que mejor resultados presento fue VA. Esta métrica no es de gran ayuda para el objetivo de este proyecto pero si para verificar que los modelos tienen la capacidad de generar querys que se puede ejecutar sin errores. Por ultimo
la métrica CM es peor en cuanto a resultados, esto se debe a que compara uno a uno los resultados con las querys verdaderas. 

<p align="center">
  <img src="/imagen/table_results.png" alt="Tabla de resultados" width="500"/>
</p>

Tabla 2: Comparación entre los modelos Gemini 1.5 Flash y GPT-4o Mini utilizados en este proyecto.


# Conclusiones
Al analizar los resultados en la Figura se observa como los modelos tienden a disminuir su eficiencia en las querys generadas a medida que la complejidad de las preguntas aumenta, en especial en los niveles Challenging. Aunque para este último caso, GPT-4o mini tiene una amplia ventaja. En general ambos modelos presentan resultados similares debido a que son versiones de los productos que compiten directamente. En conclusión, esta
 batalla la podría haber ganado Gemini 1.5 Flash, si el usuario utiliza un instrucción y pregunta clara. Cuando menos contexto tiene, GPT-4o mini es superior. Estos hallazgos resaltan la importancia de ajustar el número de ejemplos proporcionados y considerar estrategias que mejoren la precisión de las consultas generadas, especialmente en escenarios con preguntas de mayor dificultad.

<p align="center">
  <img src="/imagen/ex_total_1x4.png" alt="Grafico de resultados" width="1000"/>
</p>
Figura 2: Resultados evaluando los modelos con Execution Accuracy (EX).

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

