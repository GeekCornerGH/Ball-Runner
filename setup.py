from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "Ball Runner",
    version = "0.1",
    description = "Ball Jumping Game",
    executables = [Executable(script="Ball Runner.py", icon="icon.ico")],
)