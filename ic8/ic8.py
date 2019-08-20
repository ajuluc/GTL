# Data sources
database(
    thermoLibraries = ['BurkeH2O2', 'Klippenstein_Glarborg2016' , 'CurranPentane','FFCM1(-)','primaryThermoLibrary', 'thermo_DFT_CCSDTF12_BAC', 'DFT_QCI_thermo', 'CBS_QB3_1dHR'],
    reactionLibraries = [('CurranPentane',False),('FFCM1(-)',False),('combustion_core/version5',False)],
    seedMechanisms = ['JetSurF2.0','BurkeH2O2inN2','BurkeH2O2inArHe','C2H4+O_Klipp2017','Klippenstein_Glarborg2016','Zil_ic8_1'],
    kineticsDepositories = ['training'],
    kineticsFamilies = 'default',
    kineticsEstimator = 'rate rules',
)
# List of species 
species(
    label = 'iC8H18',
    reactive = True,
    structure = SMILES("CC(C)(C)CC(C)C"),
)

species(
    label = 'O2',
    reactive = True,
    structure = SMILES("[O][O]"),
)

species(
    label = 'N2',
    reactive = False,
    structure = SMILES("N#N"),
)

species(
    label = 'Ar',
    reactive = False,
    structure = SMILES("[Ar]"),
)


# We want CH, C2H and O to be forced into the core,
# and to have known (reproducible) species numbers
# because we use them when post-processing ignition
# delay simulations.

species(
    label = 'CH',
    reactive = True,
    structure = SMILES("[CH]"),
)

species(
    label = 'C2H',
    reactive = True,
    structure = SMILES("[C]#C"),
)

species(
    label = 'O',
    reactive = True,
    structure = SMILES("[O]"),
)


# Species showing up in JSR species profiles 
# in Figure 5 of Dagaut 2014
species(
    label = 'CO',
    reactive = True,
    structure = SMILES("[C-]#[O+]"),
)

species(
    label = 'CO2',
    reactive = True,
    structure = SMILES("O=C=O"),
)

species(
    label = 'H2O',
    reactive = True,
    structure = SMILES("O"),
)

species(
    label = 'CH2O',
    reactive = True,
    structure = SMILES("C=O"),
)

species(
    label = 'CH4',
    reactive = True,
    structure = SMILES("C"),
)

species(
    label = 'C2H4',
    reactive = True,
    structure = SMILES("C=C"),
)

species(
    label = 'C2H6',
    reactive = True,
    structure = SMILES("CC"),
)

species(
    label = 'C3H6',
    reactive = True,
    structure = SMILES("C=CC"),
)

species(
    label = 'H2',
    reactive = True,
    structure = SMILES("[H][H]"),
)

species(
    label = 'iC4H8', # isobutene
    reactive = True,
    structure = SMILES("C=C(C)C"),
)
import textwrap

def NASA(*args, **kwargs):
    # do nothing
    pass

def NASAPolynomial(*args, **kwargs):
    # do nothing
    pass

def entry(index, label, molecule, thermo, shortDesc, longDesc):
    
    if label.lower() in ['ar', 'n2']:
        # skip them
        return
        
    print("""
species(
    label='{label}',
    reactive=True,
    structure=AdjacencyList('''{molecule!s}        ''')
    )
    """.format(label=label, molecule=textwrap.indent(molecule, '        ')))

import ThermoLibrary

# Reaction systems 1 for the high temperature range with Nitrogen as the bath gas 
simpleReactor(
    temperature=[(550,'K'),(1500,'K')],#max reactor temperature must always be less than max pdep temperature
    pressure=[(1.0,'bar'),(40.0,'bar')],
    nSims=5,
    initialMoleFractions={
        # "iC8H18": 0.0165224, # phi = 1
        "iC8H18": [0.0165224/2, 0.0165224*2], # range of 0.5 < phi < 2
        "N2": 0.776947,
        "O2": 0.20653,
        },
    terminationTime=(1.0, 's'),
    terminationRateRatio=0.01,
)

# Reaction systems 2 for the high temperature range with Argon diluted in air 25% N2 75% Ar 
simpleReactor(
    temperature=[(550,'K'),(1500,'K')],#max reactor temperature must always be less than max pdep temperature
    pressure=[(1.0,'bar'),(40.0,'bar')],
    nSims=5,
    initialMoleFractions={
        # "iC8H18": 0.0165224, # phi = 1
        "iC8H18": [0.0165224/2, 0.0165224*2], # range of 0.5 < phi < 2
        "N2": 0.194237,
        "Ar": 0.58271,
        "O2": 0.20653,
        },
    terminationTime=(1.0, 's'),
    terminationRateRatio=0.01,
)


# Reaction systems 3 for the high temperature range with Argon diluted in air 20% N2 80% Ar 
simpleReactor(
    temperature=[(550,'K'),(1500,'K')],#max reactor temperature must always be less than max pdep temperature
    pressure=[(1.0,'bar'),(40.0,'bar')],
    nSims=5,
    initialMoleFractions={
        # "iC8H18": 0.0165224, # phi = 1
        "iC8H18": [0.0165224/2, 0.0165224*2], # range of 0.5 < phi < 2
        "N2": 0.155389,
        "Ar": 0.621558,
        "O2": 0.20653,
        },
    terminationTime=(1.0, 's'),
    terminationRateRatio=0.01,   
)

# Reaction system 4 for the low temperature range which is the region of interest using Nitrogen as the bath gas
simpleReactor(
    temperature=[(550,'K'),(800,'K')],
    pressure=[(1.0,'bar'),(40.0,'bar')],
    nSims=17,
    initialMoleFractions={
        # "iC8H18": 0.0165224, # phi = 1
        "iC8H18": [0.0165224/2, 0.0165224*2], # range of 0.5 < phi < 2
        "N2": 0.776947,
        "O2": 0.20653,
        },
    terminationTime=(1.0, 's'),
    terminationRateRatio=0.01,
)

# Reaction systems 5 for the low temperature range with Argon diluted in air 25% N2 75% Ar
simpleReactor(
    temperature=[(550,'K'),(800,'K')],
    pressure=[(1.0,'bar'),(40.0,'bar')],
    nSims=17,
    initialMoleFractions={
        # "iC8H18": 0.0165224, # phi = 1
        "iC8H18": [0.0165224/2, 0.0165224*2], # range of 0.5 < phi < 2
        "N2": 0.194237,
        "Ar": 0.58271,
        "O2": 0.20653,
        },
    terminationTime=(1.0, 's'),
    terminationRateRatio=0.01,
)

# Reaction systems 6 for the low temperature range with Argon diluted in air 20% N2 80% Ar
simpleReactor(
    temperature=[(550,'K'),(800,'K')],#max reactor temperature must always be less than max pdep temperature
    pressure=[(1.0,'bar'),(40.0,'bar')],
    nSims=5,
    initialMoleFractions={
        # "iC8H18": 0.0165224, # phi = 1
        "iC8H18": [0.0165224/2, 0.0165224*2], # range of 0.5 < phi < 2
        "N2": 0.155389,
        "Ar": 0.621558,
        "O2": 0.20653,
        },
    terminationTime=(1.0, 's'),
    terminationRateRatio=0.01,   
)

# Introducing staging into the model and simulator blocks

#first stage with a higher tolerance 
simulator(
    atol=1e-16,
    rtol=1e-8,
)

#second stage with a lower tolerance 
simulator(
    atol=1e-20,
    rtol=1e-8,
)

# first stage with a lower tolerance of maxNumSpecies=500

model(
    toleranceKeepInEdge=0.00,
    toleranceInterruptSimulation=1e8,
    toleranceMoveToCore=0.1,
    filterReactions = True,
    filterThreshold = 5e8, # Default is 5e8
    maximumEdgeSpecies=100000,
    maxNumObjsPerIter = 1, # number of objects (species, reactions, PDepNetworks) that can be taken from one simulation
    minCoreSizeForPrune=100,
    minSpeciesExistIterationsForPrune=2,
    maxNumSpecies=500,
)

# second stage with a lower tolerance of maxNumSpecies=1800

model(
    toleranceKeepInEdge=0.0055,
    toleranceInterruptSimulation=1e8,
    toleranceMoveToCore=0.01,
    filterReactions = True,
    filterThreshold = 5e8, # Default is 5e8
    maximumEdgeSpecies=100000,
    maxNumObjsPerIter = 3, # number of objects (species, reactions, PDepNetworks) that can be taken from one simulation
    minCoreSizeForPrune=50,
    minSpeciesExistIterationsForPrune=2,
)

pressureDependence(
        method='modified strong collision',
        maximumGrainSize=(0.5,'kcal/mol'),
        minimumNumberOfGrains=250,
        temperatures=(300,2000,'K',8),#due to thermo library max pdep=2500K cannot go to 3000K
        pressures=(0.01,100,'bar',5),
        interpolation=('Chebyshev', 6, 4),
        maximumAtoms=16,
)

options(
    units='si',
    name='Zil_ic8(2)'
    saveRestartPeriod=None,
    generateOutputHTML=True,
    generateSeedEachIteration=True,
    saveSeedToDatabase=True,
    generatePlots=False,
    saveEdgeSpecies=True,
    saveSimulationProfiles=True,
    restartFromSeed(path='Zil_ic8(2)')
 )
# Introduced the species constraint for the mechanism. Set the maximumRadicalElectrons to 2 for N2
generatedSpeciesConstraints(
    allowed=['input species','seed mechanisms','reaction libraries'],
    maximumCarbonAtoms=10,
    maximumOxygenAtoms=4,
    maximumRadicalElectrons=2,
    allowSingletO2 = True,
)

