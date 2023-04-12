import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1943224240 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t = x.max() - 0.017
    alpha = 1 - p
    return 0.017 + t/((1-alpha/2)**(1/len(x))), \
           0.017 + t/((alpha/2)**(1/len(x)))
