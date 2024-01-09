from db.DBConnector import DBConnector
from mqtt.MQTTPub import MqttPublisher


class DataDeployer:
    def __init__(self, conf):
        if conf.database.enable:
            self.database = DBConnector(conf.database)

        if conf.mqtt.enable:
            self.mqtt = MqttPublisher(conf.mqtt)
            self.mqtt.loop_stop()

    def deploy(self, data_list: list):
        try:
            self.database.insert_data(data_list)
        except:
            pass

        try:
            self.mqtt.publish(data_list)
        except:
            pass