import cantera as ct

temp = 300
p = ct.one_atm
phi = 1.0

gas = ct.Solution('gri30.cti')
gas.TP = temp, p
gas.set_equivalence_ratio(phi, 'CH4', 'O2:1.0, N2:3.76')
gas.equilibrate('HP')
t1 = gas.T
print(gas.report())

print('------------------------------------------------------')

species = {S.name: S for S in ct.Species.listFromFile('gri30.cti')}
complete_species = [species[S] for S in ('CH4','O2','N2','CO2','H2O')]
gas2 = ct.Solution(thermo='IdealGas', species=complete_species)
gas2.TP = temp, p
gas2.set_equivalence_ratio(phi, 'CH4', 'O2:1.0, N2:3.76')
gas2.equilibrate('HP')
t2 = gas2.T
print(gas2.report())

print('phi={:10.4f}, Tbe={:12.4f}, Tbt={:12.4f}'.format(phi, t1, t2) )