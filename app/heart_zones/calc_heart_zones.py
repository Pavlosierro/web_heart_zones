class HeartZones:
    def __init__(self, hr: list[int]):
        self.s1_zone = (0, 132)
        self.s2_zone = (133, 148)
        self.s3_zone = (149, 159)
        self.s4_zone = (160, 170)
        self.s5_zone = (170, 220)
        self.LT_zone = 165

        self.hr = hr

        self.s1 = 0
        self.s2 = 0
        self.s3 = 0
        self.s4 = 0
        self.s5 = 0

        self.LT = 0

        self._calc_zones()

    def _calc_zones(self):
        for i in self.hr:
            if i <= self.s1_zone[1]:
                self.s1 += 1
            elif self.s2_zone[0] <= i <= self.s2_zone[1]:
                self.s2 += 1
            elif self.s3_zone[0] <= i <= self.s3_zone[1]:
                self.s3 += 1
            elif self.s4_zone[0] <= i <= self.s4_zone[1]:
                self.s4 += 1
            elif self.s5_zone[0] <= i <= self.s5_zone[1]:
                self.s5 += 1

            if i >= self.LT_zone:
                self.LT += 1

    def __len__(self):
        return len(self.hr)

    def __str__(self):
        return f"S1: {self.s1}, S2: {self.s2}, S3: {self.s3}, S4: {self.s4}, S5: {self.s5}, LT: {self.LT}"

    def print_percentage(self):
        return f"S1: {round(self.s1 / len(self) * 100, 2)}%, " \
               f"S2: {round(self.s2 / len(self) * 100, 2)}%, " \
               f"S3: {round(self.s3 / len(self) * 100, 2)}%, " \
               f"S4: {round(self.s4 / len(self) * 100, 2)}%, " \
               f"S5: {round(self.s5 / len(self) * 100, 2)}%, " \
               f"LT: {round(self.LT / len(self) * 100, 2)}%"

    def get_results(self) -> list[int]:
        return [self.s1, self.s2, self.s3, self.s4, self.s5, self.LT]



