# from rollbar.contrib.fastapi import add_to as rollbar_add_to
from fastapi import FastAPI
from router.sv_routes import router


# from utils.config_handler import get_config_section
# from utils.rollbar_integration import init_rollbar


def get_app() -> FastAPI:
    # Initializing logging and application monitoring tools like rollbar, logger, signoz and consul configuration

    # rollbar_config = get_config_section("snm_api/rollbar")
    # snm_config = get_config_section("snm_api/snm")

    # Initialised API version

    # version = "v{}".format(snm_config.get('version'))
    version = "v1"

    fast_app = FastAPI(
        title="Sentence Vectorizer Service (SVS-API)",
        description="SVS API returns vectors/numerical representation of text sentences.",
        externalDocs={
            "name": "share point page",
            "URL": "https://xyz.doc.in"},
        version=version)

    # Initialised Logger
    # init_rollbar(rollbar_config)
    # rollbar_add_to(fast_app)

    # Including Prefix and API Version
    fast_app.include_router(router, prefix='/nlp/{}'.format(version))
    return fast_app


app = get_app()
