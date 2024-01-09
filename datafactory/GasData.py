from datetime import datetime


class GasData():
    def __init__(self, type: str, pressure: float, differential: float, timestamp: datetime ):
        self.type = type
        self.pressure = pressure
        self.differential = differential
        self.timestamp = timestamp

    def __dict__(self):
        return {'type': self.type, 'pressure': self.pressure,
                'differential': self.differential, 'timestamp': self.timestamp}

    def __str__(self):
        result = self.__dict__()
        result['timestamp'] = self.timestamp.strftime('%Y-%m-%d %H:%M:%S')

        return str(result)