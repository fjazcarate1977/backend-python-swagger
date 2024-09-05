import yaml
from yamlinclude import YamlIncludeConstructor
import connexion
from flask_cors import CORS

YamlIncludeConstructor.add_to_loader_class(
    loader_class=yaml.FullLoader, base_dir='./')

with open('swagger.yaml') as f:
    apiData = yaml.load(f, Loader=yaml.FullLoader)


app = connexion.App(__name__, specification_dir="./")
app.add_api(apiData)
CORS(app.app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
