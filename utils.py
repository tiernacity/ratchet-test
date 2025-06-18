# Sample Python file for testing ratchet

# TODO: Add type hints
def validate_email(email):
    """Validate email address format"""
    # FIXME: Use proper regex for email validation
    print(f"Validating email: {email}")
    return "@" in email

# TODO: Implement caching mechanism
def fetch_user_data(user_id):
    """Fetch user data from database"""
    # TODO: Connect to actual database
    print(f"Fetching data for user {user_id}")
    return {"id": user_id, "name": "Test User"}

# FIXME: This function is too complex
def process_transactions(transactions):
    """Process a list of transactions"""
    # TODO: Add transaction validation
    results = []
    for t in transactions:
        if t['amount'] > 0:
            if t['type'] == 'credit':
                # TODO: Add logging
                results.append({
                    'id': t['id'],
                    'status': 'approved',
                    'amount': t['amount']
                })
            else:
                # FIXME: Handle debit transactions properly
                results.append({
                    'id': t['id'],
                    'status': 'pending',
                    'amount': t['amount']
                })
    return results

print("Debug: Module loaded")