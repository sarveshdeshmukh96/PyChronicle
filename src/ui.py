from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Header, Footer, Button, Static


class PyChronicleUI(App):
    """Main Textual UI for PyChronicle."""
     
    CSS_PATH = "ui.tcss"

    TITLE = "🚀 PyChronicle"
    SUB_TITLE = "Python Code Analysis Tool"

    def compose(self) -> ComposeResult:
        """Create the UI layout."""

        yield Header()

        with Vertical():

            yield Static(
                "\n🚀 Welcome to PyChronicle\n",
                id="title"
            )

            yield Button("📂 Load Python File", id="load")

            yield Button("🌳 Parse AST", id="ast")

            yield Button("▶ Run Tracer", id="trace")

            yield Button("🗄 Execution History", id="history")

            yield Button("❌ Exit", id="exit")

            yield Static(
                "\nStatus : Ready",
                id="status"
            )

        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button clicks."""

        button_id = event.button.id

        if button_id == "load":
            self.notify("Load Python File clicked!")

        elif button_id == "ast":
            self.notify("AST Parser coming soon!")

        elif button_id == "trace":
            self.notify("Tracer coming soon!")

        elif button_id == "history":
            self.notify("History coming soon!")

        elif button_id == "exit":
            self.exit()


if __name__ == "__main__":
    PyChronicleUI().run()