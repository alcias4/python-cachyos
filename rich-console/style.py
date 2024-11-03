from rich.console import Console

console = Console()

# texto simple 

console.print("hola mundo!")

# texto de color 

console.print("hola, [bold magenta]mundo![/bold magenta]", style="bold green")

# texto subrayado

console.print("Esto es un texto [underline red]subrayado[/underline red]")