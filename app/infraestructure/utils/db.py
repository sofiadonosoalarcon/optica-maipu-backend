from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mssql+pyodbc://adminbd:Admin2025@proyectobd.database.windows.net/optica-maipu?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(DATABASE_URL, echo=True, fast_executemany=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
