# Data sources
database(
    thermoLibraries = ['BurkeH2O2', 'Klippenstein_Glarborg2016' , 'CurranPentane','primaryThermoLibrary', 'thermo_DFT_CCSDTF12_BAC', 'DFT_QCI_thermo', 'CBS_QB3_1dHR'],
    reactionLibraries = ['CurranPentane','combustion_core/version5'],
    seeiC8H18chanisms = ['BurkeH2O2inN2', 'C2H4+O_Klipp2017','Klippenstein_Glarborg2016'],
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


# Reaction systems 1 for the high temperature range
simpleReactor(
    temperature=[(550,'K'),(1200,'K')],#max reactor temperature must always be less than max pdep temperature
    pressure=[(1.0,'bar'),(40.0,'bar')],
    nSims=60,
    initialMoleFractions={
        # "iC8H18": 0.0165224, # phi = 1
        "iC8H18": [0.0165224/2, 0.0165224*2], # range of 0.5 < phi < 2
        "N2": 0.776947,
        "O2": 0.20653,
        },
#    terminationConversion={
#        'iC8H18': 0.9,
#        },
    terminationTime=(1.0, 's'),
    terminationRateRatio=0.01,
)

# Reaction system 2 for the low temperature range which is the region of interest
simpleReactor(
    temperature=[(550,'K'),(800,'K')],
    pressure=[(1.0,'bar'),(40.0,'bar')],
    nSims=80,
    initialMoleFractions={
        # "iC8H18": 0.0654, # phi = 1
        "iC8H18": [0.0165224/2, 0.0165224*2], # range of 0.5 < phi < 2
        "N2": 0.776947,
        "O2": 0.20653,
        },
#    terminationConversion={
#        'iC8H18': 0.9,
#        },
    terminationTime=(1.0, 's'),
    terminationRateRatio=0.01,
)

simulator(
    atol=1e-16,
    rtol=1e-8,
)
model(
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=0.1,
    filterReactions = True,
    filterThreshold = 5e8, # Default is 5e8
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

