from typing import Dict, Any
from datetime import datetime
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Order(db.Model, IDto):
    """
    Model declaration for Order Data Mapper.
    """
    __tablename__ = "orders"

    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    driver_id = db.Column(db.Integer, nullable=False)
    car_id = db.Column(db.Integer, nullable=False)
    pick_up_location = db.Column(db.String(255), nullable=False)
    drop_off_location = db.Column(db.String(255), nullable=False)
    order_time = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)

    def __repr__(self) -> str:
        return (f"Order({self.order_id}, {self.user_id}, {self.driver_id}, {self.car_id}, "
                f"{self.pick_up_location}, {self.drop_off_location}, {self.order_time})")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "order_id": self.order_id,
            "user_id": self.user_id,
            "driver_id": self.driver_id,
            "car_id": self.car_id,
            "pick_up_location": self.pick_up_location,
            "drop_off_location": self.drop_off_location,
            "order_time": self.order_time,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> "Order":
        return Order(**dto_dict)
