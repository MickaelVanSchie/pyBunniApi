from pyBunniApi.tools.case_convert import to_camel_case, to_snake_case


def test_to_snake_case():
    assert to_snake_case("companyName") == "company_name"
    assert to_snake_case("isFinalized") == "is_finalized"
    assert to_snake_case("id") == "id"


def test_to_camel_case():
    assert to_camel_case("company_name") == "companyName"
    assert to_camel_case("is_finalized") == "isFinalized"
    assert to_camel_case("id") == "id"
