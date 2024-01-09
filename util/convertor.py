from datafactory.GasData import GasData
from db.GasEntity import GasEntity


def dto_to_entity(dto: GasData) -> GasEntity:
    return GasEntity(type=dto.type, pressure=dto.pressure,
                     differential = dto.differential, date=dto.timestamp)


def entity_to_dto(entity: GasEntity) -> GasData:
    return GasData(type=entity.type, pressure=entity.pressure,
                     differential=entity.differential, timestamp=entity.date)
