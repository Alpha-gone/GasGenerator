import json

import time
from easydict import EasyDict
from DataDeployer import DataDeployer
from datafactory.DataMaker import DataMaker


def deploy(conf):
    data_maker = DataMaker(conf.gasList)
    deployer = DataDeployer(conf)

    while True:
        deployer.deploy(data_maker.make_gas_data())

        time.sleep(conf.generateInterval)


if __name__ == "__main__":
    conf = EasyDict(json.load(open('config/conf.json')))

    deploy(conf)

