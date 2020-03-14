from cx_Freeze import setup, Executable

# On appelle la fonction setup

assets = dict(include_files = ["assets/", "conf.dat"]) #folder,relative path. Use tuple like in the single file to set a absolute path.


setup(
    name = "Ball Runner",
    version = "0.1",
    description = "Ball Jumping Game",
    options = dict(build_exe = assets),
    executables = [Executable(script="Ball Runner.py", icon="icon.ico")],
)