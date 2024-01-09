from datafactory.GasGenerator import GasGenerator


class DataMaker:
    def __init__(self, gas_list: list):
        self.generator_list = [GasGenerator(gas_type) for gas_type in gas_list]

    def make_gas_data(self):
        return [generator.generate_data() for generator in self.generator_list]
