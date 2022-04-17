#!python3
import math

class PID:
    def __init__ (self, P = 1, I = 1, D = 1, delta_t = 0.001):
        self.P = P
        self.I = I
        self.D = D
        self.error_sum = 0
        self.pre_error = 0
        self.delta_t = delta_t

    def get_error_sum:
        return self.error_sum

    def get_pre_error:
        return self.pre_error

    def update (self, error):
        self.error_sum += error * self.delta_t
        y = self.P * error + self.I * self.error_sum + self.D * (error - self.pre_error) / self.delta_t
        self.pre_error = error
        return y


if __name__ == '__main__':
    pass
