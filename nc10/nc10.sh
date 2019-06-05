#!/bin/bash

#SBATCH --nodes=1
#SBATCH --time=1-08:43:15
#SBATCH --job-name=n-decane
#SBATCH --output=nc10.log
#SBATCH --partition=west,general
#SBATCH --exclude=c[5003]
#SBATCH --cpus-per-task=12
#SBATCH --mem-per-cpu=4Gb
#SBATCH --ntasks=1


source activate rmg_env
python $RMGpy/rmg.py -p nc10.py



