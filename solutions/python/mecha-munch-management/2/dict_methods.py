"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.
    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.
    Returns:
        dict: The updated user cart dictionary.
    """
    for item in items_to_add:
        if item not in current_cart:
            current_cart[item]=1
        else:
            current_cart[item]+=1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.
    Parameters:
        notes (iterable): Group of items to add to cart.
    Returns:
        dict: A user shopping cart dictionary.
    """
    newdict={}
    for note in notes:
        if note in newdict:
            newdict[note]+=1
        else:
            newdict[note]=1
    return newdict


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.
    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.
    Returns:
        dict: The updated "recipe ideas" dict.
    """
    ideas.update(recipe_updates)
    return ideas
    #dict {dish:dict}
                #{ingredient:count}
    #tuple(dish, {ingredient:count})

def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """
    sortdict=sorted(cart.items())
    return sortdict

def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information.
    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.
    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """
    sortlist=sorted(cart)
    revlist=reversed(sortlist)
    newdict=dict.fromkeys(revlist)
    for item, amt in cart.items():
        vallist=[]
        vallist.append(amt)
        for food, loc in aisle_mapping.items():
            if food==item:
                vallist.append(aisle_mapping[food][0])
                vallist.append(aisle_mapping[food][1])
                newdict[item]=vallist
    return newdict


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.
    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.
    Returns:
        dict: The store_inventory updated.
    """
    store=store_inventory.copy()
    for item in fulfillment_cart.keys():
        if type(store[item][0])!=str:
            if store[item][0]>=fulfillment_cart[item][0]:
                store[item][0]-=fulfillment_cart[item][0]
        if store[item][0]==0:
            store[item][0]="Out of Stock"
    return store
    
            