from insurance.logger import logging
from insurance.exception import InsuranceException
import sys
from insurance.utils import get_collection_as_dataframe


DATABASE_NAME="INSURANCE"
COLLECTION_NAME="iNSURANCE_DATA"


if __name__ == "__main__":
    try:
        data=get_collection_as_dataframe(database_name=DATABASE_NAME,collection_name=COLLECTION_NAME)
        logging.info(data.head(5))
    except Exception as e:
        raise InsuranceException(e,sys)
