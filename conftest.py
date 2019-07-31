import pytest
from flask import Flask

@pytest.fixture(scope='module')
def app() -> Flask:
    from app import Handler
    handler = Handler()
    handler.app.add_url_rule('/forecast', 'forecast', handler.forecast,
                             methods=['post'])
     
    return handler.app
