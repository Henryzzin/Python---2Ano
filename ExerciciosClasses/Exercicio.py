class Carro:
    cor = 'sem cor'
    marca = 'sem marca'
    modelo = 'sem modelo'
    motor = 'desligado'
    statusCarro='parado'

    def ligarMotor(motor):
        if(motor=='desligado'):
            motor='ligado'
    
    def desligarMotor(motor):
        if(motor!='desligado'):
            motor='desligado'

    def andar(motor, statusCarro):
        if(motor==1):
            print("Vrum... vrum...")
            statusCarro='andando'

    def parar(motor, statusCarro):
        print("*Parou*")
        statusCarro='parado'

    def informar(motor, statusCarro):
        print("Status do Movimento do Carro: ", statusCarro)
        print("Status do Motor: ", motor)