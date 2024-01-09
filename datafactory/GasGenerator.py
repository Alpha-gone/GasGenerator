from datetime import datetime, timezone, timedelta

from datafactory.GasData import GasData

import random

# import matplotlib.pyplot as plt


class GasGenerator:
    def __init__(self, gas_type):
        self._differential = round(random.uniform(2000, 5000), 2)
        self._pressure = round(random.uniform(5, 15), 2)

        self._last_normal_differential = self._differential
        self._last_normal_pressure = self._pressure

        self._anomaly_occurred = False

        self._gas_type = gas_type

        # value of graph
        # self.timestamps = []
        # self.differential_values = []
        # self.pressure_values = []

    def generate_data(self) -> GasData:
        now = datetime.now(timezone(offset=timedelta(hours=9)))

        if self._anomaly_occurred:
            self._differential = self._last_normal_differential
            self._pressure = self._last_normal_pressure
            self._anomaly_occurred = False

        # graph value append
        # self.timestamps.append(now)
        # self.differential_values.append(self._differential)
        # self.pressure_values.append(self._pressure)

        if random.random() < 0.02 and not self._anomaly_occurred:
            self._differential += round(random.uniform(50, 100), 2)
            self._pressure += round(random.uniform(0.01, 1.2), 2)
            self._anomaly_occurred = True
        else:
            self._last_normal_differential = self._differential
            self._last_normal_pressure = self._pressure

            if random.random() < 0.5:
                self._differential += round(random.uniform(5, 15), 2)
                self._pressure += round(random.uniform(0.01, 0.3), 2)
            else:
                self._differential -= round(random.uniform(5, 15), 2)
                self._pressure -= round(random.uniform(0.01, 0.3), 2)

        differential = round(max(2000, min(5000, self._differential)), 2)
        pressure = round(max(5, min(15, self._pressure)), 2)

        return GasData(self._gas_type, pressure, differential, now)

    # see generate value graph
    # def show_img(self):
    #     plt.figure(figsize=(10, 6))
    #     plt.plot(self.timestamps, self.differential_values, label='Gas Pressure', linestyle='-', marker='o')
    #     plt.plot(self.timestamps, self.pressure_values, label='Pressure', linestyle='-', marker='o')
    #     plt.xlabel('Timestamp')
    #     plt.ylabel('Value')
    #     plt.title('Gas Pressure and Pressure Over Time')
    #     plt.legend()
    #     plt.grid(True)
    #
    #     plt.show()
