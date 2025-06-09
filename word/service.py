import csv
from pathlib import Path

from common.enums import CategoryEnum
from common.service import BaseService
from config import BASE_DIR
from logger import Logger

logger = Logger.setup_logger(__name__)


CSV_WITH_WORD_PATH = BASE_DIR / "words.csv"


class WordService(BaseService):
    async def upload_words_from_csv(self) -> None:
        file = Path(CSV_WITH_WORD_PATH)
        if not file.exists():
            raise FileNotFoundError(f"CSV file not found: {CSV_WITH_WORD_PATH}")
        with file.open("r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    category = CategoryEnum(row["category"])
                    word = row["word"].strip()
                    await self.requests_repo.word_repo.create(
                        is_flush=True,
                        category=category,
                        word=word,
                    )
                    await self.requests_repo.commit()
                except Exception as exc:
                    logger.error(
                        f"Skipping row due to error: {row} | Error: {exc}",
                        exc_info=True,
                    )
