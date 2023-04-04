from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import List


class Homework:
    def __init__(self, name: str, deadline_days: int):
        self._name = name
        self._deadline = datetime.now() + timedelta(days=deadline_days)
        self._is_complete = False

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str):
        self._name = name

    def get_deadline(self) -> datetime:
        return self._deadline

    def set_deadline(self, deadline_days: int):
        self._deadline = datetime.now() + timedelta(days=deadline_days)

    def get_is_complete(self) -> bool:
        return self._is_complete

    def set_is_complete(self, is_complete: bool):
        self._is_complete = is_complete


class HomeworkRepository(ABC):
    @abstractmethod
    def save_homework(self, homework: Homework):
        pass

    @abstractmethod
    def get_homeworks(self) -> List[Homework]:
        pass


class InMemoryHomeworkRepository(HomeworkRepository):
    def __init__(self):
        self.homeworks = []

    def save_homework(self, homework: Homework):
        self.homeworks.append(homework)

    def get_homeworks(self) -> List[Homework]:
        return self.homeworks


class HomeworkService:
    def __init__(self, repository: HomeworkRepository):
        self.repository = repository

    def create_homework(self, name: str, deadline_days: int):
        homework = Homework(name, deadline_days)
        self.repository.save_homework(homework)

    def get_homeworks(self) -> List[Homework]:
        return self.repository.get_homeworks()


if __name__ == '__main__':
    repository = InMemoryHomeworkRepository()
    service = HomeworkService(repository)

    service.create_homework('Math Homework', 7)
    service.create_homework('English Essay', 5)

    homeworks = service.get_homeworks()
    for homework in homeworks:
        print(homework.get_name(), homework.get_deadline())
