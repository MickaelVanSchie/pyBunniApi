# pyBunniApi - a Bunni Python Api Client. #

### Requirements ###

+ You need a Bunni Account.
+ You need to generate an API key for your Bunni Account.
+ Python 3.10+

### Installation ###
___
```shell
$ pip install pyBunniApi
```

### Getting started with pyBunniApi ###
___
Let's start with importing the API Client

```python
from pyBunniApi.client import Client
```

Once this is done we have to initialize it.

```python
py_bunni_api = Client()
py_bunni_api.set_api_key('YOUR API KEY HERE')
py_bunni_api.set_business_id('YOUR BUSINESS ID HERE')
```

Optionally you can select if you want to receive all responses in a typed, or a flat dict. You can set this parameter with the following code:

```python
py_bunni_api.use_typing(True)
```
The default value of this parameter is `True`

### Receiving the contacts list ###
___
If your API key has access to 'READ' on the specific parts of contacts, we can use `contacts.list` to view all contacts.

```python
contacts = py_bunni_api.contacts.list()
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
___
If your API key has access to 'READ' on the invoices section, we can use `invoices.list` to gather a list of all
invoices.

```python
invoice_list = py_bunni_api.invoices.list()
```

This will return a list with all invoices, the response looks like this:

```json
[
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
```

### Building the shared invoice building blocks ###
___
Both creating an invoice PDF and creating a full invoice (see below) start from the same two building blocks:
a `Row` and a `Contact`. This part only works if your API key has access to the `WRITE` permissions of Invoice.

First, let's start by defining our rows. A row requires four parameters. One invoice can contain varying rows. We append
these by putting rows in a list.

To create a row we can initialize a `Row()`. The complete syntax would look like this:

```python
row = PyBunniApi.Row(
    unit_price=12.5,  # This should be a float.
    description="This is a test description",
    quantity=5,
    tax="NL_High_21",  # This should be a string.
)
```

For explaining how this works, one row will be enough. The next step is to create a `Contact()` This can be done like
this:

```python
contact = PyBunniApi.Contact(
    company_name="The Carrot Company",
    attn='Jim Carrot',
    street='Carrot Street',
    street_number=20,
    postal_code='1122AB',
    city='Bunny Town',
    phone_number='123456789',
)
```

With a `row` and `contact` ready, you can move on to either creating an invoice PDF or a full invoice.

### Creating an invoice PDF ###
___
This feature only generates a PDF. Said invoice will not be placed in your bookkeeping
software as of now.
You can however write your own piece of code that stores this pdf somewhere on your webserver, and sends it
to `YOUR_BUSINESS_ID@postbode.bunni.nl` in order to get it automatically placed in your bookkeeping.

Using the `row` and `contact` from above, we can build a complete invoice using `InvoicePDF()` in the following manner:

```python
invoicePdf = PyBunniApi.InvoicePDF(
    invoice_date='YYYY-MM-DD',
    invoice_number='12345.67',
    tax_mode='excl',  # This can be either `incl` or `excl`,
    design='INVOICE_DESIGN_ID',  # See "Retrieving the list of invoice designs" below for how to fetch this ID.
    contact=contact,  # We made a contact above here.
    rows=[row]
)
```

We now have an initialized `InvoicePdf` object which we can use to create an invoice (pdf) in Bunni.
We can do this by using `py_bunni_api.invoices.create_pdf`

A complete snippet of this code would look like this:

```python
invoice_pdf = py_bunni_api.invoices.create_pdf(invoicePdf)
```

This will return a single pdf url, so the expected response should look like this:

```text
https://restpack.io/cache/pdf/069aba16b0ced81a42ecba6d7fd841885f53dd9bcac71cbbcb08756bad73e1ac
```


### Creating an invoice ###
___
This feature creates an invoice which is placed in your bookkeeping.
It also allows you to fetch the invoice PDF.

Using the same `row` and `contact` from above, we can build a complete invoice using `Invoice()` in the following manner:

```python
invoice = PyBunniApi.Invoice(
    external_id='Your own ID',
    invoice_date='YYYY-MM-DD',
    invoice_number='12345.67',
    tax_mode='excl',  # This can be either `incl` or `excl`,
    design='INVOICE_DESIGN_ID',  # See "Retrieving the list of invoice designs" below for how to fetch this ID.
    contact=contact,  # We made a contact above here.
    rows=[row]
)
```

We now have an initialized `Invoice` object which we can use to create an invoice in Bunni.
We can do this by using `py_bunni_api.invoices.create_or_update`

A complete snippet of this code would look like this:

```python
py_bunni_api.invoices.create_or_update(invoice)
```
This function will not return anything if your invoice object is all good. Otherwise it returns the error received from bunni.

### Retrieving the list of invoice designs ###
___
For retrieving a list of invoice designs you can use `invoice_designs.list`
A complete snippet of this code would look like this:

```python
invoice_designs = py_bunni_api.invoice_designs.list()
```

The variable `invoice_designs` now looks like this:

```python
[
  {
    "id": "de_10XXX",
    "name": "invoice THE CARROT COMPANY",
    "createdOn": "2023-08-09T18:22:15.21Z"
  },
  {
    "id": "de_10XXX",
    "name": "New Design",
    "createdOn": "2023-08-09T16:45:21.32Z"
  }
]
```

### Retrieving a list of projects ###
___
For retrieving a list of projects we can use `projects.list`.
A complete snippet looks like this:

```python
projects = py_bunni_api.projects.list()
```

The variable `projects` should now contain a structure like this:

```python
[
  {
    "id": "pr_17413",
    "color": "#eeeeee",
    "name": "Project auto voor Danny",
    "externalId": "1100"
  }
]
```

### Retrieving a list of time ###
___
For retrieving a list of time objects we can use `time.list`. A complete snippet would look like this:

```python
time_list = py_bunni_api.time.list()
```

As a result of this piece of code time_list should contain an object which looks a lot like this:

```python
[
  {
    "id": "ti_29XXXX",
    "date": "2023-08-10",
    "duration": {
      "m": 3,
      "h": 5
    },
    "project": {
      "id": "pr_17XXX",
      "color": "#123456",
      "name": "Project name",
      "externalId": "XXX"
    },
    "description": "Time description"
  }
]
```

### Creating or updating a time ###
___
We can create or update a time with the use of `time.create_or_update`.
For creating or updating a time we first need to build a time object.

A time object requires two items called `Duration` and `Project`. So let's create those two first.

A duration object can be initialized like this:
```python
duration = PyBunniApi.Duration(
    h=10, # This is a integer which stands for whole hours.
    m=30 # This is a integer which stands for whole minutes.
)
```

The next thing we need to setup is a `Project`. We can initialize one like this:
```python
project = PyBunniApi.Project(
    id="pr_XXXXX",
    external_id="YOUR EXTERNAL ID", # Bunni documentation shows this as optional. In my experience it seems mandatory.
    color="#123456",
    name="YOUR PROJECT NAME",
)
```

With those two objects initialized we can create a `time` object. You can do that the following way:
```python
time = PyBunniApi.TimeObject(
    date="2023-08-10",
    duration=duration,
    description="YOUR TIME DESCRIPTION",
    external_id="YOUR EXTERNAL ID",
    project=project,
)
```
Now that we have created all key elements we can submit it to Bunni in the following manner:
```python
py_bunni_api.time.create_or_update(time)
```

### Retrieving a list of bank accounts ###
___
For retrieving a list of bank accounts we can use `bank_accounts.list`.
A complete snippet looks like this:

```python
bank_accounts = py_bunni_api.bank_accounts.list()
```

The variable `bank_accounts` should now contain a structure like this:

```python
[
  {
    "id": "ba_XXXXX",
    "type": {
      "name": "iban"
    },
    "name": "My bank account",
    "accountNumber": "NL00BANK0123456789"
  }
]
```

### Retrieving a list of categories ###
___
For retrieving a list of categories we can use `categories.list`.
A complete snippet looks like this:

```python
categories = py_bunni_api.categories.list()
```

The variable `categories` should now contain a structure like this:

```python
[
  {
    "id": "ca_XXXXX",
    "name": "Office supplies",
    "color": "#eeeeee",
    "ledgerNumber": "4100"
  }
]
```

### Retrieving a list of tax rates ###
___
For retrieving a list of tax rates we can use `tax_rates.list`.
A complete snippet looks like this:

```python
tax_rates = py_bunni_api.tax_rates.list()
```

The variable `tax_rates` should now contain a structure like this:

```python
[
  {
    "idName": "NL_High_21",
    "name": "21% NL",
    "percentage": 21.0,
    "diverted": False,
    "active": True,
    "activeFrom": "2019-01-01",
    "activeTo": None
  }
]
```

### Retrieving a list of transactions ###
___
For retrieving a list of transactions we can use `transactions.list`.
A complete snippet looks like this:

```python
transactions = py_bunni_api.transactions.list()
```

The variable `transactions` should now contain a structure like this:

```python
[
  {
    "id": "tr_XXXXX",
    "bankAccountId": "ba_XXXXX",
    "date": "2023-08-10",
    "accountNumber": "NL00BANK0123456789",
    "amount": 100.0,
    "description": "Transaction description"
  }
]
```

### Errors ###
___
When Bunni rejects a request (for example, missing permissions or invalid data), pyBunniApi raises a
`BunniApiException` containing the error(s) returned by Bunni. If the client itself isn't configured correctly
(missing API key or business ID), a `BunniApiSetupException` is raised instead.

```python
from pyBunniApi.error import BunniApiException, BunniApiSetupException

try:
    py_bunni_api.invoices.create_or_update(invoice)
except BunniApiException as e:
    print(f"Bunni rejected the request: {e}")
except BunniApiSetupException as e:
    print(f"The client isn't configured correctly: {e}")
```

### A little footnote ###
___
You have made it to the end of the documentation! Well done. Please note that this project is in early development.
There might be some bugs here and there. But please let me know when you find one!

Do you want to thank me, because this project helped with a puzzle you needed to solve?
You can do that by <a href="https://www.paypal.com/donate/?hosted_button_id=JVXTKP6P9H2FC">buying me a coffee ;)</a>
