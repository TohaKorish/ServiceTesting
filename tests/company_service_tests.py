import pytest

from src.company import Company
from src.company_service import CompanyService


@pytest.fixture
def sample_companies():
    company1 = Company(100)
    company2 = Company(200)
    company3 = Company(150, parent=company1)
    company4 = Company(50, parent=company2)
    company5 = Company(75, parent=company2)
    company6 = Company(80, parent=company3)
    return [company1, company2, company3, company4, company5, company6]


def test_get_top_level_parent(sample_companies):
    service = CompanyService()
    assert service.get_top_level_parent(sample_companies[5]) == sample_companies[0]


def test_get_employee_count_for_company_and_children(sample_companies):
    service = CompanyService()
    assert service.get_employee_count_for_company_and_children(sample_companies[0], sample_companies) == 330
    assert service.get_employee_count_for_company_and_children(sample_companies[1], sample_companies) == 325
    assert service.get_employee_count_for_company_and_children(sample_companies[2], sample_companies) == 230
    assert service.get_employee_count_for_company_and_children(sample_companies[3], sample_companies) == 50
    assert service.get_employee_count_for_company_and_children(sample_companies[4], sample_companies) == 75
    assert service.get_employee_count_for_company_and_children(sample_companies[5], sample_companies) == 80


def test_get_employee_count_for_company_and_children_empty():
    service = CompanyService()
    assert service.get_employee_count_for_company_and_children(Company(100), []) == 0


def test_get_employee_count_for_company_and_children_single_company():
    service = CompanyService()
    company = Company(100)
    assert service.get_employee_count_for_company_and_children(company, [company]) == 100


def test_get_employee_count_for_company_and_children_no_parent():
    service = CompanyService()
    company1 = Company(100)
    company2 = Company(200)
    company3 = Company(150)
    assert service.get_employee_count_for_company_and_children(company1, [company1, company2, company3]) == 100
    assert service.get_employee_count_for_company_and_children(company2, [company1, company2, company3]) == 200
    assert service.get_employee_count_for_company_and_children(company3, [company1, company2, company3]) == 150
