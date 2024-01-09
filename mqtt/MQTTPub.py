import paho.mqtt.client as mqtt



def _on_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Server Connect')
    else:
        print('Server Connect Fail \n Code : ' + str(rc))


def _on_disconnect(client, userdata, rc):
    print('Server Disconnect \n Code : ' + str(rc))


def _on_publish(client, userdata, mid):
    print(f'Publish Message Id: {mid}, Data: {str(userdata)}')


class MqttPublisher:
    def __init__(self, conf):

        self._topic_prefix = conf.topicPrefix

        self._client = mqtt.Client(conf.publisherName)

        self._client.on_connect = _on_connect
        self._client.on_disconnect = _on_disconnect
        self._client.on_publish = _on_publish

        self._client.connect(conf.host, conf.port, keepalive=121)
        self._client.loop_start()

    def publish(self, data_list:list):
        for data in data_list:
            self._client.publish(f'{self._topic_prefix}/{data.type}', str(data))

    def loop_stop(self):
        self._client.loop_stop()

    def server_disconnect(self):
        self._client.disconnect()
