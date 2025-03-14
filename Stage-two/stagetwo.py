# Microbiology Task (Task Code 2.1)
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset 
df = pd.read_csv('https://www.w3schools.com/python/pandas/data.csv.txt')

# Function to plot growth curves
def plot_growth_curves(df):
    strains = df['Strain'].unique()
    for strain in strains:
        subset = df[df['Strain'] == strain]
        plt.figure(figsize=(10, 5))
        sns.lineplot(data=subset, x='Time', y='OD600', hue='Type', style='Type', markers=True)
        plt.title(f'Growth Curve for {strain}')
        plt.xlabel('Time')
        plt.ylabel('OD600')
        plt.legend(title='Type')
        plt.show()

# Function to determine time to carrying capacity
def carrying_capacity_time(df):
    times = {}
    for strain in df['Strain'].unique():
        subset = df[df['Strain'] == strain]
        max_od = subset['OD600'].max()
        time_to_capacity = subset[subset['OD600'] >= max_od * 0.95]['Time'].min()
        times[strain] = time_to_capacity
    return times

# Scatter plot of time to carrying capacity
def scatter_capacity_time(times):
    times_df = pd.DataFrame(times.items(), columns=['Strain', 'Time'])
    sns.scatterplot(data=times_df, x='Strain', y='Time', hue='Strain', palette='coolwarm')
    plt.xticks(rotation=45)
    plt.title('Time to Carrying Capacity')
    plt.show()

# Run functions
plot_growth_curves(df)
times = carrying_capacity_time(df)
scatter_capacity_time(times)



# Botany and Plant Science Task (Task Code 2.3)
def calculate_metabolic_difference(df):
    df['DeltaM'] = df['DMSO_24h'] - df['DMSO_8h']
    return df

def scatter_metabolic_response(df):
    sns.scatterplot(data=df, x='WT_DeltaM', y='Mutant_DeltaM')
    plt.axline((0, 0), slope=1, color='red', linestyle='dashed')
    plt.title('Metabolic Response Difference')
    plt.show()

# Run functions
botany_df = pd.read_csv('https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/Pesticide_treatment_data.txt')
botany_df = calculate_metabolic_difference(botany_df)
scatter_metabolic_response(botany_df)

# Biochemistry & Oncology Task (Task Code 2.4)
sift_df = pd.read_csv('sift_dataset.csv')
foldx_df = pd.read_csv('foldx_dataset.csv')

sift_df['specific_Protein_aa'] = sift_df['Protein'] + '_' + sift_df['Amino_acid']
foldx_df['specific_Protein_aa'] = foldx_df['Protein'] + '_' + foldx_df['Amino_acid']

merged_df = pd.merge(sift_df, foldx_df, on='specific_Protein_aa')

delet_mutations = merged_df[(merged_df['SIFT_Score'] < 0.05) & (merged_df['FoldX_Score'] > 2)]

amino_counts = delet_mutations['Amino_acid'].value_counts()
amino_counts.plot(kind='bar')
plt.title('Frequency of Amino Acid Mutations')
plt.show()


# Transcriptomics Task (Task Code 2.6)
rnaseq_df = pd.read_csv('https://gist.githubusercontent.com/stephenturner/806e31fce55a8b7175af/raw/1a507c4c3f9f1baaa3a69187223ff3d3050628d4/results.txt')

def volcano_plot(df):
    plt.scatter(df['Log2FC'], -np.log10(df['pvalue']), c=df['pvalue'] < 0.01)
    plt.title('Volcano Plot')
    plt.xlabel('Log2 Fold Change')
    plt.ylabel('-log10(p-value)')
    plt.show()

volcano_plot(rnaseq_df)



# Public Health Task (Task Code 2.7)
nhanes_df = pd.read_csv('https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/nhanes.csv')
nhanes_df.fillna(0, inplace=True)

def histogram_plots(df):
    features = ['BMI', 'Weight', 'Weight_lbs', 'Age']
    for feature in features:
        plt.hist(df[feature], bins=30, alpha=0.5, label=feature)
    plt.legend()
    plt.title('Distribution of Health Features')
    plt.show()

histogram_plots(nhanes_df)


#link to Github: https://github.com/AMARAXO/-hackbio-biocoding-internship
# link to video description: https://www.linkedin.com/posts/michael-ogar-aa6160142_coding-teamlysine-bioinformatic[…]m=member_android&rcm=ACoAACKM2B4B7FttbpFIigAj93J4h5yCp_ZaX6k


