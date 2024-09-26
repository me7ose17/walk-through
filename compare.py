import pandas as pd 
from sklearn.manifold import TSNE  
import matplotlib.pyplot as plt  
import seaborn as sns  
import numpy as np  
import scipy.stats as ss  

def to_one():  # Define the main function to_one
    # Read landscape similarity data
    sv_df = pd.read_csv('F:\\街道的相似性\\new1\\similarity_sv.txt')  
    sv_df = sv_df.rename(columns={'similarity': 'similarity_SV'})  
    sv_df[['road1', 'road2']] = sv_df[['road1', 'road2']].apply(lambda x: sorted([x['road1'], x['road2']]), axis=1, result_type='expand') 

    print(len(sv_df))  

    # Read safety similarity data
    safe_df = pd.read_csv('F:\\街道的相似性\\new1\\similarity_safe.txt')  
    safe_df = safe_df.rename(columns={'similarity': 'similarity_safe'})  
    safe_df[['road1', 'road2']] = safe_df[['road1', 'road2']].apply(lambda x: sorted([x['road1'], x['road2']]), axis=1, result_type='expand')  

    print(len(safe_df)) 
     
    # Merge landscape and safety data
    merge_df = pd.merge(sv_df, safe_df, how='inner', on=['road1', 'road2'])  
    merge_df[['road1', 'road2']] = merge_df[['road1', 'road2']].apply(lambda x: sorted([x['road1'], x['road2']]), axis=1, result_type='expand')  
    print(len(merge_df)) 

    merge_df.to_csv('F:\\街道的相似性\\new1\\street_similarity_through0.csv', index=False)  
    
    # Read function similarity data
    function_df = pd.read_csv('F:\\街道的相似性\\new1\\similarity_function.txt')  
    function_df = function_df.rename(columns={'similarity': 'similarity_function'}) 
    function_df[['road1', 'road2']] = function_df[['road1', 'road2']].apply(lambda x: sorted([x['road1'], x['road2']]), axis=1, result_type='expand') 

    # Final merge
    final_df = pd.merge(merge_df, function_df, on=['road1', 'road2'])  
    print(len(final_df))  
    
    final_df.to_csv('F:\\街道的相似性\\new1\\street_similarity_through.csv', index=False) 
    return final_df 

if __name__ == "__main__":  
    similarity_df = to_one()  