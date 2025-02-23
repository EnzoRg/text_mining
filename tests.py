import sqlite3
import time
import math
import re

def exact_match(df, model):
    em = []

    for _, row in df.iterrows():
        predicted_sql = row[model]
        ground_truth = row['ground_truth']

        if predicted_sql == ground_truth:
            em.append(1)
        else:
            em.append(0)

    #print(f'Model: {model}')
    print('-------------------------------')
    print(f'EM - Total:\t\t{sum(em) / len(em) * 100:.2f} %')

    return em

def execution_acc(df, model, db_path):
    ex = []
    err = []

    with sqlite3.connect(db_path) as conn:
        for _, row in df.iterrows():
            predicted_sql = row[model]
            ground_truth = row['ground_truth']

            try:
                cursor = conn.cursor()
                cursor.execute(predicted_sql, ())
                predicted_res = cursor.fetchall()
                cursor.execute(ground_truth, ())
                ground_truth_res = cursor.fetchall()
                res = 0
                if set(predicted_res) == set(ground_truth_res):
                    res = 1
            except sqlite3.Error as e:
                #print(f"An error occurred: {e}")  # Print the error if something goes wrong
                #er = str(row['question_id']) + ': ' + str(e)
                res = 0
                
                #err.append(er)
            ex.append(res)

    #print(f'Execution Accuracy: {sum(ex) / len(ex) * 100:.2f} %')

    return ex #, err

def results_ex(results):
    #print(results['simple'])

    total_sum = sum([sum(valores) for valores in results.values()])
    total_count = sum([len(valores) for valores in results.values()])
    accuracy = (total_sum / total_count) * 100

    simple = (sum(results["simple"]) / len(results["simple"])) * 100
    moderate = (sum(results["moderate"]) / len(results["moderate"])) * 100
    challenging = (sum(results["challenging"]) / len(results["challenging"])) * 100
    total = (total_sum / total_count) * 100

    #print('-------------------------------')
    #print(f'EX - Simple:\t\t{simple:.2f} %')
    #print(f'EX - Moderate:\t\t{moderate:.2f} %')
    #print(f'EX - Challenging:\t{challenging:.2f} %')
    #print('-------------------------------')
    #print(f'EX - Total:\t\t{total:.2f} %')
    print(f'EX:\t{total:.2f} %')
    results = {
        'simple': simple,
        'moderate': moderate,
        'challenging': challenging,
        'total': total
        }
    
    return results


def execution_acc_by_diff(df, model, db_path):
    # Agrupar el dataframe por dificultad
    df_grouped = df.groupby('difficulty')

    # Inicializar un diccionario para almacenar los resultados
    results = {}

    # Iterar sobre los grupos de dificultad
    for difficulty, group in df_grouped:
        # Calcular la ejecución de precisión para cada grupo
        accuracy = execution_acc(group, model, db_path)

        # Almacenar los resultados en el diccionario
        results[difficulty] = accuracy

    # Devolver los resultados
    #print(f'Model: {model}')
    #results = results_ex(results)

    return results_ex(results)
    #return results #, errors

def valid_sql(df, model, db_path):
    ex = []
    err = []

    with sqlite3.connect(db_path) as conn:
        for _, row in df.iterrows():
            predicted_sql = row[model]
            ground_truth = row['ground_truth']

            try:
                cursor = conn.cursor()
                cursor.execute(predicted_sql, ())
                predicted_res = cursor.fetchall()
                cursor.execute(ground_truth, ())
                ground_truth_res = cursor.fetchall()
                res = 0
                if set(predicted_res) == set(ground_truth_res):
                    res = 1
                else:
                    res = 1
            except sqlite3.Error as e:
                #print(f"An error occurred: {e}")  # Print the error if something goes wrong
                #er = str(row['question_id']) + ': ' + str(e)
                res = 0
                
                #err.append(er)
            ex.append(res)

    #print(f'Execution Accuracy: {sum(ex) / len(ex) * 100:.2f} %')

    return ex #, err


def results_va(results):
    #print(results['simple'])

    total_sum = sum([sum(valores) for valores in results.values()])
    total_count = sum([len(valores) for valores in results.values()])

    simple = (sum(results["simple"]) / len(results["simple"])) * 100
    moderate = (sum(results["moderate"]) / len(results["moderate"])) * 100
    challenging = (sum(results["challenging"]) / len(results["challenging"])) * 100
    total = (total_sum / total_count) * 100

    #print('-------------------------------')
    #print(f'VA - Simple:\t\t{simple:.2f} %')
    #print(f'VA - Moderate:\t\t{moderate:.2f} %')
    #print(f'VA - Challenging:\t{challenging:.2f} %')
    #print('-------------------------------')
    #print(f'VA - Total:\t\t{total:.2f} %')
    print(f'VA:\t{total:.2f} %')

    results = {
        'simple': simple,
        'moderate': moderate,
        'challenging': challenging,
        'total': total
        }

    return results


def valid_sql_by_diff(df, model, db_path):
    # Agrupar el dataframe por dificultad
    df_grouped = df.groupby('difficulty')

    # Inicializar un diccionario para almacenar los resultados
    results = {}

    # Iterar sobre los grupos de dificultad
    for difficulty, group in df_grouped:
        # Calcular la ejecución de precisión para cada grupo
        accuracy = valid_sql(group, model, db_path)

        # Almacenar los resultados en el diccionario
        results[difficulty] = accuracy

    # Devolver los resultados
    #print(f'Model: {model}')
    
    
    return results_va(results)


def execute_sql(sql, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    start_time = time.time()
    cursor.execute(sql)
    exec_time = time.time() - start_time
    #print(f'Execution time: {exec_time:.2f} seconds')
    return exec_time

def eficiencia(predicted_sql, ground_truth, db_path, iterate_num):
    time_predicted = []
    time_ground_truth = []

    for i in range(iterate_num):
        #print(i)
        time_predicted.append(execute_sql(predicted_sql, db_path))
        time_ground_truth.append(execute_sql(ground_truth, db_path))

    if sum(time_predicted) != 0:
        eficiencia = math.sqrt(sum(time_ground_truth) / sum(time_predicted))
    else:
        eficiencia = 0.001  # o algún otro valor que tenga sentido en tu caso
    
    #eficiencia = math.sqrt(sum(time_ground_truth) / sum(time_predicted))
    #print(eficiencia)
    return eficiencia


def execution_ves(df, model, db_path, iterate_num=100):
    ex = []
    ves = []
    
    with sqlite3.connect(db_path) as conn:
        for _, row in df.iterrows():
            predicted_sql = row[model]
            ground_truth = row['ground_truth']

            try:
                cursor = conn.cursor()
                cursor.execute(predicted_sql, ())
                predicted_res = cursor.fetchall()
                cursor.execute(ground_truth, ())
                ground_truth_res = cursor.fetchall()
                res = 0
                if set(predicted_res) == set(ground_truth_res):
                    res = 1
                    #print(predicted_sql)
                    ves.append(eficiencia(predicted_sql, ground_truth, db_path, iterate_num))
                    
            except sqlite3.Error as e:
                #print(f"An error occurred: {e}")  # Print the error if something goes wrong
                #er = str(row['question_id']) + ': ' + str(e)
                res = 0
                
                #err.append(er)
            ex.append(res)

    #print(f'Model: {model}')
    #print('-------------------------------')
    #print(f'VES - Total:\t\t{sum(ves) / len(ex) * 100:.2f} %')
    result = sum(ves) / len(ex) * 100

    print(f'VES:\t{result:.2f} %')

    return result #, err


def extract_words(query):
    reserved_words = [
    "ABORT", "ACTION", "ADD", "AFTER", "ALL", "ALTER", "ANALYZE", "AND", "AS", "ASC",
    "ATTACH", "AUTOINCREMENT", "BEFORE", "BEGIN", "BETWEEN", "BY", "CASCADE", "CASE",
    "CAST", "CHECK", "COLLATE", "COLUMN", "COMMIT", "CONFLICT", "CONSTRAINT", "CREATE",
    "CROSS", "CURRENT_DATE", "CURRENT_TIME", "CURRENT_TIMESTAMP", "DATABASE",
    "DEFAULT", "DEFERRABLE", "DEFERRED", "DELETE", "DESC", "DETACH", "DISTINCT", "DO",
    "DROP", "EACH", "ELSE", "END", "ESCAPE", "EXCEPT", "EXCLUDED", "EXISTS", "EXPLAIN",
    "FAIL", "FILTER", "FIRST", "FOLLOWING", "FOR", "FOREIGN", "FROM", "FULL", "GENERATED",
    "GLOB", "GROUP", "GROUPS", "HAVING", "IF", "IGNORE", "IMMEDIATE", "IN", "INDEX",
    "INDEXED", "INITIALLY", "INNER", "INSERT", "INSTEAD", "INTERSECT", "INTO", "IS",
    "ISNULL", "JOIN", "KEY", "LAST", "LEFT", "LIKE", "LIMIT", "MATCH", "NATURAL", "NO",
    "NOT", "NOTHING", "NOTNULL", "NULL", "OF", "OFFSET", "ON", "OR", "ORDER", "OTHERS",
    "OVER", "PARTITION", "PLAN", "PRAGMA", "PRECEDING", "PRIMARY", "QUERY", "RAISE",
    "RANGE", "RECURSIVE", "REFERENCES", "REGEXP", "REINDEX", "RELEASE", "RENAME",
    "REPLACE", "RESTRICT", "RIGHT", "ROLLBACK", "ROW", "ROWS", "SAVEPOINT", "SELECT",
    "SET", "SHOW", "TABLE", "TEMP", "TEMPORARY", "THEN", "TIES", "TO", "TRANSACTION",
    "TRIGGER", "UNBOUNDED", "UNION", "UNIQUE", "UPDATE", "USING", "VACUUM", "VALUES",
    "VIEW", "VIRTUAL", "WHEN", "WHERE", "WINDOW", "WITH", "WITHOUT"]

    result = []

    for word in reserved_words:
        if re.search(r"\b" + word + r"\b", query, re.IGNORECASE):
            result.append(word)

    return result

def exact_set_match(df, model):
    esm = []

    for _, row in df.iterrows():
        predicted_words = extract_words(row[model])
        ground_truth_words = extract_words(row['ground_truth'])

        set_predicted = set(predicted_words)
        set_truth = set(ground_truth_words)

        comun = set_predicted & set_truth

        cantidad_comun = len(comun)

        resultado = len(comun)/len(set_truth)
        esm.append(resultado)

        #if predicted_words == ground_truth_words:
        #    esm.append(1)
        #else:
        #    esm.append(0)

    result = sum(esm) / len(esm) * 100
    
    #print(f'Model: {model}')
    #print('-------------------------------')
    #print(f'EM - Total:\t\t{sum(esm) / len(esm) * 100:.2f} %')  
    print(f'CM:\t{result:.2f} %')  

    return result

def mostrar_metricas(df, model, db_path, iterate_num=100):
    metricas = {}

    print(f'Model: {model}')
    print('-------------------------------')

    # Ejecución de precisión
    #ex = execution_acc(df, model, db_path)
    #metricas['EX'] = results_ex({'simple': ex, 'moderate': ex, 'challenging': ex})

    
    # Ejecución de precisión por dificultad
    ex_by_diff = execution_acc_by_diff(df, model, db_path)
    metricas['EX_by_diff'] = ex_by_diff
    
    # Validación de SQL
    #va = valid_sql(df, model, db_path)
    #metricas['VA'] = results_va({'simple': va, 'moderate': va, 'challenging': va})
 
    # Validación de SQL por dificultad
    va_by_diff = valid_sql_by_diff(df, model, db_path)
    metricas['VA_by_diff'] = va_by_diff

    # Eficiencia
    ves = execution_ves(df, model, db_path, iterate_num)
    metricas['VES'] = ves

    # Coincidencia exacta de conjuntos
    esm = exact_set_match(df, model)
    metricas['CM'] = esm

    return metricas

def execution_errors(df, model, db_path):
    ex = []
    err = []

    with sqlite3.connect(db_path) as conn:
        for _, row in df.iterrows():
            predicted_sql = row[model]
            ground_truth = row['ground_truth']

            try:
                cursor = conn.cursor()
                cursor.execute(predicted_sql, ())
                predicted_res = cursor.fetchall()
                cursor.execute(ground_truth, ())
                ground_truth_res = cursor.fetchall()
                res = 0
                if set(predicted_res) == set(ground_truth_res):
                    res = 1
            except sqlite3.Error as e:
                res = 0
                err.append({
                    'question_id': row['question_id'],
                    'error': str(e),
                    'predicted_sql': predicted_sql,
                    'ground_truth': ground_truth
                })

            ex.append(res)

    return err

def execution_acc_querys(df, model, db_path):
    ex = []

    df_error = pd.DataFrame(columns=['question_id', 'predicted_sql', 'ground_truth'])

    with sqlite3.connect(db_path) as conn:
        for _, row in df.iterrows():
            predicted_sql = row[model]
            ground_truth = row['ground_truth']
            question_id = row['question_id']

            try:
                cursor = conn.cursor()
                cursor.execute(predicted_sql, ())
                predicted_res = cursor.fetchall()
                cursor.execute(ground_truth, ())
                ground_truth_res = cursor.fetchall()
                res = 0
                if set(predicted_res) == set(ground_truth_res):
                    res = 1
                else: 
                    #print(f'Question ID: {question_id}')
                    #print(f'Predicted SQL:\n{predicted_sql}')
                    #print(f'Ground Truth:\n{ground_truth}')      

                    df_error = df_error._append({'question_id': question_id, 'predicted_sql': predicted_sql, 'ground_truth': ground_truth}, ignore_index=True)

            except sqlite3.Error as e:
                print(f'Question ID: {question_id}')
                print(f'Predicted SQL:\n{predicted_sql}')
                print(f'Ground Truth:\n{ground_truth}')
                print(f'Error: {e}\n') 
                res = 0

                #err.append(er)

            ex.append(res)
    return df_error