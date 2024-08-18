from wrapper import SMSActivateEmailVerificationAPI


def main():
    """
    Main function to showcase the usage of SMSActivateEmailVerificationAPI methods.
    
    This function demonstrates:
    1. Fetching available domains for a site.
    2. Purchasing an email activation.
    3. Checking for the verification code received via email.
    4. Canceling the email purchase if the verification code is not received in time.

    The script uses detailed comments and explanations for each step.

    Responses:
    - `get_domains`: Retrieves the available domains for the specified site.
    - `buy_mail_activation`: Purchases an email activation and returns the email and ID.
    - `check_mail_activation`: Checks if the verification code has been received.
    - `get_verification_code`: Continuously checks for the verification code, cancels if not received.
    - `cancel_mail_activation`: Cancels the email purchase if verification code isn't received.
    """

    # Replace with your actual API key
    api_key = "" # GET YOU API KEY AT https://bit.ly/email-activation
    sms_api = SMSActivateEmailVerificationAPI(api_key)

    # 1. Get available domains for a site (e.g., twitter.com)
    print("Fetching available domains for twitter.com...")
    domains = sms_api.get_domains("twitter.com")["popular"]
    

    # 2. Purchase a mail activation for outlook.com (this will create a new temporary email)
    print("\nPurchasing mail activation for outlook.com...")
    purchase_response = sms_api.buy_mail_activation("twitter.com", 2, "outlook.com")
    print(f"Purchased Email: {purchase_response['email']}, ID: {purchase_response['id']}")

    # 3. Continuously check for the verification code received via email
    mail_id = purchase_response["id"]
    print(f"\nChecking for verification code for Email ID: {mail_id}...")
    try:
        verification_code = sms_api.get_verification_code(mail_id)
        print(f"Verification code received: {verification_code}")
    except TimeoutError as e:
        print(str(e))
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    # If the verification code is received, it will be printed.
    # If not, the script will attempt to cancel the email purchase (you don't charge for cancelled emails) and print an appropriate message.
    
if __name__ == "__main__":
    main()
