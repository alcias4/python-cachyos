from textual.app import App
from textual.widgets import Footer, Header,Button

class Stop(App):
    BINDINGS = [
        ("d","toogle_dark_mode","Toggle dark mode"),
    ]


    def compose(self):
        """What widgets is this app compsed of"""
        
        yield Header(show_clock=True)
        yield Footer()
        yield Button("Start")
        yield Button("Stop")
    
    # This is an ACTION method.
    # It's an action method because it start with action_
    # It's associated with the action called toggle_dark_mode
    def action_toogle_dark_mode(self):
        self.dark = not self.dark

if __name__ == "__main__":
    Stop().run()
