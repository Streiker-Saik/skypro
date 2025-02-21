# import logging

# from src.utils import get_transactions_from_json
# from src.masks import get_mask_account, get_mask_card_number
#
# get_mask_account(12345678901234567890)
# get_mask_card_number(1234567890123456)
# get_transactions_from_json("data/operations.json")
#
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(name)s - %(levelname)s: %(message)s',
#                     filename=f'logs/application.log',
#                     filemode='w')
#
# mask_logger = logging.getLogger("add.mask")
# utils_logger = logging.getLogger("add.utils")
# main_logger = logging.getLogger("add.main")