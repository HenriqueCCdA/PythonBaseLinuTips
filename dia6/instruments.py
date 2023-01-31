from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum


class InstrumentKind(str, Enum):
    string = "string"
    wind = "wind"
    keys = "keys"
    drums = "drums"


class DisortionKind(str, Enum):
    wave = "wave"
    whisper = "whisper"


class ABCInstrument(ABC):

    @abstractmethod
    def play(self):
        ...


@dataclass
class DataInstrumentMixin:
    name: str
    sound: str
    kind: InstrumentKind
    colors: list[str] = field(default_factory=list)


class Instrument(DataInstrumentMixin, ABCInstrument):
    ...


@dataclass
class Guitar(Instrument):
    n_string: int = 6
    sound: str = "Ding Ding Ding"
    kind: InstrumentKind = InstrumentKind.string
    colors: list[str] = field(default_factory=lambda: ["red", "black"])

    def play(self):
        return self.sound


@dataclass
class Flute(Instrument):

    sound: str = "Flu Flu Flu"
    kind: InstrumentKind = InstrumentKind.wind
    colors: list[str] = field(default_factory=lambda: ["beige", "white"])

    def play(self):
        return self.sound

@dataclass
class EletricGuitar(Guitar):
    sound: str = "Wah Wah Wah"

    def play(self, distorcion: DisortionKind=DisortionKind.wave):
        return_from_base_class = super().play()
        if distorcion is DisortionKind.wave:
            return "~~~".join(return_from_base_class.split())
        if distorcion is DisortionKind.whisper:
            return "...".join(return_from_base_class.split())
        return  return_from_base_class
