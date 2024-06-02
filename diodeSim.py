''' This project simulates the I-V characteristics of a diode '''

import numpy as np
import matplotlib.pyplot as plt

# Calculate the current through a diode using the Shockley diode equation.
def diode_current(voltage, saturation_current, thermal_voltage, ideality_factor):
    return saturation_current * (np.exp(voltage / (ideality_factor * thermal_voltage)) - 1)

# Plot the I-V curve for the diode.
def plot_iv_curve(voltage, current):
    plt.figure(figsize=(8, 6))
    plt.plot(voltage, current, label='Diode I-V Curve')
    plt.title('I-V Characteristics of a Semiconductor Diode')
    plt.xlabel('Voltage (V)')
    plt.ylabel('Current (A)')
    plt.yscale('log')  # Use logarithmic scale for current
    plt.grid(True, which='both', ls='--')
    plt.legend()
    plt.show()

# Main function to simulate the I-V characteristics of a semiconductor diode.
def main():
    # Constants
    k = 1.380649e-23  # Boltzmann constant (J/K)
    q = 1.602176634e-19  # Elementary charge (C)
    T = 300  # Temperature in Kelvin (K)
    
    # Calculate thermal voltage
    thermal_voltage = k * T / q  # Thermal voltage (V_T)
    
    # Diode parameters
    saturation_current = 1e-12  # Saturation current (I_s) in Amperes (A)
    ideality_factor = 1.0  # Ideality factor (n)
    
    # Voltage range for the I-V curve
    voltage = np.linspace(-0.5, 0.7, 400)  # Voltage values from -0.5V to 0.7V
    
    # Calculate the current through the diode for each voltage value
    current = diode_current(voltage, saturation_current, thermal_voltage, ideality_factor)
    
    # Plot the I-V curve
    plot_iv_curve(voltage, current)
    
if __name__ == "__main__":
    main()
