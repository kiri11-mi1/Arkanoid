
class Settings:
    '''Класс настроек игры'''
    def __init__(self):
        '''Инициализация параметров игры'''
        # Настройки экрана и частоты кадров
        self.W = 600
        self.H = 400
        self.FPS = 60

        # Цвета
        self.white = 255, 255, 255
        self.red = 218, 0, 0

        # Скорость
        self.board_speed = 3
        self.ball_speed = 2