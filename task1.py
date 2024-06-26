from datetime import datetime

def get_days_from_today(date:str) -> int:
    try:
        date_arg = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError as ve:
        print(ve)
        return
    date_now = datetime.now().date()
    return (date_arg - date_now).days