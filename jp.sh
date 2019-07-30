#!/bin/bash

#SBATCH --nodes=1
#SBATCH --mem=120Gb
#SBATCH --job-name=jupyter_notebook
#SBATCH --partition=west
#SBATCH --cpus-per-task=6
#SBATCH --mem-per-cpu=4Gb
#SBATCH --ntasks=1
#SBATCH --output=jupyter_notebook.log
#SBATCH --error=jupyter_notebook.err
#SBATCH --time=5-00:00:00


source activate flame_env
/home/ajulu.c/anaconda3/envs/flame_env/bin/jupyter-notebook




