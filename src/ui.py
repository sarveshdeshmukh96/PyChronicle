from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Header, Footer, Button, Static

from controller import PyChronicleController


class PyChronicleUI(App):
    """PyChronicle Graphical User Interface"""

    CSS_PATH = "ui.tcss"

    TITLE = "PyChronicle"
    SUB_TITLE = "AST Powered Time-Travel Debugger"

    def __init__(self):
        super().__init__()
        self.controller = PyChronicleController()

    def compose(self) -> ComposeResult:
        yield Header()

        with Vertical():

            yield Static(
                "🚀 PyChronicle",
                id="title"
            )

            yield Static(
                "AST Powered Time-Travel Debugger",
                id="subtitle"
            )

            yield Button(
                "📂 Load Sample File",
                id="load"
            )

            yield Button(
                "🌳 Parse AST",
                id="ast"
            )

            yield Button(
                "📄 Export JSON Report",
                id="json"
            )

            yield Button(
                "▶ Run Execution Tracer",
                id="trace"
            )

            yield Button(
                "🗄 View Execution History",
                id="history"
            )

            yield Button(
                "❌ Exit",
                id="exit"
            )

            yield Static(
                "Status : Ready",
                id="status"
            )

        yield Footer()

    def update_status(self, message: str):
        self.query_one("#status", Static).update(
            f"Status : {message}"
        )

    async def on_button_pressed(self, event: Button.Pressed):

        button = event.button.id

        try:

            if button == "load":

                self.controller.load_file(
                    "sample_programs/sample.py"
                )

                self.update_status(
                    "Sample file loaded successfully."
                )

            elif button == "ast":

                self.controller.parse_ast()

                self.update_status(
                    "AST parsed successfully."
                )

            elif button == "json":

                self.controller.export_report()

                self.update_status(
                    "JSON report exported successfully."
                )

            elif button == "trace":

                self.controller.run_tracer()

                self.update_status(
                    "Execution tracing completed."
                )

            elif button == "history":

                sessions = self.controller.get_history()

                self.update_status(
                    f"{len(sessions)} execution session(s) found."
                )

            elif button == "exit":

                self.exit()

        except Exception as e:

            self.update_status(
                f"Error: {e}"
            )


if __name__ == "__main__":
    PyChronicleUI().run()