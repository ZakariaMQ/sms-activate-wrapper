from typing import Optional
import httpx
import time

class SMSActivateEmailVerificationAPI:
    def __init__(self, api_key:str):
        self.api_key = api_key
        self.base_url = "https://api.sms-activate.io/stubs/handler_api.php"

    def _request(self, params:dict) -> dict | None:
        try:
            response = httpx.get(self.base_url, params=params)
            response.raise_for_status()
            json_response = response.json()
            if json_response.get('status') != 'OK':
                raise ValueError(f"API Error: {json_response}")
            return json_response['response']
        except httpx.HTTPStatusError as e:
            raise ConnectionError(f"HTTP error occurred: {e}")
        except httpx.RequestError as e:
            raise ConnectionError(f"Request error occurred: {e}")
        except ValueError as e:
            raise ValueError(f"API returned an error: {e}")

    def get_domains(self, site:str) -> dict:
        params = {
            "action": "getDomains",
            "api_key": self.api_key,
            "site": site
        }
        return self._request(params)

    def buy_mail_activation(self, site:str, mail_type:int, mail_domain:str) -> dict:
        params = {
            "action": "buyMailActivation",
            "api_key": self.api_key,
            "site": site,
            "mail_type": mail_type,
            "mail_domain": mail_domain
        }
        return self._request(params)

    def reorder_mail_activation(self, mail_id:int) -> dict:
        params = {
            "action": "reorderMailActivation",
            "api_key": self.api_key,
            "id": mail_id
        }
        return self._request(params)

    def get_mail_history(self, page:int, per_page:int, search:Optional[str]=None, sort:Optional[str]=None) -> dict:
        params = {
            "action": "getMailHistory",
            "api_key": self.api_key,
            "page": page,
            "per_page": per_page,
            "search": search or "",
            "sort": sort or ""
        }
        return self._request(params)

    def cancel_mail_activation(self, mail_id:int) -> bool:
        params = {
            "action": "cancelMailActivation",
            "api_key": self.api_key,
            "id": mail_id
        }
        response = self._request(params)
        return bool(response)

    def check_mail_activation(self, mail_id:int) -> Optional[str]:
        params = {
            "action": "checkMailActivation",
            "api_key": self.api_key,
            "id": mail_id
        }
        response = self._request(params)
        return response.get("value")
    
    def get_verification_code(self, mail_id:int) -> Optional[str]:
        for _ in range(50):
            code = self.check_mail_activation(mail_id)
            if code:
                return code
            time.sleep(.5)

        cancellation_successful = self.cancel_mail_activation(mail_id)
        if cancellation_successful:
            raise TimeoutError("Verification code not received in time. Email purchase canceled.")
        else:
            raise Exception("Verification code not received and failed to cancel the email purchase.")
        
