from datetime import datetime, timedelta, timezone

class beijing:
    # utc_time = datetime.utcnow()
    utc_time = datetime.now(tz=timezone.utc)
    bj_time = utc_time.astimezone(timezone(timedelta(hours=8)))
    now = bj_time.now()


def finish_time(percent, hours, minutes, seconds):
    bj_time = beijing.bj_time
    time_spent = timedelta(hours=hours, minutes=minutes, seconds=seconds)

    all_time = time_spent/(percent/100)
    time_remain = all_time - time_spent
    end_time = bj_time + time_remain
    print(f"训练结束时间 {end_time:%Y}年 {end_time:%m}月 {end_time:%d}日 {end_time:%H}点 {end_time:%M}分")
    
    