# Trading 212 to Lunch Money Sync

## Overview

This project provides a solution to synchronize your investments from Trading 212 to Lunch Money. It allows you to keep track of your investment portfolio alongside your other financial activities in Lunch Money, providing a comprehensive view of your finances.

## Prerequisites

Before using this project, ensure you have the following:

- A Trading 212 account with API access enabled.
- A Lunch Money account with an Access Token.

## Installation

1. Clone or download this repository to your local machine.
2. Install the required dependencies by running:
   ```
   poetry install
   ```

## Configuration

1. Obtain your Trading 212 API key (Menu -> Settings -> API (Beta) -> Live Key).
2. Obtain your Lunch Money Access Token (Settings -> Developers -> Request new access token).
3. Copy the `.env.example` file to `.env` and update it with your credentials:

  ```
  TRADING212_API_KEY=<your_trading_212_api_key>
  LUNCHMONEY_ACCESS_TOKEN=<your_lunch_money_api_key>
  ```

## Usage

1. Run the project:

   ```
   poetry run python lunchmoney_t212/__init__.py
   ```

2. The script will fetch your investments from Trading 212 and sync them with your Lunch Money account.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## Disclaimer

This project is provided as-is and is not affiliated with Trading 212 or Lunch Money. Use it at your own risk.