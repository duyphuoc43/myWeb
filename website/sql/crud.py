from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from . import models
from .. import schemas


def create_statistics(db: Session, request: schemas.Statistics):
    try:
        db_statistic = models.Statistics(
            date=datetime.now(), flow=request.flow, pressure=request.pressure)
        db.add(db_statistic)
        db.commit()
        db.refresh(db_statistic)
        return db_statistic
    except IntegrityError:
        db.rollback()


def get_statistics(db: Session, request: schemas.Statistics):
    if request is None:
        db.query(models.Statistics).all()
    else:
        response = db.query(models.Statistics).filter(
            date == request.date
        )
    return response
