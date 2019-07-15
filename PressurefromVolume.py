class VolumeFromPressure(object):
    r"""Create a volume trace given a pressure trace.
    Using Cantera to evaluate the thermodynamic properties, compute a
    volume trace from a pressure trace.
    Parameters
    ----------
    pressure : `numpy.ndarray`
        1-D array containing the reactor pressure
    v_initial : `float`
        Initial volume of the experiment, in m**3
    T_initial : `float`, optional
        Initial temperature of the experiment, in Kelvin. Optional for
        Cantera versions greater than 2.2.0.
    chem_file : `str`, optional
        Filename of the chemistry file to be used
    Attributes
    ----------
    volume : `numpy.ndarray`
        The volume trace
    Notes
    -----
    The volume is computed according to the formula
    .. math:: v_i = v_{initial}*\rho_{initial}/\rho_i
    where the index :math:`i` indicates the current point. The state
    is set at each point by setting the pressure from the input array
    and the entropy to be constant. The volume is computed by the
    isentropic relationship described above.
    """
    def __init__(self, pressure, v_initial, T_initial, chem_file='species.cti', cti_source=None):
        if cti_source is None:
            gas = ct.Solution(chem_file)
        else:
            gas = ct.Solution(source=cti_source)
        gas.TP = T_initial, pressure[0]*one_bar_in_pa
        initial_entropy = gas.entropy_mass
        initial_density = gas.density
        self.volume = np.zeros((len(pressure)))
        for i, p in enumerate(pressure):
            gas.SP = initial_entropy, p*one_bar_in_pa
            self.volume[i] = v_initial*initial_density/gas.density

    def __repr__(self):
        return 'VolumeFromPressure(volume={self.volume!r})'.format(self=self)