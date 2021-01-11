import smtplib


def sendmail(to_email, message, Cofirmation_mail):

    from_email = "creativegaurav2012@gmail.com"

    response = {}
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as s:
            s.starttls()
            s.login(from_email, "********") #Removed password due to security reasons.Enter your credentials
            print("Sending Mail:", to_email)
            s.sendmail(from_email, to_email, message)
        response['email_status'] = "Success"
    except Exception as err:
        print(err)
        response['email_status'] = "Failed"

    return response
# if __name__ == "__main__":
# sendmail()
