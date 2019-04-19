from cx_Freeze import setup, Executable

setup(
    name = "Sberbank",
    version = "0.1",
    description = "sberbank_key_updater",
    executables = [Executable("sberbank.py")]
)
