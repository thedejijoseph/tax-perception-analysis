import pandas as pd
import glob
import os

def explore_codebooks():
    raw_dir = '../data/raw'
    processed_dir = '../data/processed'
    os.makedirs(processed_dir, exist_ok=True)
    
    codebooks = glob.glob(os.path.join(raw_dir, '*Codebook*.xls'))
    
    keywords = ['tax', 'morale', 'trust', 'fair', 'government', 'service', 'pay', 'compliance', 'evasion', 'institution']
    
    for cb in codebooks:
        print(f"\n--- Processing Codebook: {os.path.basename(cb)} ---")
        try:
            # Codebooks usually have variables in the first sheet, maybe starting from row 0 or 1.
            df = pd.read_excel(cb)
            
            # Print columns to understand structure
            print("Columns found:", df.columns.tolist())
            
            # Try to identify variable name and label columns
            var_col = None
            label_col = None
            for col in df.columns:
                col_lower = str(col).lower()
                if 'name' in col_lower or 'variable' in col_lower or 'q' in col_lower:
                    if not var_col: var_col = col
                if 'label' in col_lower or 'question' in col_lower or 'description' in col_lower:
                    if not label_col: label_col = col
                    
            if not var_col or not label_col:
                # If cannot automatically determine, assume standard structure (col 0: Name, Col 1: Label)
                var_col = df.columns[0]
                label_col = df.columns[1]
                
            print(f"Using '{var_col}' as Variable Name and '{label_col}' as Label.")
            
            # Save the full mapping to processed data for easy reference
            out_name = os.path.basename(cb).replace('.xls', '_mapped.csv')
            out_path = os.path.join(processed_dir, out_name)
            df[[var_col, label_col]].to_csv(out_path, index=False)
            print(f"Saved full mapping to {out_path}")
            
            # Search for keywords
            print("\nPotential Variables of Interest:")
            for idx, row in df.iterrows():
                val = str(row[label_col]).lower()
                if any(kw in val for kw in keywords):
                    print(f"{row[var_col]}: {row[label_col]}")
                    
        except Exception as e:
            print(f"Error processing {cb}: {e}")

if __name__ == '__main__':
    explore_codebooks()
