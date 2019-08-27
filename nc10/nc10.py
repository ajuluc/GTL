# Data sources
database(
    thermoLibraries = ['BurkeH2O2', 'Klippenstein_Glarborg2016' , 'CurranPentane','FFCM1(-)','primaryThermoLibrary', 'thermo_DFT_CCSDTF12_BAC', 'DFT_QCI_thermo', 'CBS_QB3_1dHR'],
    reactionLibraries = [('CurranPentane',False),('FFCM1(-)',False),('combustion_core/version5', False)],
    seedMechanisms = ['JetSurF2.0', 'BurkeH2O2inN2','BurkeH2O2inArHe', 'C2H4+O_Klipp2017','Klippenstein_Glarborg2016'],
    kineticsDepositories = ['training'],
    kineticsFamilies = 'default',
    kineticsEstimator = 'rate rules',
)
# List of species 
species(
    label = 'nC10H22',
    reactive = True,
    structure = SMILES("CCCCCCCCCC"),
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

species(
    label = 'C5H11',
    reactive = True,
    structure = SMILES("C[CH]CCC"),
)

species(
    label = 'C4H9',
    reactive = True,
    structure = SMILES("C[CH]CC"),
)

species(
    label = 'C7H15',
    reactive = True,
    structure = SMILES("CC[CH]CCCC"),
)

species(
    label = 'C7H14',
    reactive = True,
    structure = SMILES("CCC=CCCC"),
)

species(
    label = 'C4H8',
    reactive = True,
    structure = SMILES("CC=CC"),
)

species(
    label = 'C6H12',
    reactive = True,
    structure = SMILES("CCC=CCC"),
)

species(
    label = 'C6H13',
    reactive = True,
    structure = SMILES("CC[CH]CCC"),
)


species(
    label = 'CHO',
    reactive = True,
    structure = SMILES("[CH]=O"),
)

species(
    label = 'C5H1O',
    reactive = True,
    structure = SMILES("CC=CCC"),
)

species(
    label = 'C5H1O',
    reactive = True,
    structure = SMILES("CC=CCC"),
)

species(
    label = 'C2H6',
    reactive = True,
    structure = SMILES("CC"),
)


species(
    label = 'C3H3',
    reactive = True,
    structure = SMILES("[CH]C=[CH]"),
)


species(
    label = 'C6H6',
    reactive = True,
    structure = SMILES("C1=CC=CC=C1"),
)


species(
    label = 'C6H5',
    reactive = True,
    structure = SMILES("[C]1=CC=CC=C1"),
)


species(
    label = 'C4H6',
    reactive = True,
    structure = SMILES("[[CH2]C=[C]C"),
)


species(
    label = 'C4H6',
    reactive = True,
    structure = SMILES("CCC=CCCCC"),
)



species(
    label = 'C10H21OO',
    reactive = True,
    structure = SMILES("CCCCCCCCCCO[O]"),
)

species(
    label = 'C10H20OOH',
    reactive = True,
    structure = SMILES("CCCCCCC[CH]CCOO"),
)
 

species(
    label = 'OOC10H20OOH',
    reactive = True,
    structure = SMILES("CCCCCCCC(CCOO)O[O]"),
)



species(
    label = 'OC10H19OOH',
    reactive = True,
    structure = SMILES("CC(=O)CCCCCCCCOO"),
)


### Species from Cheng's 2013 model, identified via the mechanism importer 
### (not complete. about 40 species)

# skipping O2
# skipping CO2
# skipping H2O
# skipping CO
# skipping H2
# skipping OH

species(
    label='H2O2',
    reactive=True,
    structure=adjacencyList('''
        1 O u0 p2 c0 {2,S} {3,S}
        2 O u0 p2 c0 {1,S} {4,S}
        3 H u0 p0 c0 {1,S}
        4 H u0 p0 c0 {2,S}
        ''')
    )
    

species(
    label='HO2',
    reactive=True,
    structure=adjacencyList('''
        multiplicity 2
        1 O u0 p2 c0 {2,S} {3,S}
        2 O u1 p2 c0 {1,S}
        3 H u0 p0 c0 {1,S}
        ''')
    )
    

species(
    label='H',
    reactive=True,
    structure=adjacencyList('''
        multiplicity 2
        1 H u1 p0 c0
        ''')
    )
    
# skipping O
# skipping CH4

species(
    label='CH3',
    reactive=True,
    structure=adjacencyList('''
        multiplicity 2
        1 C u1 p0 c0 {2,S} {3,S} {4,S}
        2 H u0 p0 c0 {1,S}
        3 H u0 p0 c0 {1,S}
        4 H u0 p0 c0 {1,S}
        ''')
    )
    
# skipping C2H4

species(
    label='C2H5',
    reactive=True,
    structure=adjacencyList('''
        multiplicity 2
        1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2 C u1 p0 c0 {1,S} {6,S} {7,S}
        3 H u0 p0 c0 {1,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {2,S}
        7 H u0 p0 c0 {2,S}
        ''')
    )
    

species(
    label='CH3OH',
    reactive=True,
    structure=adjacencyList('''
        1 O u0 p2 c0 {2,S} {6,S}
        2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
        3 H u0 p0 c0 {2,S}
        4 H u0 p0 c0 {2,S}
        5 H u0 p0 c0 {2,S}
        6 H u0 p0 c0 {1,S}
        ''')
    )
    
# skipping HE

species(
    label='CH2OH',
    reactive=True,
    structure=adjacencyList('''
        multiplicity 2
        1 O u0 p2 c0 {2,S} {5,S}
        2 C u1 p0 c0 {1,S} {3,S} {4,S}
        3 H u0 p0 c0 {2,S}
        4 H u0 p0 c0 {2,S}
        5 H u0 p0 c0 {1,S}
        ''')
    )
    

species(
    label='CH3O',
    reactive=True,
    structure=adjacencyList('''
        multiplicity 2
        1 O u1 p2 c0 {2,S}
        2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
        3 H u0 p0 c0 {2,S}
        4 H u0 p0 c0 {2,S}
        5 H u0 p0 c0 {2,S}
        ''')
    )
    
# skipping CH2O

species(
    label='HCO',
    reactive=True,
    structure=adjacencyList('''
        multiplicity 2
        1 O u0 p2 c0 {2,D}
        2 C u1 p0 c0 {1,D} {3,S}
        3 H u0 p0 c0 {2,S}
        ''')
    )
    
# skipping C3H6

species(
    label='C2H2',
    reactive=True,
    structure=adjacencyList('''
        1 C u0 p0 c0 {2,T} {3,S}
        2 C u0 p0 c0 {1,T} {4,S}
        3 H u0 p0 c0 {1,S}
        4 H u0 p0 c0 {2,S}
        ''')
    )
    

species(
    label='HCCO',
    reactive=True,
    structure=adjacencyList('''
        multiplicity 2
        1 O u0 p2 c0 {3,D}
        2 C u1 p0 c0 {3,D} {4,S}
        3 C u0 p0 c0 {1,D} {2,D}
        4 H u0 p0 c0 {2,S}
        ''')
    )
    

species(
    label='C2H3',
    reactive=True,
    structure=adjacencyList('''
        multiplicity 2
        1 C u0 p0 c0 {2,D} {3,S} {4,S}
        2 C u1 p0 c0 {1,D} {5,S}
        3 H u0 p0 c0 {1,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {2,S}
        ''')
    )
    

species(
    label='CH2CO',
    reactive=True,
    structure=adjacencyList('''
        1 O u0 p2 c0 {3,D}
        2 C u0 p0 c0 {3,D} {4,S} {5,S}
        3 C u0 p0 c0 {1,D} {2,D}
        4 H u0 p0 c0 {2,S}
        5 H u0 p0 c0 {2,S}
        ''')
    )
    

species(
    label='C3H5',
    reactive=True,
    structure=adjacencyList('''
        multiplicity 2
        1 C u0 p0 c0 {2,S} {3,D} {4,S}
        2 C u1 p0 c0 {1,S} {5,S} {6,S}
        3 C u0 p0 c0 {1,D} {7,S} {8,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {2,S}
        6 H u0 p0 c0 {2,S}
        7 H u0 p0 c0 {3,S}
        8 H u0 p0 c0 {3,S}
        ''')
    )
    

species(
    label='C3H7',
    reactive=True,
    structure=adjacencyList('''
        multiplicity 2
        1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
        2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
        3  C u1 p0 c0 {1,S} {2,S} {10,S}
        4  H u0 p0 c0 {1,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        ''')
    )
    

species(
    label='C3H4',
    reactive=True,
    structure=adjacencyList('''
        1 C u0 p0 c0 {3,D} {4,S} {5,S}
        2 C u0 p0 c0 {3,D} {6,S} {7,S}
        3 C u0 p0 c0 {1,D} {2,D}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {2,S}
        7 H u0 p0 c0 {2,S}
        ''')
    )
    

species(
    label='C5H11CO',
    reactive=True,
    structure=adjacencyList('''
        multiplicity 2
        1  O u0 p2 c0 {7,D}
        2  C u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
        3  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
        4  C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
        5  C u0 p0 c0 {3,S} {7,S} {14,S} {15,S}
        6  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
        7  C u1 p0 c0 {1,D} {5,S}
        8  H u0 p0 c0 {4,S}
        9  H u0 p0 c0 {4,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {6,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        ''')
    )
    
# skipping C10H22

species(
    label='C10H21',
    reactive=True,
    structure=adjacencyList('''
        multiplicity 2
        1  C u0 p0 c0 {3,S} {5,S} {17,S} {18,S}
        2  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
        3  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
        4  C u0 p0 c0 {2,S} {8,S} {11,S} {12,S}
        5  C u0 p0 c0 {1,S} {9,S} {19,S} {20,S}
        6  C u0 p0 c0 {2,S} {10,S} {21,S} {22,S}
        7  C u0 p0 c0 {3,S} {10,S} {23,S} {24,S}
        8  C u0 p0 c0 {4,S} {25,S} {26,S} {27,S}
        9  C u0 p0 c0 {5,S} {28,S} {29,S} {30,S}
        10 C u1 p0 c0 {6,S} {7,S} {31,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {2,S}
        14 H u0 p0 c0 {2,S}
        15 H u0 p0 c0 {3,S}
        16 H u0 p0 c0 {3,S}
        17 H u0 p0 c0 {1,S}
        18 H u0 p0 c0 {1,S}
        19 H u0 p0 c0 {5,S}
        20 H u0 p0 c0 {5,S}
        21 H u0 p0 c0 {6,S}
        22 H u0 p0 c0 {6,S}
        23 H u0 p0 c0 {7,S}
        24 H u0 p0 c0 {7,S}
        25 H u0 p0 c0 {8,S}
        26 H u0 p0 c0 {8,S}
        27 H u0 p0 c0 {8,S}
        28 H u0 p0 c0 {9,S}
        29 H u0 p0 c0 {9,S}
        30 H u0 p0 c0 {9,S}
        31 H u0 p0 c0 {10,S}
        ''')
    )
    

species(
    label='C10H20',
    reactive=True,
    structure=adjacencyList('''
        1  C u0 p0 c0 {2,S} {3,S} {15,S} {16,S}
        2  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
        3  C u0 p0 c0 {1,S} {8,S} {17,S} {18,S}
        4  C u0 p0 c0 {5,S} {7,S} {11,S} {12,S}
        5  C u0 p0 c0 {4,S} {9,S} {19,S} {20,S}
        6  C u0 p0 c0 {2,S} {10,S} {21,S} {22,S}
        7  C u0 p0 c0 {4,S} {23,S} {24,S} {25,S}
        8  C u0 p0 c0 {3,S} {26,S} {27,S} {28,S}
        9  C u0 p0 c0 {5,S} {10,D} {29,S}
        10 C u0 p0 c0 {6,S} {9,D} {30,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {2,S}
        14 H u0 p0 c0 {2,S}
        15 H u0 p0 c0 {1,S}
        16 H u0 p0 c0 {1,S}
        17 H u0 p0 c0 {3,S}
        18 H u0 p0 c0 {3,S}
        19 H u0 p0 c0 {5,S}
        20 H u0 p0 c0 {5,S}
        21 H u0 p0 c0 {6,S}
        22 H u0 p0 c0 {6,S}
        23 H u0 p0 c0 {7,S}
        24 H u0 p0 c0 {7,S}
        25 H u0 p0 c0 {7,S}
        26 H u0 p0 c0 {8,S}
        27 H u0 p0 c0 {8,S}
        28 H u0 p0 c0 {8,S}
        29 H u0 p0 c0 {9,S}
        30 H u0 p0 c0 {10,S}
        ''')
    )


# Reaction systems 1 for the high temperature range with Nitrogen as the bath gas for air 0.1%nC10H22 
simpleReactor(
    temperature=[(550,'K'),(1500,'K')],#max reactor temperature must always be less than max pdep temperature
    pressure=[(1.0,'bar'),(40.0,'bar')],
    nSims=5,
    initialMoleFractions={
        # "nC10H22": 0.000983928, # phi = 1
        "nC10H22": [0.000983928/2, 0.000983928*2], # range of 0.5 < phi < 2
        "N2": 0.983765 ,
        "O2": 0.0152509,
        },
    terminationTime=(1.0, 's'),
    terminationRateRatio=0.01,
)



# Reaction systems 2 for the high temperature range with Argon diluted in 3.1% Oxygen 0.2% nC10H22
simpleReactor(
    temperature=[(550,'K'),(1500,'K')],#max reactor temperature must always be less than max pdep temperature
    pressure=[(1.0,'bar'),(40.0,'bar')],
    nSims=5,
    initialMoleFractions={
        # "nC10H22": 0.00200401, # phi = 1
        "nC10H22": [0.00200401/2, 0.00200401*2], # range of 0.5 < phi < 2
        "Ar":  0.966934,
        "O2":  0.0310621,
        },
    terminationTime=(1.0, 's'),
    terminationRateRatio=0.01,
)


# Reaction systems 3 for the high temperature range with Argon diluted in air 23.25% O2 1.5% nC10H22 
simpleReactor(
    temperature=[(550,'K'),(1500,'K')],#max reactor temperature must always be less than max pdep temperature
    pressure=[(1.0,'bar'),(40.0,'bar')],
    nSims=5,
    initialMoleFractions={
        # "nC10H22": 0.015, # phi = 1
        "nC10H22": [0.015/2, 0.015*2], # range of 0.5 < phi < 2
        "Ar": 0.7525,
        "O2": 0.2325,
        },
    terminationTime=(1.0, 's'),
    terminationRateRatio=0.01,   
)

# Reaction systems 4 for the high temperature range with Argon diluted in air 8.4% O2 0.52% nC10H22 
simpleReactor(
    temperature=[(550,'K'),(1500,'K')],#max reactor temperature must always be less than max pdep temperature
    pressure=[(1.0,'bar'),(40.0,'bar')],
    nSims=5,
    initialMoleFractions={
        # "nC10H22": 0.00541817, # phi = 1
        "nC10H22": [0.00541817/2, 0.00541817*2], # range of 0.5 < phi < 2
        "Ar": 0.9106,
        "O2": 0.0839816,
        },
    terminationTime=(1.0, 's'),
    terminationRateRatio=0.01,  
)


# Reaction systems 5 for the high temperature range with Argon diluted in air 11% O2 0.82% nC10H22 
simpleReactor(
    temperature=[(550,'K'),(1500,'K')],#max reactor temperature must always be less than max pdep temperature
    pressure=[(1.0,'bar'),(40.0,'bar')],
    nSims=5,
    initialMoleFractions={
        # "nC10H22": 0.00710461, # phi = 1
        "nC10H22": [0.00710461/2, 0.00710461*2], # range of 0.5 < phi < 2
        "Ar": 0.882774,
        "O2": 0.110121,
        },
    terminationTime=(1.0, 's'),
    terminationRateRatio=0.01,      
)    


# Reaction systems 6 for the high temperature range with Argon diluted in air 7.5% O2 0.49% nC10H22 
simpleReactor(
    temperature=[(550,'K'),(1500,'K')],#max reactor temperature must always be less than max pdep temperature
    pressure=[(1.0,'bar'),(40.0,'bar')],
    nSims=5,
    initialMoleFractions={
        # "nC10H22": 0.00483901, # phi = 1
        "nC10H22": [0.00483901/2, 0.00483901*2], # range of 0.5 < phi < 2
        "Ar": 0.920156,
        "O2": 0.0750046,
        },
    terminationTime=(1.0, 's'),
    terminationRateRatio=0.01,      
) 



# Reaction system 7 for the low temperature range which is the region of interest using Argon as the bath gas with 12.7% O2 0.74% nC10H22
simpleReactor(
    temperature=[(550,'K'),(800,'K')],
    pressure=[(1.0,'bar'),(40.0,'bar')],
    nSims=17,
    initialMoleFractions={
        # "nC10H22": 0.00818705, # phi = 1
        "nC10H22": [0.00818705/2, 0.00818705*2], # range of 0.5 < phi < 2
        "Ar": 0.864914,
        "O2": 0.126899,
        },
    terminationTime=(1.0, 's'),
    terminationRateRatio=0.01,
)

# Reaction system 8 for the low temperature range which is the region of interest using Argon as the bath gas with 4.16% O2 0.81% nC10H22
simpleReactor(
    temperature=[(550,'K'),(800,'K')],
    pressure=[(1.0,'bar'),(40.0,'bar')],
    nSims=17,
    initialMoleFractions={
        # "nC10H22": 0.00269849, # phi = 1
        "nC10H22": [0.00269849/2, 0.00269849*2], # range of 0.5 < phi < 2
        "Ar": 0.955475 ,
        "O2": 0.0418265,
        },
    terminationTime=(1.0, 's'),
    terminationRateRatio=0.01,
)


# Reaction system 9 for the low temperature range which is the region of interest using Argon as the bath gas with 7.4% O2 0.75% nC10H22
simpleReactor(
    temperature=[(550,'K'),(800,'K')],
    pressure=[(1.0,'bar'),(40.0,'bar')],
    nSims=17,
    initialMoleFractions={
        # "nC10H22": 0.00478724, # phi = 1
        "nC10H22": [0.00478724/2, 0.00478724*2], # range of 0.5 < phi < 2
        "Ar": 0.92101 ,
        "O2": 0.0742023,
        },
    terminationTime=(1.0, 's'),
    terminationRateRatio=0.01,
)



# Reaction system 10 for the low temperature range which is the region of interest using Argon as the bath gas with 17.6% O2 0.78% nC10H22
simpleReactor(
    temperature=[(550,'K'),(800,'K')],
    pressure=[(1.0,'bar'),(40.0,'bar')],
    nSims=17,
    initialMoleFractions={
        # "nC10H22": 0.0113146, # phi = 1
        "nC10H22": [0.0113146/2, 0.0113146*2], # range of 0.5 < phi < 2
        "Ar": 0.813309 ,
        "O2": 0.175377,
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
    atol=1e-16,
    rtol=1e-8,
)

model(
    toleranceKeepInEdge=0.05,
    toleranceInterruptSimulation=1e8,
    toleranceMoveToCore=0.5,
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
    name='Zil_nc10(2)',
    saveRestartPeriod=None,
    generateOutputHTML=False,
    generateSeedEachIteration=True,
    saveSeedToDatabase=True,
    generatePlots=False,
    verboseComments=False,
    saveEdgeSpecies=False,
    saveSimulationProfiles=True, 
)

# Introduced the species constraint for the mechanism. Set the maximumRadicalElectrons to 2 for N2
generatedSpeciesConstraints(
    allowed=['input species','seed mechanisms','reaction libraries'],
    maximumCarbonAtoms=10,
    maximumOxygenAtoms=4,
    maximumRadicalElectrons=2,
    allowSingletO2 = True,
)

