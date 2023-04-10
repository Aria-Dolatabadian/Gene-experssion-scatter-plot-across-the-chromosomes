import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define the number of genes and chromosomes
n_genes = 5000
n_chromosomes = 4

# Define the length of each chromosome
chr_lengths = [10000000, 15000000, 20000000, 20000000]

# Generate random gene positions and expression values for each chromosome
gene_positions = []
gene_expressions = []
for i in range(n_chromosomes):
    positions = np.random.randint(0, chr_lengths[i], size=n_genes)
    expressions = np.random.normal(loc=5, scale=2, size=n_genes)
    gene_positions.append(positions)
    gene_expressions.append(expressions)

# Combine the data into a single dataframe
gene_data = pd.DataFrame({
    "chromosome": [f"chr{i+1}" for i in range(n_chromosomes) for j in range(n_genes)],
    "position": np.concatenate(gene_positions),
    "expression": np.concatenate(gene_expressions)
})

# Save the data to a CSV file
gene_data.to_csv("gene_data1.csv", index=False)

import pandas as pd
import matplotlib.pyplot as plt
#
# Read gene data from a CSV file
gene_data = pd.read_csv("gene_data1.csv")
#
# Define chromosome boundaries and colors
chr_boundaries = [(0, 1000000), (1000000, 2000000), (2000000, 3000000),(3000000, 4000000)]
chr_colors = ["green", "blue", "orange","red"]

# Create a scatter plot for each chromosome
fig, ax = plt.subplots(figsize=(10,5))
for i, bounds in enumerate(chr_boundaries):
    chr_genes = gene_data[(gene_data["position"] >= bounds[0]) & (gene_data["position"] < bounds[1])]
    ax.scatter(chr_genes["position"], chr_genes["expression"], s=5, c=chr_colors[i], alpha=0.8, label=f"Chromosome {i+1}")

# Set plot title, axis labels, and legend
ax.set_title("Gene distribution across chromosomes")
ax.set_xlabel("Position on chromosome")
ax.set_ylabel("Gene expression")
ax.legend(bbox_to_anchor=(1.04, 0.5), loc='center left')


# Save the plot as a PNG file
plt.savefig("gene_distribution.png", dpi=300)
plt.show()





import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define the number of genes and chromosomes
n_genes = 5000
n_chromosomes = 4

# Define the length of each chromosome
chr_lengths = [10000000, 15000000, 20000000, 20000000]

# Generate random gene positions and expression values for each chromosome
gene_positions = []
gene_expressions = []
for i in range(n_chromosomes):
    positions = np.random.randint(0, chr_lengths[i], size=n_genes)
    expressions = np.random.normal(loc=5, scale=2, size=n_genes)
    gene_positions.append(positions)
    gene_expressions.append(expressions)

# Combine the data into a single dataframe
gene_data = pd.DataFrame({
    "chromosome": [f"chr{i+1}" for i in range(n_chromosomes) for j in range(n_genes)],
    "position": np.concatenate(gene_positions),
    "expression": np.concatenate(gene_expressions)
})

# Save the data to a CSV file
gene_data.to_csv("gene_data2.csv", index=False)

# Read gene data from a CSV file
gene_data = pd.read_csv("gene_data2.csv")

# Define chromosome boundaries and colors
chr_boundaries = [(1000000, 5000000), (5000000, 10000000), (10000000, 15000000), (15000000, 20000000)]
chr_colors = ["#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

# Create a scatter plot for each chromosome
fig, ax = plt.subplots(figsize=(10,5))
for i, bounds in enumerate(chr_boundaries):
    chr_genes = gene_data[(gene_data["position"] >= bounds[0]) & (gene_data["position"] < bounds[1])]
    ax.scatter(chr_genes["position"], chr_genes["expression"], s=5, c=chr_colors[i], alpha=0.8, label=f"Chromosome {i+1}")

# Set plot title, axis labels, and legend
ax.set_title("Gene distribution across chromosomes")
ax.set_xlabel("Position on chromosome")
ax.set_ylabel("Gene expression")
ax.legend(bbox_to_anchor=(1.04, 0.5), loc='center left')

# Save the plot as a PNG file
plt.savefig("gene_distribution.png", dpi=300)
plt.show()




import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define the number of genes and chromosomes
n_genes = 5000
n_chromosomes = 4

# Define the length of each chromosome
chr_lengths = [10000000, 15000000, 20000000, 20000000]

# Generate random gene positions and expression values for each chromosome
gene_positions = []
gene_expressions = []
for i in range(n_chromosomes):
    positions = np.random.randint(0, chr_lengths[i], size=n_genes)
    expressions = np.random.normal(loc=5, scale=2, size=n_genes)
    gene_positions.append(positions)
    gene_expressions.append(expressions)

# Combine the data into a single dataframe
gene_data = pd.DataFrame({
    "chromosome": [f"chr{i+1}" for i in range(n_chromosomes) for j in range(n_genes)],
    "position": np.concatenate(gene_positions),
    "expression": np.concatenate(gene_expressions)
})

# Save the data to a CSV file
gene_data.to_csv("gene_data3.csv", index=False)

# Read gene data from a CSV file
gene_data = pd.read_csv("gene_data3.csv")

# Define chromosome boundaries and colors
chr_boundaries = [(0, 1000000), (1000000, 2000000), (2000000, 3000000),(3000000, 4000000)]
chr_colors = ["green", "blue", "orange","red"]

# Create a scatter plot for each chromosome
fig, ax = plt.subplots(figsize=(10,5))
for i, bounds in enumerate(chr_boundaries):
    chr_genes = gene_data[(gene_data["position"] >= bounds[0]) & (gene_data["position"] < bounds[1])]
    chr_genes["position"] = chr_genes["position"] - bounds[0]
    ax.scatter(chr_genes["position"], chr_genes["expression"], s=5, c=chr_colors[i], alpha=0.8, label=f"Chromosome {i+1}")

# Set plot title, axis labels, and legend
ax.set_title("Gene distribution across chromosomes")
ax.set_xlabel("Position on chromosome")
ax.set_ylabel("Gene expression")
ax.legend(bbox_to_anchor=(1.04, 0.5), loc='center left')

# Save the plot as a PNG file
plt.savefig("gene_distribution.png", dpi=300)
plt.show()
#
#
#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define the number of genes and chromosomes
n_genes = 5000
n_chromosomes = 4

# Define the length of each chromosome
chr_lengths = [10000000, 15000000, 20000000, 20000000]

# Generate random gene positions and expression values for each chromosome
gene_positions = []
gene_expressions = []
for i in range(n_chromosomes):
    positions = np.random.randint(0, chr_lengths[i], size=n_genes)
    expressions = np.random.normal(loc=5, scale=2, size=n_genes)
    gene_positions.append(positions)
    gene_expressions.append(expressions)

# Combine the data into a single dataframe
gene_data = pd.DataFrame({
    "chromosome": [f"chr{i+1}" for i in range(n_chromosomes) for j in range(n_genes)],
    "position": np.concatenate(gene_positions),
    "expression": np.concatenate(gene_expressions)
})

# Save the data to a CSV file
gene_data.to_csv("gene_data4.csv", index=False)

# Read gene data from a CSV file
gene_data = pd.read_csv("gene_data4.csv")

# Define chromosome boundaries and colors
chr_boundaries = [(0, 1000000), (1000000, 2000000), (2000000, 3000000), (3000000, 4000000)]
chr_colors = ["green", "blue", "orange", "red"]

# Create a scatter plot for each chromosome
fig, axs = plt.subplots(nrows=1, ncols=n_chromosomes, figsize=(15,5))

for i, bounds in enumerate(chr_boundaries):
    chr_genes = gene_data[(gene_data["position"] >= bounds[0]) & (gene_data["position"] < bounds[1])]
    axs[i].scatter(chr_genes["position"] - bounds[0], chr_genes["expression"], s=5, c=chr_colors[i], alpha=0.8)
    axs[i].set_title(f"Chromosome {i+1}")
    axs[i].set_xlabel("Position on chromosome")
    axs[i].set_ylabel("Gene expression")

# Set common plot title
fig.suptitle("Gene distribution across chromosomes")

# Adjust position of legend
fig.legend(bbox_to_anchor=(1.04, 0.5), loc='center left')

# Save the plot as a PNG file
plt.savefig("gene_distribution.png", dpi=300)

# Show the plot
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define the number of genes and chromosomes
n_genes = 5000
n_chromosomes = 4

# Define the length of each chromosome
chr_lengths = [10000000, 15000000, 20000000, 20000000]

# Generate random gene positions and expression values for each chromosome
gene_positions = []
gene_expressions = []
for i in range(n_chromosomes):
    positions = np.random.randint(0, chr_lengths[i], size=n_genes)
    expressions = np.random.normal(loc=5, scale=2, size=n_genes)
    gene_positions.append(positions)
    gene_expressions.append(expressions)

# Combine the data into a single dataframe
gene_data = pd.DataFrame({
    "chromosome": [f"chr{i+1}" for i in range(n_chromosomes) for j in range(n_genes)],
    "position": np.concatenate(gene_positions),
    "expression": np.concatenate(gene_expressions)
})

# Save the data to a CSV file
gene_data.to_csv("gene_data5.csv", index=False)

# Read gene data from a CSV file
gene_data = pd.read_csv("gene_data5.csv")

# Define chromosome boundaries and colors
chr_boundaries = [(0, 1000000), (1000000, 2000000), (2000000, 3000000),(3000000, 4000000)]
chr_colors = ["green", "blue", "orange","red"]

# Create a scatter plot for each chromosome
fig, axs = plt.subplots(n_chromosomes, 1, figsize=(10, 20), sharex=True, sharey=True)
for i, bounds in enumerate(chr_boundaries):
    chr_genes = gene_data[(gene_data["position"] >= bounds[0]) & (gene_data["position"] < bounds[1])]
    axs[i].scatter(chr_genes["position"] - bounds[0], chr_genes["expression"], s=5, c=chr_colors[i], alpha=0.8)
    axs[i].set_title(f"Chromosome {i+1}")

# Set plot title, axis labels, and legend
fig.suptitle("Gene distribution across chromosomes")
fig.text(0.5, 0.04, "Position on chromosome", ha="center")
fig.text(0.04, 0.5, "Gene expression", va="center", rotation="vertical")

# Save the plot as a PNG file
plt.savefig("gene_distribution.png", dpi=300)
plt.show()

