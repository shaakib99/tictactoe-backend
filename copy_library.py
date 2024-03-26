import shutil
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Copying library to the project")
    shutil.copytree("../tic-tac-toe-lib", "./__lib__", dirs_exist_ok=True)
    logger.info("Library copied successfully")