from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from jinja2 import Template

class Workshop:
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        self.components = []

    def text(self, content: str):
        self.components.append(f'<p>{content}</p>')

    def render(self):
        template = Template("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{{ title }}</title>
            <script defer src="https://unpkg.com/react@18/umd/react.development.js"></script>
            <script defer src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
            <script defer src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
        </head>
        <body>
            <div id="root">{{ content | safe }}</div>
        </body>
        </html>
        """)
        return template.render(title=self.title, content="".join(self.components))

app = FastAPI()
fw = Workshop("AI Workshop", "Eine interaktive Plattform zur KI-gestützten Zusammenarbeit")
fw.text("Willkommen zum AI-Workshop!")

@app.get("/", response_class=HTMLResponse)
def home():
    return fw.render()