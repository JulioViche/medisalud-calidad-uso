from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True)
class Classification:
    characteristic: str
    justification: str
    matched_rule: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


@dataclass(frozen=True)
class Metric:
    code: str
    name: str
    characteristic: str
    value: float
    unit: str
    target: str
    status: str
    source: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

