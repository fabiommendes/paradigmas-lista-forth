import subprocess
from pathlib import Path
from typing import Sequence
from pytest import fixture
import rich 
import shlex
import re
import os 

ANSWER_KEY = os.environ.get("ANSWER_KEY", "auto").lower()
STACK_RE  = re.compile(r"<\d+> (.*)$", re.MULTILINE)
CMD = ["gforth", "FILE", "-e", "bye"]
CMD = ["flatpak", "run", "--filesystem=host","org.gforth.gforth", "FILE", "-e", "bye"]

BASE_PATH = Path(__file__).parent.parent 

class Run:
    def __init__(self, file: str, program: Sequence[str] = (), stdin: str | None=None):
        cmd = [*CMD]
        cmd[CMD.index("FILE")] = get_file_path_argument(file)
        cmd[-1] = " ".join([*program, "bye"])

        self.result = subprocess.run(cmd, capture_output=True, text=True, input=stdin)
        try:
            self.result.check_returncode()
        except subprocess.CalledProcessError as e:
            shell_cmd = shlex.join(cmd[:-1] + ["..."])
            rich.print(f"[b green]$[/] [yellow]{shell_cmd}[/]")
            
            rich.print(f"\nComandos extras:")
            for cmd in [*program, "bye"]:
                rich.print(f"  [cyan]{cmd}[/]")

            rich.print(f"\n[red]Erro no arquivo {file}:[/]")
            for line in self.result.stdout.strip("\n").splitlines():
                rich.print(f"  [bold]{line}[/]")
            for line in self.result.stderr.strip("\n").splitlines():
                rich.print(f"  [red]{line}[/]")

            raise RuntimeError(f"Erro rodando arquivo Forth {file}: {e}")
        
        self.stdout = self.result.stdout

    @property
    def output(self):
        return self.stdout.strip()
    
    @property
    def lines(self):
        return [line.rstrip() for line in self.output.splitlines()]

    @property
    def stack(self):
        match = STACK_RE.search(self.stdout)
        if not match:
            print("Saída inválida:")
            print(indent(self.stdout))
            raise ValueError("esperava encontrar uma representação da pilha")
        
        return [int(x) for x in match.group(1).split()] 

    def __repr__(self):
        return f"Run(stdout={self.stdout!r})"


@fixture
def io():
    """
    Fixture to interact with the Forth files.
    """
    return Run



def indent(text: str, spaces: int = 2) -> str:
    """Indent each line of the given text by a specified number of spaces."""
    indentation = ' ' * spaces
    return '\n'.join(f"{indentation}{line}" for line in text.splitlines()   )


def get_file_path_argument(file: str) -> str:
    """
    Get the file path argument for the Forth command.
    """
    
    answer_key = BASE_PATH / file.replace(".fs", ".answer.fs")
    path = BASE_PATH / file
    
    if ANSWER_KEY == "auto" and answer_key.exists() or ANSWER_KEY in ["1", "true"]:
        path = answer_key

    if not path.exists():
        raise FileNotFoundError(f"Arquivo {file} não encontrado em {BASE_PATH}")    

    return str(path.relative_to(Path.cwd()))