import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style for plots
sns.set_theme(style="whitegrid")

def generate_visualizations(data_file, output_dir):
    print(f"Loading cleaned data from {data_file}...")
    df = pd.read_csv(data_file)
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 1. Distribution of Ratings
    plt.figure(figsize=(10, 6))
    sns.histplot(df['rate'].dropna(), bins=20, kde=True, color='skyblue')
    plt.title('Distribution of Restaurant Ratings', fontsize=15)
    plt.xlabel('Rating', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.savefig(os.path.join(output_dir, 'rating_distribution.png'))
    plt.close()
    
    # 2. Distribution of Approx Cost for Two
    plt.figure(figsize=(10, 6))
    sns.histplot(df['approx_cost(for two people)'].dropna(), bins=20, kde=True, color='salmon')
    plt.title('Distribution of Approx Cost (for two people)', fontsize=15)
    plt.xlabel('Cost', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.savefig(os.path.join(output_dir, 'cost_distribution.png'))
    plt.close()
    
    # 3. Top 10 Cuisines
    plt.figure(figsize=(12, 8))
    # 'cuisines' could be a comma separated string, let's just take the first one for simplicity or split them
    all_cuisines = df['cuisines'].dropna().str.split(', ').explode()
    top_cuisines = all_cuisines.value_counts().head(10)
    sns.barplot(x=top_cuisines.values, y=top_cuisines.index, palette='viridis')
    plt.title('Top 10 Cuisines in Bangalore', fontsize=15)
    plt.xlabel('Count', fontsize=12)
    plt.ylabel('Cuisine', fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'top_cuisines.png'))
    plt.close()
    
    # 4. Online Order vs Ratings
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='online_order', y='rate', data=df, palette='Set2')
    plt.title('Ratings: Online Order vs In-person', fontsize=15)
    plt.xlabel('Online Order Available', fontsize=12)
    plt.ylabel('Rating', fontsize=12)
    plt.savefig(os.path.join(output_dir, 'online_order_ratings.png'))
    plt.close()

    # 5. Book Table vs Ratings
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='book_table', y='rate', data=df, palette='Set1')
    plt.title('Ratings: Book Table vs No Booking', fontsize=15)
    plt.xlabel('Book Table Available', fontsize=12)
    plt.ylabel('Rating', fontsize=12)
    plt.savefig(os.path.join(output_dir, 'book_table_ratings.png'))
    plt.close()

    print(f"Visualizations saved to {output_dir}")

def check_imbalance(data_file, output_dir):
    print(f"Checking dataset imbalance from {data_file}...")
    df = pd.read_csv(data_file)
    
    # 6. Class Imbalance: Online Order
    plt.figure(figsize=(8, 6))
    sns.countplot(x='online_order', data=df, palette='pastel')
    plt.title('Class Distribution: Online Order', fontsize=15)
    plt.savefig(os.path.join(output_dir, 'imbalance_online_order.png'))
    plt.close()
    
    # 7. Class Imbalance: Book Table
    plt.figure(figsize=(8, 6))
    sns.countplot(x='book_table', data=df, palette='pastel')
    plt.title('Class Distribution: Book Table', fontsize=15)
    plt.savefig(os.path.join(output_dir, 'imbalance_book_table.png'))
    plt.close()
    
    # 8. Type of Restaurant Distribution
    plt.figure(figsize=(12, 6))
    sns.countplot(x='listed_in(type)', data=df, palette='magma')
    plt.title('Distribution of Restaurant Types', fontsize=15)
    plt.xticks(rotation=45)
    plt.savefig(os.path.join(output_dir, 'imbalance_rest_type.png'))
    plt.close()

def correlation_analysis(data_file, output_dir):
    print(f"Performing correlation analysis from {data_file}...")
    df = pd.read_csv(data_file)
    
    # Filter for numeric columns
    numeric_df = df.select_dtypes(include=[np.number])
    
    # Map boolean columns to int for correlation
    if 'online_order' in df.columns:
        numeric_df['online_order_val'] = df['online_order'].astype(int)
    if 'book_table' in df.columns:
        numeric_df['book_table_val'] = df['book_table'].astype(int)
    
    corr_matrix = numeric_df.corr()
    
    # 9. Correlation Heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Feature Correlation Heatmap', fontsize=15)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'correlation_heatmap.png'))
    plt.close()

    return corr_matrix

def bivariate_analysis(data_file, output_dir):
    print(f"Performing bivariate analysis from {data_file}...")
    df = pd.read_csv(data_file)
    
    # 10. Votes vs Rating
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='votes', y='rate', data=df, alpha=0.5, color='teal')
    plt.title('Bivariate Analysis: Votes vs Rating', fontsize=15)
    plt.xlabel('Votes', fontsize=12)
    plt.ylabel('Rating', fontsize=12)
    plt.savefig(os.path.join(output_dir, 'bivariate_votes_rate.png'))
    plt.close()
    
    # 11. Location vs Rating (Top 10 Locations)
    top_locations = df['location'].value_counts().head(10).index
    df_top_loc = df[df['location'].isin(top_locations)]
    plt.figure(figsize=(14, 8))
    sns.boxplot(x='location', y='rate', data=df_top_loc, palette='cool')
    plt.title('Bivariate Analysis: Location vs Rating (Top 10 Locations)', fontsize=15)
    plt.xticks(rotation=45)
    plt.savefig(os.path.join(output_dir, 'bivariate_location_rate.png'))
    plt.close()
    
    # 12. Cuisines Count vs Rating
    plt.figure(figsize=(10, 6))
    sns.regplot(x='cuisines_count', y='rate', data=df, scatter_kws={'alpha':0.3}, line_kws={'color':'red'})
    plt.title('Bivariate Analysis: Cuisines Count vs Rating', fontsize=15)
    plt.xlabel('Number of Cuisines Offered', fontsize=12)
    plt.ylabel('Rating', fontsize=12)
    plt.savefig(os.path.join(output_dir, 'bivariate_cuisines_rate.png'))
    plt.close()

def feature_selection(data_file, output_dir):
    print(f"Performing feature selection from {data_file}...")
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.preprocessing import LabelEncoder
    
    df = pd.read_csv(data_file)
    # Drop rows with missing rate as it's our target
    df = df.dropna(subset=['rate'])
    
    # Select features for importance analysis
    features = ['votes', 'approx_cost(for two people)', 'cuisines_count', 'online_order', 'book_table', 'location', 'rest_type']
    X = df[features].copy()
    y = df['rate']
    
    # Preprocessing
    le = LabelEncoder()
    X['location'] = le.fit_transform(X['location'].astype(str))
    X['rest_type'] = le.fit_transform(X['rest_type'].astype(str))
    X['online_order'] = X['online_order'].astype(int)
    X['book_table'] = X['book_table'].astype(int)
    X = X.fillna(0) # Simple fill for cost if any
    
    # Fit Random Forest
    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    rf.fit(X, y)
    
    # Get feature importance
    importances = pd.Series(rf.feature_importances_, index=features).sort_values(ascending=False)
    
    # 13. Label Feature Importance
    plt.figure(figsize=(10, 6))
    sns.barplot(x=importances.values, y=importances.index, palette='rocket')
    plt.title('Feature Importance for Restaurant Ratings', fontsize=15)
    plt.xlabel('Importance Score', fontsize=12)
    plt.ylabel('Features', fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'feature_importance.png'))
    plt.close()
    
    return importances

if __name__ == "__main__":
    import numpy as np
    input_csv = "cleaned_restaurant_data.csv"
    output_folder = "visuals"
    generate_visualizations(input_csv, output_folder)
    check_imbalance(input_csv, output_folder)
    corr = correlation_analysis(input_csv, output_folder)
    bivariate_analysis(input_csv, output_folder)
    importance = feature_selection(input_csv, output_folder)
    print("Top Features:\n", importance)
