from eve import Eve
from eve_sqlalchemy import SQL
from eve_sqlalchemy.validation import ValidatorSQL

from registries.structure import Base
from settings import SETTINGS

if __name__ == "__main__":
    application = Eve(auth=0, validator=ValidatorSQL, data=SQL, settings=SETTINGS)

    db = application.data.driver
    Base.metadata.bind = db.engine
    db.Model = Base
    db.create_all()
    application.run(debug=True, port=5001)