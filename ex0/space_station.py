from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)

    print("Valid station created:")
    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2024-01-15T10:00:00",  #type: ignore[arg-type]
    )
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    status = "Operational" if station.is_operational else "Offline"
    print(f"Status: {status}")

    print()
    print("=" * 40)
    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="ISS002",
            name="Faulty Station",
            crew_size=25,
            power_level=50.0,
            oxygen_level=50.0,
            last_maintenance="2024-01-15T10:00:00",  #type: ignore[arg-type]
        )
    except ValidationError as error:
        print(error.errors()[0]["msg"])


if __name__ == "__main__":
    main()
