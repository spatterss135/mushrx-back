from flask import Flask
from flask import jsonify
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin
def create_app():
    app = Flask(__name__)
    CORS(app)


    # config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Strawhat987@localhost:5432/mushrx'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route('/')
    def hello():
        data_array = []
        data = models.Point.query.all()
        for dp in data:
            data_array.append({'latitude': dp.latitude, 'longitude': dp.longitude, 'found_on': dp.found_on})
        return jsonify(data_array)


    from . import user
    app.register_blueprint(user.bp)

    from . import userpoint
    app.register_blueprint(userpoint.bp)
    # Initial Mushroom data
    # from . import data
    # app.register_blueprint(data.bp)
    
    # from . import soildata
    # from moreldata.soilstuff import facts
    # @app.route('/soil')
    # def index():
    #     return jsonify(soildata.getHelp(facts['hours']))
    return app