from human import Human


class Worker(Human):
    def __init__(self,
                 name='',
                 surname='',
                 payment=0,
                 working_hours=0
                 ):
        self.payment = payment
        self.working_hours = working_hours
        super().__init__(name, surname)
