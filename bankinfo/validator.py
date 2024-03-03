import concurrent.futures
import requests
import pprint


class BankInfoValidator:
    def __init__(self) -> None:
        """
        Initializes the PhoneNumberValidator class with an API key.

        Args:
            api_key (str): Your API key for the NumLookupAPI.
        """

        self.api_url = "https://ccdcapi.alipay.com/validateAndCacheCardInfo.json"
        self.params = {"_input_charset": "utf-8", "cardNo": None, "cardBinCheck": True}

    def validate(self, bank_number: str) -> dict:
        """ """
        if not bank_number:
            raise ValueError("bank_number cannot be empty!")
        self.params["cardNo"] = bank_number
        response = self._make_api_call(self.params)
        if response.ok:
            return response.json()
        else:
            response.raise_for_status()

    def _make_api_call(self, params: dict) -> requests.Response:
        response = requests.get(self.api_url, params=params)
        return response

    def get_bank_logos(self, bank_numbers: str) -> dict:
        """ """
        _url = "https://apimg.alipay.com/combo.png?d=cashier&t="
        params = {
            "d": "cashier",
            "t": bank_numbers,
        }

        response = requests.get(_url, params)
        if response.ok:
            return response.json()
        else:
            response.raise_for_status()


def print_info(bank_num, bankValidate: BankInfoValidator):
    pprint.pprint(bankValidate.validate(bank_num), depth=1)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="get bank info")

    bank_info = BankInfoValidator()

    parser.add_argument("bank", metavar="N", type=str, nargs="+", help="银行卡")
    args = parser.parse_args()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for bno in args.bank:
            bno = bno.strip()
            executor.submit(print_info, bno, bank_info)


if __name__ == "__main__":
    main()
