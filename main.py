def errorcode(x) :
    error_codes = {
    400: 'Bad Request'
    401: 'Unauthorized'
    402: 'Payment Required'
    403: 'Forbidden'
    404: 'Not Found'
    405: 'Method Not Allowed'
    }
    return error_code.get(x, 'Error')

#test
error_number = 400
print({error_number} - {errorcode(error_number)}
quit()
