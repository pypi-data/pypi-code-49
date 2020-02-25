class BMI:
    """Class that will calculate the body mass index."""

    def __init__(self, sex, weight, height):
        self.sex = sex
        self.weight = weight
        self.height = height
        self.reg_male = {'V1': 20.7, 'V2': 26.4, 'V3': 27.8, 'V4': 31.1}
        self.reg_female = {'V1': 19.1, 'V2': 25.8, 'V3': 27.3, 'V4': 32.3}

    def calc_bmi(self):
        """
        This method will perform the body mass index calculation.
        Applied within the "calc_bmi" method.
        """
        try:
            w = float(self.validate_hw(self.weight, 0, 350))
            h = float(self.validate_hw(self.height, 0, 3))
            return w / (h * h)
        except Exception:
            return False

    def validate_sex(self):
        """Method to validate the person's gender.
        """
        if self.sex == 'm' or self.sex == 'f':
            return self.sex
        return False

    @staticmethod
    def validate_hw(hw, value1, value2):
        """
        This is a static method for validating weight and height.
        The height cannot be greater than 3 meters and neither the weight
        above 350, nor can both be zeroed or negative
        """
        if float(hw) <= value1 or float(hw) > value2:
            return False
        return hw

    @staticmethod
    def reply(result_bmi, reg):
        """
        The purpose of this statistical method is to receive the calculation
        of the body mass index already done, and to compare it with the
        statistical data informed in the initializer method of the class.
        """
        if result_bmi < reg['V1']:
            return 'Under weight.'
        elif reg['V1'] <= result_bmi < reg['V2']:
            return 'Normal weight.'
        elif reg['V2'] <= result_bmi < reg['V3']:
            return 'Marginally overweight.'
        elif reg['V3'] <= result_bmi < reg['V4']:
            return 'Overweight.'
        elif result_bmi > reg['V4']:
            return 'Obesity.'

    def main(self):
        if self.calc_bmi():
            if self.validate_sex() == 'm':
                return self.reply(self.calc_bmi(), self.reg_male)
            elif self.validate_sex() == 'f':
                return self.reply(self.calc_bmi(), self.reg_female)
        return False
