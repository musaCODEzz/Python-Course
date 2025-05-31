#abstraction
#removing complexity by hiding unnecessary details
class EmailService:
    #connecting to server
    def _connect_server(self):
        print('connecting to server....')
    
    def _authenticate_email(self):
        print('authenticating email....')
    #sending email
    def send_email(self):
        self._connect_server()
        self._authenticate_email()
        print('Sending email....')
        self._disconnect_server()
  #disconnecting from server      
    def _disconnect_server(self):
        print('Disconnecting from server....')

email = EmailService()
email.send_email()