class DC_Motor:
    # 30 ohms
    Ra = 30
    # 0.006 mH
    La = 0.006
    # 0.05 V / (rad/s)
    Kb = 0.05
    # 0.05 N.m / A
    Kt = 0.05
    # 35 * 10 ^ -6 kg.m^2 / s
    B = 35 * (10 ** -6)
    # 40 * 10 ^ -6 kg.m^2
    J = 40 * (10 ** -6)

    def __init__ (self, delta_t = 0.001):
        self.delta_t = delta_t
        self.voltage = 0
        self._i = 0
        self._w = 0
        self.delta_i = 0
        self.delta_w = 0
        self.angle = 0


    def update (self, voltage):
        self.voltage = voltage
        A = self.Ra * self.delta_t / 2 + self.La
        B = self.Kb * self.delta_t / 2
        C = self.voltage - self.Ra * self._i - self.Kb * self._w

        D = self.Kt * self.delta_t / 2
        E = -(self.B * self.delta_t / 2 + self.J)
        F = self.B * self._w - self.Kt * self._i

        self.delta_i = (C * E - F * B) / (A * E - B * D)
        self.delta_w = (C * D - A * F) / (D * B - A * E)

        self.angle += self._w * self.delta_t
        self._w += self.delta_w * self.delta_t
        self._i += self.delta_i * self.delta_t

if __name__ == '__main__':
    mt = 0
    dc = DC_Motor()
    target = 100
    print('time,angle,target')
    while True:
        mt += 1
        error = target - dc.angle
        dc.update(error / 2)
        print(f'{mt/1000},{dc.angle}, {target}')
        if mt > 5000:
            break
