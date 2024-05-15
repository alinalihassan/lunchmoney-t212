"""
Fetch Account total from Trading 212 and update your asset in LunchMoney.
"""

from os import getenv

from lunchable import LunchMoney
from lunchable.models.assets import AssetsObject

from trading212 import Trading212


def find_t212_asset(lunch: LunchMoney) -> AssetsObject:
    '''Look for Asset with name "Trading 212"'''

    return next(
        (asset for asset in lunch.get_assets() if asset.name == "Trading 212"),
        None,
    )


def sync_investments():
    t212_client = Trading212(getenv("TRADING212_API_KEY"))

    total = t212_client.fetch_account_cash().total
    currency_code = t212_client.fetch_account_metadata().currencyCode.lower()

    lunch = LunchMoney(access_token=getenv("LUNCHMONEY_ACCESS_TOKEN"))
    asset = find_t212_asset(lunch)

    if asset is None:
        lunch.insert_asset(
            type_name="investment",
            name="Trading 212",
            balance=total,
            currency=currency_code,
            institution_name="Trading 212",
        )
        print("Trading 212 investments created!")
    else:
        lunch.update_asset(asset.id, balance=total, currency=currency_code)
        print("Trading 212 investments updated!")


if __name__ == "__main__":
    sync_investments()
