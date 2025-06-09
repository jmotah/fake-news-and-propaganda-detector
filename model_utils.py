import pandas as pd

def normalize_misinfo_dataset(file_path: str) -> pd.DataFrame:
    """
    Normalizes the misinfo dataset CSV files to contain a text and label column. A '1' label value indicates a true piece of
    text while a '0' label value indicates a false piece of text.
    
    Parameters:
        file_path: The filepath of the CSV file to normalize
        
    Returns:
        pd.Dataframe: A normalized dataframe containing only text and labels column
    """
    df = pd.read_csv(file_path, usecols=["text"])
    
    label_value = file_path[25:]
    
    if file_path[25:42] == "DataSet_Misinfo_F" or file_path[25:] == "EXTRA_RussianPropagandaSubset.csv":
        label_value = 0
    elif file_path[25:42] == "DataSet_Misinfo_T":
        label_value = 1
    else:
        raise IOError("The specified file does not work with this method. It may be spelled wrong.")
    
    if label_value == None:
        raise ValueError("The label value cannot be without a boolean value! Currently set to None!")
    else:
        df["label"] = label_value
    
    return df

def normalize_fakenewsnet_dataset(file_path: str) -> pd.DataFrame:
    """    
    Normalizes the fakenewnet dataset CSV files to contain a text and label column. A '1' label value indicates a true piece of
    text while a '0' label value indicates a false piece of text.
    
    Parameters:
        file_path: The filepath of the CSV file to normalize
        
    Returns:
        pd.Dataframe: A normalized dataframe containing only text and labels column
    """
    df = pd.read_csv(file_path, usecols=["title"])
    df.rename(columns={"title": "text"}, inplace=True)
    
    label_value = None
    
    if file_path[29:40] == "gossipcop_f" or file_path[29:41] == "politifact_f":
        label_value = 0
    elif file_path[29:40] == "gossipcop_r" or file_path[29:41] == "politifact_r":
        label_value = 1
    else:
        raise IOError("The specified file does not work with this method. It may be spelled wrong.")
    
    if label_value == None:
        raise ValueError("The label value cannot be without a boolean value! Currently set to None!")
    else:
        df["label"] = label_value
        
    return df

def normalize_liar_dataset(file_path: str) -> pd.DataFrame:
    """    
    Normalizes the liar dataset TSV files to contain a text and label column. A '1' label value indicates a true piece of
    text while a '0' label value indicates a false piece of text.
    
    Parameters:
        file_path: The filepath of the TSV file to normalize
        
    Returns:
        pd.Dataframe: A normalized dataframe containing only text and labels column
    """
    # CHAT GPT CITATION #1 FOR LINE 74
    df = pd.read_csv(file_path, sep="\t", header=None)
    column_names = ["_", "label", "text", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
    df.columns = column_names
    df = df[['text', 'label']]
    
    true_labels = ["true", "mostly-true", "half-true"]
    false_labels = ["pants-fire", "false", "barely-true"]
    
    for index, row in df.iterrows():
        if row['label'] in true_labels:
            row['label'] = 1
        elif row['label'] in false_labels:
            row['label'] = 0
        else:
            raise ValueError("Error re-assigning the proper label to the row!")
        
    return df