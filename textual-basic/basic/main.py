from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Label


class MyApp(App):

    def compose(self) -> ComposeResult:
        # añadir widgets como el cambezado , footer y una label.
        yield Header()
        yield Label("!Hola desde Textual!", id="mensaje")
        yield Footer()



if __name__ == "__main__":
    app = MyApp()
    app.run()