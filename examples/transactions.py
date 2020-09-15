from vesicashapi.transactions import Transactions

transaction = Transactions.create(
    title="Purchase Of An Iphone",
    type="oneoff",
    quantity=1,
    amount=20000,
    description="Iphone Purchase",
    parties={
        sender: 5841206525,
        recipient: 9432695230,
        buyer: 5841206525,
        seller: 9432695230,
        charge_bearer: 5841206525
    },
    inspection_period=1,
    due_date="2/12/2020",
    currency="NGN"
)

print(transaction)