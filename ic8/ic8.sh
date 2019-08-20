#!/bin/bash

#SBATCH --nodes=1
#SBATCH --time=unlimited
#SBATCH --mem=120Gb
#SBATCH --job-name=IC8
#SBATCH --output=IC8.log
#SBATCH --partition=west
#SBATCH --exclude=c[5003]



source activate rmg_env
python $RMGpy/rmg.py -p ic8.py



