# pyBunniApi - a Bunni Python Api Client. #

### Requirements ###

+ You need a Bunni Account.
+ You need to generate an API key for your Bunni Account.
+ Python 3.10

### Installation ###

```shell
$ pip install https://github.com/sme4gle/pyBunniApi-master
```

### Getting started with pyBunniApi ###

Let's start with importing the API Client

```python
from pyBunniApi import PyBunniApi
```

Once this is done we have to initialize it.

```python
pyBunniApi = PyBunniApi()
pyBunniApi.set_api_key('YOUR API KEY HERE')
pyBunniApi.set_business_id('YOUR BUSINESS ID HERE')
```

### Receiving the contacts list ###

If your API key has access to 'READ' on the specific parts of contacts, we can use `contacts.list` to view all contacts.

```python
contacts = pyBunniApi.contacts.list()
```

This will return a list of contacts. The response looks like this:

```json
[
  {
    'id': 'co_XXXXXX',
    'companyName': 'CompanyName',
    'toTheAttentionOf': 'Berry the Bunny',
    'street': 'Carrotstreet',
    'streetNumber': '9',
    'postalCode': '1234AB',
    'city': '',
    'phoneNumber': '123456789',
    'vatIdentificationNumber': None,
    'chamberOfCommerceNumber': None,
    'color': '#112233',
    'fields': [],
    'emailAddresses': [
      'berry_the_bunny@bunni.nl'
    ]
  }
]
```

### Receiving a list of invoices ###

If your API key has access to 'READ' on the invoices section, we can use `invoices.list` to gather a list of all
invoices.

```python
invoice_list = pyBunniApi.invoices.list()
```

This will return a list with all invoices, the response looks like this:

```json
{
  'items': [
    {
      'id': 'in_XXXXXX',
      'invoiceDate': '2023-08-09',
      'invoiceNumber': '2023005',
      'isFinalized': True,
      'duePeriodDays': 30,
      'pdfUrl': 'https://superlongpdfurl.pdf',
      'rows': [
        {
          'description': 'This is the description of your row.',
          'quantity': 1.0,
          'unitPrice': 100
        }
      ]
    }
  ]
}
```

### Creating an invoice ###

Please note, that as of now this feature only generates a PDF. Said invoice will not be placed in your bookkeeping
software as of now.
You can however write your own piece of code that stores this pdf somewhere on your webserver, and sends it
to `YOUR_BUSINESS_ID@postbode.bunni.nl` in order to get it automatically placed in your bookkeeping.

Anyways, this part is a little bit more spicy and requires a few more steps.
Again, this only works if your API key has access to the `WRITE` permissions of Invoice.

First, let's start by defining our rows. A row requires four parameters. One invoice can contain varying rows. We append
these bu putting rows in a list.

To create row we can initialize a `Row()`. The complete syntax would look like this:

```python
row = pyBunniApi.Row(
    unit_price=12.5,  # This should be a float.
    description="This is a test description",
    quantity=5,
    tax="NL_High_21",  # This should be a string.
)
```

For explaining how this works, one row will be enough. The next step is to create a `Contact()` This can be done like
this:

```python
contact = pyBunniApi.Contact(
    company_name="The Carrot Company",
    attn='Jim Carrot',
    street='Carrot Street',
    street_number=20,
    postal_code='1122AB',
    city='Bunny Town',
    phone_number='123456789',
)
```

Now we can build a complete invoice using `Invoice()` by the following manner:

```python
invoice = Invoice(
    invoice_date='YYYY-MM-DD',
    invoice_number='12345.67',
    tax_mode='excl',  # This can be either `incl` or `excl`,
    design='INVOICE_DESIGN_ID',  # A little down here I'll explain how you can fetch this ID.
    contact=contact,  # We made a contact above here.
    rows=[row]
)
```

We now have a initialized `Invoice` object which we can use to create a invoice (pdf) in Bunni.
We can do this by using `pyBunniApi.invoices.create`

A complete snippet of this code would look like this:
```python
invoice_pdf = pyBunniApi.invoices.create(invoice)
```
This will return a single pdf url, so the expected response should look like this:
```text
https://restpack.io/cache/pdf/069aba16b0ced81a42ecba6d7fd841885f53dd9bcac71cbbcb08756bad73e1ac
```