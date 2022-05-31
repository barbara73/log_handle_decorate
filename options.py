from dataclasses import dataclass, field


@dataclass
class Options:
    log_level: str = field(default='ERROR')
