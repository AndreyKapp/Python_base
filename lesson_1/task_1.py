"""1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* *до месяца, до года, больше года: по аналогии."""

def convert_time(seconds):
    days=seconds//86400
    seconds=seconds %(24 *3600)
    hour=seconds//3600
    seconds%=3600
    minutes = seconds // 60
    seconds%=60
    print(f"{days}:{hour}:{minutes}:{seconds}")
convert_time(100000)

    

    