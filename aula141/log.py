from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:  # super classe

    def _log(self, msg):  # metodo '_log'  protected
        raise NotImplementedError('Implemente o metodo log')

    def log_error(self, msg):
        # repassando o log error para as classes abaixo
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        # repassando o log success para as classes abaixo
        return self._log(f'success: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('salvando no log:',msg_formatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada) 
        


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    lp = LogPrintMxin()
    lp.log_error('coisa qualquer')
    lp.log_success('success')
    lf = LogFileMxin()
    lf.log_error('qualquer coisa')
    lf.log_success('Que legal')
    
