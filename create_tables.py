from app.database import Base, engine
from app.models import User

# Create all tables defined in the models
print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully.")
