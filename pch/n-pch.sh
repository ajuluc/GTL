#!/bin/bash

#SBATCH --nodes=1
#SBATCH --time=8-09:44:15
#SBATCH --job-name=n-pch
#SBATCH --output=n-pch.log
#SBATCH --partition=west
#SBATCH --exclude=c[5003]
#SBATCH --cpus-per-task=12
#SBATCH --mem-per-cpu=4Gb
#SBATCH --ntasks=1


source activate rmg_env
python $RMGpy/rmg.py -p n-pch.py



