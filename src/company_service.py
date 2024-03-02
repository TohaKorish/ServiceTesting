from typing import List

from src.company import Company
from src.company_service_interface import ICompanyService


class CompanyService(ICompanyService):
    def get_top_level_parent(self, child: Company) -> None | Company:
        while child.get_parent():
            child = child.get_parent()
        return child

    def get_employee_count_for_company_and_children(self, company: Company, companies: List[Company]) -> int:
        total_employee_count = 0

        # Find the specified company in the list of companies
        for comp in companies:
            if comp == company:
                total_employee_count += comp.get_employee_count()  # Add employee count of the specified company
                break

        # Check for child companies of the specified company and add their employee count
        for comp in companies:
            if comp.get_parent() == company:
                total_employee_count += self.get_employee_count_for_company_and_children(comp, companies)

        return total_employee_count
