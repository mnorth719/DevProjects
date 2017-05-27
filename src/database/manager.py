# Database management.
# Responsible for:
#   1. Making sure DB exists and is running
#   2. Safe wrapper around lower level DB calls.
#   3. Simple interactions


from sqlalchemy import create_engine

db_engine = create_engine('sqlite:///:memory:')