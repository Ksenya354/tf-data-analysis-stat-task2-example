import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1943224240 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    b = x.max()
    alpha = 1 - p
    loc = 0.017
    return b/2 - loc, \
           b/(2*alpha**(1/len(x))) - loc
