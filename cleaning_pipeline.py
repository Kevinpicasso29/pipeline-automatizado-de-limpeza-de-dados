import pandas as pd # type: ignore
import numpy as np # type: ignore

# Função para carregar o conjunto de dados
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print(f"Dados carregados com sucesso de {file_path}.")
        return data
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return None

# Função para tratar valores ausentes
def handle_missing_values(df, strategy='mean', columns=None):
    try:
        if columns is None:
            columns = df.columns
            
        for col in columns:
            if df[col].isnull().sum() > 0:
                if strategy == 'mean':
                    df[col].fillna(df[col].mean(), inplace=True)
                elif strategy == 'median':
                    df[col].fillna(df[col].median(), inplace=True)
                elif strategy == 'mode':
                    df[col].fillna(df[col].mode()[0], inplace=True)
                print(f"Valores ausentes na coluna {col} tratados com a estratégia {strategy}.")
            else:
                print(f"Sem valores ausentes na coluna {col}.")
        return df
    except Exception as e:
        print(f"Erro ao tratar valores ausentes: {e}")
        return df

# Função para formatação de dados
def format_data(df):
    try:
        if 'data' in df.columns:
            df['data'] = pd.to_datetime(df['data'], errors='coerce')
            print("Coluna 'data' formatada para datetime.")
        
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].str.strip()
            print(f"Coluna '{col}' formatada (removendo espaços extras).")
        
        return df
    except Exception as e:
        print(f"Erro na formatação dos dados: {e}")
        return df

# Função para detecção e tratamento de outliers
def handle_outliers(df, columns=None):
    try:
        if columns is None:
            columns = df.select_dtypes(include=['float64', 'int64']).columns
        
        for col in columns:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            df[col] = np.where(df[col] < lower_bound, lower_bound, df[col])
            df[col] = np.where(df[col] > upper_bound, upper_bound, df[col])
            print(f"Outliers na coluna '{col}' tratados.")
        
        return df
    except Exception as e:
        print(f"Erro ao tratar outliers: {e}")
        return df

# Função para registrar as ações de limpeza
def log_actions(actions):
    with open('cleaning_log.txt', 'a') as log_file:
        log_file.write("\n".join(actions) + "\n")
        print("Ações registradas no log.")

# Função principal
def clean_data(file_path):
    actions = []
    try:
        df = load_data(file_path)
        if df is None:
            return None
        
        actions.append("Iniciando o tratamento de valores ausentes...")
        df = handle_missing_values(df)
        
        actions.append("Iniciando a formatação de dados...")
        df = format_data(df)
        
        actions.append("Iniciando a detecção e tratamento de outliers...")
        df = handle_outliers(df)
        
        log_actions(actions)
        print("Limpeza de dados concluída.")
        return df
    
    except Exception as e:
        print(f"Erro no pipeline de limpeza de dados: {e}")
        return None

# Executar o pipeline
if __name__ == "__main__":
    cleaned_data = clean_data('data.csv')
