import sys

from loguru import logger


logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")

def main():
    pass

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info('Script the script was interrupted by clicking Ctrl+C')
    logger.info('Close')
