from pyBunniApi.objects.category import Category
from pyBunniApi.objects.row import Row


def test_row_as_dict_minimal():
    row = Row(description="Test", quantity=2, unit_price=10.0)
    assert row.as_dict() == {
        "unitPrice": 10.0,
        "description": "Test",
        "quantity": 2,
        "tax_rate": None,
        "bookingCategory": None,
    }


def test_row_as_dict_with_tax_and_category():
    category = Category(id="1", name="Test", color="#FFFFFF", ledger_number="1234")
    row = Row(
        description="Test",
        quantity=2,
        unit_price=10.0,
        tax="NL_High_21",
        booking_category=category,
    )
    assert row.as_dict() == {
        "unitPrice": 10.0,
        "description": "Test",
        "quantity": 2,
        "tax_rate": {"id": "NL_High_21"},
        "bookingCategory": category.as_dict(),
    }
