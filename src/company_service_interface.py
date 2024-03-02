from abc import ABC
from typing import List

from src.company import Company


class ICompanyService(ABC):
    def get_top_level_parent(self, child) -> None | Company:
        raise NotImplementedError("Method not implemented")

    def get_employee_count_for_company_and_children(self, company: Company, companies: List[Company]) -> int:
        raise NotImplementedError("Method not implemented")
