class pidControl():
    def __init__(self,p_value = 0,i_value = 0,d_value = 0,current_timestamp = 0):
        ###
        ## PID Coefficient ##
        self.t         = current_timestamp
        self.kp        = p_value
        self.ki        = i_value
        self.kd        = d_value
        self.integral2 = 0
        self.e2        = 0
        ##


    def PID(self,ref, current):
        e1 = ref - current # hata degerimiz
        integra1 = e1*self.t+self.integral2
        turev = (e1-self.e2)/self.t
        self.e2=e1
        self.integral2 = integra1

        return (self.kp*e1) + (self.ki*integra1) + (self.kd*turev)