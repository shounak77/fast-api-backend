import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from main import app
from database import get_db, DbBase
from models.tariff import TariffORM



SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
DbBase.metadata.create_all(bind=engine)

@pytest.fixture(scope="module")
def db():
    """Fixture to provide a test database connection"""
    DbBase.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        DbBase.metadata.drop_all(bind=engine)


@pytest.fixture(scope="module")
def client(db):
    """Fixture to provide a test client with overridden DB"""
    def override_get_db():
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


@pytest.fixture(scope="module")
def test_tariff(db):
    """Fixture to create a sample tariff for testing in the database"""
    test_tariff_1 = TariffORM(
        name="TestTariff",
        description="Descreption",
        rate=0.08,
        currency="USD",
        tax_rate=0.05,
        code="63JK9"
    )

    db.add(test_tariff_1)
    db.commit()
    db.refresh(test_tariff_1) # id availabe after refresh
    yield test_tariff_1
    db.delete(test_tariff_1)  # Clean up after tests
    db.commit()
