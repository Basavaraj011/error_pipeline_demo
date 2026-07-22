import traceback

from data_loader import load_data
from data_validator import validate_dat
from data_loader import load_data
from data_validator import validate_data
import sys


def run_pipeline():

    valid_data = [record for record in data if is_valid_record(record)]
    data = load_data("data.txt")

    valid_data = [record for record in data if is_valid_record(record)]

    results = process_data(valid_data)

    for r in results:
        print("Processed:", r)

    data = load_data("data.txt")
    valid_data = validate_data(data)
    results = process_data(valid_data)
    for r in results:
        print("Processed:", r)
        print("\nPipeline crashed!\n")

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
