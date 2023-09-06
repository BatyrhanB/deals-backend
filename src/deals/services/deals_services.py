from typing import List, Dict, Union, Tuple
import csv
import magic
from io import TextIOWrapper
from django.db.models import Sum, Count

from common.exceptions import SomethingGetWrongException
from deals.models import Deals


class DealsService(object):
    @classmethod
    def _validate_csv_file(cls, uploaded_file):
        """
        Checks whether the file is a valid CSV file

        Args:
            uploaded_file: Uploaded CSV file

        Raises:
            ValueError: If the file is not a CSV file
        """
        mime = magic.Magic()
        file_type = mime.from_buffer(uploaded_file.read(1024))
        if "csv" not in file_type.lower():
            raise ValueError("Incorrect file format. Only CSV files are allowed.")
        uploaded_file.seek(0)

    @classmethod
    def _process_csv_data(cls, uploaded_file):
        """
        Processes data from the CSV file and saves it in the database

        Args:
            uploaded_file: Uploaded CSV file
        """

        csv_file = TextIOWrapper(uploaded_file, encoding="utf-8")
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            cls._create_deal_from_csv_row(row)

    @classmethod
    def _create_deal_from_csv_row(cls, row):
        """
        Creates a Deals instance from a CSV row and saves it in the database

        Args:
            row: A CSV row containing data to create a Deals instance

        Raises:
            ValueError: If the format of the row is incorrect or the data is of the wrong format
        """

        if len(row) != 5:
            raise ValueError("Invalid CSV format. Each row must contain 5 fields.")
        customer, item, total, quantity, date = row
        try:
            Deals.objects.create(customer=customer, item=item, total=int(total), quantity=int(quantity), date=date)
        except ValueError:
            raise ValueError("Invalid data format. Fields must be integers.")

    @classmethod
    def _clear_existing_data(cls):
        """
        Cleans existing data in the database before loading a new version of the file.
        """
        Deals.objects.all().delete()

    @classmethod
    def deals_upload_from_csv(cls, uploaded_file) -> Tuple[bool, str]:
        """
        Uploads data from a CSV file to the Deals database

        Args:
            uploaded_file: Uploaded CSV file

        Returns:
            Tuple[bool, str]: A tuple indicating the success of the operation and an error message
        """
        try:
            cls._clear_existing_data()  # В требованиях в пункте 2 не очень понятно, что имелось в виду, поэтому сделал так чтобы все удалялось
            cls._validate_csv_file(uploaded_file)
            cls._process_csv_data(uploaded_file)
            return True, ""
        except Exception as e:
            return False, str(e)


class CustomerService:
    @classmethod
    def get_top_customers(cls) -> List[Dict[str, Union[str, float, List[str]]]]:
        """
        Get information about the top 5 customers based on spent money and their unique list of gems.

        Returns:
            List[Dict[str, Union[str, float, List[str]]]]: List of top customers with their data.

        Raises:
            SomethingGetWrongException: If there's an issue with the database query.
        """
        try:
            top_customers = (
                Deals.objects.values("customer").annotate(spent_money=Sum("total")).order_by("-spent_money")[:5]
            )
        except Exception as e:
            raise SomethingGetWrongException(f"Failed to retrieve top customers: {str(e)}")

        customer_data = []
        for customer in top_customers:
            username = customer["customer"]
            spent_money = customer["spent_money"]

            customer_gems = cls.get_customer_gems(username)

            customer_data.append(
                {
                    "username": username,
                    "spent_money": spent_money,
                    "gems": list(customer_gems),
                }
            )

        return customer_data

    @classmethod
    def get_customer_gems(cls, username: str) -> set:
        """
        Get a set of unique gems purchased by a specific customer.

        Args:
            username (str): The username of the customer.

        Returns:
            set: A set containing unique gem names.

        Raises:
            SomethingGetWrongException: If there's an issue with the database query.
        """
        try:
            gems_query = Deals.objects.filter(
                customer=username,
                item__in=Deals.objects.values("item")
                .annotate(customer_count=Count("customer"))
                .filter(customer_count__gte=2)
                .values_list("item", flat=True),
            )
            customer_gems = set(gems_query.values_list("item", flat=True))
        except Exception as e:
            raise SomethingGetWrongException(f"Failed to retrieve gems for customer {username}: {str(e)}")

        return customer_gems
