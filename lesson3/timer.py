import time

"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""



class Timer:
    def __enter__(self):
        self.start_time = time.time()  # сохраняем текущее время на момент начала блока
        return self  # возвращаем сам объект, чтобы его можно было использовать в контексте `with`

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()  # сохраняем текущее время на момент окончания блока
        self.elapsed_time = self.end_time - self.start_time  # вычисляем разницу во времени
        print(f"Execution time: {self.elapsed_time} seconds")  # выводим время выполнения
        return self.elapsed_time

with Timer() as timer:
    # блок кода
    time.sleep(3)  # например, задержка в 2 секунды

    
    # код для проверки 
    print("Execution time:", timer.elapsed_time)
