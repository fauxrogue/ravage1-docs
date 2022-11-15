from pathlib import Path
from subprocess import call

dest = Path().home().resolve().joinpath('Desktop', 'ravage1_docs')

# Build documentation.
call(['mkdocs', 'build', '-d', str(dest)])
