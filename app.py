import connexion

app = connexion.App(__name__, specification_dir='.')
app.add_api("openapi.yaml")

def welcome_page():
    return {"message": "Welcome!"}

# def hello():
#     return {"message": "Hello!"}

if __name__ == "__main__":
    app.run(port=8040)