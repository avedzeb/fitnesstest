
"""
action, тип int — количество совершённых действий (число шагов при ходьбе и беге либо гребков — при плавании);
duration, тип float — длительность тренировки;
weight, тип float — вес спортсмена.
"""
from email import message


class Training:
    M_IN_KM = 1000

    def __init__(self, action: int, duration: float, weight: float):
        self.action = action
        self.duration = duration
        self.weight = weight

        #init funct
    
    def get_distance(self):
        return self.action * self.LEN_STEP / self.M_IN_KM 

    def get_mean_speed(self):
        return self.get_distance() / self.duration

    def get_spent_calories(self):
        pass


    def show_training_info(self,training_type: str):
        message = InfoMessage(training_type,self.duration, self.get_distance(), self.get_mean_speed(), self.get_spent_calories())
        return message.get_message()



"""
Class for running
"""
class Running(Training):
    LEN_STEP = 0.65

    def __init__(self, action: int, duration: float, weight: float):
        super().__init__(action, duration, weight)

    def get_spent_calories(self):
        calorie_coeff_1 = 18
        calorie_coeff_2 = 20
        return (calorie_coeff_1 * self.get_mean_speed() - calorie_coeff_2) * self.weight / self.M_IN_KM * self.duration * 60

    def show_training_info(self):
        super().show_training_info('RUN')

"""
Class for walking
"""
class SportsWalking(Training):
    LEN_STEP = 0.65

    def __init__(self, action: int, duration: float, weight: float, height: float):
        self.height = height
        super().__init__(action, duration, weight)

    def get_spent_calories(self):
        calorie_coeff_1 = 0.035
        calorie_coeff_2 = 0.029
        return (calorie_coeff_1 * self.weight + (self.get_mean_speed()**2 // self.height) * calorie_coeff_2 * self.weight) * self.duration * 60
    
    def show_training_info(self):
        super().show_training_info('WALK')
"""
Class for swimming
"""
class Swimming(Training):
    LEN_STEP = 1.38

    def __init__(self, action: int, duration: float, weight: float, length_pool: float, count_pool: int):
        self.count_pool = count_pool
        self.length_pool = length_pool
        super().__init__(action, duration, weight)

    def get_spent_calories(self):
        return (self.get_mean_speed() + 1.1) * 2 * self.weight  


    def get_mean_speed(self):
        return self.length_pool * self.count_pool / self.M_IN_KM / self.duration
    
    def show_training_info(self):
        super().show_training_info('SWIM')


class InfoMessage:

    def __init__(self, training_type: str, duration: float, distance: float, speed: float, calories: int ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self):
        duration = round(self.duration, 3)
        distance = round(self.distance, 3)
        speed = round(self.speed, 3)
        calories = round(self.calories, 3)
        print(f'Тип тренировки: {self.training_type}; Длительность: {duration} ч.; Дистанция: {distance} км; Ср. скорость: {speed} км/ч; Потрачено ккал: {calories}. ')




train = Running(15000,1,75)
train.show_training_info()

train = Swimming(720,1,80,25,40)
train.show_training_info()

train = SportsWalking(9000,1,75,180)
train.show_training_info()
