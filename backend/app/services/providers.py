from abc import ABC, abstractmethod
import shutil
from dataclasses import dataclass

@dataclass
class CapabilityStatus:
    provider: str
    configured: bool
    available: bool
    detail: str

class ProcessingProvider(ABC):
    @abstractmethod
    def status(self) -> CapabilityStatus:
        raise NotImplementedError

class LocalProcessingProvider(ProcessingProvider):
    def status(self) -> CapabilityStatus:
        ffmpeg = shutil.which("ffmpeg")
        return CapabilityStatus("local", True, ffmpeg is not None,
            f"FFmpeg found at {ffmpeg}" if ffmpeg else "FFmpeg is not installed or not on PATH.")

class CloudProcessingProvider(ProcessingProvider):
    def status(self) -> CapabilityStatus:
        return CapabilityStatus("cloud", False, False,
            "No cloud provider configured. Media will not be uploaded automatically.")
