import pytest

from src.company import Company
from src.company_service_interface import ICompanyService


def test_valid_company_creation():
    company = Company(150)
    company_service = ICompanyService()
    with pytest.raises(NotImplementedError):
        company_service.get_employee_count_for_company_and_children(company, [company, company])
    with pytest.raises(NotImplementedError):
        company_service.get_top_level_parent(company)
