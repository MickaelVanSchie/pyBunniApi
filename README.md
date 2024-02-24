# pyBunniApi - a Bunni Python Api Client. #

### Requirements ###

+ You need a Bunni Account.
+ You need to generate an API key for your Bunni Account.
+ Python 3.10

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

### Creating an invoice PDF ###
___
This feature only generates a PDF. Said invoice will not be placed in your bookkeeping
software as of now.
You can however write your own piece of code that stores this pdf somewhere on your webserver, and sends it
to `YOUR_BUSINESS_ID@postbode.bunni.nl` in order to get it automatically placed in your bookkeeping.

Anyways, this part is a little bit more spicy and requires a few more steps.
Again, this only works if your API key has access to the `WRITE` permissions of Invoice.

First, let's start by defining our rows. A row requires four parameters. One invoice can contain varying rows. We append
these bu putting rows in a list.

To create row we can initialize a `Row()`. The complete syntax would look like this:

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

Now we can build a complete invoice using `InvoicePDF()` by the following manner:

```python
invoicePdf = PyBunniApi.InvoicePDF(
    invoice_date='YYYY-MM-DD',
    invoice_number='12345.67',
    tax_mode='excl',  # This can be either `incl` or `excl`,
    design='INVOICE_DESIGN_ID',  # A little down here I'll explain how you can fetch this ID.
    contact=contact,  # We made a contact above here.
    rows=[row]
)
```

We now have a initialized `InvoicePdf` object which we can use to create a invoice (pdf) in Bunni.
We can do this by using `py_bunni_api.invoices.create_pdf`

A complete snippet of this code would look like this:

```python
invoice_pdf = py_bunni_api.invoices.create_pdf(invoicePdf)
```

This will return a single pdf url, so the expected response should look like this:

```text
https://restpack.io/cache/pdf/069aba16b0ced81a42ecba6d7fd841885f53dd9bcac71cbbcb08756bad73e1ac
```


### Creating an invoice###
___
This feature creates an invoice which is placed in your bookkeeping.
It also allows you to fetch the invoice PDF.

First, let's start by defining our rows. A row requires four parameters. One invoice can contain varying rows. We append
these bu putting rows in a list.

To create row we can initialize a `Row()`. The complete syntax would look like this:

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

Now we can build a complete invoice using `InvoicePDF()` by the following manner:

```python
invoicePdf = PyBunniApi.Invoice(
    external_id='Your own ID',
    invoice_date='YYYY-MM-DD',
    invoice_number='12345.67',
    tax_mode='excl',  # This can be either `incl` or `excl`,
    design='INVOICE_DESIGN_ID',  # A little down here I'll explain how you can fetch this ID.
    contact=contact,  # We made a contact above here.
    rows=[row]
)
```

We now have a initialized `Invoice` object which we can use to create a invoice in Bunni.
We can do this by using `py_bunni_api.invoices.create_or_update`

A complete snippet of this code would look like this:

```python
invoice_pdf = py_bunni_api.invoices.create_or_update(invoice)
```
This function will not return anything if your invoice object is all good. Otherwise it returns the error received from bunni.

### Retreiving the list of invoice designs ###
___
For retrieving a list of invoice designs you can use `invoice_designs.list`
A complete snippet of this code would look like this:

```python
invoice_designs = py_bunni_api.invoice_designs.list()
```

The variable `invoice_designs` now looks like this:

```json
[
  {
    id: "de_10XXX",
    name: "invoice THE CARROT COMPANY",
    createdOn: "2023-08-09T18:22:15.21Z"
  },
  {
    id: "de_10XXX",
    name: "New Design",
    createdOn: "2023-08-09T16:45:21.32Z"
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

The variable `projects` should now contain a JSON structure like this:

```json
[
  {
    id: "pr_17413",
    color: "#eeeeee",
    name: "Project auto voor Danny",
    externalId: "1100"
  }
]
```

### Retieving a list of time ###
___
For retrieving a list of time objects we can use `time.list`. A complete snippet would look like this:

```python
time_list = py_bunni_api.time.list()
```

As a result of this piece of code time_list should contain an object which looks alot like this:

```json
[
  {
    id: "ti_29XXXX",
    date: "2023-08-10",
    duration: {
      m: 3,
      h: 5
    },
    project: {
      id: "pr_17XXX",
      color: "#123456",
      name: "Project name",
      externalId: "XXX"
    },
    description: "Time description"
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


### A little footnote ###
___
You have made it to the end of the documentation! Well done. Please note that this project is in early development.
There might be some bugs here and there. But please let me know when you find one!

Do you want to thank me, because this project helped with a puzzle you needed to solve?
You can do that by <a href="https://www.paypal.com/donate/?hosted_button_id=JVXTKP6P9H2FC">buying me a coffee ;)</a>