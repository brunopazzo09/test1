class Transaction:
    def __init__(self, property, unique_id, price, transfer_date, duration, PPD_type, record_status):
        self.unique_id=unique_id
        self.property = property
        self.price=price
        self.transfer_date=transfer_date
        self.duration=duration
        self.PPD_type=PPD_type
        self.record_status=record_status

    def __str__(self):
        return f"Transaction: Property={self.property}, Unique ID={self.unique_id}, Price={self.price}, " \
               f"Transfer Date={self.transfer_date}, Duration={self.duration}, PPD Type={self.PPD_type}, " \
               f"Record Status={self.record_status}"

