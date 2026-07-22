from pathlib import Path
from tarfile import open as open_tar
from zipfile import ZipFile

forbidden_reference = b"po" + b"lar"


def verify_file(path: str, content: bytes) -> None:
    if forbidden_reference in path.lower().encode() or forbidden_reference in content.lower():
        raise RuntimeError(f"Forbidden public reference in {path}")


artifacts = [*Path("dist").glob("*.whl"), *Path("dist").glob("*.tar.gz")]

for artifact in artifacts:
    if artifact.name.endswith(".whl"):
        with ZipFile(artifact) as archive:
            for member in archive.infolist():
                verify_file(member.filename, archive.read(member))
        continue

    with open_tar(artifact, "r:gz") as archive:
        for member in archive.getmembers():
            if member.isfile():
                extracted_file = archive.extractfile(member)
                if extracted_file is not None:
                    verify_file(member.name, extracted_file.read())

print("Verified Python release artifacts")
