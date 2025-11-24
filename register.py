def borrow_book():
    print("\n--- Borrow a Book ---")

    # Ask for member name and validate
    member_name = input("Enter member name: ").strip()
    if member_name not in members:
        print("Member not found.")
        return

    member_profile = members[member_name]

    # Check if member can borrow more books
    if not borrow_allowed(member_profile):
        print("You have reached the maximum borrow limit (3 books).")
        return

    # Ask for book ID
    book_id = input("Enter the book ID you want to borrow: ").strip()

    # Validate book exists
    if book_id not in catalogue:
        print("Invalid book ID.")
        return

    # Validate availability
    if not is_book_available(book_id):
        print(f"'{catalogue[book_id]['title']}' is currently unavailable.")
        return

    # Update catalogue copies
    catalogue[book_id]["copies"] -= 1

    # Append book to member list
    member_profile["borrowed"].append(book_id)

    print(f"You have successfully borrowed '{catalogue[book_id]['title']}'.")

    # Save updates
    save_members()
