from typing import Tuple
import csv
import magic
from io import TextIOWrapper

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

        csv_file = TextIOWrapper(uploaded_file, encoding='utf-8')
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
            Deals.objects.create(
                customer=customer,
                item=item,
                total=int(total),
                quantity=int(quantity),
                date=date
            )
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
            cls._clear_existing_data() # В требованиях в пункте 2 не очень понятно, что имелось в виду, поэтому сделал так чтобы все удалялось
            cls._validate_csv_file(uploaded_file)
            cls._process_csv_data(uploaded_file)
            return True, ""
        except Exception as e:
            return False, str(e)