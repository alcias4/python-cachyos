from rich.progress import Progress
import time
with Progress() as progress:
    
    task1 = progress.add_task("[cyan]Cargando...", total=10000)

    # while not progress.finished:
    #     progress.update(task1, advance=1)

    for i in range(1,10001):
        progress.update(task1, advance=1)
        print(f"Numeor actual {i}")
        