# Data sources
database(
    thermoLibraries = ['BurkeH2O2', 'Klippenstein_Glarborg2016' , 'primaryThermoLibrary', 'thermo_DFT_CCSDTF12_BAC', 'DFT_QCI_thermo', 'CBS_QB3_1dHR'],
    reactionLibraries = ['combustion_core/version5'],
    seedMechanisms = ['BurkeH2O2inN2', 'C2H4+O_Klipp2017','Klippenstein_Glarborg2016'],
    kineticsDepositories = ['training'],
    kineticsFamilies = 'default',
    kineticsEstimator = 'rate rules',
    
)
# List of species 
species(
    label = 'DME',
    reactive = True,
    structure = SMILES("COC"),
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


# We want C2H and O to be forced into the core,
# and to have known (reproducible) species numbers
# because we use them when post-processing ignition
# delay simulations.
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


# Species showing up in sensitivity analysis at low temperature ignition
# Figure 17 in Zhao et al 2007
species(
    label = 'CH3OCH2O2',
    reactive = True,
    structure = SMILES("COCO[O]"),
)

species(
    label = 'CH2OCH2O2H',
    reactive = True,
    structure = SMILES("[CH2]OCOO"),
)

species(
    label = 'CH2O',
    reactive = True,
    structure = SMILES("C=O"),
)

species(
    label = 'CH3OCH2',
    reactive = True,
    structure = SMILES("[CH2]OC"),
)

species(
    label = 'O2CH2OCH2O2H',
    reactive = True,
    structure = SMILES("[O]OCOCOO"),
)

# Reaction systems 1 for the high temperature range
simpleReactor(
    temperature=[(500,'K'),(1900,'K')],#max reactor temperature must always be less than max pdep temperature
    pressure=[(1.0,'bar'),(40.0,'bar')],
    nSims=20,
    initialMoleFractions={
        # "DME": 0.0654, # phi = 1
        "DME": [0.0654/2, 0.0654*2], # range of 0.5 < phi < 2
        "N2": 0.7383,
        "O2": 0.1963,
        },
#    terminationConversion={
#        'DME': 0.9,
#        },
    terminationTime=(1.0, 's')
)

# Reaction system 2 for the low temperature range which is the region of interest
simpleReactor(
    temperature=[(500,'K'),(900,'K')],
    pressure=[(1.0,'bar'),(40.0,'bar')],
    nSims=10,
    initialMoleFractions={
        # "DME": 0.0654, # phi = 1
        "DME": [0.0654/2, 0.0654*2], # range of 0.5 < phi < 2
        "N2": 0.7383,
        "O2": 0.1963,
        },
#    terminationConversion={
#        'DME': 0.9,
#        },
    terminationTime=(1.0, 's')
)

simulator(
    atol=1e-16,
    rtol=1e-8,
)
model(
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=0.1,
    filterReactions = True,
    maximumEdgeSpecies=100000,
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
    saveRestartPeriod=None,
    generateOutputHTML=True,
    generatePlots=False,
    saveEdgeSpecies=True,
    saveSimulationProfiles=True,
 )
# Introduced the species constraint for the mechanism. Set the maximumRadicalElectrons to 2 for N2
generatedSpeciesConstraints(
    allowed=['input species','seed mechanisms','reaction libraries'],
    maximumCarbonAtoms=10,
    maximumRadicalElectrons=2,
)

