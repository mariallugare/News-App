# from flask import Flask 
# from config import config_options
# from flask_bootstrap import Bootstrap

# bootstrap = Bootstrap()

# def create_app(config_name):
  
#    # Initializing the application
#    app = Flask(__name__,instance_relative_config = True)

#    # Setting up app configuration
#    app.config.from_object(config_options[config_name])

#    # Initializing Flask Bootstrap Extension
#    bootstrap.init_app(app)

#    # Registering the blueprint
#    from .main import main as main_blueprint
#    app.register_blueprint(main_blueprint)
  
#    # Setting app configuration
#    from .api_requests import configure_api_requests
#    configure_api_requests(app)
  
#    return app


























from flask import Flask
from config import config_options


def create_app(config_name):
    
    app = Flask(__name__)
    
     
    app.config.from_object(config_options[config_name])
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    
    from .requests import configure_request
    configure_request(app)
    
    return app