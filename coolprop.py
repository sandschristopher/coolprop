import CoolProp.CoolProp as CP

fluid = "Helium"
temperature = 90.25
pressure = 344738

'''

Props(OutputName, InputName1, InputProp1, InputName2, InputProp2, Fluid) 

'''

print("\n")

density = CP.PropsSI('D', 'T', temperature, 'P', pressure, fluid)

print("Density of " + fluid + " at " + str(temperature) + " K and " + str(pressure) + " Pa: " 
      + str(density) + " kg/m^3")

dynamic_viscosity = CP.PropsSI('V', 'T', temperature, 'P', pressure, fluid)

print("Dynamic viscosity of " + fluid + " at " + str(temperature) + " K and " + str(pressure) + " Pa: " 
      + str(dynamic_viscosity) + " Pa-s")

kinematic_viscosity = dynamic_viscosity/density

print("Kinematic viscosity of " + fluid + " at " + str(temperature) + " K and " + str(pressure) + " Pa: " 
      + str(kinematic_viscosity) + " m^2/s")

thermal_conductivity =  CP.PropsSI('L', 'T', temperature, 'P', pressure, fluid)

print("Thermal conductivity of " + fluid + " at " + str(temperature) + " K and " + str(pressure) + " Pa: " 
      + str(thermal_conductivity) + " W/m-K")

saturation_pressure = CP.PropsSI('P', 'T', temperature, 'Q', 1, fluid)

print("Saturation pressure of " + fluid + " at " + str(temperature) + " K: "
      + str(saturation_pressure) + " Pa")

specific_heat = CP.PropsSI('C', 'T', temperature, 'P', pressure, fluid)

print("Specific heat of " + fluid + " at " + str(temperature) + " K and " + str(pressure) + " Pa: " 
      + str(specific_heat) + " kJ/kg")

print("\n")

