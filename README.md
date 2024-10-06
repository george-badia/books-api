## Sample API Requests:

1. **Create a new book (POST):**

   - Endpoint: `/books`
   - Method: `POST`
   - Body:
     ```json
     {
       "title": "The Great Gatsby",
       "author": "F. Scott Fitzgerald",
       "genre": "Fiction"
     }
     ```

2. **Update book information (PATCH):**

   - Endpoint: `/books/<id>`
   - Method: `PATCH`
   - Body:
     ```json
     {
       "title": "To Kill a Mockingbird",
       "author": "Harper Lee"
     }
     ```

3. **Delete a book (DELETE):**
   - Endpoint: `/books/<id>`
   - Method: `DELETE`
