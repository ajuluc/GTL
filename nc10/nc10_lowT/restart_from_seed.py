restartFromSeed(path='seed')

# Data sources
database(
    thermoLibraries = ['BurkeH2O2', 'Klippenstein_Glarborg2016' , 'JetSurF2.0', 'CurranPentane','FFCM1(-)','primaryThermoLibrary', 'thermo_DFT_CCSDTF12_BAC', 'DFT_QCI_thermo', 'CBS_QB3_1dHR'],
    reactionLibraries = [('CurranPentane',False),('FFCM1(-)',False),('combustion_core/version5', False)],
    seedMechanisms = ['BurkeH2O2inN2','BurkeH2O2inArHe', 'Klippenstein_Glarborg2016', 'C2H4+O_Klipp2017','JetSurF2.0'],
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
    label = 'C2H6',
    reactive = True,
    structure = SMILES("CC"),
)

species(
    label = 'C5H1O',
    reactive = True,
    structure = SMILES("CC=CCC"),
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
    structure = SMILES("[CH2]C=[C]C"),
)


species(
    label = 'C4H6',
    reactive = True,
    structure = SMILES("CCC=CCCCC"),
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

# R

species(
    label='R_1',
    reactive=True,
    structure=SMILES("CCC[CH]CCCCCC")
)


species(
    label='R_2',
    reactive=True,
    structure=SMILES("CCCC[CH]CCCCC")
)


species(
    label='R_3',
    reactive=True,
    structure=SMILES("C[CH]CCCCCCCC")
)


species(
    label='R_4',
    reactive=True,
    structure=SMILES("CC[CH]CCCCCCC")
)


species(
    label='R_5',
    reactive=True,
    structure=SMILES("[CH2]CCCCCCCCC")
)


# H

species(
    label='H_1',
    reactive=True,
    structure=SMILES("[H]")
)

# ROO

species(
    label='ROO_1',
    reactive=True,
    structure=SMILES("CCCCCCCCCCO[O]")
)


species(
    label='ROO_2',
    reactive=True,
    structure=SMILES("CCCCCCCCC(C)O[O]")
)


species(
    label='ROO_3',
    reactive=True,
    structure=SMILES("CCCCCCC(CCC)O[O]")
)


species(
    label='ROO_4',
    reactive=True,
    structure=SMILES("CCCCCCCC(CC)O[O]")
)


species(
    label='ROO_5',
    reactive=True,
    structure=SMILES("CCCCCC(CCCC)O[O]")
)

##############################
# QOOH

species(
    label='QOOH_1',
    reactive=True,
    structure=SMILES("CCCCCC[CH]CCCOO")
)


species(
    label='QOOH_2',
    reactive=True,
    structure=SMILES("CCCC[CH]CCCCCOO")
)


species(
    label='QOOH_3',
    reactive=True,
    structure=SMILES("CCCCCCCC[C](C)OO")
)


species(
    label='QOOH_4',
    reactive=True,
    structure=SMILES("CCCCCCC[CH]C(C)OO")
)


species(
    label='QOOH_5',
    reactive=True,
    structure=SMILES("[CH2]C(CCCCCCCC)OO")
)


species(
    label='QOOH_6',
    reactive=True,
    structure=SMILES("CCCCCC[CH]CC(C)OO")
)


species(
    label='QOOH_7',
    reactive=True,
    structure=SMILES("CCCCC[CH]CCC(C)OO")
)


species(
    label='QOOH_8',
    reactive=True,
    structure=SMILES("CCCCCCCC[CH]COO")
)


species(
    label='QOOH_9',
    reactive=True,
    structure=SMILES("[CH2]CCC(CCCCCC)OO")
)


species(
    label='QOOH_10',
    reactive=True,
    structure=SMILES("CC[CH]CCCC(CCC)OO")
)


species(
    label='QOOH_11',
    reactive=True,
    structure=SMILES("CCCC[CH]C(CCCC)OO")
)


species(
    label='QOOH_12',
    reactive=True,
    structure=SMILES("CCC[CH]C(CCCCC)OO")
)


species(
    label='QOOH_13',
    reactive=True,
    structure=SMILES("CCC[CH]CC(CCCC)OO")
)


species(
    label='QOOH_14',
    reactive=True,
    structure=SMILES("CC[CH]CC(CCCCC)OO")
)


species(
    label='QOOH_15',
    reactive=True,
    structure=SMILES("CC[CH]CCC(CCCC)OO")
)


species(
    label='QOOH_16',
    reactive=True,
    structure=SMILES("C[CH]CCC(CCCCC)OO")
)


species(
    label='QOOH_17',
    reactive=True,
    structure=SMILES("C[CH]CCCC(CCCC)OO")
)


species(
    label='QOOH_18',
    reactive=True,
    structure=SMILES("[CH2]CCCC(CCCCC)OO")
)


species(
    label='QOOH_19',
    reactive=True,
    structure=SMILES("[CH2]CCCCC(CCCC)OO")
)


species(
    label='QOOH_20',
    reactive=True,
    structure=SMILES("C[CH]CCCCC(CCC)OO")
)


species(
    label='QOOH_21',
    reactive=True,
    structure=SMILES("CCCCCCC[C](CC)OO")
)


species(
    label='QOOH_22',
    reactive=True,
    structure=SMILES("CCCCCC[CH]C(CC)OO")
)


species(
    label='QOOH_23',
    reactive=True,
    structure=SMILES("C[CH]C(CCCCCCC)OO")
)


species(
    label='QOOH_24',
    reactive=True,
    structure=SMILES("CCCCC[CH]CC(CC)OO")
)


species(
    label='QOOH_25',
    reactive=True,
    structure=SMILES("[CH2]CC(CCCCCCC)OO")
)


species(
    label='QOOH_26',
    reactive=True,
    structure=SMILES("CCCC[CH]CCC(CC)OO")
)


species(
    label='QOOH_27',
    reactive=True,
    structure=SMILES("CCC[CH]CCCC(CC)OO")
)


species(
    label='QOOH_28',
    reactive=True,
    structure=SMILES("CC[CH]CCCCC(CC)OO")
)


species(
    label='QOOH_29',
    reactive=True,
    structure=SMILES("CCCCC[C](CCCC)OO")
)


species(
    label='QOOH_30',
    reactive=True,
    structure=SMILES("CCC[CH]CCCCC(C)OO")
)


species(
    label='QOOH_31',
    reactive=True,
    structure=SMILES("CCCCCC[C](CCC)OO")
)


species(
    label='QOOH_32',
    reactive=True,
    structure=SMILES("CCCCC[CH]C(CCC)OO")
)


species(
    label='QOOH_33',
    reactive=True,
    structure=SMILES("CC[CH]C(CCCCCC)OO")
)


species(
    label='QOOH_34',
    reactive=True,
    structure=SMILES("CCCC[CH]CC(CCC)OO")
)


species(
    label='QOOH_35',
    reactive=True,
    structure=SMILES("C[CH]CC(CCCCCC)OO")
)


species(
    label='QOOH_36',
    reactive=True,
    structure=SMILES("CCC[CH]CCC(CCC)OO")
)


species(
    label='QOOH_37',
    reactive=True,
    structure=SMILES("CCCCC[CH]CCCCOO")
)


species(
    label='QOOH_38',
    reactive=True,
    structure=SMILES("CCCCCCC[CH]CCOO")
)


species(
    label='QOOH_39',
    reactive=True,
    structure=SMILES("CCCCCCCCC[CH]OO")
)


species(
    label='QOOH_40',
    reactive=True,
    structure=SMILES("CCCC[CH]CCCC(C)OO")
)

##############################
# O2QOOH

species(
    label='O2QOOH_1',
    reactive=True,
    structure=SMILES("CCCCCCC(CC(C)O[O])OO")
)


species(
    label='O2QOOH_2',
    reactive=True,
    structure=SMILES("CCCC(CCC(CCC)OO)O[O]")
)


species(
    label='O2QOOH_3',
    reactive=True,
    structure=SMILES("CCCCCC(CCCCOO)O[O]")
)


species(
    label='O2QOOH_4',
    reactive=True,
    structure=SMILES("CCCCCCCC(CCOO)O[O]")
)


species(
    label='O2QOOH_5',
    reactive=True,
    structure=SMILES("CCCCCCCCCC(O[O])OO")
)


species(
    label='O2QOOH_6',
    reactive=True,
    structure=SMILES("CCCCC(CCCC(C)OO)O[O]")
)


species(
    label='O2QOOH_7',
    reactive=True,
    structure=SMILES("CCCCCCC(CCC)(O[O])OO")
)


species(
    label='O2QOOH_8',
    reactive=True,
    structure=SMILES("CCCCCC(O[O])C(CCC)OO")
)


species(
    label='O2QOOH_9',
    reactive=True,
    structure=SMILES("CCCCCCC(OO)C(CC)O[O]")
)


species(
    label='O2QOOH_10',
    reactive=True,
    structure=SMILES("CCCCC(CC(CCC)OO)O[O]")
)


species(
    label='O2QOOH_11',
    reactive=True,
    structure=SMILES("CCCCCCCC(CC)(O[O])OO")
)


species(
    label='O2QOOH_12',
    reactive=True,
    structure=SMILES("CCCCCCC(O[O])C(CC)OO")
)


species(
    label='O2QOOH_13',
    reactive=True,
    structure=SMILES("CCCCCCCC(OO)C(C)O[O]")
)


species(
    label='O2QOOH_14',
    reactive=True,
    structure=SMILES("CCCCCC(CC(CC)OO)O[O]")
)


species(
    label='O2QOOH_15',
    reactive=True,
    structure=SMILES("CCCCCCCC(CCO[O])OO")
)


species(
    label='O2QOOH_16',
    reactive=True,
    structure=SMILES("CCCCC(CCC(CC)OO)O[O]")
)


species(
    label='O2QOOH_17',
    reactive=True,
    structure=SMILES("CCCC(CCCC(CC)OO)O[O]")
)


species(
    label='O2QOOH_18',
    reactive=True,
    structure=SMILES("CCC(CCCCC(CC)OO)O[O]")
)


species(
    label='O2QOOH_19',
    reactive=True,
    structure=SMILES("CCCCCC(CCCC)(O[O])OO")
)


species(
    label='O2QOOH_20',
    reactive=True,
    structure=SMILES("CCCC(CCCCC(C)OO)O[O]")
)


species(
    label='O2QOOH_21',
    reactive=True,
    structure=SMILES("CCCCC(CCCC(C)O[O])OO")
)


species(
    label='O2QOOH_22',
    reactive=True,
    structure=SMILES("CCCCCC(CCCCO[O])OO")
)


species(
    label='O2QOOH_23',
    reactive=True,
    structure=SMILES("CCCCC(CCCCCO[O])OO")
)


species(
    label='O2QOOH_24',
    reactive=True,
    structure=SMILES("CCCCCCCCC(C)(O[O])OO")
)


species(
    label='O2QOOH_25',
    reactive=True,
    structure=SMILES("CCCCCCCCC(CO[O])OO")
)


species(
    label='O2QOOH_26',
    reactive=True,
    structure=SMILES("CCCCC(CCCCCOO)O[O]")
)


species(
    label='O2QOOH_27',
    reactive=True,
    structure=SMILES("CCCCCCCC(O[O])C(C)OO")
)


species(
    label='O2QOOH_28',
    reactive=True,
    structure=SMILES("CCCCCCC(CC(C)OO)O[O]")
)


species(
    label='O2QOOH_29',
    reactive=True,
    structure=SMILES("CCCCCC(CCC(C)OO)O[O]")
)


species(
    label='O2QOOH_30',
    reactive=True,
    structure=SMILES("CCCCCCCCC(COO)O[O]")
)


species(
    label='O2QOOH_31',
    reactive=True,
    structure=SMILES("CCCCCCC(CCCO[O])OO")
)


species(
    label='O2QOOH_32',
    reactive=True,
    structure=SMILES("CCCC(CCCC(CC)O[O])OO")
)


species(
    label='O2QOOH_33',
    reactive=True,
    structure=SMILES("CCCCC(O[O])C(CCCC)OO")
)


species(
    label='O2QOOH_34',
    reactive=True,
    structure=SMILES("CCCCCC(OO)C(CCC)O[O]")
)


species(
    label='O2QOOH_35',
    reactive=True,
    structure=SMILES("CCCCC(CC(CCC)O[O])OO")
)


species(
    label='O2QOOH_36',
    reactive=True,
    structure=SMILES("CCCCCC(CC(CC)O[O])OO")
)


species(
    label='O2QOOH_37',
    reactive=True,
    structure=SMILES("CCCCCCC(CCCOO)O[O]")
)


species(
    label='O2QOOH_38',
    reactive=True,
    structure=SMILES("CCCCC(CCC(CC)O[O])OO")
)


species(
    label='O2QOOH_39',
    reactive=True,
    structure=SMILES("CCCCCC(CCC(C)O[O])OO")
)


species(
    label='O2QOOH_40',
    reactive=True,
    structure=SMILES("CCCC(CCCCC(C)O[O])OO")
)

##############################
# HOOQjOOH

species(
    label='HOOQjOOH_1',
    reactive=True,
    structure=SMILES("CCCCCC[C](CCCOO)OO")
)


species(
    label='HOOQjOOH_2',
    reactive=True,
    structure=SMILES("CCCC[C](OO)C(CCCC)OO")
)


species(
    label='HOOQjOOH_3',
    reactive=True,
    structure=SMILES("CCCCCCCC[C](COO)OO")
)


species(
    label='HOOQjOOH_4',
    reactive=True,
    structure=SMILES("CCCCC[C](CCC(C)OO)OO")
)


species(
    label='HOOQjOOH_5',
    reactive=True,
    structure=SMILES("CCCCCC(CC[C](C)OO)OO")
)


species(
    label='HOOQjOOH_6',
    reactive=True,
    structure=SMILES("CCCCCCC(CC[CH]OO)OO")
)


species(
    label='HOOQjOOH_7',
    reactive=True,
    structure=SMILES("CCCC[C](CCC(CC)OO)OO")
)


species(
    label='HOOQjOOH_8',
    reactive=True,
    structure=SMILES("CCCCC(CC[C](CC)OO)OO")
)


species(
    label='HOOQjOOH_9',
    reactive=True,
    structure=SMILES("CCC[C](CCCC(CC)OO)OO")
)


species(
    label='HOOQjOOH_10',
    reactive=True,
    structure=SMILES("CCCC(CCC[C](CC)OO)OO")
)


species(
    label='HOOQjOOH_11',
    reactive=True,
    structure=SMILES("CC[C](CCCCC(CC)OO)OO")
)


species(
    label='HOOQjOOH_12',
    reactive=True,
    structure=SMILES("CCC[C](CCCCC(C)OO)OO")
)


species(
    label='HOOQjOOH_13',
    reactive=True,
    structure=SMILES("CCCC(CCCC[C](C)OO)OO")
)


species(
    label='HOOQjOOH_14',
    reactive=True,
    structure=SMILES("CCCCC(CCCC[CH]OO)OO")
)


species(
    label='HOOQjOOH_15',
    reactive=True,
    structure=SMILES("CCCC[C](CCCCCOO)OO")
)


species(
    label='HOOQjOOH_16',
    reactive=True,
    structure=SMILES("CCCCCCCCC([CH]OO)OO")
)


species(
    label='HOOQjOOH_17',
    reactive=True,
    structure=SMILES("CCCCCCCC(OO)[C](C)OO")
)


species(
    label='HOOQjOOH_18',
    reactive=True,
    structure=SMILES("CCCCCCC[C](OO)C(C)OO")
)


species(
    label='HOOQjOOH_19',
    reactive=True,
    structure=SMILES("CCCCC[C](CC(CC)OO)OO")
)


species(
    label='HOOQjOOH_20',
    reactive=True,
    structure=SMILES("CCC[C](CCC(CCC)OO)OO")
)


species(
    label='HOOQjOOH_21',
    reactive=True,
    structure=SMILES("CCCCCC(CCC[CH]OO)OO")
)


species(
    label='HOOQjOOH_22',
    reactive=True,
    structure=SMILES("CCCCCC[C](CC(C)OO)OO")
)


species(
    label='HOOQjOOH_23',
    reactive=True,
    structure=SMILES("CCCCC[C](CCCCOO)OO")
)


species(
    label='HOOQjOOH_24',
    reactive=True,
    structure=SMILES("CCCCCCC[C](CCOO)OO")
)


species(
    label='HOOQjOOH_25',
    reactive=True,
    structure=SMILES("CCCCCCCC(C[CH]OO)OO")
)


species(
    label='HOOQjOOH_26',
    reactive=True,
    structure=SMILES("CCCCCCCCC[C](OO)OO")
)


species(
    label='HOOQjOOH_27',
    reactive=True,
    structure=SMILES("CCCC[C](CCCC(C)OO)OO")
)


species(
    label='HOOQjOOH_28',
    reactive=True,
    structure=SMILES("CCCCC(CCC[C](C)OO)OO")
)


species(
    label='HOOQjOOH_29',
    reactive=True,
    structure=SMILES("CCCCC[C](OO)C(CCC)OO")
)


species(
    label='HOOQjOOH_30',
    reactive=True,
    structure=SMILES("CCCCCC(OO)[C](CCC)OO")
)


species(
    label='HOOQjOOH_31',
    reactive=True,
    structure=SMILES("CCCCCCC(OO)[C](CC)OO")
)


species(
    label='HOOQjOOH_32',
    reactive=True,
    structure=SMILES("CCCCCC[C](OO)C(CC)OO")
)


species(
    label='HOOQjOOH_33',
    reactive=True,
    structure=SMILES("CCCCCCC(C[C](C)OO)OO")
)


species(
    label='HOOQjOOH_34',
    reactive=True,
    structure=SMILES("CCCC[C](CC(CCC)OO)OO")
)


species(
    label='HOOQjOOH_35',
    reactive=True,
    structure=SMILES("CCCCC(C[C](CCC)OO)OO")
)


species(
    label='HOOQjOOH_36',
    reactive=True,
    structure=SMILES("CCCCCC(C[C](CC)OO)OO")
)

##############################
# ketohydroperoxide

species(
    label='ketohydroperoxide_1',
    reactive=True,
    structure=SMILES("CCCCC(=O)CCC(CC)OO")
)


species(
    label='ketohydroperoxide_2',
    reactive=True,
    structure=SMILES("CCCCC(CCC(=O)CC)OO")
)


species(
    label='ketohydroperoxide_3',
    reactive=True,
    structure=SMILES("CCCC(=O)CCCC(CC)OO")
)


species(
    label='ketohydroperoxide_4',
    reactive=True,
    structure=SMILES("CCCC(CCCC(=O)CC)OO")
)


species(
    label='ketohydroperoxide_5',
    reactive=True,
    structure=SMILES("CCC(=O)CCCCC(CC)OO")
)


species(
    label='ketohydroperoxide_6',
    reactive=True,
    structure=SMILES("CCCC(=O)CCCCC(C)OO")
)


species(
    label='ketohydroperoxide_7',
    reactive=True,
    structure=SMILES("CCCCCC(=O)CCC(C)OO")
)


species(
    label='ketohydroperoxide_8',
    reactive=True,
    structure=SMILES("CCCCCCC(=O)CCCOO")
)


species(
    label='ketohydroperoxide_9',
    reactive=True,
    structure=SMILES("CCCC(=O)CCC(CCC)OO")
)


species(
    label='ketohydroperoxide_10',
    reactive=True,
    structure=SMILES("CCCCCC(CCCC=O)OO")
)


species(
    label='ketohydroperoxide_11',
    reactive=True,
    structure=SMILES("CCCCCCC(=O)C(CC)OO")
)


species(
    label='ketohydroperoxide_12',
    reactive=True,
    structure=SMILES("CCCCCCC(CC(C)=O)OO")
)


species(
    label='ketohydroperoxide_13',
    reactive=True,
    structure=SMILES("CCCCC(=O)CC(CCC)OO")
)


species(
    label='ketohydroperoxide_14',
    reactive=True,
    structure=SMILES("CCCCC(CC(=O)CCC)OO")
)


species(
    label='ketohydroperoxide_15',
    reactive=True,
    structure=SMILES("CCCCCC(CC(=O)CC)OO")
)


species(
    label='ketohydroperoxide_16',
    reactive=True,
    structure=SMILES("CCCCCCC(=O)CC(C)OO")
)


species(
    label='ketohydroperoxide_17',
    reactive=True,
    structure=SMILES("CCCCCC(=O)CCCCOO")
)


species(
    label='ketohydroperoxide_18',
    reactive=True,
    structure=SMILES("CCCCCCCC(=O)CCOO")
)


species(
    label='ketohydroperoxide_19',
    reactive=True,
    structure=SMILES("CCCCCCCC(CC=O)OO")
)


species(
    label='ketohydroperoxide_20',
    reactive=True,
    structure=SMILES("CCCCCCCCCC(=O)OO")
)


species(
    label='ketohydroperoxide_21',
    reactive=True,
    structure=SMILES("CCCCC(=O)CCCC(C)OO")
)


species(
    label='ketohydroperoxide_22',
    reactive=True,
    structure=SMILES("CCCCC(CCCC(C)=O)OO")
)


species(
    label='ketohydroperoxide_23',
    reactive=True,
    structure=SMILES("CCCCCC(=O)C(CCC)OO")
)


species(
    label='ketohydroperoxide_24',
    reactive=True,
    structure=SMILES("CCCCCC(OO)C(=O)CCC")
)


species(
    label='ketohydroperoxide_25',
    reactive=True,
    structure=SMILES("CCCCCCC(OO)C(=O)CC")
)


species(
    label='ketohydroperoxide_26',
    reactive=True,
    structure=SMILES("CCCCCCCCC(C=O)OO")
)


species(
    label='ketohydroperoxide_27',
    reactive=True,
    structure=SMILES("CCCCCCCC(OO)C(C)=O")
)


species(
    label='ketohydroperoxide_28',
    reactive=True,
    structure=SMILES("CCCCCCCC(=O)C(C)OO")
)


species(
    label='ketohydroperoxide_29',
    reactive=True,
    structure=SMILES("CCCCCC(=O)CC(CC)OO")
)


species(
    label='ketohydroperoxide_30',
    reactive=True,
    structure=SMILES("CCCC(CCCCC(C)=O)OO")
)


species(
    label='ketohydroperoxide_31',
    reactive=True,
    structure=SMILES("CCCCC(CCCCC=O)OO")
)


species(
    label='ketohydroperoxide_32',
    reactive=True,
    structure=SMILES("CCCCCC(CCC(C)=O)OO")
)


species(
    label='ketohydroperoxide_33',
    reactive=True,
    structure=SMILES("CCCCCCCCC(=O)COO")
)


species(
    label='ketohydroperoxide_34',
    reactive=True,
    structure=SMILES("CCCCC(=O)C(CCCC)OO")
)


species(
    label='ketohydroperoxide_35',
    reactive=True,
    structure=SMILES("CCCCCCC(CCC=O)OO")
)


species(
    label='ketohydroperoxide_36',
    reactive=True,
    structure=SMILES("CCCCC(=O)CCCCCOO")
)

##############################
# alkoxy_radical

species(
    label='alkoxy_radical_1',
    reactive=True,
    structure=SMILES("CCCCCC(=O)CC([O])CC")
)


species(
    label='alkoxy_radical_2',
    reactive=True,
    structure=SMILES("CCCC([O])CCCCC(C)=O")
)


species(
    label='alkoxy_radical_3',
    reactive=True,
    structure=SMILES("CCCCC([O])CCCCC=O")
)


species(
    label='alkoxy_radical_4',
    reactive=True,
    structure=SMILES("CCCCCC([O])CCC(C)=O")
)


species(
    label='alkoxy_radical_5',
    reactive=True,
    structure=SMILES("CCCCCCCCC(=O)C[O]")
)


species(
    label='alkoxy_radical_6',
    reactive=True,
    structure=SMILES("CCCCC(=O)C([O])CCCC")
)


species(
    label='alkoxy_radical_7',
    reactive=True,
    structure=SMILES("CCCCCCC([O])CCC=O")
)


species(
    label='alkoxy_radical_8',
    reactive=True,
    structure=SMILES("CCCCC(=O)CCCCC[O]")
)


species(
    label='alkoxy_radical_9',
    reactive=True,
    structure=SMILES("CCCCCCCC([O])CC=O")
)


species(
    label='alkoxy_radical_10',
    reactive=True,
    structure=SMILES("CCCCCCCCCC([O])=O")
)


species(
    label='alkoxy_radical_11',
    reactive=True,
    structure=SMILES("CCCCC(=O)CCCC(C)[O]")
)


species(
    label='alkoxy_radical_12',
    reactive=True,
    structure=SMILES("CCCCC([O])CCCC(C)=O")
)


species(
    label='alkoxy_radical_13',
    reactive=True,
    structure=SMILES("CCCCCC(=O)C([O])CCC")
)


species(
    label='alkoxy_radical_14',
    reactive=True,
    structure=SMILES("CCCCCC([O])C(=O)CCC")
)


species(
    label='alkoxy_radical_15',
    reactive=True,
    structure=SMILES("CCCCCCC([O])C(=O)CC")
)


species(
    label='alkoxy_radical_16',
    reactive=True,
    structure=SMILES("CCCCCCCCC([O])C=O")
)


species(
    label='alkoxy_radical_17',
    reactive=True,
    structure=SMILES("CCCCCCCC([O])C(C)=O")
)


species(
    label='alkoxy_radical_18',
    reactive=True,
    structure=SMILES("CCCCCCCC(=O)C(C)[O]")
)


species(
    label='alkoxy_radical_19',
    reactive=True,
    structure=SMILES("CCCC([O])CCCC(=O)CC")
)


species(
    label='alkoxy_radical_20',
    reactive=True,
    structure=SMILES("CCCCC(=O)CCC([O])CC")
)


species(
    label='alkoxy_radical_21',
    reactive=True,
    structure=SMILES("CCCC(=O)CCCC([O])CC")
)


species(
    label='alkoxy_radical_22',
    reactive=True,
    structure=SMILES("CCC(=O)CCCCC([O])CC")
)


species(
    label='alkoxy_radical_23',
    reactive=True,
    structure=SMILES("CCCCC([O])CCC(=O)CC")
)


species(
    label='alkoxy_radical_24',
    reactive=True,
    structure=SMILES("CCCC(=O)CCCCC(C)[O]")
)


species(
    label='alkoxy_radical_25',
    reactive=True,
    structure=SMILES("CCCCCC(=O)CCC(C)[O]")
)


species(
    label='alkoxy_radical_26',
    reactive=True,
    structure=SMILES("CCCCCCC(=O)CCC[O]")
)


species(
    label='alkoxy_radical_27',
    reactive=True,
    structure=SMILES("CCCC(=O)CCC([O])CCC")
)


species(
    label='alkoxy_radical_28',
    reactive=True,
    structure=SMILES("CCCCCC([O])CCCC=O")
)


species(
    label='alkoxy_radical_29',
    reactive=True,
    structure=SMILES("CCCCCCC(=O)C([O])CC")
)


species(
    label='alkoxy_radical_30',
    reactive=True,
    structure=SMILES("CCCCCCC([O])CC(C)=O")
)


species(
    label='alkoxy_radical_31',
    reactive=True,
    structure=SMILES("CCCCC(=O)CC([O])CCC")
)


species(
    label='alkoxy_radical_32',
    reactive=True,
    structure=SMILES("CCCCC([O])CC(=O)CCC")
)


species(
    label='alkoxy_radical_33',
    reactive=True,
    structure=SMILES("CCCCCC([O])CC(=O)CC")
)


species(
    label='alkoxy_radical_34',
    reactive=True,
    structure=SMILES("CCCCCCC(=O)CC(C)[O]")
)


species(
    label='alkoxy_radical_35',
    reactive=True,
    structure=SMILES("CCCCCC(=O)CCCC[O]")
)


species(
    label='alkoxy_radical_36',
    reactive=True,
    structure=SMILES("CCCCCCCC(=O)CC[O]")
)

##############################
# OH

species(
    label='OH_1',
    reactive=True,
    structure=SMILES("[OH]")
)

##############################
# QeneOOH

species(
    label='QeneOOH_1',
    reactive=True,
    structure=SMILES("CCC=CCC(CCCC)OO")
)


species(
    label='QeneOOH_2',
    reactive=True,
    structure=SMILES("CC=CCC(CCCCC)OO")
)


species(
    label='QeneOOH_3',
    reactive=True,
    structure=SMILES("C=CCCCCC(CCC)OO")
)


species(
    label='QeneOOH_4',
    reactive=True,
    structure=SMILES("CCCC=CCCCCCOO")
)


species(
    label='QeneOOH_5',
    reactive=True,
    structure=SMILES("CCCCCCC=CC(C)OO")
)


species(
    label='QeneOOH_6',
    reactive=True,
    structure=SMILES("CCCCCC=CCC(C)OO")
)


species(
    label='QeneOOH_7',
    reactive=True,
    structure=SMILES("CC=CCCCC(CCC)OO")
)


species(
    label='QeneOOH_8',
    reactive=True,
    structure=SMILES("C=CCC(CCCCCC)OO")
)


species(
    label='QeneOOH_9',
    reactive=True,
    structure=SMILES("CCC=CCCC(CCC)OO")
)


species(
    label='QeneOOH_10',
    reactive=True,
    structure=SMILES("CC=CC(CCCCCC)OO")
)


species(
    label='QeneOOH_11',
    reactive=True,
    structure=SMILES("CCCC=CCC(CCC)OO")
)


species(
    label='QeneOOH_12',
    reactive=True,
    structure=SMILES("CCCCC=CCCCCOO")
)


species(
    label='QeneOOH_13',
    reactive=True,
    structure=SMILES("CCCCCC=CCCCOO")
)


species(
    label='QeneOOH_14',
    reactive=True,
    structure=SMILES("CCCCCCC=CCCOO")
)


species(
    label='QeneOOH_15',
    reactive=True,
    structure=SMILES("CCCCCCCC=CCOO")
)


species(
    label='QeneOOH_16',
    reactive=True,
    structure=SMILES("CCCCCCCCC=COO")
)


species(
    label='QeneOOH_17',
    reactive=True,
    structure=SMILES("CCCC=CCCCC(C)OO")
)


species(
    label='QeneOOH_18',
    reactive=True,
    structure=SMILES("CCCC=CC(CCCC)OO")
)


species(
    label='QeneOOH_19',
    reactive=True,
    structure=SMILES("CCC=CC(CCCCC)OO")
)


species(
    label='QeneOOH_20',
    reactive=True,
    structure=SMILES("CCCCC=CCCC(C)OO")
)


species(
    label='QeneOOH_21',
    reactive=True,
    structure=SMILES("CCCCCC=C(CCC)OO")
)


species(
    label='QeneOOH_22',
    reactive=True,
    structure=SMILES("CCC=C(CCCCCC)OO")
)


species(
    label='QeneOOH_23',
    reactive=True,
    structure=SMILES("CCCCC=CC(CCC)OO")
)


species(
    label='QeneOOH_24',
    reactive=True,
    structure=SMILES("CCCCCCC=C(CC)OO")
)


species(
    label='QeneOOH_25',
    reactive=True,
    structure=SMILES("CC=C(CCCCCCC)OO")
)


species(
    label='QeneOOH_26',
    reactive=True,
    structure=SMILES("CCCCCC=CC(CC)OO")
)


species(
    label='QeneOOH_27',
    reactive=True,
    structure=SMILES("C=CC(CCCCCCC)OO")
)


species(
    label='QeneOOH_28',
    reactive=True,
    structure=SMILES("CCCCC=CCC(CC)OO")
)


species(
    label='QeneOOH_29',
    reactive=True,
    structure=SMILES("CCCC=CCCC(CC)OO")
)


species(
    label='QeneOOH_30',
    reactive=True,
    structure=SMILES("CCC=CCCCC(CC)OO")
)


species(
    label='QeneOOH_31',
    reactive=True,
    structure=SMILES("CC=CCCCCC(CC)OO")
)


species(
    label='QeneOOH_32',
    reactive=True,
    structure=SMILES("CCCCC=C(CCCC)OO")
)


species(
    label='QeneOOH_33',
    reactive=True,
    structure=SMILES("CCCC=C(CCCCC)OO")
)


species(
    label='QeneOOH_34',
    reactive=True,
    structure=SMILES("CCC=CCCCCC(C)OO")
)


species(
    label='QeneOOH_35',
    reactive=True,
    structure=SMILES("CC=CCCC(CCCC)OO")
)


species(
    label='QeneOOH_36',
    reactive=True,
    structure=SMILES("C=CCCCC(CCCC)OO")
)


species(
    label='QeneOOH_37',
    reactive=True,
    structure=SMILES("C=CCCC(CCCCC)OO")
)


species(
    label='QeneOOH_38',
    reactive=True,
    structure=SMILES("CCCCCCCC=C(C)OO")
)


species(
    label='QeneOOH_39',
    reactive=True,
    structure=SMILES("C=C(CCCCCCCC)OO")
)

##############################
# ROOH

species(
    label='ROOH_1',
    reactive=True,
    structure=SMILES("CCCCCCC(CCC)OO")
)


species(
    label='ROOH_2',
    reactive=True,
    structure=SMILES("CCCCCCCCCCOO")
)


species(
    label='ROOH_3',
    reactive=True,
    structure=SMILES("CCCCCCCC(CC)OO")
)


species(
    label='ROOH_4',
    reactive=True,
    structure=SMILES("CCCCCC(CCCC)OO")
)


species(
    label='ROOH_5',
    reactive=True,
    structure=SMILES("CCCCCCCCC(C)OO")
)

##############################
# RO

species(
    label='RO_1',
    reactive=True,
    structure=SMILES("CCCCCCC([O])CCC")
)


species(
    label='RO_2',
    reactive=True,
    structure=SMILES("CCCCCCCCC(C)[O]")
)


species(
    label='RO_3',
    reactive=True,
    structure=SMILES("CCCCCCCCCC[O]")
)


species(
    label='RO_4',
    reactive=True,
    structure=SMILES("CCCCCCCC([O])CC")
)


species(
    label='RO_5',
    reactive=True,
    structure=SMILES("CCCCCC([O])CCCC")
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
    atol=1e-20,
    rtol=1e-12,
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
    name='Zil_nc10_low',
    saveRestartPeriod=None,
    generateOutputHTML=True,
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
    maximumCarbonAtoms=12,
    maximumOxygenAtoms=4,
    maximumRadicalElectrons=2,
    allowSingletO2 = True,
)

