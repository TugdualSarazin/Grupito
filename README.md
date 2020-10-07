# Grupito


# Conda env
## Create conda env
Create conda environment from environment.yml file
````shell script
conda env create -f environment.yml
````

# Save conda env
When you update dependencies update the conda config file 
````shell script
conda env export > environment.yml
````
