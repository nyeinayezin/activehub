from flask import Flask
from app.web import web


app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

app.register_blueprint(web)


if __name__ == "__main__":
    app.run(debug=True)