class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 LEN_STEP: float,
                 M_IN_KM: float
                 ) -> None:
        self.LEN_STEP = 0.65
        self.M_IN_KM = 1000
        self.action = 42
    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

print(Training)