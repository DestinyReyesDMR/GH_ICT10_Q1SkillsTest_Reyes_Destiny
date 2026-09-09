# main.py
from pyscript import document

def generate_receipt(event):
    checkboxes = document.querySelectorAll('.menu-checkbox')
    receipt_items = document.querySelector('#receiptItems')
    empty_notice = document.querySelector('#emptyNotice')
    receipt = document.querySelector('#receipt')
    
    selected_items = []
    subtotal = 0.0

    for cb in checkboxes:
        if cb.checked:
            val = float(cb.value)
            name = cb.getAttribute('data-name')
            selected_items.append((name, val))
            subtotal += val

    if not selected_items:
        empty_notice.style.display = 'block'
        receipt.style.display = 'none'
        return

    empty_notice.style.display = 'none'
    receipt_items.innerHTML = ''

    for name, val in selected_items:
        row = document.createElement('div')
        row.className = 'receipt-row d-flex justify-content-between fw-semibold text-dark mb-1'
        row.innerHTML = f'<span>1x {name}</span><span>₱{val:.2f}</span>'
        receipt_items.appendChild(row)

    vat = subtotal * 0.12
    total = subtotal + vat

    document.querySelector('#subtotal').textContent = f'₱{subtotal:.2f}'
    document.querySelector('#vat').textContent = f'₱{vat:.2f}'
    document.querySelector('#total').textContent = f'₱{total:.2f}'

    receipt.style.display = 'block'