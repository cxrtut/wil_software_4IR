let cart = [];

function updateCartCount() {
    const cartCount = cart.length;
    document.getElementById('cart-count').innerText = cartCount;

    const totalPrice = cart.reduce((total, item) => total + (item.itemPrice * item.quantity), 0);
    document.getElementById('total-price').innerText = 'R' + totalPrice;
}

function addToCart(itemName, itemPrice, itemType) {
    const item = { itemName, itemType, itemPrice, quantity: 1 };

    let existingItem = cart.find(cartItem => cartItem.itemName === itemName);

    if (existingItem) {
        existingItem.quantity++;
    } else {
        cart.push(item);
    }

    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartCount();
}

window.onload = function() {
    cart = JSON.parse(localStorage.getItem('cart')) || [];
    updateCartCount();
};

function deleteItem(itemName) {
    cart = cart.filter(item => item.itemName !== itemName);
    localStorage.setItem('cart', JSON.stringify(cart));
    showCartModal();
    updateCartCount();
}

function updateQuantity(itemName, newQuantity) {
    const item = cart.find(cartItem => cartItem.itemName === itemName);
    if (item && newQuantity > 0) {
        item.quantity = newQuantity;
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    showCartModal();
    updateCartCount();
}

function showCartModal() {
    const modal = document.getElementById('cart-modal');
    const tableBody = document.querySelector('#cart-modal table tbody');
    tableBody.innerHTML = '';
    let totalItems = 0;
    let totalPrice = 0;

    cart.forEach(item => {
        let row = document.createElement('tr');
        let nameCell = document.createElement('td');
        nameCell.innerText = item.itemName;
        row.appendChild(nameCell);

        let typeCell = document.createElement('td');
        typeCell.innerText = item.itemType;
        row.appendChild(typeCell);

        let quantityCell = document.createElement('td');
        quantityCell.innerHTML = `<input type="number" value="${item.quantity}" min="1" onchange="updateQuantity('${item.itemName}', this.value)">`;
        row.appendChild(quantityCell);

        let priceCell = document.createElement('td');
        priceCell.innerText = 'R' + item.itemPrice;
        row.appendChild(priceCell);

        let actionsCell = document.createElement('td');
        actionsCell.innerHTML = `<button onclick="deleteItem('${item.itemName}')">Delete</button>`;
        row.appendChild(actionsCell);

        tableBody.appendChild(row);

        totalItems += item.quantity;
        totalPrice += item.itemPrice * item.quantity;
    });

    document.getElementById('total-items').innerText = totalItems;
    document.getElementById('total-price').innerText = 'R' + totalPrice;
    modal.style.display = 'block';
}

function hideCartModal() {
    document.getElementById('cart-modal').style.display = 'none';
}

function checkout() {
    alert('Proceeding to checkout...');
}



// Function to get the CSRF token from the cookies
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Function to check availability
function checkAvailability(event) {
    event.preventDefault(); // Prevent form submission and page reload

    const startDate = document.getElementById('start_date').value;
    const endDate = document.getElementById('end_date').value;

    if (!startDate || !endDate) {
        alert('Please select both start and end dates.');
        return;
    }

    // Fetch the available equipment from the backend
    fetch('/check-availability/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')  // Use the getCookie function to get the CSRF token
        },
        body: JSON.stringify({ start_date: startDate, end_date: endDate })
    })
    .then(response => response.json())
    .then(data => {
        const resultsDiv = document.getElementById('availability-results');
        resultsDiv.innerHTML = '';  // Clear previous results

        if (data.available_equipment.length > 0) {
            data.available_equipment.forEach(item => {
                const itemDiv = document.createElement('div');
                itemDiv.textContent = `${item.name} - Quantity Available: ${item.quantity}`;
                resultsDiv.appendChild(itemDiv);
            });
        } else {
            resultsDiv.textContent = 'No equipment available for the selected date range.';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('There was an error checking availability.');
    });
}
