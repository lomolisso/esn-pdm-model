import matplotlib.pyplot as plt


gateway_accuracy_arr = [98.58857762336731, 98.81036650657654, 98.711792345047, 98.68715178489686, 98.95822178840638, 98.711792345047, 97.52894412994385, 98.12037121772767, 96.59252535820008, 89.91435539245606, 85.87295782089234, 70.59449326515198, 50.16571056365967, 31.41263198375702]
gateway_final_sparcity_arr = [30.0, 35.0, 40.0, 45.0, 50.0, 55.00000000000001, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0]

sensor_accuracy_arr = [97.06073176383973, 97.82465469360352, 96.37073647499085, 92.94540655136109, 92.3786259841919, 79.04693257331849, 81.2401331615448, 63.94096982002259, 62.58562576293946, 47.03609120368958, 49.50035881519318, 40.998635406494145, 20.052356238365174, 24.414110894203187]
sensor_final_sparcity_arr = [30.0, 35.0, 40.0, 45.0, 50.0, 55.00000000000001, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0]

# Plot the accuracy vs sparcity for the gateway and sensor model
plt.plot(gateway_final_sparcity_arr, gateway_accuracy_arr, label='Gateway Model', marker='o', markersize=5, zorder=5)
plt.plot(sensor_final_sparcity_arr, sensor_accuracy_arr, label='Sensor Model', marker='o', markersize=5, zorder=4)

# Add labels for the axes and the title
plt.xlabel('Model Sparcity (%)')
plt.ylabel('Model Accuracy (%)')

# Vertical lines at x=0.45 and x=0.65
plt.axvline(x=50, color='tab:orange', linestyle='--', alpha=0.5, zorder=3)
plt.axvline(x=65, color='tab:blue', linestyle='--', alpha=0.5, zorder=4)

# Show grid for better readability
plt.grid(axis="y")

# ticks

# Display legend
plt.legend()

# Show plot
plt.show()