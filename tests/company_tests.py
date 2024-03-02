import pytest

from src.company import Company


def test_valid_company_creation():
    company = Company(100)
    assert company.get_employee_count() == 100
    assert company.get_parent() is None


def test_invalid_employee_count_type():
    with pytest.raises(TypeError):
        Company("invalid")


def test_invalid_employee_count_value():
    with pytest.raises(ValueError):
        Company(0)


def test_valid_company_with_parent():
    parent_company = Company(200)
    child_company = Company(50, parent=parent_company)
    assert child_company.get_employee_count() == 50
    assert child_company.get_parent() == parent_company


def test_invalid_parent_type():
    with pytest.raises(TypeError):
        Company(100, parent="invalid")


def test_parent_self_reference():
    with pytest.raises(ValueError):
        company = Company(150)
        company.set_parent(company)
